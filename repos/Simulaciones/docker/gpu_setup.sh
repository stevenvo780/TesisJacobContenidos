#!/usr/bin/env bash
# gpu_setup.sh — Construye y levanta el contenedor GPU persistente
#
# Uso:
#   bash repos/Simulaciones/docker/gpu_setup.sh          # Build + start
#   bash repos/Simulaciones/docker/gpu_setup.sh rebuild   # Rebuild from scratch
#   bash repos/Simulaciones/docker/gpu_setup.sh stop      # Stop container
#   bash repos/Simulaciones/docker/gpu_setup.sh status    # Check status

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$SCRIPT_DIR"

ACTION="${1:-start}"

case "$ACTION" in
    rebuild)
        echo "▶ Rebuild completo..."
        docker-compose down -v 2>/dev/null || true
        docker-compose build --no-cache
        docker-compose up -d
        echo "▶ Verificando GPU..."
        sleep 3
        docker exec tesis-gpu python -c "
import cupy as cp
n = cp.cuda.runtime.getDeviceCount()
for i in range(n):
    props = cp.cuda.runtime.getDeviceProperties(i)
    name = props.get('name', b'?')
    if isinstance(name, bytes): name = name.decode()
    mem = props.get('totalGlobalMem', 0) / (1024**3)
    print(f'  GPU {i}: {name} ({mem:.1f} GB)')
print(f'CuPy {cp.__version__} — {n} GPU(s) OK')
" 2>&1
        ;;
    start)
        if docker ps --format '{{.Names}}' | grep -q '^tesis-gpu$'; then
            echo "✓ Contenedor tesis-gpu ya está corriendo"
            docker exec tesis-gpu python -c "from gpu_backend import gpu_info; print(gpu_info())"
        else
            echo "▶ Levantando contenedor..."
            docker-compose up -d
            sleep 3
            echo "▶ Verificando GPU..."
            docker exec tesis-gpu python -c "
import cupy as cp
print(f'CuPy {cp.__version__} — GPUs: {cp.cuda.runtime.getDeviceCount()}')
a = cp.ones(10000000, dtype=cp.float64)
print(f'Test: sum = {float(cp.sum(a))} — GPU OK')
" 2>&1
        fi
        ;;
    stop)
        echo "▶ Deteniendo contenedor..."
        docker-compose down
        echo "✓ Contenedor detenido (datos y cache persistentes)"
        ;;
    status)
        if docker ps --format '{{.Names}}' | grep -q '^tesis-gpu$'; then
            echo "✓ tesis-gpu: RUNNING"
            docker exec tesis-gpu nvidia-smi --query-gpu=name,memory.used,memory.total,utilization.gpu --format=csv 2>&1
        else
            echo "✗ tesis-gpu: NOT RUNNING"
            echo "  Ejecuta: bash $0 start"
        fi
        ;;
    *)
        echo "Uso: $0 {start|stop|rebuild|status}"
        exit 1
        ;;
esac
