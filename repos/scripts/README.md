# Scripts de la Tesis

Herramientas para ejecutar, auditar y documentar las 29 simulaciones ABM+ODE.

## 🚀 Ejecución de simulaciones

Solo existen **dos scripts** para correr las simulaciones:

### `cpu_run.sh` — Ejecución local en CPU

Ejecuta los 29 casos en paralelo usando procesos locales. **No requiere Docker ni GPU.**

```bash
# Todos los casos (auto: N workers = min(nproc, 16))
./cpu_run.sh

# Caso específico (match parcial, case-insensitive)
./cpu_run.sh --case clima
./cpu_run.sh --case falsacion          # matchea los 3

# Grid personalizado
./cpu_run.sh --grid 100

# Dividir en tandas
./cpu_run.sh --parts 3
./cpu_run.sh --parts 5 --part 2        # solo tanda 2 de 5

# Limitar workers
./cpu_run.sh --workers 4

# Ver plan sin ejecutar
./cpu_run.sh --dry-run
```

| Flag | Default | Descripción |
|------|---------|-------------|
| `--grid SIZE` | 200 | Grid size del ABM |
| `--parts N` | 1 | Dividir en N tandas |
| `--part K` | todas | Ejecutar solo tanda K |
| `--case NOMBRE` | — | Filtrar por nombre (parcial) |
| `--workers N` | auto | Workers paralelos |
| `--perm N` | 9999 | Permutaciones EDI |
| `--boot N` | 5000 | Bootstrap samples |
| `--refine N` | 50000 | Iteraciones refinamiento |
| `--runs N` | 50 | N_RUNS para C5 |
| `--dry-run` | — | Solo muestra el plan |

Logs: `/tmp/cpu_run_g{GRID}_logs/`

---

### `gpu_run.sh` — Ejecución en GPU (Docker)

Ejecuta los 29 casos dentro del contenedor Docker `tesis-gpu` con distribución multi-GPU dinámica. **Requiere Docker + NVIDIA Container Toolkit.**

```bash
# Todos de golpe (ambas GPUs, auto-distribución)
./gpu_run.sh

# Auto-escalado: grid = 200 × N partes
./gpu_run.sh --parts 3                # grid=600, 3 tandas de ~10

# Caso específico
./gpu_run.sh --case deforest --grid 500

# Forzar una sola GPU
./gpu_run.sh --gpu 0                   # solo RTX 5070 Ti
./gpu_run.sh --gpu 1 --case clima      # solo RTX 2060

# Grid explícito (desactiva auto-escalado)
./gpu_run.sh --grid 1000 --parts 5

# Ver plan sin ejecutar
./gpu_run.sh --dry-run
```

| Flag | Default | Descripción |
|------|---------|-------------|
| `--grid SIZE` | auto (200×parts) | Grid size del ABM |
| `--parts N` | 1 | Dividir en N tandas |
| `--part K` | todas | Ejecutar solo tanda K |
| `--case NOMBRE` | — | Filtrar por nombre (parcial) |
| `--gpu N` | auto | Forzar GPU N (0 o 1) |
| `--perm N` | 9999 | Permutaciones EDI |
| `--boot N` | 5000 | Bootstrap samples |
| `--refine N` | 50000 | Iteraciones refinamiento |
| `--runs N` | 50 | N_RUNS para C5 |
| `--container C` | tesis-gpu | Contenedor Docker |
| `--dry-run` | — | Solo muestra el plan |

Distribución multi-GPU:
- Workers por GPU calculados por VRAM libre (proporcional)
- Cola dinámica con `flock`: la GPU rápida toma más casos
- Sub-batching dinámico en `abm_core_gpu.py` maneja competición por VRAM

Logs: `docker exec tesis-gpu ls /tmp/gpu_run_g{GRID}_logs/`

---

## 🔧 Scripts de utilidad

| Script | Descripción | Uso |
|--------|-------------|-----|
| `tesis.py` | CLI principal: scaffold, build, sync, audit, validate | `python3 tesis.py build` |
| `actualizar_tablas_002.py` | Actualiza tablas en `02_Modelado_Simulacion.md` desde metrics.json | `python3 actualizar_tablas_002.py` |
| `auditar_simulaciones.py` | Auditoría documental y métrica (solo lectura) | `python3 auditar_simulaciones.py` |
| `auditoria_cientifica_profunda.py` | Auditoría caso-por-caso: estructura, imports, ejecución, coherencia | `python3 auditoria_cientifica_profunda.py` |
| `_audit_fresh.py` | Auditoría rápida de todos los metrics.json | `python3 _audit_fresh.py` |
| `evaluar_simulaciones.py` | Resumen de métricas en Markdown | `python3 evaluar_simulaciones.py --write` |
| `generar_docs_casos.py` | Genera los 5 docs/ estándar para casos 19-29 | `python3 generar_docs_casos.py` |
| `regenerar_readmes.py` | Regenera README.md de cada caso desde metrics.json | `python3 regenerar_readmes.py` |
| `replay_hash.py` | Genera/verifica hashes MD5 de outputs | `python3 replay_hash.py --verify` |
| `verificar_consistencia.py` | Verifica sync entre repos/Simulaciones y TesisDesarrollo | `python3 verificar_consistencia.py` |

## 📁 Archivos de datos

| Archivo | Descripción |
|---------|-------------|
| `tesis_manifest.json` | Manifiesto de secciones de la tesis |
| `replay_baseline.json` | Baseline de hashes para reproducibilidad |
| `templates/` | Plantillas para scaffolding de nuevos casos |
