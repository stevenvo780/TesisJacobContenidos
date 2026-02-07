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

## Flujo de Sincronización (SCP — repos/Simulaciones está en .gitignore)

**IMPORTANTE:** `repos/Simulaciones/` está excluido del git principal. La sincronización se hace con SCP directo.

### Enviar archivos al torre

```bash
export SSHPASS='[REDACTED]'
TOWER="stev@10.8.0.11"
REMOTE="/datos/repos/Personal/hiper-objeto-simulaciones/repos/Simulaciones"

# Archivo individual (ej. hybrid_validator.py)
sshpass -p "$SSHPASS" scp -o StrictHostKeyChecking=no \
    /workspace/repos/Simulaciones/common/hybrid_validator.py \
    $TOWER:$REMOTE/common/

# validate.py de un caso específico
sshpass -p "$SSHPASS" scp -o StrictHostKeyChecking=no \
    /workspace/repos/Simulaciones/01_caso_clima/src/validate.py \
    $TOWER:$REMOTE/01_caso_clima/src/

# Mega run script
sshpass -p "$SSHPASS" scp -o StrictHostKeyChecking=no \
    /workspace/repos/Simulaciones/mega_run_v7.py \
    $TOWER:$REMOTE/
```

### Borrar caché de datos (OBLIGATORIO si cambia data.py o parámetros)

```bash
# Un caso
sshpass -p "$SSHPASS" ssh $TOWER "rm -f $REMOTE/NN_caso_X/data/*.csv"

# Todos los casos
sshpass -p "$SSHPASS" ssh $TOWER 'for d in '$REMOTE'/*/data; do rm -f "$d"/*.csv 2>/dev/null; done'
```

### Traer resultados de la torre

```bash
# Un caso
sshpass -p "$SSHPASS" scp $TOWER:$REMOTE/01_caso_clima/outputs/metrics.json \
    /workspace/repos/Simulaciones/01_caso_clima/outputs/
sshpass -p "$SSHPASS" scp $TOWER:$REMOTE/01_caso_clima/outputs/report.md \
    /workspace/repos/Simulaciones/01_caso_clima/outputs/

# Todos los 32 casos (metrics.json + report.md)
for case in $(ls -d /workspace/repos/Simulaciones/[0-9]*/); do
    case_name=$(basename "$case")
    sshpass -p "$SSHPASS" scp $TOWER:$REMOTE/$case_name/outputs/metrics.json \
        /workspace/repos/Simulaciones/$case_name/outputs/ 2>/dev/null
    sshpass -p "$SSHPASS" scp $TOWER:$REMOTE/$case_name/outputs/report.md \
        /workspace/repos/Simulaciones/$case_name/outputs/ 2>/dev/null
done

# Copiar también a TesisDesarrollo
for case in $(ls -d /workspace/repos/Simulaciones/[0-9]*/); do
    case_name=$(basename "$case")
    cp /workspace/repos/Simulaciones/$case_name/outputs/metrics.json \
       /workspace/TesisDesarrollo/02_Modelado_Simulacion/$case_name/ 2>/dev/null
    cp /workspace/repos/Simulaciones/$case_name/outputs/report.md \
       /workspace/TesisDesarrollo/02_Modelado_Simulacion/$case_name/ 2>/dev/null
done
```

## Ejecución de Simulaciones en la Torre

### Caso individual

```bash
sshpass -p '[REDACTED]' ssh stev@10.8.0.11 \
  "cd /datos/repos/Personal/hiper-objeto-simulaciones/01_caso_clima/src && python3 validate.py"
```

### Todos los 32 casos secuencial (mega_run v7)

```bash
# Copiar el script mega_run a la torre
sshpass -p "$SSHPASS" scp /workspace/repos/Simulaciones/mega_run_v7.py \
  $TOWER:$REMOTE/

# Ejecutar en background con nohup (-u para output no-buffered)
sshpass -p "$SSHPASS" ssh $TOWER \
  "cd $REMOTE && nohup python3 -u mega_run_v7.py > mega_run_v8.log 2>&1 & echo PID=\$!"

# Monitorear progreso
sshpass -p "$SSHPASS" ssh $TOWER "tail -30 $REMOTE/mega_run_v8.log"

# Ver qué procesos python corren
sshpass -p "$SSHPASS" ssh $TOWER "ps aux | grep python | grep -v grep"

# Solo casos específicos
sshpass -p "$SSHPASS" ssh $TOWER \
  "cd $REMOTE && nohup python3 -u mega_run_v7.py 4 19 23 29 > rerun.log 2>&1 & echo PID=\$!"
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
