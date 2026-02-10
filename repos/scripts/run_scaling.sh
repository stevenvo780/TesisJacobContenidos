#!/usr/bin/env bash
# run_scaling.sh — Ejecuta los 6 casos escalables con High Performance params
# Machine: 32 cores, 128GB RAM, RTX 5070 Ti + RTX 2060
#
# Variables HYPER controlan parámetros estadísticos:
#   HYPER_N_PERM=4999   → Permutaciones (4999 da p-value resolución 0.0002)
#   HYPER_N_BOOT=2000   → Bootstrap samples para CI
#   HYPER_N_REFINE=15000 → Iteraciones de refinamiento en calibración ABM
#
# Los grid_size y n_runs están en cada validate.py individual.

set -euo pipefail

export HYPER_N_PERM=4999
export HYPER_N_BOOT=2000
export HYPER_N_REFINE=15000

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
