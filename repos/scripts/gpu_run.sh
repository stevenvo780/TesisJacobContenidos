#!/usr/bin/env bash
# ══════════════════════════════════════════════════════════════════════════════
# gpu_run.sh — Ejecutor escalable de simulaciones con distribución multi-GPU
#
# Cada proceso Python ve AMBAS GPUs y elige automáticamente la que tenga más
# VRAM libre al arrancar. Así los casos se reparten entre GPUs naturalmente:
# los primeros saturan GPU 0 (más grande) y los siguientes caen a GPU 1.
#
# ── USO ───────────────────────────────────────────────────────────────────────
#
#   # Todo de golpe (29 en paralelo, grid=200 — ambas GPUs auto)
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
#   # Dry-run (muestra plan sin ejecutar)
#   ./gpu_run.sh --parts 5 --dry-run
#
# ── FLAGS ─────────────────────────────────────────────────────────────────────
#
#   --grid SIZE     Grid size del ABM (default: auto = 200 × parts)
#   --parts N       Dividir en N tandas (1-10, default: 1 = todos de golpe)
#                   Sin --grid: auto-escala grid = 200 × N
#   --part K        Ejecutar solo tanda K de N (default: todas)
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
PERM=9999
BOOT=5000
REFINE=50000
RUNS=50
CONTAINER="tesis-gpu"
DRY_RUN=0

# ── Cleanup trap: al cancelar, matar todos los validate.py dentro del contenedor
cleanup() {
    echo ""
    echo "⚠ Ctrl+C detectado — matando procesos Python en ${CONTAINER}..."
    docker exec "$CONTAINER" bash -c 'pkill -f "python3 validate.py" 2>/dev/null; sleep 1; pkill -9 -f "python3 validate.py" 2>/dev/null' 2>/dev/null || true
    echo "✓ Procesos Python terminados dentro del contenedor."
    exit 130
}
trap cleanup INT TERM

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
        --perm)      PERM="$2";      shift 2 ;;
        --boot)      BOOT="$2";      shift 2 ;;
        --refine)    REFINE="$2";    shift 2 ;;
        --runs)      RUNS="$2";      shift 2 ;;
        --container) CONTAINER="$2"; shift 2 ;;
        --dry-run)   DRY_RUN=1;      shift ;;
        --help|-h)
            head -40 "$0" | tail -36
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

