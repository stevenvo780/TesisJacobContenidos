#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════════════════
# gpu_run.sh — Ejecutor escalable de simulaciones con distribución multi-GPU
#
# Divide los 29 casos en particiones para controlar VRAM y permite escalar
# el grid_size inversamente al número de casos simultáneos.
#
# ── USO ───────────────────────────────────────────────────────────────────────
#
#   # Todo de golpe (29 en paralelo, grid=200 — cabe en 16GB)
#   ./gpu_run.sh
#
#   # AUTO-ESCALADO: grid = 200 × parts (si no se pasa --grid)
#   ./gpu_run.sh --parts 2          # grid=400 auto, 2 tandas de ~15
#   ./gpu_run.sh --parts 3          # grid=600 auto, 3 tandas de ~10
#   ./gpu_run.sh --parts 5          # grid=1000 auto, 5 tandas de ~6
#
#   # Forzar grid explícito (desactiva auto-escalado)
#   ./gpu_run.sh --grid 500 --parts 2
#   ./gpu_run.sh --grid 1000 --parts 5 --part 3
#
#   # Forzar GPU específica
#   ./gpu_run.sh --grid 500 --gpu 0              # solo 5070 Ti
#   ./gpu_run.sh --grid 200 --gpu 1              # solo 2060
#
#   # Distribuir entre 2 GPUs por VRAM (automático)
#   ./gpu_run.sh --parts 2 --distribute
#
#   # Dry-run (muestra plan sin ejecutar)
#   ./gpu_run.sh --parts 5 --dry-run
#
# ── FLAGS ─────────────────────────────────────────────────────────────────────
#
#   --grid SIZE     Grid size del ABM (default: auto = 200 × parts)
#   --parts N       Dividir en N tandas (1-10, default: 1 = todos de golpe)
#                   Sin --grid: auto-escala grid = 200 × N
#   --part K        Ejecutar solo tanda K de N (default: todas)
#   --gpu ID        Forzar GPU (0=5070Ti, 1=2060)
#   --distribute    Auto-distribuir entre GPUs por proporción VRAM
#   --perm N        Permutaciones EDI (default: 9999)
#   --boot N        Bootstrap samples (default: 5000)
#   --refine N      Iteraciones refinamiento (default: 50000)
#   --runs N        N_RUNS para C5 (default: 50)
#   --container C   Nombre del contenedor Docker (default: tesis-gpu)
#   --dry-run       Solo muestra el plan, no ejecuta
#   --help          Muestra este mensaje
#
# ══════════════════════════════════════════════════════════════════════════════
set -euo pipefail

# ── Defaults ──────────────────────────────────────────────────────────────────
GRID=200
GRID_EXPLICIT=0
PARTS=1
PART=0          # 0 = todas las partes
GPU_ID=""       # vacío = no forzar
DISTRIBUTE=0
PERM=9999
BOOT=5000
REFINE=50000
RUNS=50
CONTAINER="tesis-gpu"
DRY_RUN=0

# ── GPU inventory (VRAM en MB) ────────────────────────────────────────────────
# Se detecta en runtime, estos son fallbacks
GPU0_NAME="RTX 5070 Ti"
GPU0_VRAM=16303
GPU1_NAME="RTX 2060"
GPU1_VRAM=6144

# ── Parse args ────────────────────────────────────────────────────────────────
while [[ $# -gt 0 ]]; do
    case "$1" in
        --grid)      GRID="$2"; GRID_EXPLICIT=1; shift 2 ;;
        --parts)     PARTS="$2";     shift 2 ;;
        --part)      PART="$2";      shift 2 ;;
        --gpu)       GPU_ID="$2";    shift 2 ;;
        --distribute) DISTRIBUTE=1;  shift ;;
        --perm)      PERM="$2";      shift 2 ;;
        --boot)      BOOT="$2";      shift 2 ;;
        --refine)    REFINE="$2";    shift 2 ;;
        --runs)      RUNS="$2";      shift 2 ;;
        --container) CONTAINER="$2"; shift 2 ;;
        --dry-run)   DRY_RUN=1;      shift ;;
        --help|-h)
            head -44 "$0" | tail -40
            exit 0 ;;
        *) echo "Flag desconocido: $1"; exit 1 ;;
    esac
done

# ── Auto-escalado de grid ─────────────────────────────────────────────────────
BASE_GRID=200
if [[ $GRID_EXPLICIT -eq 0 && $PARTS -gt 1 ]]; then
    GRID=$(( BASE_GRID * PARTS ))
    echo "[auto-grid] grid = ${BASE_GRID} × ${PARTS} partes = ${GRID}"
fi

