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
#   # Todo de golpe (29 en paralelo, grid por caso)
#   ./gpu_run.sh
#
#   # Dry-run (muestra plan sin ejecutar)
#   ./gpu_run.sh --parts 5 --dry-run
#
#   # Ejecutar solo un caso específico (match parcial, case-insensitive)
#   ./gpu_run.sh --case clima
#
#   # Forzar uso de una sola GPU
#   ./gpu_run.sh --gpu 0              # solo RTX 5070 Ti
#   ./gpu_run.sh --gpu 1 --case clima  # solo RTX 2060, caso clima
#
#   # Escalado de grid (ponderado por tamaño base)
#   ./gpu_run.sh --grid-mult 2
#
#   # Secuencial: un caso a la vez (para grids enormes que necesitan toda la VRAM)
#   ./gpu_run.sh --step-by-step
#   ./gpu_run.sh --step-by-step --gpu 0
#
# ── FLAGS ─────────────────────────────────────────────────────────────────────
#
#   --parts N       Dividir en N tandas (1-10, default: 1 = todos de golpe)
#   --part K        Ejecutar solo tanda K de N (default: todas)
#   --case NOMBRE   Filtrar casos por nombre (match parcial, case-insensitive)
#                   Ej: --case clima → 01_caso_clima
#   --gpu N         Forzar uso de GPU N solamente (0 o 1)
#   --step-by-step  Ejecutar caso por caso secuencialmente (1 worker)
#   --perm N        Permutaciones EDI (default: 9999)
#   --boot N        Bootstrap samples (default: 5000)
#   --refine N      Iteraciones refinamiento (default: 50000)
#   --runs N        N_RUNS para C5 (default: 50)
#   --grid-mult X   Multiplicador de grid (ponderado por tamaño base)
#   --container C   Nombre del contenedor Docker (default: tesis-gpu)
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
CASE_TIMEOUT=0       # 0 = auto (según grid máximo del lote)
GRID_MULT="1.0"

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
        --parts)     PARTS="$2";     shift 2 ;;
        --part)      PART="$2";      shift 2 ;;
        --perm)      PERM="$2";      shift 2 ;;
        --boot)      BOOT="$2";      shift 2 ;;
        --refine)    REFINE="$2";    shift 2 ;;
        --runs)      RUNS="$2";      shift 2 ;;
        --grid-mult) GRID_MULT="$2"; shift 2 ;;
        --container) CONTAINER="$2"; shift 2 ;;
        --case)      CASE_FILTER="$2"; shift 2 ;;
        --gpu)       FORCE_GPU="$2";   shift 2 ;;
        --timeout)   CASE_TIMEOUT="$2"; shift 2 ;;
        --step-by-step) STEP_BY_STEP=1; shift ;;
        --dry-run)   DRY_RUN=1;      shift ;;
        --help|-h)
            head -40 "$0" | tail -36
            exit 0 ;;
        *) echo "Flag desconocido: $1"; exit 1 ;;
    esac
done

# ── Auto timeout por lote ────────────────────────────────────────────────────
# Si no se especificó --timeout, se calcula tras resolver grids por caso.

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

