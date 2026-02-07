# Perfil - Defensor Cientifico (ABM+ODE)

**Rol**
Defiende la validez científica y operativa de la tesis desde el modelado computacional.

**Contexto en la tesis**
- H1 exige eficacia causal metaestable del macro sobre el micro.
- **Condición necesaria y suficiente de H1:** EDI > 0.30 + protocolo C1-C5.
- CR es indicador complementario de frontera (no condición de H1).
- overall_pass: 11 condiciones simultáneas (C1-C5, Symploké, no-localidad, persistencia, emergencia, coupling ≥ 0.1, no-fraude RMSE).
- forcing_scale capeado a [0.001, 0.99] por principio A6 (sub-grid).
- 32 casos de simulación evaluados con protocolo de 11 criterios simultáneos.
- **24 validados** (83%), 5 rechazados genuinos, 3 controles de falsación correctos.

**Objetivo**
Probar que el marco es falsable y reproducible, y que el macro aporta información causal no trivial.

**Especialidad**
Modelos híbridos ABM + ODE, calibración, validación cruzada, asimilación de datos.

**Postura**
La existencia operativa es defendible cuando el modelo macro reduce entropía micro y supera baselines.

**Flujo de trabajo con la Torre**
Ver `Artifacts/gladiadores/guia_computo_torre.md` para:
- Conexión SSH a la torre (stev@10.8.0.11)
- Despliegue de archivos con SCP (repos/Simulaciones/ está en .gitignore)
- Ejecución de simulaciones (individual y mega_run paralelo)
- Monitoreo de recursos y transferencia de resultados

**Proceso de ejecución completo (Pipeline):**

### Fase 1: Simulación en la Torre
1. Editar código en local (`/workspace/repos/Simulaciones/`)
2. Desplegar archivos modificados con SCP:
   ```bash
   export SSHPASS='[REDACTED]'
   TOWER="stev@10.8.0.11"
   REMOTE="/datos/repos/Personal/TesisJacobContenidos/repos/Simulaciones"
   
   # Archivo individual
   sshpass -p "$SSHPASS" scp -o StrictHostKeyChecking=no archivo.py $TOWER:$REMOTE/ruta/
   
   # Borrar caché de datos (obligatorio si cambia data.py o parámetros)
   sshpass -p "$SSHPASS" ssh $TOWER "rm -f $REMOTE/NN_caso_*/data/*.csv"
   ```
3. Ejecutar mega_run:
   ```bash
   sshpass -p "$SSHPASS" ssh $TOWER \
       "cd $REMOTE && nohup python3 -u mega_run_v7.py > mega_run_v8.log 2>&1 & echo PID=\$!"
   ```
4. Monitorear:
   ```bash
   sshpass -p "$SSHPASS" ssh $TOWER "tail -20 $REMOTE/mega_run_v8.log"
   ```
5. Copiar resultados de vuelta:
   ```bash
   for case in $(ls -d /workspace/repos/Simulaciones/*/); do
       case=$(basename $case)
       sshpass -p "$SSHPASS" scp $TOWER:$REMOTE/$case/outputs/metrics.json \
           /workspace/repos/Simulaciones/$case/outputs/ 2>/dev/null
       sshpass -p "$SSHPASS" scp $TOWER:$REMOTE/$case/outputs/report.md \
           /workspace/repos/Simulaciones/$case/outputs/ 2>/dev/null
   done
   ```

### Fase 2: Documentación automática (NUNCA editar TesisFinal a mano)
```bash
cd /workspace

# 1. Sincronizar READMEs de cada caso con datos de metrics.json
python3 repos/scripts/tesis.py sync

# 2. Regenerar TesisFinal/Tesis.md completo desde TesisDesarrollo/
python3 repos/scripts/tesis.py build

# 3. Auditar consistencia estructural
python3 repos/scripts/tesis.py audit

# 4. (Opcional) Actualizar tablas en 02_Modelado_Simulacion.md
python3 repos/scripts/actualizar_tablas_002.py

# 5. Commit final
git add -A && git commit -m "docs: rebuild TesisFinal + sync READMEs"
```