# ── Detectar GPUs ─────────────────────────────────────────────────────────────
detect_gpus() {
    local ngpu
    ngpu=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits 2>/dev/null | wc -l)
    if [[ $ngpu -ge 1 ]]; then
        GPU0_VRAM=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits -i 0 2>/dev/null | tr -d ' ')
        GPU0_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader -i 0 2>/dev/null | tr -d ' ')
    fi
    if [[ $ngpu -ge 2 ]]; then
        GPU1_VRAM=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader,nounits -i 1 2>/dev/null | tr -d ' ')
        GPU1_NAME=$(nvidia-smi --query-gpu=name --format=csv,noheader -i 1 2>/dev/null | tr -d ' ')
    fi
    echo "$ngpu"
}

N_GPUS=$(detect_gpus)

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
TOTAL=${#ALL_CASES[@]}

# ── VRAM estimada por simulación (MB) ────────────────────────────────────────
# Base: grid × grid × 8 bytes × ~20 buffers × batch_size(~500)
# + overhead CuPy (~500MB)
estimate_vram_per_sim() {
    local g=$1
    # Cada sim en batch: grid^2 * 8 * 6 buffers (grids, nb_mean, noise, etc.)
    # Batch de 500 sims: × 500
    # + overhead de forcing, series, etc.
    local bytes_per_batch=$(( g * g * 8 * 6 * 500 ))
    local mb=$(( bytes_per_batch / 1048576 + 500 ))  # +500MB overhead CuPy
    echo "$mb"
}

# Cuántos casos simultáneos caben en una GPU
max_concurrent_for_gpu() {
    local gpu_vram=$1
    local grid=$2
    local vram_per_sim
    vram_per_sim=$(estimate_vram_per_sim "$grid")
    # Reservar 20% de VRAM para overhead
    local usable=$(( gpu_vram * 80 / 100 ))
    local max=$(( usable / vram_per_sim ))
    # Mínimo 1, máximo 29
    [[ $max -lt 1 ]] && max=1
    [[ $max -gt 29 ]] && max=29
    echo "$max"
}

# ── Dividir array en N partes ─────────────────────────────────────────────────
# Retorna el slice para la parte K (1-indexed) de N
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

# ── Ejecutar un grupo de casos en el contenedor ──────────────────────────────
run_batch() {
    local gpu_device=$1
    shift
    local cases=("$@")
    local ncases=${#cases[@]}
    
    if [[ $ncases -eq 0 ]]; then
        echo "  (sin casos para esta tanda)"
        return 0
    fi
    
    local log_dir="/tmp/gpu_run_g${GRID}_logs"
    
    # Construir el comando interno
    local inner_script="
export HYPER_GRID_SIZE=${GRID}
export HYPER_N_PERM=${PERM}
export HYPER_N_BOOT=${BOOT}
export HYPER_N_REFINE=${REFINE}
export HYPER_N_RUNS=${RUNS}
export CUDA_VISIBLE_DEVICES=${gpu_device}

mkdir -p ${log_dir}
echo \"[GPU ${gpu_device}] ${ncases} casos, grid=${GRID}\"

PIDS=()
NAMES=()
for case in ${cases[*]}; do
    SRC=\"/workspace/repos/Simulaciones/\${case}/src\"
    LOG=\"${log_dir}/\${case}.log\"
    if [ ! -f \"\${SRC}/validate.py\" ]; then
        echo \"  [SKIP] \${case}\"
        continue
    fi
    (cd \"\$SRC\" && START=\$SECONDS && python3 validate.py > \"\$LOG\" 2>&1 && echo \"ELAPSED=\$((\$SECONDS - \$START))s\" >> \"\$LOG\") &
    PIDS+=(\$!)
    NAMES+=(\"\$case\")
done

FAIL=0
for i in \"\${!NAMES[@]}\"; do
    if wait \"\${PIDS[\$i]}\" 2>/dev/null; then S=\"OK\"; else S=\"FAIL\"; FAIL=\$((FAIL+1)); fi
    LOG=\"${log_dir}/\${NAMES[\$i]}.log\"
    ELAPSED=\$(grep '^ELAPSED' \"\$LOG\" 2>/dev/null | cut -d= -f2 || echo '?')
    EDI=\$(grep -oP 'EDI[=:]\s*-?[\d.]+' \"\$LOG\" 2>/dev/null | tail -1 || echo '?')
    echo \"  [\$S] \${NAMES[\$i]} — \$ELAPSED — \$EDI\"
done
echo \"  Failures: \$FAIL/${ncases}\"
"

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "  [DRY-RUN] GPU=$gpu_device, ${ncases} casos: ${cases[*]}"
        echo "  VRAM estimada: $(estimate_vram_per_sim $GRID) MB/sim"
        return 0
    fi
    
    docker exec "$CONTAINER" bash -c "$inner_script"
}

# ══════════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════════

echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  gpu_run.sh — Ejecución escalable multi-GPU                ║"
echo "╠══════════════════════════════════════════════════════════════╣"
echo "║  Grid:     ${GRID}×${GRID}"
echo "║  Parts:    ${PARTS}  $([ $PART -gt 0 ] && echo "(solo parte ${PART})" || echo "(todas)")"
echo "║  GPUs:     ${N_GPUS} detectadas"
echo "║  GPU 0:    ${GPU0_NAME} — ${GPU0_VRAM} MB"
[[ $N_GPUS -ge 2 ]] && \
echo "║  GPU 1:    ${GPU1_NAME} — ${GPU1_VRAM} MB"
echo "║  Distrib:  $([ $DISTRIBUTE -eq 1 ] && echo "auto por VRAM" || echo "no")"
[[ -n "$GPU_ID" ]] && \
echo "║  GPU fix:  ${GPU_ID}"
echo "║  Params:   perm=${PERM} boot=${BOOT} refine=${REFINE} runs=${RUNS}"
echo "║  Contendr: ${CONTAINER}"
echo "║  VRAM/sim: ~$(estimate_vram_per_sim $GRID) MB"
[[ $DRY_RUN -eq 1 ]] && \
echo "║  *** DRY RUN — no se ejecuta nada ***"
echo "╚══════════════════════════════════════════════════════════════╝"
echo ""

# Verificar contenedor
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "ERROR: Contenedor '${CONTAINER}' no está corriendo."
    echo "Lánzalo con:"
    echo "  docker run -d --name tesis-gpu --gpus all \\"
    echo "    -v /datos/repos/Personal/TesisJacobContenidos:/workspace \\"
    echo "    -w /workspace docker-gpu:latest sleep infinity"
    exit 1
fi

START_GLOBAL=$SECONDS

# ── Modo: distribuir entre GPUs ───────────────────────────────────────────────
if [[ $DISTRIBUTE -eq 1 && $N_GPUS -ge 2 ]]; then
    # Proporción por VRAM
    TOTAL_VRAM=$(( GPU0_VRAM + GPU1_VRAM ))
    GPU0_SHARE=$(( TOTAL * GPU0_VRAM / TOTAL_VRAM ))
    GPU1_SHARE=$(( TOTAL - GPU0_SHARE ))
    
    echo "═══ Distribución por VRAM ═══"
    echo "  GPU 0 (${GPU0_NAME}, ${GPU0_VRAM}MB): ${GPU0_SHARE} casos"
    echo "  GPU 1 (${GPU1_NAME}, ${GPU1_VRAM}MB): ${GPU1_SHARE} casos"
    echo ""
    
    GPU0_CASES=("${ALL_CASES[@]:0:$GPU0_SHARE}")
    GPU1_CASES=("${ALL_CASES[@]:$GPU0_SHARE}")
    
    if [[ $PARTS -gt 1 ]]; then
        # Subdividir cada GPU en tandas
        echo "Subdividiendo en ${PARTS} tandas por GPU..."
        for p in $(seq 1 "$PARTS"); do
            if [[ $PART -gt 0 && $p -ne $PART ]]; then continue; fi
            echo ""
            echo "═══ Tanda ${p}/${PARTS} ═══"
            
            P0_CASES=($(get_partition GPU0_CASES "$PARTS" "$p"))
            P1_CASES=($(get_partition GPU1_CASES "$PARTS" "$p"))
            
            echo "  GPU 0: ${#P0_CASES[@]} casos"
            echo "  GPU 1: ${#P1_CASES[@]} casos"
            
            # Lanzar ambas GPUs en paralelo
            run_batch 0 "${P0_CASES[@]}" &
            PID0=$!
            run_batch 1 "${P1_CASES[@]}" &
            PID1=$!
            wait $PID0 $PID1
        done
    else
        # Todo de golpe, dividido entre GPUs
        echo "═══ Ejecución: GPU 0 + GPU 1 en paralelo ═══"
        run_batch 0 "${GPU0_CASES[@]}" &
        PID0=$!
        run_batch 1 "${GPU1_CASES[@]}" &
        PID1=$!
        wait $PID0 $PID1
    fi

# ── Modo: GPU fija o auto, con particiones ────────────────────────────────────
else
    TARGET_GPU="${GPU_ID:-0}"
    
    for p in $(seq 1 "$PARTS"); do
        if [[ $PART -gt 0 && $p -ne $PART ]]; then continue; fi
        
        CASES_STR=$(get_partition ALL_CASES "$PARTS" "$p")
        read -ra CASES_ARR <<< "$CASES_STR"
        
        echo "═══ Tanda ${p}/${PARTS} — ${#CASES_ARR[@]} casos — GPU ${TARGET_GPU} ═══"
        run_batch "$TARGET_GPU" "${CASES_ARR[@]}"
        
        if [[ $p -lt $PARTS && $PART -eq 0 ]]; then
            echo ""
            echo "--- Pausa 5s entre tandas (liberar VRAM) ---"
            sleep 5
        fi
    done
fi

ELAPSED_GLOBAL=$(( SECONDS - START_GLOBAL ))
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  COMPLETADO en ${ELAPSED_GLOBAL}s                          "
echo "║  Logs: docker exec ${CONTAINER} ls /tmp/gpu_run_g${GRID}_logs/"
echo "╚══════════════════════════════════════════════════════════════╝"
