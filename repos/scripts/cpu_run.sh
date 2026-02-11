#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════════════════
# cpu_run.sh — Ejecutor paralelo de simulaciones en CPU (sin Docker, sin GPU)
#
# Ejecuta los 29 casos de simulación localmente usando procesos paralelos.
# Para ejecución con GPU, usar gpu_run.sh.
#
# ── USO ───────────────────────────────────────────────────────────────────────
#
#   # Todos los 29 casos en paralelo (workers = min(nproc, casos))
#   ./cpu_run.sh
#
#   # Dividir en tandas
#   ./cpu_run.sh --parts 3
#   ./cpu_run.sh --parts 5 --part 2   # solo tanda 2 de 5
#
#   # Caso específico (match parcial, case-insensitive)
#   ./cpu_run.sh --case clima
#   ./cpu_run.sh --case falsacion      # matchea los 3 falsación
#
#   # Limitar workers paralelos
#   ./cpu_run.sh --workers 4
#
#   # Secuencial: un caso a la vez (para grids enormes que usan toda la RAM)
#   ./cpu_run.sh --step-by-step
#
#   # Dry-run
#   ./cpu_run.sh --dry-run
#
# ── FLAGS ─────────────────────────────────────────────────────────────────────
#
#   --parts N       Dividir en N tandas (default: 1 = todos de golpe)
#   --part K        Ejecutar solo tanda K de N (default: todas)
#   --case NOMBRE   Filtrar casos por nombre (match parcial, case-insensitive)
#   --workers N     Workers paralelos (default: auto = min(nproc, ncasos))
#   --step-by-step  Ejecutar caso por caso secuencialmente (1 a la vez)
#   --perm N        Permutaciones EDI (default: 9999)
#   --boot N        Bootstrap samples (default: 5000)
#   --refine N      Iteraciones refinamiento (default: 50000)
#   --runs N        N_RUNS para C5 (default: 50)
#   --dry-run       Solo muestra el plan, no ejecuta
#   --help          Muestra este mensaje
#
# ══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

# ── Rutas ─────────────────────────────────────────────────────────────────────
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SIM_DIR="$(cd "$SCRIPT_DIR/../Simulaciones" && pwd)"

# ── Defaults ──────────────────────────────────────────────────────────────────
PARTS=1
PART=0
PERM=9999
BOOT=5000
REFINE=50000
RUNS=50
WORKERS=0          # 0 = auto
STEP_BY_STEP=0
DRY_RUN=0
CASE_FILTER=""

# ── Cleanup trap ──────────────────────────────────────────────────────────────
cleanup() {
    echo ""
    echo "⚠ Ctrl+C detectado — matando procesos validate.py..."
    pkill -f "python3 validate.py" 2>/dev/null || true
    sleep 1
    pkill -9 -f "python3 validate.py" 2>/dev/null || true
    echo "✓ Procesos terminados."
    exit 130
}
trap cleanup INT TERM

# ── Parse args ────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
    case "$1" in
        --parts)     PARTS="$2";       shift 2 ;;
        --part)      PART="$2";        shift 2 ;;
        --perm)      PERM="$2";        shift 2 ;;
        --boot)      BOOT="$2";        shift 2 ;;
        --refine)    REFINE="$2";      shift 2 ;;
        --runs)      RUNS="$2";        shift 2 ;;
        --workers)   WORKERS="$2";     shift 2 ;;
        --case)      CASE_FILTER="$2"; shift 2 ;;
        --step-by-step) STEP_BY_STEP=1;  shift ;;
        --dry-run)   DRY_RUN=1;        shift ;;
        --help|-h)
            head -45 "$0" | tail -41
            exit 0 ;;
        *) echo "Flag desconocido: $1"; exit 1 ;;
    esac
done