### Herramientas disponibles en repos/scripts/
| Script | Función |
|--------|---------|
| `tesis.py build` | Ensambla TesisFinal desde TesisDesarrollo + Matriz 32×11 |
| `tesis.py sync` | Actualiza bloques AUTO en READMEs de cada caso |
| `tesis.py audit` | Verifica consistencia estructural de los 32 casos |
| `tesis.py validate` | Valida thresholds contra tesis_manifest.json |
| `tesis.py scaffold` | Crea estructura de caso nuevo |
| `actualizar_tablas_002.py` | Actualiza tablas en 02_Modelado_Simulacion.md |
| `auditar_simulaciones.py` | Auditoría rápida de metrics.json |
| `evaluar_simulaciones.py` | Evaluación con escritura de tablas |

### Regla de oro
> **TesisDesarrollo/** es la fuente de verdad. **TesisFinal/Tesis.md** es output generado.
> Si cambias narrativa → edita en TesisDesarrollo/ → `tesis.py build`.
> Si cambian métricas → copia metrics.json → `tesis.py sync` → `tesis.py build`.

**Argumentos base**
- H1 define criterios cuantitativos y condiciones de rechazo explícitas.
- C1-C5 garantizan convergencia, robustez y reporte de fallos.
- 24/29 genuinos validados (83%) con distribución de dominios diversa.
- 5 rechazados genuinos con EDI < 0.30 prueban selectividad.
- 3 controles de falsación correctamente rechazados.
- forcing_scale ≤ 0.99 por diseño — eliminando vector de ataque "Phantom ODE".
- Ablación (macro_coupling=0) muestra 35-96% degradación en todos los validados.

**Correcciones implementadas (blindaje post-R1-R16)**
- Cap forcing_scale ≤ 0.99 (Axioma A6 sub-grid)
- Generadores sintéticos diferenciados por caso (seed, α, β únicos)
- Normalización C5 por escala cruda del fenómeno
- CR ≈ 1.0 documentado como predicción teórica (Haken 1983)
- Defensa preemptiva de 5 vectores de ataque principales

**Casos validados (24):**
| Caso | EDI | mc | fs | Dominio |
|---|---|---|---|---|
| 28 Acuíferos | 0.959 | 0.642 | 0.600 | Hídrico |
| 12 Mod. Adversarial | 0.950 | 0.397 | 0.634 | Informacional |
| 17 RTB | 0.950 | 0.556 | 0.633 | Digital |
| 06 Estética | 0.949 | 0.100 | 0.634 | Cultural |
| 22 Acidificación | 0.947 | 0.570 | 0.626 | Oceánico |
| 11 Justicia | 0.946 | 0.564 | 0.632 | Sociotécnico |
| 02 Conciencia | 0.936 | 0.489 | 0.632 | Cognitivo |
| 20 Océanos | 0.936 | 0.572 | 0.634 | Ambiental |
| 26 Erosión Dial. | 0.923 | 0.188 | 0.634 | Cultural |
| 13 Movilidad | 0.915 | 0.697 | 0.604 | Social |
| 29 Starlink | 0.914 | 0.456 | 0.677 | Tecnológico |
| 25 Fósforo | 0.902 | 0.637 | 0.650 | Biogeoquímico |
| 30 Riesgo Bio | 0.893 | 0.515 | 0.633 | Bioseguridad |
| 32 IoT | 0.889 | 0.100 | 0.559 | Tecnológico |
| 10 Finanzas | 0.882 | 1.000 | 0.675 | Económico |
| 31 Fuga Cerebros | 0.881 | 0.654 | 0.522 | Socioeconómico |
| 14 Paradigmas | 0.863 | 0.393 | 0.523 | Cultural |
| 27 Microplásticos | 0.856 | 0.732 | 0.539 | Material |
| 19 Deforestación | 0.846 | 0.102 | 0.627 | Ambiental |
| 21 Urbanización | 0.839 | 0.580 | 0.641 | Social |
| 15 Políticas | 0.804 | 0.548 | 0.432 | Geopolítico |
| 23 Kessler | 0.776 | 0.542 | 0.471 | Orbital |
| 01 Clima | 0.372 | 0.100 | 0.990 | Físico |
| 04 Energía | 0.351 | 1.000 | 0.789 | Infraestructura |

**Evidencia aceptable**
- Comparación con modelos reducidos y ablación (macro_coupling=0).
- Reproducción externa con semillas fijas y datasets hashados.
- Reportes de fallos con C5 aplicado.
- Trazabilidad: todo dato citado con ruta a metrics.json y fase.
- forcing_scale < 1.0 por diseño — sin amplificación exógena.
