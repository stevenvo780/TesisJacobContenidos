# Scripts de la Tesis

Herramientas para ejecutar, auditar y documentar las **29 simulaciones ABM+ODE** del proyecto de tesis doctoral *"Irrealismo Operativo de Hiperobjetos"*.

---

## 🚀 Ejecución de simulaciones

Existen **dos scripts ejecutores** mutuamente excluyentes. Ambos producen `metrics.json` y `report.md` en `{caso}/outputs/`.

| | `cpu_run.sh` | `gpu_run.sh` |
|---|---|---|
| **Dónde corre** | Localmente (Python nativo) | Dentro del contenedor Docker `tesis-gpu` |
| **Aceleración** | Solo CPU (NumPy) | GPU via CuPy (sub-batching automático) |
| **Requisitos** | Python 3.10+, dependencias instaladas | Docker + NVIDIA Container Toolkit |
| **Multi-GPU** | N/A | Sí — distribución proporcional por VRAM |
| **Velocidad (grid=50)** | ~15s/caso | ~6s/caso |
| **Velocidad (grid=2000)** | ~horas/caso | ~minutos/caso |

---

### `cpu_run.sh` — Ejecución local en CPU

No requiere Docker ni GPU. Workers paralelos auto-ajustados a los cores disponibles.

```bash
# ─── Básico ───────────────────────────────────────────────────
./cpu_run.sh                           # 29 casos, grid por caso, auto workers

# ─── Caso específico (match parcial, case-insensitive) ────────
./cpu_run.sh --case clima              # 01_caso_clima
./cpu_run.sh --case deforest           # 16_caso_deforestacion
./cpu_run.sh --case falsacion          # 06, 07, 08 (matchea los 3)

# ─── Tandas (dividir 29 casos en bloques) ────────────────────
./cpu_run.sh --parts 3                 # 3 tandas secuenciales
./cpu_run.sh --parts 5 --part 2        # solo la tanda 2 de 5

# ─── Control de paralelismo ──────────────────────────────────
./cpu_run.sh --workers 4               # máximo 4 procesos simultáneos

# ─── Secuencial (1 caso a la vez) ───────────────────────────
./cpu_run.sh --step-by-step

# ─── Previsualizar sin ejecutar ──────────────────────────────
./cpu_run.sh --dry-run
./cpu_run.sh --case falsacion --dry-run
```

**Flags completas:**

| Flag | Default | Descripción |
|------|---------|-------------|
| `--parts N` | 1 | Dividir casos en N tandas |
| `--part K` | todas | Ejecutar solo la tanda K de N |
| `--case NOMBRE` | — | Filtrar por nombre (match parcial, case-insensitive) |
| `--workers N` | auto | Workers paralelos (auto = `min(nproc, 16)`) |
| `--step-by-step` | off | Secuencial: 1 caso a la vez, output live en terminal |
| `--perm N` | 9999 | Permutaciones para test EDI |
| `--boot N` | 5000 | Bootstrap samples para intervalos de confianza |
| `--refine N` | 50000 | Iteraciones de refinamiento en calibración |
| `--runs N` | 50 | Simulaciones por configuración (C5) |
| `--dry-run` | off | Solo muestra el plan, no ejecuta nada |

**Logs:** `/tmp/cpu_run_logs/{caso}.log`

---

### `gpu_run.sh` — Ejecución en GPU (Docker)

Ejecuta dentro del contenedor Docker `tesis-gpu`. Distribución multi-GPU dinámica con cola de trabajo `flock`. Sub-batching automático en VRAM.

```bash
# ─── Básico ───────────────────────────────────────────────────
./gpu_run.sh                           # 29 casos, grid por caso, ambas GPUs

# ─── Caso específico ─────────────────────────────────────────
./gpu_run.sh --case deforest           # 16_caso_deforestacion
./gpu_run.sh --case deforest

# ─── Forzar una GPU específica ───────────────────────────────
./gpu_run.sh --gpu 0                   # solo RTX 5070 Ti (16 GB)
./gpu_run.sh --gpu 1 --case clima      # solo RTX 2060 (6 GB)

# ─── Secuencial (1 caso/GPU a la vez) ─────────────────────────
./gpu_run.sh --step-by-step                        # 2 GPUs: 2 casos simultáneos (1/GPU)
./gpu_run.sh --step-by-step --gpu 0                # 1 GPU: puramente secuencial

# ─── Previsualizar sin ejecutar ──────────────────────────────
./gpu_run.sh --dry-run
./gpu_run.sh --parts 5 --dry-run
```

**Flags completas:**

