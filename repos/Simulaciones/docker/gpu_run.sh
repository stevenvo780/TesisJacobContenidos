#!/usr/bin/env bash
# gpu_run.sh — Ejecuta un caso de simulación dentro del contenedor GPU
#
# Uso:
#   bash repos/Simulaciones/docker/gpu_run.sh 16_caso_deforestacion
#   bash repos/Simulaciones/docker/gpu_run.sh all    # Ejecutar los 6 escalables
#   bash repos/Simulaciones/docker/gpu_run.sh 16_caso_deforestacion "HYPER_GRID_SIZE=500"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
CONTAINER="tesis-gpu"

# Verificar que el contenedor existe
if ! docker ps --format '{{.Names}}' | grep -q "^${CONTAINER}$"; then
    echo "✗ Contenedor $CONTAINER no está corriendo. Ejecuta primero:"
    echo "  bash $SCRIPT_DIR/gpu_setup.sh start"
    exit 1
fi

CASE="${1:-}"
EXTRA_ENV="${2:-}"

ESCALABLES=(
    "16_caso_deforestacion"
    "24_caso_microplasticos"
    "27_caso_riesgo_biologico"
    "13_caso_politicas_estrategicas"
    "21_caso_salinizacion"
    "06_caso_falsacion_exogeneidad"
)

run_case() {
    local case="$1"
    local src="/workspace/repos/Simulaciones/${case}/src"
    echo ""
    echo "▶ $case"
    echo "  $(date +%H:%M:%S) — Iniciando (GPU batch, grid=${HYPER_GRID_SIZE:-500})..."
    
    local START_T=$SECONDS
    docker exec -w "$src" \
        -e "HYPER_GRID_SIZE=${HYPER_GRID_SIZE:-500}" \
        -e "HYPER_N_PERM=${HYPER_N_PERM:-9999}" \
        -e "HYPER_N_BOOT=${HYPER_N_BOOT:-5000}" \
        -e "HYPER_N_REFINE=${HYPER_N_REFINE:-50000}" \
        -e "HYPER_N_RUNS=${HYPER_N_RUNS:-50}" \
        ${EXTRA_ENV:+-e "$EXTRA_ENV"} \
        "$CONTAINER" \
        python3 validate.py 2>&1 | tail -10
    local ELAPSED=$(( SECONDS - START_T ))
    echo "  ✓ Completado en ${ELAPSED}s (GPU batch)"
}

if [ "$CASE" = "all" ]; then
    echo "═══════════════════════════════════════════════"
    echo " GPU SCALING RUN — $(date)"
    echo "═══════════════════════════════════════════════"
    for c in "${ESCALABLES[@]}"; do
        run_case "$c"
    done
    echo ""
    echo "═══════════════════════════════════════════════"
    echo " GPU SCALING COMPLETO — $(date)"
    echo "═══════════════════════════════════════════════"
elif [ -n "$CASE" ]; then
    run_case "$CASE"
else
    echo "Uso: $0 {case_name|all} [EXTRA_ENV]"
    echo "Casos escalables:"
    for c in "${ESCALABLES[@]}"; do
        echo "  - $c"
    done
fi
