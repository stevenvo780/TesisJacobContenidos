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
#   # Ejecutar solo un caso específico (match parcial, case-insensitive)
#   ./gpu_run.sh --case clima
#   ./gpu_run.sh --case deforestacion --grid 500
#
#   # Forzar uso de una sola GPU
#   ./gpu_run.sh --gpu 0              # solo RTX 5070 Ti
#   ./gpu_run.sh --gpu 1 --case clima  # solo RTX 2060, caso clima
#
#   # Secuencial: un caso a la vez (para grids enormes que necesitan toda la VRAM)
#   ./gpu_run.sh --step-by-step --grid 5000
#   ./gpu_run.sh --step-by-step --gpu 0 --grid 3000
#
# ── FLAGS ─────────────────────────────────────────────────────────────────────
#
#   --grid SIZE     Grid size del ABM (default: auto = 200 × parts)
#   --parts N       Dividir en N tandas (1-10, default: 1 = todos de golpe)
#                   Sin --grid: auto-escala grid = 200 × N
#   --part K        Ejecutar solo tanda K de N (default: todas)
#   --case NOMBRE   Filtrar casos por nombre (match parcial, case-insensitive)
#                   Ej: --case clima → 01_caso_clima
#   --gpu N         Forzar uso de GPU N solamente (0 o 1)
#   --step-by-step  Ejecutar caso por caso secuencialmente (1 worker)
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
STEP_BY_STEP=0
CASE_FILTER=""
FORCE_GPU=-1

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
        --case)      CASE_FILTER="$2"; shift 2 ;;
        --gpu)       FORCE_GPU="$2";   shift 2 ;;
        --step-by-step) STEP_BY_STEP=1; shift ;;
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