| Flag | Default | Descripción |
|------|---------|-------------|
| `--parts N` | 1 | Dividir en N tandas (1–10) |
| `--part K` | todas | Ejecutar solo la tanda K de N |
| `--case NOMBRE` | — | Filtrar por nombre (match parcial, case-insensitive) |
| `--gpu N` | auto | Forzar GPU N (0 o 1). Auto = ambas GPUs |
| `--step-by-step` | off | Secuencial: 1 caso/GPU. Con 2 GPUs → 2 simultáneos |
| `--perm N` | 9999 | Permutaciones para test EDI |
| `--boot N` | 5000 | Bootstrap samples para intervalos de confianza |
| `--refine N` | 50000 | Iteraciones de refinamiento en calibración |
| `--runs N` | 50 | Simulaciones por configuración (C5) |
| `--container C` | tesis-gpu | Nombre del contenedor Docker |
| `--dry-run` | off | Solo muestra el plan, no ejecuta nada |

**Logs:** `docker exec tesis-gpu ls /tmp/gpu_run_logs/`

---

### 🧠 ¿Cuándo usar cada modo?

| Situación | Comando recomendado |
|-----------|---------------------|
| Desarrollo rápido / debug de un caso | `cpu_run.sh --case NOMBRE` |
| Validación completa de los 29 casos | `gpu_run.sh` |
| Sensibilidad de grid en un caso | Editar `grid_size` en `validate.py` del caso |
| Secuencial (1 caso por GPU) | `gpu_run.sh --step-by-step --case NOMBRE` |
| Sin GPU disponible | `cpu_run.sh` |
| Prueba rápida (params mínimos) | `--runs 5 --perm 99 --boot 100 --refine 100` |
| Verificar plan sin ejecutar | `--dry-run` (disponible en ambos) |

### ⚙️ Arquitectura interna

```
cpu_run.sh                          gpu_run.sh
    │                                   │
    ├── flock cola dinámica             ├── flock cola dinámica
    ├── N workers (1 por core)          ├── N workers (proporcional a VRAM/GPU)
    │                                   ├── CUDA_VISIBLE_DEVICES por worker
    ▼                                   ▼
  python3 validate.py               docker exec tesis-gpu python3 validate.py
    │                                   │
    ├── abm_core.py (NumPy)             ├── abm_core_gpu.py (CuPy)
    │                                   │   └── sub-batching: 25% VRAM libre
    ├── ode.py                          ├── ode.py
    ├── metrics.py → EDI, C1-C5         ├── metrics.py → EDI, C1-C5
    └── outputs/metrics.json            └── outputs/metrics.json
```

**Sub-batching GPU:** Cada proceso reserva el 25% de la VRAM libre para ejecutar B simulaciones simultáneas. B se ajusta automáticamente según grid y VRAM disponible. Si OOM con B=1, cae a CPU transparentemente.

**VRAM por proceso (estimada):**

| Grid | RTX 5070 Ti (16 GB) | RTX 2060 (6 GB) |
|------|---------------------|------------------|
| 50 | ~550 MB | ~550 MB |
| 200 | ~650 MB | ~650 MB |
| 500 | ~1450 MB | ~950 MB |
| 2000 | ~2330 MB | ~805 MB |

---

## 🔧 Scripts de utilidad

### Auditoría y validación

| Script | Qué hace | Uso |
|--------|----------|-----|
| `auditar_simulaciones.py` | Auditoría documental: estructura, métricas, coherencia (solo lectura) | `python3 auditar_simulaciones.py` |
| `auditoria_cientifica_profunda.py` | Auditoría caso-por-caso: imports, ejecución, resultados | `python3 auditoria_cientifica_profunda.py` |
| `_audit_fresh.py` | Auditoría rápida de todos los `metrics.json` existentes | `python3 _audit_fresh.py` |
| `verificar_consistencia.py` | Verifica sincronización entre `repos/Simulaciones/` y `TesisDesarrollo/` | `python3 verificar_consistencia.py` |
| `replay_hash.py` | Genera o verifica hashes MD5 de outputs para reproducibilidad | `python3 replay_hash.py --verify` |

### Generación de documentos

| Script | Qué hace | Uso |
|--------|----------|-----|
| `tesis.py` | CLI principal: scaffold, build, sync, audit, validate | `python3 tesis.py build` |
| `evaluar_simulaciones.py` | Resumen de métricas en tablas Markdown | `python3 evaluar_simulaciones.py --write` |
| `actualizar_tablas_002.py` | Actualiza tablas en `02_Modelado_Simulacion.md` desde `metrics.json` | `python3 actualizar_tablas_002.py` |
| `generar_docs_casos.py` | Genera los 5 docs/ estándar para casos 19-29 | `python3 generar_docs_casos.py` |
| `regenerar_readmes.py` | Regenera `README.md` de cada caso desde `metrics.json` | `python3 regenerar_readmes.py` |

### Datos

| Archivo | Descripción |
|---------|-------------|
| `tesis_manifest.json` | Manifiesto de secciones de la tesis |
| `replay_baseline.json` | Baseline de hashes MD5 para reproducibilidad |
| `templates/` | Plantillas para scaffolding de nuevos casos |