# ── Lista de los 29 casos ────────────────────────────────────────────────────
ALL_CASES=(
    01_caso_clima
    02_caso_conciencia
    03_caso_contaminacion
    04_caso_energia
    05_caso_epidemiologia
    06_caso_falsacion_exogeneidad
    07_caso_falsacion_no_estacionariedad
    08_caso_falsacion_observabilidad
    09_caso_finanzas
    10_caso_justicia
    11_caso_movilidad
    12_caso_paradigmas
    13_caso_politicas_estrategicas
    14_caso_postverdad
    15_caso_wikipedia
    16_caso_deforestacion
    17_caso_oceanos
    18_caso_urbanizacion
    19_caso_acidificacion_oceanica
    20_caso_kessler
    21_caso_salinizacion
    22_caso_fosforo
    23_caso_erosion_dialectica
    24_caso_microplasticos
    25_caso_acuiferos
    26_caso_starlink
    27_caso_riesgo_biologico
    28_caso_fuga_cerebros
    29_caso_iot
)

# ── Filtrar por caso específico (--case) ──────────────────────────────────────
if [[ -n "$CASE_FILTER" ]]; then
    FILTERED=()
    for c in "${ALL_CASES[@]}"; do
        if [[ "${c,,}" == *"${CASE_FILTER,,}"* ]]; then
            FILTERED+=("$c")
        fi
    done
    if [[ ${#FILTERED[@]} -eq 0 ]]; then
        echo "ERROR: Ningún caso coincide con '$CASE_FILTER'"
        echo "Casos disponibles:"
        printf '  %s\n' "${ALL_CASES[@]}"
        exit 1
    fi
    if [[ ${#FILTERED[@]} -gt 1 ]]; then
        echo "[--case] Múltiples casos coinciden con '$CASE_FILTER':"
        printf '  → %s\n' "${FILTERED[@]}"
        echo "[--case] Ejecutando todos los ${#FILTERED[@]} coincidentes."
    else
        echo "[--case] Caso: ${FILTERED[0]}"
    fi
    ALL_CASES=("${FILTERED[@]}")
fi

TOTAL=${#ALL_CASES[@]}

# ── Dividir array en N partes ─────────────────────────────────────────────────
get_partition() {
    local -n _arr=$1
    local n_parts=$2
    local which_part=$3
    local total=${#_arr[@]}
    local chunk=$(( (total + n_parts - 1) / n_parts ))
    local start=$(( (which_part - 1) * chunk ))
    local end=$(( start + chunk ))
    [[ $end -gt $total ]] && end=$total
    echo "${_arr[@]:$start:$((end - start))}"
}

# ── Workers automáticos ──────────────────────────────────────────────────────
NCORES=$(nproc 2>/dev/null || echo 4)
if [[ $STEP_BY_STEP -eq 1 ]]; then
    WORKERS=1
elif [[ $WORKERS -eq 0 ]]; then
    WORKERS=$NCORES
    [[ $WORKERS -gt $TOTAL ]] && WORKERS=$TOTAL
    [[ $WORKERS -gt 16 ]] && WORKERS=16    # cap razonable para CPU
fi

# ── Ejecutar un grupo de casos con cola dinámica ─────────────────────────────
run_batch() {
    local cases=("$@")
    local ncases=${#cases[@]}

    if [[ $ncases -eq 0 ]]; then
        echo "  (sin casos para esta tanda)"
        return 0
    fi

    local nw=$WORKERS
    [[ $nw -gt $ncases ]] && nw=$ncases

    echo "  Workers: ${nw} (CPU: ${NCORES} cores)"
    echo "  Modo: cola dinámica — ${nw} procesos paralelos"
    echo "  Logs: /tmp/cpu_run_logs/  (tail -f para detalle)"

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "  [DRY-RUN] ${ncases} casos → ${nw} workers"
        echo "  Casos: ${cases[*]}"
        return 0
    fi

    local LOG_DIR="/tmp/cpu_run_logs"
    mkdir -p "$LOG_DIR"

    local QUEUE_FILE=$(mktemp /tmp/_cpu_queue_XXXXXX)
    local LOCK_FILE="${QUEUE_FILE}.lock"
    local RESULT_FILE=$(mktemp /tmp/_cpu_results_XXXXXX)

    printf '%s\n' "${cases[@]}" > "$QUEUE_FILE"

    # ── Worker: toma casos de la cola hasta vaciarla ──
    cpu_worker() {
        local worker_id=$1
        local count=0

        while true; do
            local caso
            caso=$(flock "$LOCK_FILE" bash -c '
                head -1 "$1" 2>/dev/null
                sed -i "1d" "$1" 2>/dev/null
            ' -- "$QUEUE_FILE")

            [[ -z "$caso" ]] && break

            local SRC="${SIM_DIR}/${caso}/src"
            local LOG="${LOG_DIR}/${caso}.log"

            if [[ ! -f "${SRC}/validate.py" ]]; then
                echo "  [W${worker_id}] SKIP ${caso}"
                echo "SKIP ${caso}" >> "$RESULT_FILE"
                continue
            fi

            echo "  [W${worker_id}] ▶ ${caso}"
            local START=$SECONDS

            (
                cd "$SRC"
                export PYTHONIOENCODING=utf-8
                export HYPER_N_PERM=$PERM
                export HYPER_N_BOOT=$BOOT
                export HYPER_N_REFINE=$REFINE
                export HYPER_N_RUNS=$RUNS
                python3 validate.py 2>&1
            ) | \
                tee "$LOG" | \
                grep --line-buffered -E '(▶|[0-9]/6|FIN)' | \
                sed -u "s/^/  [W${worker_id}] /"
            local RC=${PIPESTATUS[0]}
            local ELAPSED=$(( SECONDS - START ))
            echo "ELAPSED=${ELAPSED}s" >> "$LOG"

            local EDI
            EDI=$(grep -oP 'EDI[=:]\s*-?[\d.]+' "$LOG" 2>/dev/null | tail -1 || echo '?')

            if [[ $RC -eq 0 ]]; then
                echo "  [W${worker_id}] ✓ ${caso} — ${ELAPSED}s — ${EDI}"
                echo "OK ${caso} ${ELAPSED}s ${EDI}" >> "$RESULT_FILE"
            else
                echo "  [W${worker_id}] ✗ ${caso} — ${ELAPSED}s (exit ${RC})"
                echo "FAIL ${caso} ${ELAPSED}s exit=${RC}" >> "$RESULT_FILE"
            fi
            count=$((count + 1))
        done
        echo "  [W${worker_id}] Terminado (${count} casos)"
    }

    # ── Lanzar N workers ──
    local WPIDS=()
    for ((i=0; i<nw; i++)); do
        cpu_worker "$i" &
        WPIDS+=($!)
    done

    # ── Esperar ──
    local FAIL=0
    for pid in "${WPIDS[@]}"; do
        wait "$pid" 2>/dev/null || FAIL=$((FAIL+1))
    done

    # ── Resumen ──
    echo ""
    echo "  ═══ Resumen de tanda ═══"
    local TOTAL_OK=0 TOTAL_FAIL=0 TOTAL_SKIP=0
    while read -r line; do
        case "$line" in
            OK*)   TOTAL_OK=$((TOTAL_OK+1)) ;;
            FAIL*) TOTAL_FAIL=$((TOTAL_FAIL+1)) ;;
            SKIP*) TOTAL_SKIP=$((TOTAL_SKIP+1)) ;;
        esac
    done < "$RESULT_FILE"

    echo "  OK: ${TOTAL_OK}  FAIL: ${TOTAL_FAIL}  SKIP: ${TOTAL_SKIP}"

    rm -f "$QUEUE_FILE" "$LOCK_FILE" "$RESULT_FILE"
}

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  cpu_run.sh — Ejecución paralela CPU (sin GPU/Docker)      ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║  Grid:     por caso (validate.py)"
echo "║  Parts:    ${PARTS}  $([ $PART -gt 0 ] && echo "(solo parte ${PART})" || echo "(todas)")"
echo "║  Casos:    ${TOTAL}$( [[ -n "$CASE_FILTER" ]] && echo " (filtro: ${CASE_FILTER})" )"
echo "║  Workers:  ${WORKERS} (cores: ${NCORES})$( [[ $STEP_BY_STEP -eq 1 ]] && echo " ⇢ SECUENCIAL" )"
echo "║  Params:   perm=${PERM} boot=${BOOT} refine=${REFINE} runs=${RUNS}"
echo "║  SimDir:   ${SIM_DIR}"
[[ $DRY_RUN -eq 1 ]] && \
echo "║  *** DRY RUN — no se ejecuta nada ***"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

START_GLOBAL=$SECONDS

# ── Ejecutar por tandas ───────────────────────────────────────────────────────────────────
if [[ $STEP_BY_STEP -eq 1 ]]; then
    # ── Modo secuencial: un caso a la vez, toda la RAM disponible ──
    echo "═══ Modo SECUENCIAL — ${TOTAL} casos, 1 a la vez ═══"
    LOG_DIR="/tmp/cpu_run_logs"
    mkdir -p "$LOG_DIR"
    TOTAL_OK=0; TOTAL_FAIL=0; TOTAL_SKIP=0
    for ((i=0; i<TOTAL; i++)); do
        caso=${ALL_CASES[$i]}
        echo ""
        echo "  [$((i+1))/${TOTAL}] ▶ ${caso}"
        if [[ $DRY_RUN -eq 1 ]]; then
            echo "  [DRY-RUN] ${caso}"
            continue
        fi
        SRC="${SIM_DIR}/${caso}/src"
        LOG="${LOG_DIR}/${caso}.log"
        if [[ ! -f "${SRC}/validate.py" ]]; then
            echo "  [$((i+1))/${TOTAL}] SKIP ${caso}"
            TOTAL_SKIP=$((TOTAL_SKIP+1))
            continue
        fi
        START_CASE=$SECONDS
        (
            cd "$SRC"
            export PYTHONIOENCODING=utf-8
            export HYPER_N_PERM=$PERM
            export HYPER_N_BOOT=$BOOT
            export HYPER_N_REFINE=$REFINE
            export HYPER_N_RUNS=$RUNS
            python3 validate.py 2>&1 | tee "$LOG"
        )
        RC=$?
        ELAPSED_CASE=$(( SECONDS - START_CASE ))
        EDI=$(grep -oP 'EDI[=:]\s*-?[\d.]+' "$LOG" 2>/dev/null | tail -1 || echo '?')
        if [[ $RC -eq 0 ]]; then
            echo "  [$((i+1))/${TOTAL}] ✓ ${caso} — ${ELAPSED_CASE}s — ${EDI}"
            TOTAL_OK=$((TOTAL_OK+1))
        else
            echo "  [$((i+1))/${TOTAL}] ✗ ${caso} — ${ELAPSED_CASE}s (exit ${RC})"
            TOTAL_FAIL=$((TOTAL_FAIL+1))
        fi
    done
    echo ""
    echo "  ═══ Resumen secuencial ═══"
    echo "  OK: ${TOTAL_OK}  FAIL: ${TOTAL_FAIL}  SKIP: ${TOTAL_SKIP}"
else
    # ── Modo paralelo por tandas (comportamiento normal) ──
    for p in $(seq 1 "$PARTS"); do
        if [[ $PART -gt 0 && $p -ne $PART ]]; then continue; fi

        CASES_STR=$(get_partition ALL_CASES "$PARTS" "$p")
        read -ra CASES_ARR <<< "$CASES_STR"

        echo "═══ Tanda ${p}/${PARTS} — ${#CASES_ARR[@]} casos ═══"
        run_batch "${CASES_ARR[@]}"

        if [[ $p -lt $PARTS && $PART -eq 0 ]]; then
            echo ""
            echo "--- Pausa 2s entre tandas ---"
            sleep 2
        fi
    done
fi

ELAPSED_GLOBAL=$(( SECONDS - START_GLOBAL ))
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  COMPLETADO en ${ELAPSED_GLOBAL}s                          "
echo "║  Logs: ls /tmp/cpu_run_logs/"
echo "╚══════════════════════════════════════════════════════════════╝"
