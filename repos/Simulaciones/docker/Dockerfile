# Dockerfile — GPU compute backend para simulaciones ABM+ODE
# Base: CUDA 12.8 runtime + Python 3.12 sobre Ubuntu 24.04
# Compatible con RTX 5070 Ti (Blackwell, sm_120) y RTX 2060 (Turing, sm_75)
# Usa runtime (no devel): CuPy wheels vienen precompilados con kernels sm_120
FROM nvidia/cuda:12.8.0-runtime-ubuntu24.04

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Sistema base + Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3 python3-pip python3-dev python3-venv \
    git curl wget build-essential \
    && rm -rf /var/lib/apt/lists/*

# Alias python
RUN ln -sf /usr/bin/python3 /usr/bin/python

# Directorio de trabajo
WORKDIR /workspace

# Dependencias Python — instalar en sistema (es contenedor dedicado)
COPY requirements-gpu.txt /tmp/requirements-gpu.txt
RUN pip install --break-system-packages --no-cache-dir -r /tmp/requirements-gpu.txt

# Verificación de CUDA al build
RUN python -c "import cupy; print(f'CuPy {cupy.__version__} — GPUs: {cupy.cuda.runtime.getDeviceCount()}')" \
    || echo "WARN: CuPy GPU check deferred to runtime (no GPU during build)"

# Entrypoint por defecto: shell interactivo para dev
CMD ["python"]
