# Guía de Cómputo — Torre de Simulación

## Conexión a la Torre

```bash
# Conectar por SSH
sshpass -p '[REDACTED]' ssh -o StrictHostKeyChecking=no stev@10.8.0.11

# Ruta del repositorio en la torre
cd /datos/repos/Personal/hiper-objeto-simulaciones
```

**Datos de acceso:**
- Host: `10.8.0.11` (red local)
- Usuario: `stev`
- Password: `[REDACTED]`
- Puerto SSH: 22

## Hardware Disponible

| Componente | Especificación | Uso |
|---|---|---|
| CPU | AMD 9950X3D, 32 hilos | Calibración paralela (16 workers) |
| RAM | 128 GB + 192 GB SWAP (RAID0 SSD) | Modelos grandes en memoria |
| GPU | NVIDIA 5070Ti 16 GB | Grid ABM masivos (CUDA/CuPy) |
| Disco | 7 TB (3 SSD RAID0) | Datasets y cachés |
| Refrigeración | Líquida | Procesos sostenidos largo plazo |

## Flujo Git Push/Pull (Sincronización entre máquinas)

El repositorio `repos/Simulaciones` se sincroniza entre la máquina local (workspace) y la torre vía git.

### Desde la máquina local → torre

```bash
# 1. Hacer cambios en local
cd /workspace/repos/Simulaciones
# ... editar archivos ...
git add -A && git commit -m "descripción del cambio"
git push origin main

# 2. En la torre: pull para recibir cambios
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 \
  "cd /datos/repos/Personal/hiper-objeto-simulaciones && git pull"
```

### Desde la torre → máquina local

```bash
# 1. En la torre: commit y push
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 \
  "cd /datos/repos/Personal/hiper-objeto-simulaciones && git add -A && git commit -m 'resultados torre' && git push"

# 2. En local: pull para recibir resultados
cd /workspace/repos/Simulaciones && git pull
```

### Sincronizar resultados específicos (SCP)

```bash
# Copiar metrics.json de un caso específico (torre → local)
sshpass -p '[REDACTED]' scp stev@10.8.0.11:/datos/repos/Personal/hiper-objeto-simulaciones/25_caso_fosforo/outputs/metrics.json \
  /workspace/TesisDesarrollo/02_Modelado_Simulacion/25_caso_fosforo/metrics.json

# Copiar todos los outputs de un caso
sshpass -p '[REDACTED]' scp -r stev@10.8.0.11:/datos/repos/Personal/hiper-objeto-simulaciones/01_caso_clima/outputs/ \
  /workspace/repos/Simulaciones/01_caso_clima/outputs/

# Copiar todos los metrics.json de golpe
for n in $(seq -w 1 32); do
  caso=$(sshpass -p '[REDACTED]' ssh stev@10.8.0.11 "ls -d /datos/repos/Personal/hiper-objeto-simulaciones/${n}_caso_* 2>/dev/null" | head -1)
  if [ -n "$caso" ]; then
    nombre=$(basename "$caso")
    sshpass -p '[REDACTED]' scp stev@10.8.0.11:${caso}/outputs/metrics.json \
      /workspace/TesisDesarrollo/02_Modelado_Simulacion/${nombre}/metrics.json 2>/dev/null
  fi
done
```

## Ejecución de Simulaciones en la Torre

### Caso individual

```bash
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 \
  "cd /datos/repos/Personal/hiper-objeto-simulaciones/01_caso_clima/src && python3 validate.py"
```

### Todos los 32 casos en paralelo (mega_run)

```bash
# Copiar el script mega_run a la torre (si es nuevo)
sshpass -p '[REDACTED]' scp /workspace/repos/Simulaciones/mega_run_v6.py \
  stev@10.8.0.11:/datos/repos/Personal/hiper-objeto-simulaciones/

# Ejecutar en background con nohup
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 \
  "cd /datos/repos/Personal/hiper-objeto-simulaciones && nohup python3 mega_run_v6.py > mega_run.log 2>&1 &"

# Monitorear progreso
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 \
  "tail -30 /datos/repos/Personal/hiper-objeto-simulaciones/mega_run.log"

# Ver qué procesos python corren
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 "ps aux | grep python | grep -v grep"
```

### Monitoreo de recursos

```bash
# RAM y CPU en tiempo real
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 "htop" 

# Resumen rápido de uso
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 "free -h && echo '---' && nproc && echo '---' && nvidia-smi 2>/dev/null || echo 'GPU no detectada'"
```

## Estructura del Repo en la Torre

```
/datos/repos/Personal/hiper-objeto-simulaciones/
├── common/
│   └── hybrid_validator.py    # Motor de validación (compartido)
├── 01_caso_clima/
│   ├── src/                   # validate.py, abm.py, ode.py, metrics.py, data.py
│   ├── outputs/               # metrics.json, report.md (generados)
│   └── data/                  # CSVs cacheados
├── 02_caso_conciencia/
│   └── ...
├── ...
├── 32_caso_iot/
│   └── ...
├── mega_run_v6.py             # Orquestador paralelo (16 workers)
└── requirements.txt
```

## Notas Importantes

1. **Cache de datos**: Los CSVs descargados se cachean en `{caso}/data/`. Si hay problemas con datos stale, borrar el directorio `data/` del caso antes de re-ejecutar.
2. **Meteostat**: Los datos de clima varían entre descargas (API no determinista). Usar siempre el CSV cacheado para reproducibilidad.
3. **World Bank**: Algunos indicadores fueron archivados (EN.ATM.CO2E.PC, ER.H2O.FWTL.ZS). Los reemplazos están documentados en cada `data.py`.
4. **Memoria**: El mega_run con 16 workers puede usar ~40GB RAM. No lanzar otros procesos pesados simultáneamente.
5. **Git en la torre**: El repo puede tener directorios antiguos sin numeración (`caso_clima` vs `01_caso_clima`). Los nuevos numerados son los correctos.