# ── Grid por caso (desde validate.py) ─────────────────────────────────────────
declare -A CASE_GRID
declare -A CASE_GRID_BASE
declare -A CASE_TOPOLOGY
build_case_grid_map() {
    local cases=("$@")
    local out
    out=$(SIM_DIR="$SIM_DIR" GRID_MULT="$GRID_MULT" python3 - <<'PY' "${cases[@]}"
import os, re, sys, pathlib, json
sim_dir = pathlib.Path(os.environ["SIM_DIR"])
grid_mult = float(os.environ.get("GRID_MULT", "1.0"))
cases = sys.argv[1:]

def weight_for_grid(base):
    if base <= 10:
        return 0.0
    return min(1.0, max(0.0, (base - 10) / 15.0))

for c in cases:
    base = 1
    use_topo = False

    # Primero: intentar leer case_config.json (fuente canónica)
    cfg_path = sim_dir / c / "case_config.json"
    if cfg_path.exists():
        try:
            cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
            base = int(cfg.get("execution", {}).get("grid_size", base))
        except (json.JSONDecodeError, KeyError, ValueError):
            pass  # fallback al scraping

    # Fallback: leer validate.py si case_config.json no tenía grid_size
    path = sim_dir / c / "src" / "validate.py"
    if base <= 1 and path.exists():
        text = path.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"grid_size\s*=\s*(\d+)", text)
        if m:
            base = int(m.group(1))

    # Detectar topology desde validate.py
    if path.exists():
        text = path.read_text(encoding="utf-8", errors="ignore")
        if re.search(r"use_topology\s*=\s*True", text):
            use_topo = True

    scaled = base
    if grid_mult != 1.0:
        w = weight_for_grid(base)
        factor = 1.0 + (grid_mult - 1.0) * w
        scaled = int(round(base * factor))
        if scaled < base:
            scaled = base
    if use_topo and scaled > 50:
        scaled = 50
    print(f"{c} {base} {scaled} {1 if use_topo else 0}")
PY
)
    local max_g=1
    while read -r c base scaled topo; do
        [[ -z "$c" ]] && continue
        CASE_GRID["$c"]="$scaled"
        CASE_GRID_BASE["$c"]="$base"
        CASE_TOPOLOGY["$c"]="$topo"
        if [[ "$scaled" -gt "$max_g" ]]; then
            max_g="$scaled"
        fi
    done <<< "$out"
    echo "$max_g"
}

grid_timeout() {
    local g=$1
    local t=$(( g * g / 300 ))
    [[ $t -lt 600 ]] && t=600
    [[ $t -gt 14400 ]] && t=14400
    echo "$t"
}

MAX_GRID=$(build_case_grid_map "${ALL_CASES[@]}")
if [[ $CASE_TIMEOUT -eq 0 ]]; then
    CASE_TIMEOUT=$(grid_timeout "$MAX_GRID")
fi

