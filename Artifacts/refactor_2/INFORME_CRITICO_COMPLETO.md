# INFORME CRITICO EXHAUSTIVO — Refactor 2
## Auditoria Post-Gladiadores: Debilidades Tecnicas Solucionables

**Fecha:** 2026-02-08
**Auditor:** Claude Opus 4.6 (revision independiente)
**Alcance:** Todas las criticas del Torneo de Gladiadores (20 rondas) + auditoria tecnica del codigo + revision de datos

---

## ACTUALIZACIÓN POST‑EJECUCIÓN (2026-02-08)

**Resumen crítico tras re‑ejecución completa con motor corregido:**

- **Validaciones reales ejecutadas (29/29)** con `HYPER_GRID_SIZE=20` y `HYPER_N_RUNS=5`.  
  Resultado: **EDI válido en 1/29** y **overall_pass = 0/29**.  
- **Distribución nula EDI (GPU):** umbral recomendado **0.3248**;  
  **P(EDI>0.30 | H0) = 0.19**, por lo tanto **0.30 no es significativo**.  
- **Run GPU mega‑escala ejecutado** (`universal_run.py`):  
  **470x470 grid**, **6000 batches**, **421.7s** totales, outputs en `outputs_gpu/`.  
- **Notas operativas:** `pytrends` no instalado → casos 02 y 14 usan fallback sintético.  

**Conclusión provisional:** Con el pipeline limpio (sin leakage y EDI corregido), la validación **colapsa**. La hipótesis H1 queda **no confirmada** bajo criterios estrictos.  

---

## INDICE

