#!/usr/bin/env bash
# run_scaling.sh — Ejecuta los 6 casos escalables con High Performance params
# Machine: 32 cores, 128GB RAM, RTX 5070 Ti + RTX 2060
#
# Variables HYPER controlan parámetros estadísticos:
#   HYPER_N_PERM=9999   → Permutaciones (9999 da p-value resolución 0.0001)
#   HYPER_N_BOOT=5000   → Bootstrap samples para CI (alta precisión)
#   HYPER_N_REFINE=50000 → Iteraciones de refinamiento en calibración ABM
#   HYPER_GRID_SIZE=150  → Grid 150×150 = 22500 agentes (vs 400 default)
#   HYPER_N_RUNS=30      → 30 runs de perturbación C5 (vs 5 default)
#
# Los grid_size y n_runs están en cada validate.py individual.
# HYPER_GRID_SIZE solo aplica si el caso ya tiene grid_size > 1.

set -euo pipefail

export HYPER_N_PERM=9999
export HYPER_N_BOOT=5000
export HYPER_N_REFINE=50000
export HYPER_GRID_SIZE=150
export HYPER_N_RUNS=30

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
SIM_DIR="$(cd "$SCRIPT_DIR/../Simulaciones" && pwd)"

CASES=(
    "16_caso_deforestacion"
    "24_caso_microplasticos"
    "27_caso_riesgo_biologico"
    "13_caso_politicas_estrategicas"
    "21_caso_salinizacion"
    "06_caso_falsacion_exogeneidad"
)

echo "═══════════════════════════════════════════════"
echo " SCALING RUN — $(date)"
echo " HYPER_N_PERM=$HYPER_N_PERM  HYPER_N_BOOT=$HYPER_N_BOOT  HYPER_N_REFINE=$HYPER_N_REFINE"
echo "═══════════════════════════════════════════════"

for case in "${CASES[@]}"; do
    SRC="$SIM_DIR/$case/src"
    echo ""
    echo "▶ $case"
    echo "  $(date +%H:%M:%S) — Iniciando..."
    
    if [ ! -f "$SRC/validate.py" ]; then
        echo "  ✗ No existe validate.py"
        continue
    fi
    
    # Run from src/ directory (bare imports require it)
    START_T=$SECONDS
    (cd "$SRC" && python3 validate.py) 2>&1 | tail -5
    ELAPSED=$(( SECONDS - START_T ))
    
    echo "  ✓ Completado en ${ELAPSED}s"
done

echo ""
echo "═══════════════════════════════════════════════"
echo " SCALING COMPLETO — $(date)"
echo "═══════════════════════════════════════════════"