# ── VRAM estimada por proceso (MB) ───────────────────────────────────────────
# Replica la lógica de abm_core_gpu.py:
#   1) Contexto CUDA: ~500 MB
#   2) B = min(n_runs, free×0.25 / (grid²×8×20))    ← factor 20 para B (conservador)
#   3) Pico = contexto + B × grid²×8×10 / 1048576   ← factor 10 (arrays vivas reales)
# Resultado: ligeramente por encima del pico real observado (seguro).
# Args: $1=grid  $2=gpu_free_MB(default 16000)  $3=n_runs(default 50)
estimate_vram_per_process() {
    local g=$1
    local gpu_free=${2:-16000}
    local nruns=${3:-${RUNS:-50}}
    local CUDA_CTX_MB=500
    # vram_per_sim para calcular B (factor 20, misma fórmula que Python)
    local vps_b=$(( g * g * 8 * 20 / 1048576 ))
    [[ $vps_b -lt 1 ]] && vps_b=1
    # Budget = 25% de VRAM libre
    local budget_mb=$(( gpu_free * 25 / 100 ))
    # B = min(n_runs, budget / vps)
    local b=$(( budget_mb / vps_b ))
    [[ $b -gt $nruns ]] && b=$nruns
    [[ $b -lt 1 ]] && b=1
    # Pico real: factor 10 (arrays vivas simultáneas, no el safety 20)
    local vps_real=$(( g * g * 8 * 10 / 1048576 ))
    [[ $vps_real -lt 1 ]] && vps_real=1
    local peak=$(( CUDA_CTX_MB + b * vps_real ))
    echo "$peak"
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
            # Si --gpu N está activo, solo incluir esa GPU
            if [[ $FORCE_GPU -ge 0 ]]; then
                if [[ "$gid" == "$FORCE_GPU" ]]; then
                    available_gpus+=("$gid")
                    gpu_free_mb+=("$gmb")
                fi
            else
                # Sin threshold fijo: incluir TODA GPU detectada.
                # El cálculo de vram_max_workers descartará las insuficientes.
                available_gpus+=("$gid")
                gpu_free_mb+=("$gmb")
            fi
        done <<< "$gpu_csv"
    fi
    # Fallback si no hay GPUs detectadas
    if [[ ${#available_gpus[@]} -eq 0 ]]; then
        if [[ $FORCE_GPU -ge 0 ]]; then
            echo "  WARN: GPU ${FORCE_GPU} no encontrada, usando GPU 0"
        fi
        available_gpus=(0)
        gpu_free_mb=(8000)
    fi
    
    # Calcular workers por GPU: suficientes para mantener CPU y GPU ocupadas
    # Mientras un proceso hace ABM en GPU, otros hacen calibración/datos en CPU.
    # Con grid grande, el ABM tarda mucho → necesitamos más workers CPU-bound.
    # Mínimo: max(ncores/ngpus, 4) workers por GPU para overlap CPU/GPU
    #
    # PERO: cada proceso CuPy crea un contexto CUDA (~500MB overhead).
    # Con 14 procesos en una GPU de 3.4GB libre → 7GB solo en contextos → OOM.
    # Por eso limitamos por VRAM: max_vram_workers = free / (500 + grid_vram_per_sim).
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
        
        # VRAM por proceso: contexto CUDA + 25% de VRAM libre (sub-batch de CuPy)
        local vram_per_process
        vram_per_process=$(estimate_vram_per_process "$GRID" "$free")
        
        # Cuántos procesos CuPy caben en esta GPU (VRAM-aware)
        local vram_max_workers=$(( free * 80 / 100 / (vram_per_process > 0 ? vram_per_process : 1) ))
        
        # Si la GPU no puede ni con 1 proceso, saltarla
        if [[ $vram_max_workers -lt 1 ]]; then
            echo "    GPU ${available_gpus[$i]}: ${free}MB libre → insuficiente (~${vram_per_process}MB/proceso), SALTADA"
            workers_per_gpu+=(0)
            continue
        fi
        
        # CPU-based minimum (para overlap CPU/GPU)
        local nw=$min_per_gpu
        
        # Cap por VRAM: nunca más workers de lo que la GPU soporta
        [[ $nw -gt $vram_max_workers ]] && nw=$vram_max_workers
        
        echo "    GPU ${available_gpus[$i]}: ${free}MB libre, ~${vram_per_process}MB/proceso → max ${vram_max_workers} por VRAM, candidatos: ${nw}"
        
        workers_per_gpu+=("$nw")
        total_workers=$((total_workers + nw))
    done
    
    # Si total_workers > ncases, reducir proporcionalmente manteniendo ambas GPUs
    if [[ $total_workers -gt $ncases ]]; then
        local excess=$((total_workers - ncases))
        total_workers=0
        # Reducir proporcionalmente, empezando por las GPUs con más workers
        for i in "${!workers_per_gpu[@]}"; do
            local nw=${workers_per_gpu[$i]}
            [[ $nw -eq 0 ]] && continue
            # Reducción proporcional: cada GPU cede en proporción a sus workers
            local total_nonzero=0
            for w in "${workers_per_gpu[@]}"; do total_nonzero=$((total_nonzero + w)); done
            if [[ $total_nonzero -gt 0 ]]; then
                local reduction=$(( excess * nw / total_nonzero ))
                nw=$((nw - reduction))
                [[ $nw -lt 1 ]] && nw=1
            fi
            workers_per_gpu[$i]=$nw
        done
        # Ajuste fino: recalcular total y recortar el exceso restante de la mayor
        total_workers=0
        for w in "${workers_per_gpu[@]}"; do total_workers=$((total_workers + w)); done
        while [[ $total_workers -gt $ncases ]]; do
            # Recortar 1 de la GPU con más workers
            local max_idx=0 max_val=0
            for i in "${!workers_per_gpu[@]}"; do
                if [[ ${workers_per_gpu[$i]} -gt $max_val ]]; then
                    max_val=${workers_per_gpu[$i]}
                    max_idx=$i
                fi
            done
            workers_per_gpu[$max_idx]=$((max_val - 1))
            total_workers=$((total_workers - 1))
        done
    fi
    
    # Construir mapa de workers → GPUs
    for i in "${!available_gpus[@]}"; do
        local nw=${workers_per_gpu[$i]}
        for ((w=0; w<nw; w++)); do
            worker_gpu_map+="${available_gpus[$i]} "
        done
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
export PYTHONIOENCODING=utf-8
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
echo \"  Logs: ${log_dir}/  (tail -f ${log_dir}/<caso>.log para detalle)\"

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
        
        (cd \"\$SRC\" && HYPER_GPU_DEVICE=\$gpu_id python3 validate.py 2>&1) | \
            tee \"\$LOG\" | \
            grep --line-buffered -E '(▶|[0-9]/6|FIN)' | \
            sed -u \"s/^/  [W\${worker_id}\\/GPU\${gpu_id}] /\"
        local RC=\${PIPESTATUS[0]}
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
echo "║  Casos:    ${TOTAL}$( [[ -n "$CASE_FILTER" ]] && echo " (filtro: ${CASE_FILTER})" )"
echo "║  GPUs:     ${N_GPUS} detectadas$( [[ $FORCE_GPU -ge 0 ]] && echo " → forzada GPU ${FORCE_GPU}" )"
echo "║  GPU 0:    ${GPU0_NAME} — ${GPU0_VRAM} MB"
[[ $N_GPUS -ge 2 ]] && \
echo "║  GPU 1:    ${GPU1_NAME} — ${GPU1_VRAM} MB"
echo "║  Distrib:  $( [[ $STEP_BY_STEP -eq 1 ]] && { [[ $FORCE_GPU -ge 0 || $N_GPUS -lt 2 ]] && echo "SECUENCIAL — 1 caso a la vez, 1 GPU" || echo "SECUENCIAL — 1 caso/GPU, ${N_GPUS} GPUs en paralelo"; } || echo "cola dinámica — N workers/GPU, overlap CPU+GPU" )"
echo "║  Params:   perm=${PERM} boot=${BOOT} refine=${REFINE} runs=${RUNS}"
echo "║  Contendr: ${CONTAINER}"
echo "║  VRAM/proc: ~$(estimate_vram_per_process $GRID) MB"
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

# ── Ejecutar por tandas ───────────────────────────────────────────────────────────────────
if [[ $STEP_BY_STEP -eq 1 ]]; then
    # ── Modo secuencial: 1 caso por GPU, todas las GPUs en paralelo ──
    # Con --gpu N: solo 1 GPU → puramente secuencial
    # Sin --gpu: N GPUs → N casos simultáneos (1 por GPU)
    
    # Determinar GPUs disponibles para step-by-step
    sbs_gpus=()
    if [[ $FORCE_GPU -ge 0 ]]; then
        sbs_gpus=($FORCE_GPU)
    else
        for ((g=0; g<N_GPUS; g++)); do
            sbs_gpus+=($g)
        done
    fi
    n_sbs_gpus=${#sbs_gpus[@]}
    
    if [[ $n_sbs_gpus -eq 1 ]]; then
        echo "═══ Modo SECUENCIAL — ${TOTAL} casos, 1 a la vez ═══"
        echo "  GPU: ${sbs_gpus[0]} (toda la VRAM para cada caso)"
    else
        echo "═══ Modo SECUENCIAL — ${TOTAL} casos, ${n_sbs_gpus} GPUs (1 caso/GPU) ═══"
        for g in "${sbs_gpus[@]}"; do
            echo "  GPU ${g}: 1 caso a la vez"
        done
    fi
    
    TOTAL_OK=0; TOTAL_FAIL=0; TOTAL_SKIP=0
    
    # Función para ejecutar un caso en una GPU específica
    _run_step_case() {
        local caso=$1
        local gpu=$2
        local idx=$3
        local total=$4
        local tag="GPU${gpu}"
        
        echo "  [${idx}/${total}] ▶ ${caso} (${tag})"
        if [[ $DRY_RUN -eq 1 ]]; then
            echo "  [DRY-RUN] ${caso}"
            return 0
        fi
        
        local inner="
export PYTHONIOENCODING=utf-8
export HYPER_GRID_SIZE=${GRID}
export HYPER_N_PERM=${PERM}
export HYPER_N_BOOT=${BOOT}
export HYPER_N_REFINE=${REFINE}
export HYPER_N_RUNS=${RUNS}
mkdir -p /tmp/gpu_run_g${GRID}_logs
SRC=/workspace/repos/Simulaciones/${caso}/src
if [ ! -f \"\${SRC}/validate.py\" ]; then echo SKIP; exit 0; fi
cd \"\${SRC}\" && HYPER_GPU_DEVICE=${gpu} python3 validate.py
"
        local t0=$SECONDS
        docker exec "$CONTAINER" bash -c "$inner" > >(tee /tmp/gpu_step_${caso}.log) 2>&1
        local rc=$?
        local elapsed=$(( SECONDS - t0 ))
        local edi=$(grep -oP 'EDI[=:]\s*-?[\d.]+' /tmp/gpu_step_${caso}.log 2>/dev/null | tail -1 || echo '?')
        
        if [[ $rc -eq 0 ]]; then
            echo "  [${idx}/${total}] ✓ ${caso} (${tag}) — ${elapsed}s — ${edi}"
            return 0
        else
            echo "  [${idx}/${total}] ✗ ${caso} (${tag}) — ${elapsed}s (exit ${rc})"
            return 1
        fi
    }
    
    i=0
    while [[ $i -lt $TOTAL ]]; do
        echo ""
        # Lanzar hasta n_sbs_gpus casos en paralelo (1 por GPU)
        pids=()
        pid_casos=()
        pid_gpus=()
        
        for ((g_idx=0; g_idx<n_sbs_gpus && i<TOTAL; g_idx++)); do
            caso=${ALL_CASES[$i]}
            gpu=${sbs_gpus[$g_idx]}
            i=$((i+1))
            
            _run_step_case "$caso" "$gpu" "$i" "$TOTAL" &
            pids+=($!)
            pid_casos+=("$caso")
            pid_gpus+=("$gpu")
        done
        
        # Esperar a que terminen todos los de esta ronda
        for ((p_idx=0; p_idx<${#pids[@]}; p_idx++)); do
            wait ${pids[$p_idx]}
            rc=$?
            if [[ $rc -eq 0 ]]; then
                TOTAL_OK=$((TOTAL_OK+1))
            else
                TOTAL_FAIL=$((TOTAL_FAIL+1))
            fi
        done
    done
    
    echo ""
    echo "  ═══ Resumen secuencial ═══"
    echo "  OK: ${TOTAL_OK}  FAIL: ${TOTAL_FAIL}"
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