1. [Resumen Ejecutivo](#1-resumen-ejecutivo)
2. [Las 20 Criticas del Torneo — Clasificacion por Solucionabilidad](#2-criticas-del-torneo)
3. [Hallazgos Criticos Nuevos (Auditoria Tecnica)](#3-hallazgos-criticos)
4. [Tabla Maestra de Metricas — Anomalias](#4-tabla-de-metricas)
5. [Auditoria de Fuentes de Datos — Variables Faltantes](#5-datos-faltantes)
6. [Plan de Mejoras Concretas por Prioridad](#6-plan-de-mejoras)
7. [Veredicto Final](#7-veredicto)

---

## 1. RESUMEN EJECUTIVO

La tesis presenta un marco computacional ABM+ODE para validar la existencia de hiperobjetos. Tras 20 rondas de debate adversarial y auditoria tecnica profunda del codigo, se identifican **7 problemas criticos** que debilitan la tesis, de los cuales **5 son solucionables tecnicamente**:

| Problema | Severidad | Solucionable? | Esfuerzo |
|----------|-----------|---------------|----------|
| ODE generica (28/29 iguales) | CRITICA | SI | ALTO |
| Data leakage en forcing (obs[t-1]) | CRITICA | SI | MEDIO |
| 46% de casos usan datos sinteticos | CRITICA | SI | ALTO |
| Agentes homogeneos (dom_share=1/N) | ALTA | SI | MEDIO |
| EDI no involucra la ODE | ALTA | SI | MEDIO |
| 9 casos con EDI>0.90 (tautologia) | ALTA | PARCIAL | MEDIO |
| Proxies inadecuados (3 casos) | MEDIA | SI | BAJO |

**Si se resuelven estos problemas, la tesis pasa de "aprobacion muy condicionada" a potencialmente solida.**

---

## 2. CRITICAS DEL TORNEO — Clasificacion por Solucionabilidad

### GRUPO A: SOLUCIONABLES TECNICAMENTE (mejorando simulaciones)

| # | Critica | Iteracion | Solucion Propuesta |
|---|---------|-----------|-------------------|
| C1 | **EDI > 0.30 es numero magico** | R1, Brutal | Derivar umbral de distribucion nula (bootstrap de EDI bajo ruido puro). Ya existe parcialmente con `edi_null_distribution_analysis.py`. Ejecutar y publicar la distribucion. |
| C2 | **EI = 0.0 en todos los casos** | R3 | Bug ya corregido (KDE). Verificar que EI > 0 en ejecucion actual. |
| C3 | **ODE tiene correlacion nula en Clima (-0.027)** | R15 | La ODE de Clima tiene alpha=0.001 (casi inerte). Implementar ODE con balance radiativo real usando CO2 como forcing en lugar de obs[t-1]. |
| C4 | **forcing_scale > 1.0 viola A6** | R13, R17 | Ya corregido: cap en 0.99. Verificar en todos los metrics.json actuales (CONFIRMADO: ningun caso viola A6 actualmente). |
| C5 | **Dominance_share = 1/N (agentes clonados)** | R19, R20 | Existe `abm_gpu_v3.py` con forcing_gradient pero NO se usa. Integrar en validaciones: topologias no regulares, forzamiento espacial heterogeneo, parametros locales. |
| C6 | **macro_coupling = 1.0 (esclavizacion)** | R11, R17 | 22/29 casos tienen mc > 0.5. Recalibrar con restriccion mc < 0.5 y reportar cual es el mc minimo que mantiene EDI > 0.30. |
| C7 | **Datos sinteticos en 12 casos** | R11, Brutal | Implementar fuentes de datos reales para al menos 8 de los 12 casos sinteticos (ver Seccion 5). |
| C8 | **Proxies inadecuados** (Kessler=vuelos, Starlink=internet) | Nueva | Reemplazar con datos de CelesTrak (objetos orbitales) para Kessler y Starlink. |
| C9 | **Fases sinteticas compartidas entre casos** | Nueva | Al menos 5 grupos de casos comparten parametros sinteticos identicos. Cada caso debe tener parametros de ODE sintetica calibrados a su dominio. |
| C10 | **Data leakage: forcing contiene obs[t-1]** | Nueva | En `hybrid_validator.py:646-647`, `lag_forcing = obs[t-1]` contamina la validacion. El forcing debe construirse SOLO con datos del periodo de entrenamiento. |

### GRUPO B: REQUIEREN REFACTOR ARQUITECTURAL

| # | Critica | Iteracion | Solucion Propuesta |
|---|---------|-----------|-------------------|
| C11 | **ODE generica (28/29 usan la misma ecuacion)** | R15, R19 | Implementar ODEs domain-specific: balance radiativo (clima), Heston/GBM (finanzas), Darcy (acuiferos), SEIR (epidemio ya lo tiene). Minimo 5 ODEs distintas. |
| C12 | **EDI compara ABM_completo vs ABM_nulo (umbral trivial)** | R20, Nueva | Redisenar EDI para comparar ABM+ODE_acoplado vs ABM_solo. Requiere implementar acoplamiento bidireccional ABM-ODE real. |
| C13 | **No hay acoplamiento ABM-ODE en el codigo** | Nueva | ABM y ODE corren independientemente. Implementar paso de informacion ODE->ABM (estado macro guia agentes) y ABM->ODE (estadisticas micro informan parametros macro). |
| C14 | **Grid 20x20 (400 agentes) es toy-model** | R5, Pendientes | Escalar a 100x100 (10,000 agentes) o usar GPU v3 existente con grids mayores. Reportar sensibilidad al tamano de grid. |

### GRUPO C: CRITICAS ONTOLOGICAS (no solucionables con codigo)

| # | Critica | Iteracion | Estrategia Defensiva |
|---|---------|-----------|---------------------|
| C15 | **"Constriccion macro" no es "ontologia fuerte"** | R19, R20, Veredicto | Aceptar: la tesis valida constriccion macro efectiva bajo realismo operativo debil. Declerar explicitamente. |
| C16 | **Circularidad en calibracion** | Termonuclear | El forcing contiene datos observacionales, pero la evaluacion se hace sin assimilation. Documentar el protocolo de separacion train/eval. |
| C17 | **"Inercia de datos" vs "ontologia"** | Termonuclear | Admitir que el marco detecta inercia informacional. Argumentar que la inercia es evidencia de constriccion (no al reves). |
| C18 | **Sesgo de predictibilidad** | Pendientes | Las series suaves dan EDI alto. Documentar como limitacion. Incluir test de sensibilidad a ruido. |
| C19 | **Paradoja Estetica > Justicia** | Termonuclear | Justicia ahora es sintetico (EDI=0.946, tautologico). Si se pasa a datos reales, el resultado sera genuino. |
| C20 | **Tono "Modo Dios"** | Brutal | Revisar narrativa de capitulos 02-04, agregar mas humildad y limitaciones explicitas. |

---

## 3. HALLAZGOS CRITICOS NUEVOS (Auditoria Tecnica)

### 3.1. DATA LEAKAGE EN EL FORCING (SEVERIDAD: CRITICA)

**Archivo:** `common/hybrid_validator.py`, lineas 644-647

```python
forcing_trend, trend_params = build_forcing_from_training(obs[:val_start], steps)
lag_forcing = [obs[0]] + obs[:-1]  # <-- FUGA DE DATOS
forcing_series = [forcing_trend[i] + 0.5 * lag_forcing[i] for i in range(steps)]
```

**Problema:** El `lag_forcing` es `obs[t-1]` para TODO el rango temporal, incluyendo el periodo de validacion. Esto significa que durante la evaluacion (t >= val_start), el ABM recibe como forcing las observaciones reales del periodo que se intenta predecir, desplazadas un paso.

**Impacto:** Infla artificialmente las metricas del ABM completo y, por extension, el EDI. La mejora del ABM sobre el modelo nulo viene en parte de este data leakage, no de emergencia macro genuina.

**Solucion:** Truncar `lag_forcing` al periodo de entrenamiento y extrapolar para el periodo de validacion:
```python
# Correcto: solo usar datos del entrenamiento
lag_forcing = [obs[0]] + obs[:val_start-1]  # Solo entrenamiento
# Para validacion: extrapolar con ultimo valor o tendencia
```

### 3.2. LA ODE NO PARTICIPA EN EL EDI (SEVERIDAD: ALTA)

**Archivo:** `common/hybrid_validator.py`, lineas 696-720

El EDI se calcula como:
```
EDI = (RMSE_reduced - RMSE_abm) / RMSE_reduced
```

Donde:
- `RMSE_abm` = error del ABM **completo** (con forcing + macro_coupling)
- `RMSE_reduced` = error del ABM **sin forcing NI macro_coupling**

La ODE se ejecuta y reporta, pero **no entra en el calculo del EDI**. El EDI mide "cuanto ayuda tener forcing" vs "no tener nada", no "cuanto ayuda la ODE".

### 3.3. ABM y ODE CORREN INDEPENDIENTEMENTE (SEVERIDAD: ALTA)

```python
abm = simulate_abm_fn(eval_params, steps, seed=2)   # Independiente
ode = simulate_ode_fn(eval_params, steps, seed=3)    # Independiente
```

No hay acoplamiento bidireccional. El `macro_coupling` dentro del ABM acopla cada celda al **promedio de la propia grilla**, NO a la salida de la ODE. Esto contradice la narrativa de "acoplamiento hiperobjeto-materia".

### 3.4. HOMOGENIZACION RAPIDA DE AGENTES (SEVERIDAD: ALTA)

Simulacion directa del ABM con parametros tipicos:

| Paso | Varianza inter-agente | CoV |
|------|----------------------|-----|
| 0 | 8.242 | -- |
| 5 | 0.014 | 0.005 |
| 10 | 0.0002 | 0.001 |
| 20 | 0.0002 | 0.002 |

La varianza cae un **99.7%** en 10 pasos. La combinacion de difusion isotopica + macro_coupling homogeniza la grilla casi instantaneamente. La GPU v3 con `forcing_gradient` fue creada para resolver esto, pero **no se usa en ninguna validacion**.

### 3.5. 9 CASOS CON EDI > 0.90 REPORTAN overall_pass=true (INCONSISTENCIA)

Las reglas de rechazo dicen EDI > 0.90 = RECHAZO por tautologia. Sin embargo, 9 casos en fase real superan este umbral y aun reportan `overall_pass: true`:

| Caso | EDI Real | overall_pass |
|------|----------|-------------|
| 02 Conciencia | 0.936 | true (INCONSISTENTE) |
| 10 Justicia | 0.946 | true (INCONSISTENTE) |
| 11 Movilidad | 0.915 | true (INCONSISTENTE) |
| 17 Oceanos | 0.936 | true (INCONSISTENTE) |
| 19 Acidificacion | 0.947 | true (INCONSISTENTE) |
| 22 Fosforo | 0.902 | true (INCONSISTENTE) |
| 23 Erosion | 0.923 | true (INCONSISTENTE) |
| 25 Acuiferos | 0.959 | true (INCONSISTENTE) |
| 26 Starlink | 0.914 | true (INCONSISTENTE) |

**Nota:** `edi.valid` es `false` en estos casos, pero `overall_pass` no lo refleja. El campo `overall_pass` no incorpora la regla de rechazo por EDI > 0.90.

---

## 4. TABLA MAESTRA DE METRICAS — ANOMALIAS

### 4.1. Resumen de Estado Real de los 29 Casos

| Grupo | Casos | Cantidad |
|-------|-------|----------|
| **Genuinamente validados** (EDI 0.30-0.90, datos reales, pass=true) | 04, 09, 12, 16 | **4** |
| **Tautologicos** (EDI > 0.90, datos reales) | (ninguno con datos reales) | **0** |
| **Tautologicos** (EDI > 0.90, datos sinteticos) | 02,10,11,17,19,22,23,25,26 | **9** |
| **Validados con datos reales pero borderline** | 01 (clima, EDI=0.37) | **1** |
| **Validados con datos sinteticos en rango** | 13,20,24,27,28,29 | **6** |
| **Rechazados correctamente** | 03,05,14,15,21 | **5** |
| **Controles de falsacion (correctos)** | 06,07,08 | **3** |
| **Caso bandera overall_pass=false** | 01 (clima) | **1** |

### 4.2. Conteo Honesto

- **Casos con datos reales Y EDI en rango valido (0.30-0.90):** Solo 4 (Energia, Finanzas, Paradigmas, Deforestacion) + Clima (0.37 pero overall_pass=false)
- **Casos con datos sinteticos:** 12 de 26 no-falsacion (46%)
- **Casos con macro_coupling > 0.5:** 22 de 29 (76%)
- **Casos donde ODE corr < 0:** 3 (clima, contaminacion, epidemiologia)

### 4.3. Flags Criticos por Caso (Fase Real)

| Caso | EDI | ODE corr | mc | Tipo dato | Flags |
|------|-----|----------|-----|-----------|-------|
| 01 Clima | 0.372 | **-0.027** | 0.10 | REAL | ODE fantasma, pass=false |
| 02 Conciencia | **0.936** | 0.983 | 0.49 | SINT | Tautologico |
| 03 Contaminacion | 0.125 | **-0.192** | **1.00** | REAL | Rechazado, ODE fantasma |
| 04 Energia | 0.354 | 0.414 | **1.00** | REAL | mc=1.0 (esclavizado) |
| 05 Epidemiologia | 0.176 | **-0.004** | **0.64** | REAL | Rechazado, ODE fantasma |
| 06 Falsac.Exog | -0.401 | 0.678 | **0.97** | REAL | Falsacion correcta |
| 07 Falsac.NoEst | 0.090 | 0.893 | **1.00** | REAL | Falsacion correcta |
| 08 Falsac.Obs | 0.000 | N/A | N/A | REAL | Falsacion correcta |
| 09 Finanzas | 0.882 | 0.986 | **1.00** | REAL | mc=1.0 (esclavizado) |
| 10 Justicia | **0.946** | 0.985 | **0.56** | SINT | Tautologico + sintetico |
| 11 Movilidad | **0.915** | 0.989 | **0.70** | SINT | Tautologico + sintetico |
| 12 Paradigmas | 0.863 | 0.993 | 0.39 | SINT | Mejor caso sintetico |
| 13 Politicas | 0.804 | 0.994 | **0.55** | SINT | mc>0.5 |
| 14 Postverdad | 0.154 | 0.988 | **0.80** | SINT | Rechazado, ABM corr=-0.85 |
| 15 Wikipedia | 0.018 | 0.518 | **1.00** | REAL | Rechazado |
| 16 Deforestacion | 0.846 | 0.894 | 0.10 | REAL | **MEJOR CASO** |
| 17 Oceanos | **0.936** | 0.990 | **0.57** | SINT | Tautologico + sintetico |
| 18 Urbanizacion | 0.839 | 0.999 | **0.58** | REAL | mc>0.5 |
| 19 Acidificacion | **0.947** | 0.992 | **0.57** | SINT | Tautologico + sintetico |
| 20 Kessler | 0.776 | 0.984 | **0.54** | REAL* | Proxy debil |
| 21 Salinizacion | 0.176 | 0.802 | **0.85** | REAL* | Rechazado, proxy debil |
| 22 Fosforo | **0.902** | 0.883 | **0.64** | REAL | Tautologico |
| 23 Erosion | **0.923** | 0.989 | 0.19 | SINT | Tautologico + sintetico |
| 24 Microplasticos | 0.856 | 0.994 | **0.73** | SINT | mc>0.5 |
| 25 Acuiferos | **0.959** | 0.990 | **0.64** | SINT | Tautologico + sintetico |
| 26 Starlink | **0.914** | 0.994 | 0.46 | REAL* | Tautologico + proxy nulo |
| 27 Riesgo Biol | 0.893 | 0.981 | **0.52** | SINT | mc>0.5 |
| 28 Fuga Cerebros | 0.881 | 0.992 | **0.65** | SINT | mc>0.5 |
| 29 IoT | 0.889 | 0.991 | 0.10 | SINT | Mejor calibrado sintetico |

---

## 5. AUDITORIA DE FUENTES DE DATOS — VARIABLES FALTANTES

### 5.1. Casos Sinteticos que PUEDEN Migrar a Datos Reales

| Caso | Variable Real Disponible | API/Fuente | Esfuerzo |
|------|-------------------------|------------|----------|
| **17 Oceanos** | SST (Sea Surface Temp) | NOAA ERSST v5 | BAJO |
| **19 Acidificacion** | pH oceanico | Hawaii Ocean Time-series (HOT) | BAJO |
| **25 Acuiferos** | GRACE water storage | NASA GRACE-FO | MEDIO |
| **12 Paradigmas** | Citations/papers por campo | OpenAlex API | MEDIO |
| **28 Fuga Cerebros** | R&D gasto % PIB | World Bank GB.XPD.RSDV.GD.ZS | BAJO |
| **29 IoT** | Suscripciones moviles | World Bank IT.CEL.SETS.P2 | BAJO |
| **13 Politicas** | Gasto militar % PIB | World Bank MS.MIL.XPND.GD.ZS | BAJO |
| **27 Riesgo Biol** | Mortalidad infantil | World Bank SH.DYN.MORT | BAJO |
| **11 Movilidad** | Vehiculos per capita | World Bank IS.VEH.NVEH.P3 | BAJO |
| **24 Microplasticos** | Produccion de plasticos | PlasticsEurope (manual) | MEDIO |
| **14 Postverdad** | Google Trends "fake news" | Google Trends API | BAJO |
| **10 Justicia** | Rule of Law Index | World Bank RL.EST | BAJO |

### 5.2. Proxies Inadecuados que Deben Reemplazarse

| Caso | Proxy Actual | Reemplazo Recomendado | API |
|------|-------------|----------------------|-----|
| 20 Kessler | Salidas aereas | Objetos en orbita | CelesTrak TLE |
| 26 Starlink | Usuarios internet | Satelites activos | CelesTrak TLE |
| 21 Salinizacion | Tierra arable % | Conductividad suelo | FAO GLOSIS |

### 5.3. Variables Faltantes para Casos con Datos Reales

**01 Clima** (actualmente solo temperatura):
- CO2 atmosferico → NOAA ESRL (Mauna Loa)
- Irradiancia solar → LASP TSI
- Contenido calor oceanico → NOAA OHC

**09 Finanzas** (actualmente solo SPY):
- VIX volatilidad → Yahoo Finance ^VIX
- Fed Funds Rate → FRED API
- Multiple activos → yfinance (QQQ, IWM, GLD)

**05 Epidemiologia** (actualmente solo casos COVID):
- Muertes → OWID new_deaths_smoothed
- Vacunacion → OWID people_vaccinated
- Stringency index → OxCGRT

**04 Energia** (actualmente solo carga GB):
- Precio electricidad → ENTSOE
- Renovables % → OPSD
- Temperatura → Meteostat

---

## 6. PLAN DE MEJORAS CONCRETAS POR PRIORIDAD

### PRIORIDAD 1: CRITICA (sin esto la tesis NO pasa)

| Accion | Archivo(s) | Descripcion |
|--------|-----------|-------------|
| **P1.1** Corregir data leakage | `common/hybrid_validator.py:646-647` | El `lag_forcing` no debe incluir obs del periodo de validacion. Truncar a entrenamiento y extrapolar. |
| **P1.2** Implementar ODEs domain-specific | `caso_*/src/ode.py` | Al menos para los 5 casos bandera: clima (balance radiativo), finanzas (volatilidad estocastica), epidemiologia (ya tiene SEIR), oceanos (difusion termica), acuiferos (Darcy). |
| **P1.3** Migrar 8+ casos sinteticos a datos reales | `caso_*/src/data.py` | Ver tabla 5.1. Priorizar oceanos, acidificacion, acuiferos, paradigmas, politicas, movilidad, justicia, fuga cerebros. |
| **P1.4** Corregir inconsistencia EDI>0.90 vs overall_pass | `common/hybrid_validator.py` | Si `edi.valid = false` (por >0.90), entonces `overall_pass` debe ser `false`. |

### PRIORIDAD 2: ALTA (fortalece significativamente)

| Accion | Archivo(s) | Descripcion |
|--------|-----------|-------------|
| **P2.1** Integrar heterogeneidad de agentes | `caso_*/src/abm.py` o usar `common/abm_gpu_v3.py` | Activar `forcing_gradient`, topologias no regulares (small-world), parametros locales variables. |
| **P2.2** Implementar acoplamiento ABM-ODE real | `common/hybrid_validator.py` + `caso_*/src/` | La salida de la ODE debe alimentar al ABM (como forcing o constraint macro), y las estadisticas del ABM deben informar parametros de la ODE. |
| **P2.3** Redisenar EDI para incluir la ODE | `common/hybrid_validator.py` | Comparar ABM_con_ODE vs ABM_sin_ODE, no vs ABM_sin_nada. |
| **P2.4** Restringir macro_coupling < 0.5 | `common/hybrid_validator.py` | Agregar restriccion en calibracion. Reportar resultados con mc limitado. |
| **P2.5** Reemplazar proxies inadecuados | `20_caso_kessler/src/data.py`, `26_caso_starlink/src/data.py` | Usar CelesTrak para datos orbitales reales. |

### PRIORIDAD 3: MEDIA (mejora robustez y credibilidad)

| Accion | Archivo(s) | Descripcion |
|--------|-----------|-------------|
| **P3.1** Escalar grid a 100x100 | `common/abm_gpu_v3.py` + validaciones | Demostrar que resultados son estables con N=10,000. |
| **P3.2** Independizar fases sinteticas por caso | `caso_*/src/validate.py` | Cada caso debe tener ODE sintetica con parametros calibrados a su dominio, no compartidos. |
| **P3.3** Agregar variables multivariadas | `caso_*/src/data.py` | Ver tabla 5.3. Al menos CO2 para clima, VIX para finanzas. |
| **P3.4** Publicar distribucion nula del EDI | `common/edi_null_distribution_analysis.py` | Ejecutar y documentar el umbral 0.30 derivado de la distribucion nula bajo ruido puro. |
| **P3.5** Replay total con hashes | Scripts de verificacion | Regenerar todos los outputs, registrar MD5, versionar en git. |

---

## 7. VEREDICTO FINAL

### Estado Actual de la Tesis

La tesis tiene un **nucleo conceptual valido** (la idea de medir constriccion macro via ABM+ODE es genuinamente innovadora), pero la **implementacion computacional tiene defectos estructurales** que la hacen vulnerable a criticas demoledoras:

1. **Solo 4 casos son genuinamente validados** con datos reales y EDI en rango: Energia, Finanzas, Paradigmas (sintetico), Deforestacion.
2. **El caso bandera (Clima) tiene overall_pass=false** y su ODE es un fantasma (corr = -0.027).
3. **El 46% de los "hiperobjetos" validados no existen** — son datos sinteticos generados por la misma ODE que luego se valida.
4. **El data leakage en el forcing** infla todas las metricas artificialmente.
5. **Los agentes son identicos** en la practica (varianza cae 99.7% en 10 pasos).

### Potencial Tras las Mejoras

Si se implementan las mejoras de Prioridad 1 y 2:

- **12 casos nuevos con datos reales** eliminarian la critica de "sinteticos"
- **ODEs domain-specific** darian credibilidad cientifica a cada caso
- **Corregir el data leakage** producira EDIs mas bajos pero mas honestos
- **Heterogeneidad de agentes** responderia la critica nuclear de "agentes clonados"
- **Acoplamiento real ABM-ODE** justificaria el nombre "modelo hibrido"

**La tesis es rescatable, pero requiere refactoring profundo en las simulaciones.** Las mejoras no son cosmeticas: son cambios en la arquitectura del motor de validacion que produciran resultados diferentes (y potencialmente mejores) a los actuales.

### Estimacion de Casos Post-Mejora

Con datos reales, ODEs adecuadas y forcing limpio, la estimacion conservadora es:

| Resultado Esperado | Casos |
|-------------------|-------|
| Validados genuinos (EDI 0.30-0.90) | 8-12 |
| Rechazados honestos | 8-12 |
| Controles de falsacion | 3 |
| Borderline (a investigar) | 4-6 |

**8-12 casos genuinamente validados con datos reales y ODEs especificas seria un resultado mucho mas fuerte que los 24 "validados" actuales con datos sinteticos y ODE generica.**

---

*Informe generado por Claude Opus 4.6 — Auditoria independiente post-Gladiadores*
*Todos los hallazgos son verificables en los archivos referenciados del repositorio.*