# ── Pre-asignar GPUs proporcionalmente a VRAM libre ──────────────────────────
# Evita race condition: si 29 procesos arrancan juntos, todos verían la misma
# VRAM libre y elegirían la misma GPU. Asignamos desde bash ANTES de lanzar.
compute_gpu_assignments() {
    local ncases=$1
    # Obtener VRAM libre de cada GPU
    local gpu_free
    gpu_free=$(nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits 2>/dev/null)
    
    if [[ -z "$gpu_free" ]]; then
        # Sin nvidia-smi, todo a GPU 0
        for ((i=0; i<ncases; i++)); do echo 0; done
        return
    fi
    
    local -a gpu_ids=()
    local -a gpu_mbs=()
    local total_free=0
    while IFS=', ' read -r gid gmb; do
        gid=$(echo "$gid" | tr -d ' ')
        gmb=$(echo "$gmb" | tr -d ' ')
        gpu_ids+=("$gid")
        gpu_mbs+=("$gmb")
        total_free=$((total_free + gmb))
    done <<< "$gpu_free"
    
    local ngpus=${#gpu_ids[@]}
    if [[ $ngpus -le 1 || $total_free -eq 0 ]]; then
        for ((i=0; i<ncases; i++)); do echo "${gpu_ids[0]:-0}"; done
        return
    fi
    
    # Asignar proporcionalmente: GPU con 15GB libre y GPU con 3GB libre
    # → 83% y 17% de los procesos respectivamente
    local -a gpu_count=()
    local assigned=0
    for ((g=0; g<ngpus; g++)); do
        if [[ $g -eq $((ngpus-1)) ]]; then
            gpu_count+=($((ncases - assigned)))
        else
            local cnt=$(( ncases * gpu_mbs[g] / total_free ))
            [[ $cnt -lt 1 && ${gpu_mbs[g]} -gt 500 ]] && cnt=1
            gpu_count+=("$cnt")
            assigned=$((assigned + cnt))
        fi
    done
    
    # Emitir asignaciones
    for ((g=0; g<ngpus; g++)); do
        for ((c=0; c<${gpu_count[g]}; c++)); do
            echo "${gpu_ids[g]}"
        done
    done
}

# ── Ejecutar un grupo de casos con COLA DINÁMICA multi-worker por GPU ────────
# Múltiples workers por GPU comparten la cola. La calibración y datos son
# CPU-bound, así que varios procesos por GPU mantienen CPU y GPU ocupadas.
# El sub-batching dinámico de abm_core_gpu.py maneja la competición por VRAM.
run_batch() {
    local cases=("$@")
    local ncases=${#cases[@]}
    
    if [[ $ncases -eq 0 ]]; then
        echo "  (sin casos para esta tanda)"
        return 0
    fi
    
    # Detectar GPUs disponibles desde el host
    local -a available_gpus=()
    local -a gpu_free_mb=()
    local gpu_csv
    gpu_csv=$(nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits 2>/dev/null)
    if [[ -n "$gpu_csv" ]]; then
        while IFS=', ' read -r gid gmb; do
            gid=$(echo "$gid" | tr -d ' ')
            gmb=$(echo "$gmb" | tr -d ' ')
            if [[ $gmb -gt 1000 ]]; then
                available_gpus+=("$gid")
                gpu_free_mb+=("$gmb")
            fi
        done <<< "$gpu_csv"
    fi
    [[ ${#available_gpus[@]} -eq 0 ]] && available_gpus=(0) && gpu_free_mb=(8000)
    
    # Calcular workers por GPU: suficientes para mantener CPU y GPU ocupadas
    # Mientras un proceso hace ABM en GPU, otros hacen calibración/datos en CPU.
    # Con grid grande, el ABM tarda mucho → necesitamos más workers CPU-bound.
    # Mínimo: max(ncores/ngpus, 4) workers por GPU para overlap CPU/GPU
    local vram_est
    vram_est=$(estimate_vram_per_sim "$GRID")
    local total_workers=0
    local -a workers_per_gpu=()
    local worker_gpu_map=""  # "0 0 0 1 1" — qué GPU para cada worker
    
    # Detectar cores CPU disponibles
    local ncores
    ncores=$(nproc 2>/dev/null || echo 8)
    local ngpus=${#available_gpus[@]}
    # Workers mínimos por GPU: balancear CPU entre GPUs, mínimo 4
    local min_per_gpu=$(( ncores / ngpus ))
    [[ $min_per_gpu -lt 4 ]] && min_per_gpu=4
    [[ $min_per_gpu -gt 15 ]] && min_per_gpu=15  # cap razonable
    
    for i in "${!available_gpus[@]}"; do
        local free=${gpu_free_mb[$i]}
        # Cuántos caben en VRAM (con margen 30%)
        local vram_fit=$(( free * 70 / 100 / (vram_est > 0 ? vram_est : 1) ))
        [[ $vram_fit -lt 1 ]] && vram_fit=1
        # Más workers para overlap CPU/GPU
        local nw=$vram_fit
        [[ $nw -lt $min_per_gpu ]] && nw=$min_per_gpu
        # No más workers que casos restantes
        local remaining=$((ncases - total_workers))
        [[ $nw -gt $remaining ]] && nw=$remaining
        [[ $nw -lt 1 ]] && nw=1
        workers_per_gpu+=("$nw")
        for ((w=0; w<nw; w++)); do
            worker_gpu_map+="${available_gpus[$i]} "
        done
        total_workers=$((total_workers + nw))
    done
    
    # No más workers que casos
    [[ $total_workers -gt $ncases ]] && total_workers=$ncases
    
    echo "  Workers: ${total_workers} (${#available_gpus[@]} GPUs: ${available_gpus[*]})"
    for i in "${!available_gpus[@]}"; do
        echo "    GPU ${available_gpus[$i]}: ${workers_per_gpu[$i]} workers (${gpu_free_mb[$i]}MB libre)"
    done
    echo "  Modo: cola dinámica — ${total_workers} workers, la GPU rápida toma más"
    
    local log_dir="/tmp/gpu_run_g${GRID}_logs"
    local cases_str="${cases[*]}"
    # Trim trailing space
    worker_gpu_map=$(echo "$worker_gpu_map" | xargs)
    
    local inner_script="
export HYPER_GRID_SIZE=${GRID}
export HYPER_N_PERM=${PERM}
export HYPER_N_BOOT=${BOOT}
export HYPER_N_REFINE=${REFINE}
export HYPER_N_RUNS=${RUNS}

trap 'kill \$(jobs -p) 2>/dev/null; wait; exit 130' INT TERM

mkdir -p ${log_dir}

# Cola de casos
QUEUE_FILE=/tmp/_gpu_queue_\$\$
LOCK_FILE=/tmp/_gpu_queue_\$\$.lock
RESULT_FILE=/tmp/_gpu_results_\$\$

CASES_ALL=(${cases_str})
printf '%s\n' \"\${CASES_ALL[@]}\" > \"\$QUEUE_FILE\"
touch \"\$RESULT_FILE\"

WORKER_GPUS=(${worker_gpu_map})
N_WORKERS=\${#WORKER_GPUS[@]}

echo \"[\${#CASES_ALL[@]} casos, grid=${GRID}, \${N_WORKERS} workers en ${#available_gpus[@]} GPUs]\"

# ── Worker: toma casos de la cola hasta vaciarla ──
gpu_worker() {
    local gpu_id=\$1
    local worker_id=\$2
    local count=0
    
    while true; do
        # Pop atómico del primer caso de la cola
        local caso
        caso=\$(flock \"\$LOCK_FILE\" bash -c '
            head -1 \"\$1\" 2>/dev/null
            sed -i \"1d\" \"\$1\" 2>/dev/null
        ' -- \"\$QUEUE_FILE\")
        
        [[ -z \"\$caso\" ]] && break
        
        local SRC=\"/workspace/repos/Simulaciones/\${caso}/src\"
        local LOG=\"${log_dir}/\${caso}.log\"
        
        if [ ! -f \"\${SRC}/validate.py\" ]; then
            echo \"  [W\${worker_id}/GPU\${gpu_id}] SKIP \${caso}\"
            echo \"SKIP \${caso} GPU\${gpu_id}\" >> \"\$RESULT_FILE\"
            continue
        fi
        
        echo \"  [W\${worker_id}/GPU\${gpu_id}] ▶ \${caso}\"
        local START=\$SECONDS
        
        (cd \"\$SRC\" && HYPER_GPU_DEVICE=\$gpu_id python3 validate.py > \"\$LOG\" 2>&1)
        local RC=\$?
        local ELAPSED=\$((\$SECONDS - \$START))
        echo \"ELAPSED=\${ELAPSED}s\" >> \"\$LOG\"
        
        local EDI=\$(grep -oP 'EDI[=:]\s*-?[\\d.]+' \"\$LOG\" 2>/dev/null | tail -1 || echo '?')
        
        if [ \$RC -eq 0 ]; then
            echo \"  [W\${worker_id}/GPU\${gpu_id}] ✓ \${caso} — \${ELAPSED}s — \${EDI}\"
            echo \"OK \${caso} GPU\${gpu_id} \${ELAPSED}s \${EDI}\" >> \"\$RESULT_FILE\"
        else
            echo \"  [W\${worker_id}/GPU\${gpu_id}] ✗ \${caso} — \${ELAPSED}s (exit \${RC})\"
            echo \"FAIL \${caso} GPU\${gpu_id} \${ELAPSED}s exit=\${RC}\" >> \"\$RESULT_FILE\"
        fi
        count=\$((count + 1))
    done
    echo \"  [W\${worker_id}/GPU\${gpu_id}] Terminado (\${count} casos)\"
}

# ── Lanzar N workers ──
WPIDS=()
for i in \"\${!WORKER_GPUS[@]}\"; do
    gpu_worker \"\${WORKER_GPUS[\$i]}\" \"\$i\" &
    WPIDS+=(\$!)
done

# ── Esperar a que todos terminen ──
FAIL=0
for pid in \"\${WPIDS[@]}\"; do
    wait \"\$pid\" 2>/dev/null || FAIL=\$((FAIL+1))
done

# ── Resumen ──
echo \"\"
echo \"  ═══ Resumen de tanda ═══\"
TOTAL_OK=0; TOTAL_FAIL=0; TOTAL_SKIP=0
while read -r line; do
    case \"\$line\" in
        OK*)   TOTAL_OK=\$((TOTAL_OK+1)) ;;
        FAIL*) TOTAL_FAIL=\$((TOTAL_FAIL+1)) ;;
        SKIP*) TOTAL_SKIP=\$((TOTAL_SKIP+1)) ;;
    esac
done < \"\$RESULT_FILE\"

for gpu in ${available_gpus[*]}; do
    cnt=\$(grep -c \"GPU\${gpu}\" \"\$RESULT_FILE\" 2>/dev/null || echo 0)
    echo \"  GPU \${gpu}: \${cnt} casos\"
done
echo \"  OK: \${TOTAL_OK}  FAIL: \${TOTAL_FAIL}  SKIP: \${TOTAL_SKIP}\"

rm -f \"\$QUEUE_FILE\" \"\$LOCK_FILE\" \"\$RESULT_FILE\"
"

    if [[ $DRY_RUN -eq 1 ]]; then
        echo "  [DRY-RUN] ${ncases} casos → ${total_workers} workers"
        for i in "${!available_gpus[@]}"; do
            echo "    GPU ${available_gpus[$i]}: ${workers_per_gpu[$i]} workers"
        done
        echo "  Casos: ${cases[*]}"
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
echo "║  Distrib:  cola dinámica — N workers/GPU, overlap CPU+GPU"
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

# ── Ejecutar por tandas ───────────────────────────────────────────────────────
# Cada proceso Python ve AMBAS GPUs y elige la de más VRAM libre al arrancar.
# Así los primeros procesos saturan GPU 0, y los siguientes caen en GPU 1.
for p in $(seq 1 "$PARTS"); do
    if [[ $PART -gt 0 && $p -ne $PART ]]; then continue; fi
    
    CASES_STR=$(get_partition ALL_CASES "$PARTS" "$p")
    read -ra CASES_ARR <<< "$CASES_STR"
    
    echo "═══ Tanda ${p}/${PARTS} — ${#CASES_ARR[@]} casos ═══"
    run_batch "${CASES_ARR[@]}"
    
    if [[ $p -lt $PARTS && $PART -eq 0 ]]; then
        echo ""
        echo "--- Pausa 5s entre tandas (liberar VRAM) ---"
        sleep 5
    fi
done

ELAPSED_GLOBAL=$(( SECONDS - START_GLOBAL ))
echo ""
echo "╔══════════════════════════════════════════════════════════════╗"
echo "║  COMPLETADO en ${ELAPSED_GLOBAL}s                          "
echo "║  Logs: docker exec ${CONTAINER} ls /tmp/gpu_run_g${GRID}_logs/"
echo "╚══════════════════════════════════════════════════════════════╝"
