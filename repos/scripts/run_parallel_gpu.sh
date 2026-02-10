#!/bin/bash
# run_parallel_gpu.sh — Ejecuta TODOS los casos EN PARALELO dentro de Docker
# Usa los 32 cores + GPU simultáneamente.
# Cada caso es un proceso independiente. CUDA maneja concurrencia.

set -uo pipefail

export HYPER_N_PERM=9999
export HYPER_N_BOOT=5000
export HYPER_N_REFINE=50000
export HYPER_GRID_SIZE=200
export HYPER_N_RUNS=50

WORKSPACE="/workspace/repos/Simulaciones"
LOG_DIR="/tmp/parallel_logs"
mkdir -p "$LOG_DIR"

# Los 6 casos escalables
CASES=(
    "16_caso_deforestacion"
    "24_caso_microplasticos"
    "27_caso_riesgo_biologico"
    "13_caso_politicas_estrategicas"
    "21_caso_salinizacion"
    "06_caso_falsacion_exogeneidad"
)

echo "=== PARALLEL GPU RUN === $(date)"
echo "CASES: ${#CASES[@]}  GRID=$HYPER_GRID_SIZE  PERM=$HYPER_N_PERM  REFINE=$HYPER_N_REFINE  RUNS=$HYPER_N_RUNS"
echo "Launching all cases simultaneously..."
echo ""

PIDS=()
for case in "${CASES[@]}"; do
    SRC="$WORKSPACE/$case/src"
    LOG="$LOG_DIR/${case}.log"
    
    if [ ! -f "$SRC/validate.py" ]; then
        echo "[SKIP] $case — no validate.py"
        continue
    fi
    
    echo "[LAUNCH] $case → $LOG"
    (
        cd "$SRC"
        START=$SECONDS
        python3 validate.py > "$LOG" 2>&1
        ELAPSED=$(( SECONDS - START ))
        echo "ELAPSED=${ELAPSED}s" >> "$LOG"
    ) &
    PIDS+=($!)
done

echo ""
echo "All ${#PIDS[@]} cases launched. PIDs: ${PIDS[*]}"
echo "Waiting for completion..."
echo ""

# Esperar a que todos terminen
FAILURES=0
for i in "${!CASES[@]}"; do
    case="${CASES[$i]}"
    pid="${PIDS[$i]}"
    if wait "$pid"; then
        STATUS="OK"
    else
        STATUS="FAIL"
        FAILURES=$((FAILURES + 1))
    fi
    LOG="$LOG_DIR/${case}.log"
    ELAPSED=$(grep "^ELAPSED=" "$LOG" 2>/dev/null | cut -d= -f2 || echo "?")
    EDI=$(grep -oP 'EDI[=:]\s*[\d.]+' "$LOG" 2>/dev/null | tail -1 || echo "?")
    echo "[$STATUS] $case — ${ELAPSED} — $EDI"
done

echo ""
echo "=== DONE === $(date) — Failures: $FAILURES/${#CASES[@]}"
echo ""

# Resumen detallado
echo "=== DETAILED RESULTS ==="
for case in "${CASES[@]}"; do
    LOG="$LOG_DIR/${case}.log"
    echo ""
    echo "--- $case ---"
    tail -15 "$LOG" 2>/dev/null || echo "(no log)"
done
