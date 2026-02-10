#!/usr/bin/env bash
# Test: ¿ambas GPUs trabajan al mismo tiempo?
# Lanza 4 procesos (2 en GPU 0, 2 en GPU 1) y monitorea desde HOST

CONTAINER="tesis-gpu"

# Limpiar
docker exec "$CONTAINER" bash -c 'pkill -9 -f "python3 validate.py" 2>/dev/null' || true
sleep 1

echo "=== Lanzando 4 procesos en contenedor ==="

# GPU 0: 2 procesos
docker exec -d -e HYPER_GPU_DEVICE=0 -e HYPER_GRID_SIZE=200 -e HYPER_N_PERM=99 -e HYPER_N_BOOT=100 -e HYPER_N_REFINE=500 -e HYPER_N_RUNS=5 \
    "$CONTAINER" bash -c 'cd /workspace/repos/Simulaciones/16_caso_deforestacion/src && python3 validate.py > /tmp/_test_g0a.log 2>&1'
echo "  deforestacion -> GPU 0"

docker exec -d -e HYPER_GPU_DEVICE=0 -e HYPER_GRID_SIZE=200 -e HYPER_N_PERM=99 -e HYPER_N_BOOT=100 -e HYPER_N_REFINE=500 -e HYPER_N_RUNS=5 \
    "$CONTAINER" bash -c 'cd /workspace/repos/Simulaciones/22_caso_fosforo/src && python3 validate.py > /tmp/_test_g0b.log 2>&1'
echo "  fosforo -> GPU 0"

# GPU 1: 2 procesos
docker exec -d -e HYPER_GPU_DEVICE=1 -e HYPER_GRID_SIZE=200 -e HYPER_N_PERM=99 -e HYPER_N_BOOT=100 -e HYPER_N_REFINE=500 -e HYPER_N_RUNS=5 \
    "$CONTAINER" bash -c 'cd /workspace/repos/Simulaciones/21_caso_salinizacion/src && python3 validate.py > /tmp/_test_g1a.log 2>&1'
echo "  salinizacion -> GPU 1"

docker exec -d -e HYPER_GPU_DEVICE=1 -e HYPER_GRID_SIZE=200 -e HYPER_N_PERM=99 -e HYPER_N_BOOT=100 -e HYPER_N_REFINE=500 -e HYPER_N_RUNS=5 \
    "$CONTAINER" bash -c 'cd /workspace/repos/Simulaciones/29_caso_iot/src && python3 validate.py > /tmp/_test_g1b.log 2>&1'
echo "  iot -> GPU 1"

echo ""
sleep 3

echo "=== Monitoreo nvidia-smi desde HOST (cada 2s, 40 muestras) ==="
echo "  Columnas: GPU, Util%, VRAM_usada(MB), VRAM_libre(MB)"
echo ""

for i in $(seq 1 40); do
    ALIVE=$(docker exec "$CONTAINER" bash -c 'pgrep -f "python3 validate.py" | wc -l' 2>/dev/null || echo 0)
    GPU_DATA=$(nvidia-smi --query-gpu=index,utilization.gpu,memory.used,memory.free --format=csv,noheader,nounits 2>/dev/null)
    TS=$(date +%H:%M:%S)
    echo -n "[$TS] t=${i} procs=$ALIVE | "
    echo "$GPU_DATA" | while IFS=', ' read -r gid util used free; do
        gid=$(echo "$gid" | tr -d ' ')
        util=$(echo "$util" | tr -d ' ')
        used=$(echo "$used" | tr -d ' ')
        echo -n "GPU${gid}:${util}%/${used}MB  "
    done
    echo ""
    
    if [ "$ALIVE" -eq 0 ]; then
        echo "  -> Todos terminaron"
        break
    fi
    sleep 2
done

echo ""
echo "=== Logs stderr (gpu_backend lines) ==="
for f in _test_g0a _test_g0b _test_g1a _test_g1b; do
    echo "--- $f ---"
    docker exec "$CONTAINER" grep -i "gpu_backend\|CUDA_VISIBLE" "/tmp/${f}.log" 2>/dev/null | head -3
done
echo "DONE"