# ── VRAM estimada por proceso (MB) ───────────────────────────────────────────
# Replica la lógica de abm_core_gpu.py con márgenes más conservadores:
#   1) Contexto CuPy+CUDA: ~900 MB (medido empíricamente, incluye runtime,
#      memory pool, driver overhead — NO los 500 originales que subestimaban)
#   2) B = min(n_runs, free×0.20 / (grid²×8×20))    ← 20% VRAM budget (no 25%)
#   3) Pico = contexto + B × grid²×8×10 / 1048576
# Resultado: conservador — evita OOM cuando múltiples procesos comparten GPU.
# Args: $1=grid  $2=gpu_free_MB(default 16000)  $3=n_runs(default 50)
estimate_vram_per_process() {
    local g=$1
    local gpu_free=${2:-16000}
    local nruns=${3:-${RUNS:-50}}
    local CUDA_CTX_MB=900   # CuPy context + CUDA runtime + memory pool
    # vram_per_sim para calcular B (factor 20, misma fórmula que Python)
    local vps_b=$(( g * g * 8 * 20 / 1048576 ))
    [[ $vps_b -lt 1 ]] && vps_b=1
    # Budget = 20% de VRAM libre (conservador — múltiples procesos compiten)
    local budget_mb=$(( gpu_free * 20 / 100 ))
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

# ── Asignación de casos a GPUs por tamaño de grid ────────────────────────────
# Usa carga relativa (grid²) y VRAM libre para enviar casos grandes a GPU grande.
declare -a AVAILABLE_GPUS=()
declare -a GPU_FREE_MB=()
declare -A GPU_CASES=()
declare -A GPU_MAX_GRID=()

assign_cases_to_gpus() {
    local cases=("$@")
    local -A gpu_load=()
    GPU_CASES=()
    GPU_MAX_GRID=()
    for i in "${!AVAILABLE_GPUS[@]}"; do
        local gid="${AVAILABLE_GPUS[$i]}"
        gpu_load["$gid"]=0
        GPU_CASES["$gid"]=""
        GPU_MAX_GRID["$gid"]=0
    done

    local sorted
    sorted=$(for c in "${cases[@]}"; do
        local g="${CASE_GRID[$c]:-1}"
        echo "$g $c"
    done | sort -nr | awk '{print $2}')

    for c in $sorted; do
        local g="${CASE_GRID[$c]:-1}"
        local w=$(( g * g ))
        local best_gid=""
        local best_ratio=0
        local best_cap=0
        for i in "${!AVAILABLE_GPUS[@]}"; do
            local gid="${AVAILABLE_GPUS[$i]}"
            local cap="${GPU_FREE_MB[$i]}"
            local load="${gpu_load[$gid]:-0}"
            [[ $cap -le 0 ]] && cap=1
            local ratio=$(( load * 1000 / cap ))
            if [[ -z "$best_gid" || $ratio -lt $best_ratio || ( $ratio -eq $best_ratio && $cap -gt $best_cap ) ]]; then
                best_gid="$gid"
                best_ratio="$ratio"
                best_cap="$cap"
            fi
        done
        GPU_CASES["$best_gid"]+="${c} "
        gpu_load["$best_gid"]=$(( gpu_load["$best_gid"] + w ))
        if [[ $g -gt ${GPU_MAX_GRID[$best_gid]:-0} ]]; then
            GPU_MAX_GRID["$best_gid"]="$g"
        fi
    done

    for i in "${!AVAILABLE_GPUS[@]}"; do
        local gid="${AVAILABLE_GPUS[$i]}"
        GPU_CASES["$gid"]=$(echo "${GPU_CASES[$gid]}" | xargs)
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
    AVAILABLE_GPUS=()
    GPU_FREE_MB=()
    local gpu_csv
    gpu_csv=$(nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits 2>/dev/null)
    if [[ -n "$gpu_csv" ]]; then
        while IFS=', ' read -r gid gmb; do
            gid=$(echo "$gid" | tr -d ' ')
            gmb=$(echo "$gmb" | tr -d ' ')
            # Si --gpu N está activo, solo incluir esa GPU
            if [[ $FORCE_GPU -ge 0 ]]; then
                if [[ "$gid" == "$FORCE_GPU" ]]; then
                    AVAILABLE_GPUS+=("$gid")
                    GPU_FREE_MB+=("$gmb")
                fi
            else
                # Sin threshold fijo: incluir TODA GPU detectada.
                # El cálculo de vram_max_workers descartará las insuficientes.
                AVAILABLE_GPUS+=("$gid")
                GPU_FREE_MB+=("$gmb")
            fi
        done <<< "$gpu_csv"
    fi
    # Fallback si no hay GPUs detectadas
    if [[ ${#AVAILABLE_GPUS[@]} -eq 0 ]]; then
        if [[ $FORCE_GPU -ge 0 ]]; then
            echo "  WARN: GPU ${FORCE_GPU} no encontrada, usando GPU 0"
        fi
        AVAILABLE_GPUS=(0)
        GPU_FREE_MB=(8000)
    fi

    # Asignar casos a GPUs según tamaño de grid
    assign_cases_to_gpus "${cases[@]}"
    
    # Calcular workers por GPU: suficientes para mantener CPU y GPU ocupadas
    # Mientras un proceso hace ABM en GPU, otros hacen calibración/datos en CPU.
    # Con grid grande, el ABM tarda mucho → necesitamos más workers CPU-bound.
    # Mínimo: max(ncores/ngpus, 4) workers por GPU para overlap CPU/GPU
    #
    # PERO: cada proceso CuPy crea un contexto CUDA (~500MB overhead).
    # Con 14 procesos en una GPU de 3.4GB libre → 7GB solo en contextos → OOM.
    # Por eso limitamos por VRAM: max_vram_workers = free / (900 + grid_vram_per_sim).
    # Cap conservador (65%) para dejar margen a fragmentación y memory pool.
    local total_workers=0
    local -a workers_per_gpu=()
    local worker_gpu_map=""  # "0 0 0 1 1" — qué GPU para cada worker
    
    # Detectar cores CPU disponibles
    local ncores
    ncores=$(nproc 2>/dev/null || echo 8)
    local ngpus=${#AVAILABLE_GPUS[@]}
    # Workers mínimos por GPU: balancear CPU entre GPUs, mínimo 4
    local min_per_gpu=$(( ncores / ngpus ))
    [[ $min_per_gpu -lt 4 ]] && min_per_gpu=4
    [[ $min_per_gpu -gt 15 ]] && min_per_gpu=15  # cap razonable
    
    for i in "${!AVAILABLE_GPUS[@]}"; do
        local gid="${AVAILABLE_GPUS[$i]}"
        local free=${GPU_FREE_MB[$i]}
        local max_grid="${GPU_MAX_GRID[$gid]:-1}"
        
        # VRAM por proceso: contexto CuPy+CUDA (~900MB) + arrays de trabajo
        local vram_per_process
        vram_per_process=$(estimate_vram_per_process "$max_grid" "$free")
        
        # Cuántos procesos CuPy caben en esta GPU (65% VRAM — conservador)
        # 65% (no 80%) → margen para fragmentación, memory pool, driver overhead
        local vram_max_workers=$(( free * 65 / 100 / (vram_per_process > 0 ? vram_per_process : 1) ))
        
        # Guard: si la GPU no tiene al menos 1.5× lo que necesita 1 proceso, saltarla
        local min_vram_for_one=$(( vram_per_process * 3 / 2 ))
        if [[ $free -lt $min_vram_for_one ]]; then
            echo "    GPU ${gid}: ${free}MB libre < ${min_vram_for_one}MB mínimo (1.5×${vram_per_process}MB), SALTADA"
            workers_per_gpu+=(0)
            continue
        fi
        
        # Si la GPU no puede ni con 1 proceso por VRAM, saltarla
        if [[ $vram_max_workers -lt 1 ]]; then
            echo "    GPU ${gid}: ${free}MB libre → insuficiente (~${vram_per_process}MB/proceso), SALTADA"
            workers_per_gpu+=(0)
            continue
        fi
        
        # CPU-based minimum (para overlap CPU/GPU)
        local nw=$min_per_gpu
        
        # Cap por VRAM: nunca más workers de lo que la GPU soporta
        [[ $nw -gt $vram_max_workers ]] && nw=$vram_max_workers
        
        echo "    GPU ${gid}: ${free}MB libre, grid_max=${max_grid}, ~${vram_per_process}MB/proceso → max ${vram_max_workers} por VRAM, candidatos: ${nw}"
        
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
    for i in "${!AVAILABLE_GPUS[@]}"; do
        local nw=${workers_per_gpu[$i]}
        for ((w=0; w<nw; w++)); do
            worker_gpu_map+="${AVAILABLE_GPUS[$i]} "
        done
    done
    
    # No más workers que casos
    [[ $total_workers -gt $ncases ]] && total_workers=$ncases
    
    echo "  Workers: ${total_workers} (${#AVAILABLE_GPUS[@]} GPUs: ${AVAILABLE_GPUS[*]})"
    for i in "${!AVAILABLE_GPUS[@]}"; do
        local gid="${AVAILABLE_GPUS[$i]}"
        echo "    GPU ${gid}: ${workers_per_gpu[$i]} workers (${GPU_FREE_MB[$i]}MB libre, grid_max=${GPU_MAX_GRID[$gid]:-1})"
    done
    echo "  Modo: cola dinámica — ${total_workers} workers, la GPU rápida toma más"
    
    local log_dir="/tmp/gpu_run_logs"
    local cases_str="${cases[*]}"
    # Trim trailing space
    worker_gpu_map=$(echo "$worker_gpu_map" | xargs)
    local gpu_cases_decl=""
    for gid in "${AVAILABLE_GPUS[@]}"; do
        local clist="${GPU_CASES[$gid]}"
        gpu_cases_decl+="CASES_GPU_${gid}=(${clist})"$'\n'
    done
    local grid_map_decl="declare -A CASE_GRID_MAP"$'\n'
    for c in "${cases[@]}"; do
        local g="${CASE_GRID[$c]:-1}"
        grid_map_decl+="CASE_GRID_MAP[\"${c}\"]=${g}"$'\n'
    done

    local inner_script="
export PYTHONIOENCODING=utf-8
export HYPER_N_PERM=${PERM}
export HYPER_N_BOOT=${BOOT}
export HYPER_N_REFINE=${REFINE}
export HYPER_N_RUNS=${RUNS}

trap 'kill \$(jobs -p) 2>/dev/null; wait; exit 130' INT TERM

mkdir -p ${log_dir}

RUN_ID=\$\$
RESULT_FILE=/tmp/_gpu_results_\${RUN_ID}
touch \"\$RESULT_FILE\"

${gpu_cases_decl}
${grid_map_decl}

# Colas por GPU
for gid in ${AVAILABLE_GPUS[*]}; do
    q=\"/tmp/_gpu_queue_\${RUN_ID}_gpu\${gid}\"
    eval \"printf '%s\\n' \\\"\\\${CASES_GPU_\${gid}[@]}\\\" > \\\"\\\$q\\\"\"
    touch \"\${q}.lock\"
done

WORKER_GPUS=(${worker_gpu_map})
N_WORKERS=\${#WORKER_GPUS[@]}

echo \"[\${#WORKER_GPUS[@]} workers, ${#AVAILABLE_GPUS[@]} GPUs] Casos: ${cases_str}\"
echo \"  Logs: ${log_dir}/  (tail -f ${log_dir}/<caso>.log para detalle)\"

# ── Worker: toma casos de la cola hasta vaciarla ──
gpu_worker() {
    local gpu_id=\$1
    local worker_id=\$2
    local count=0
    
    while true; do
        # Pop atómico del primer caso de la cola de su GPU
        local caso
        local QUEUE_FILE=\"/tmp/_gpu_queue_\${RUN_ID}_gpu\${gpu_id}\"
        local LOCK_FILE=\"\${QUEUE_FILE}.lock\"
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
        
        # Timeout: matar procesos colgados (OOM, hang en CuPy, etc.)
        local TIMEOUT=${CASE_TIMEOUT}
        local GRID_CASE=\${CASE_GRID_MAP[\$caso]:-}
        timeout --signal=KILL \$TIMEOUT bash -c 'cd \"\$1\" && HYPER_GPU_DEVICE=\$2 HYPER_GRID_SIZE=\$3 python3 validate.py 2>&1' _ \"\$SRC\" \"\$gpu_id\" \"\$GRID_CASE\" | \
            tee \"\$LOG\" | \
            grep --line-buffered -E '(▶|[0-9]/6|FIN)' | \
            sed -u \"s/^/  [W\${worker_id}\\/GPU\${gpu_id}] /\"
        local RC=\${PIPESTATUS[0]}
        local ELAPSED=\$((\$SECONDS - \$START))
        echo \"ELAPSED=\${ELAPSED}s\" >> \"\$LOG\"
        
        local EDI=\$(grep -oP 'EDI[=:]\s*-?[\\d.]+' \"\$LOG\" 2>/dev/null | tail -1 || echo '?')
        
        if [ \$RC -eq 137 ]; then
            echo \"  [W\${worker_id}/GPU\${gpu_id}] ⏰ \${caso} — TIMEOUT \${TIMEOUT}s (killed)\"
            echo \"TIMEOUT \${caso} GPU\${gpu_id} \${TIMEOUT}s\" >> \"\$RESULT_FILE\"
        elif [ \$RC -eq 0 ]; then
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
TOTAL_OK=0; TOTAL_FAIL=0; TOTAL_SKIP=0; TOTAL_TIMEOUT=0
while read -r line; do
    case \"\$line\" in
        OK*)      TOTAL_OK=\$((TOTAL_OK+1)) ;;
        FAIL*)    TOTAL_FAIL=\$((TOTAL_FAIL+1)) ;;
        SKIP*)    TOTAL_SKIP=\$((TOTAL_SKIP+1)) ;;
        TIMEOUT*) TOTAL_TIMEOUT=\$((TOTAL_TIMEOUT+1)) ;;
    esac
done < \"\$RESULT_FILE\"

for gpu in ${AVAILABLE_GPUS[*]}; do
    cnt=\$(grep -c \"GPU\${gpu}\" \"\$RESULT_FILE\" 2>/dev/null || echo 0)
    echo \"  GPU \${gpu}: \${cnt} casos\"
done
echo \"  OK: \${TOTAL_OK}  FAIL: \${TOTAL_FAIL}  TIMEOUT: \${TOTAL_TIMEOUT}  SKIP: \${TOTAL_SKIP}\"

rm -f /tmp/_gpu_queue_\${RUN_ID}_gpu* /tmp/_gpu_queue_\${RUN_ID}_gpu*.lock \"\$RESULT_FILE\"
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
echo "║  Grid:     por caso (max=${MAX_GRID})"
echo "║  Parts:    ${PARTS}  $([ $PART -gt 0 ] && echo "(solo parte ${PART})" || echo "(todas)")"
echo "║  Casos:    ${TOTAL}$( [[ -n "$CASE_FILTER" ]] && echo " (filtro: ${CASE_FILTER})" )"
echo "║  GPUs:     ${N_GPUS} detectadas$( [[ $FORCE_GPU -ge 0 ]] && echo " → forzada GPU ${FORCE_GPU}" )"
echo "║  GPU 0:    ${GPU0_NAME} — ${GPU0_VRAM} MB"
[[ $N_GPUS -ge 2 ]] && \
echo "║  GPU 1:    ${GPU1_NAME} — ${GPU1_VRAM} MB"
echo "║  Distrib:  $( [[ $STEP_BY_STEP -eq 1 ]] && { [[ $FORCE_GPU -ge 0 || $N_GPUS -lt 2 ]] && echo "SECUENCIAL — 1 caso a la vez, 1 GPU" || echo "SECUENCIAL — cola compartida, ${N_GPUS} GPUs independientes"; } || echo "cola dinámica — N workers/GPU, overlap CPU+GPU" )"
echo "║  Params:   perm=${PERM} boot=${BOOT} refine=${REFINE} runs=${RUNS}"
echo "║  GridMult: ${GRID_MULT} (ponderado)"
echo "║  Timeout:  ${CASE_TIMEOUT}s por caso"
echo "║  Contendr: ${CONTAINER}"
echo "║  VRAM/proc: ~$(estimate_vram_per_process $MAX_GRID) MB"
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
    # ── Modo secuencial: 1 caso por GPU, GPUs INDEPENDIENTES ──
    # Cada GPU tiene su propia cola y procesa sin esperar a la otra.
    # Con --gpu N: solo 1 GPU → puramente secuencial.
    # Sin --gpu: N GPUs → N colas independientes, la GPU rápida toma más casos.
    
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
        echo "═══ Modo SECUENCIAL — ${TOTAL} casos, ${n_sbs_gpus} GPUs INDEPENDIENTES ═══"
        echo "  Cada GPU toma casos de una cola compartida (la más rápida hace más)"
        for g in "${sbs_gpus[@]}"; do
            echo "  GPU ${g}: 1 caso a la vez"
        done
    fi
    
    TOTAL_OK=0; TOTAL_FAIL=0; TOTAL_SKIP=0
    
    LOG_DIR="/tmp/gpu_run_logs"
    mkdir -p "$LOG_DIR"   # crear dir localmente para tee
    QUEUE_DIR=$(mktemp -d /tmp/_sbs_queue_XXXXXX)
    RESULT_FILE=$(mktemp /tmp/_sbs_results_XXXXXX)
    touch "$RESULT_FILE"

    # VRAM libre por GPU (solo las usadas en step-by-step)
    AVAILABLE_GPUS=()
    GPU_FREE_MB=()
    gpu_csv=$(nvidia-smi --query-gpu=index,memory.free --format=csv,noheader,nounits 2>/dev/null)
    if [[ -n "$gpu_csv" ]]; then
        while IFS=', ' read -r gid gmb; do
            gid=$(echo "$gid" | tr -d ' ')
            gmb=$(echo "$gmb" | tr -d ' ')
            if [[ " ${sbs_gpus[*]} " == *" ${gid} "* ]]; then
                AVAILABLE_GPUS+=("$gid")
                GPU_FREE_MB+=("$gmb")
            fi
        done <<< "$gpu_csv"
    fi
    if [[ ${#AVAILABLE_GPUS[@]} -eq 0 ]]; then
        AVAILABLE_GPUS=("${sbs_gpus[@]}")
        for _ in "${sbs_gpus[@]}"; do GPU_FREE_MB+=(8000); done
    fi

    # Asignar casos a GPUs por tamaño de grid
    assign_cases_to_gpus "${ALL_CASES[@]}"

    for gid in "${sbs_gpus[@]}"; do
        q="${QUEUE_DIR}/gpu${gid}"
        printf '%s\n' ${GPU_CASES[$gid]:-} > "$q"
        touch "${q}.lock"
    done
    
    # Función: loop de GPU independiente — toma casos de cola compartida
    _gpu_loop() {
        local gpu=$1
        local tag="GPU${gpu}"
        local count=0
        
        while true; do
            # Pop atómico de la cola compartida
            local caso
            local QUEUE_FILE="${QUEUE_DIR}/gpu${gpu}"
            local LOCK_FILE="${QUEUE_FILE}.lock"
            caso=$(flock "$LOCK_FILE" bash -c '
                head -1 "$1" 2>/dev/null
                sed -i "1d" "$1" 2>/dev/null
            ' -- "$QUEUE_FILE")
            
            [[ -z "$caso" ]] && break
            count=$((count + 1))
            
            local SRC="/workspace/repos/Simulaciones/${caso}/src"
            local LOG="${LOG_DIR}/${caso}.log"
            local GRID_CASE=${CASE_GRID[$caso]:-1}
            
            echo "  [${tag}] ▶ ${caso}"
            if [[ $DRY_RUN -eq 1 ]]; then
                echo "  [DRY-RUN] ${caso}"
                echo "OK ${caso} ${tag} 0s" >> "$RESULT_FILE"
                continue
            fi
            
            local inner="
export PYTHONIOENCODING=utf-8
export HYPER_GRID_SIZE=${GRID_CASE}
export HYPER_N_PERM=${PERM}
export HYPER_N_BOOT=${BOOT}
export HYPER_N_REFINE=${REFINE}
export HYPER_N_RUNS=${RUNS}
mkdir -p ${LOG_DIR}
SRC=/workspace/repos/Simulaciones/${caso}/src
if [ ! -f \"\${SRC}/validate.py\" ]; then echo SKIP; exit 0; fi
cd \"\${SRC}\" && timeout --signal=KILL ${CASE_TIMEOUT} bash -c 'HYPER_GPU_DEVICE=${gpu} python3 validate.py' 2>&1
"
            local t0=$SECONDS
            docker exec "$CONTAINER" bash -c "$inner" 2>&1 | tee "$LOG"
            local rc=${PIPESTATUS[0]}
            local elapsed=$(( SECONDS - t0 ))
            local edi=$(grep -oP 'EDI[=:]\s*-?[\d.]+' "$LOG" 2>/dev/null | tail -1 || echo '?')
            
            if [[ $rc -eq 137 ]]; then
                echo "  [${tag}] ⏰ ${caso} — TIMEOUT ${CASE_TIMEOUT}s"
                echo "TIMEOUT ${caso} ${tag} ${CASE_TIMEOUT}s" >> "$RESULT_FILE"
            elif [[ $rc -eq 0 ]]; then
                echo "  [${tag}] ✓ ${caso} — ${elapsed}s — ${edi}"
                echo "OK ${caso} ${tag} ${elapsed}s ${edi}" >> "$RESULT_FILE"
            else
                echo "  [${tag}] ✗ ${caso} — ${elapsed}s (exit ${rc})"
                echo "FAIL ${caso} ${tag} ${elapsed}s exit=${rc}" >> "$RESULT_FILE"
            fi
        done
        echo "  [${tag}] Terminado (${count} casos)"
    }
    
    # Lanzar un loop por GPU, todos comparten la misma cola
    GPU_PIDS=()
    for g in "${sbs_gpus[@]}"; do
        _gpu_loop "$g" &
        GPU_PIDS+=($!)
    done
    
    # Esperar a que todas las GPUs terminen su cola
    for pid in "${GPU_PIDS[@]}"; do
        wait "$pid" 2>/dev/null || true
    done
    
    # Resumen
    echo ""
    echo "  ═══ Resumen secuencial ═══"
    while read -r line; do
        case "$line" in
            OK*)      TOTAL_OK=$((TOTAL_OK+1)) ;;
            FAIL*)    TOTAL_FAIL=$((TOTAL_FAIL+1)) ;;
            SKIP*)    TOTAL_SKIP=$((TOTAL_SKIP+1)) ;;
            TIMEOUT*) TOTAL_FAIL=$((TOTAL_FAIL+1)) ;;
        esac
    done < "$RESULT_FILE"
    for g in "${sbs_gpus[@]}"; do
        cnt=$(grep -c "GPU${g}" "$RESULT_FILE" 2>/dev/null || echo 0)
        echo "  GPU ${g}: ${cnt} casos"
    done
    echo "  OK: ${TOTAL_OK}  FAIL: ${TOTAL_FAIL}  SKIP: ${TOTAL_SKIP}"
    rm -rf "$QUEUE_DIR" "$RESULT_FILE"
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
echo "║  Logs: docker exec ${CONTAINER} ls /tmp/gpu_run_logs/"
echo "╚══════════════════════════════════════════════════════════════╝"
