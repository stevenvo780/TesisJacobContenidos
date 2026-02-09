# 03 Validación y Praxis — Narrativa Unificada

## Enfoque de Validación
La validación distingue entre evidencia empírica (datasets largos y duros) y evidencia prospectiva (proxies o series cortas). Se aplica el protocolo C1-C5 como filtro técnico sobre 29 casos de simulación. La evaluación se realiza con `assimilation_strength=0.0` (zero-nudging), eliminando toda asistencia observacional durante la fase de validación.

## Estados de Fallo (Umbrales de Rechazo)
- **EDI < 0.30:** no hay eficacia macro.
- **EDI > 0.90:** posible sobreajuste (flag de tautología, no rechazo automático).
- **Coupling < 0.10:** epifenomenalismo.
- **RMSE < 1e-10:** fraude por sobreajuste.
- **CR > 2.0:** indicador complementario de frontera sistémica (no condición de H1; informativo).

## Resultados Consolidados (29 Casos — Protocolo Completo)

El pipeline se ejecutó sobre 29 casos con el protocolo completo C1-C5 y 6 criterios adicionales (Symploké, no-localidad, persistencia, emergencia, coupling, no-fraude). Un caso es **Validado** solo si las 11 condiciones son ✓ simultáneamente. La significancia estadística se evalúa mediante permutation test con 999 permutaciones (seed=42).

> **Estado actual:** Bajo el pipeline limpio (sin data leakage, zero-nudging, 999 permutaciones): **overall_pass = 2/29** (Deforestación y Microplásticos). La hipótesis H1 queda **parcialmente confirmada** bajo la taxonomía de emergencia diferenciada.

### Taxonomía de Emergencia (6 categorías)

| Categoría | Criterio | Conteo | Función |
|-----------|----------|--------|---------|
| **strong** | EDI > 0.30, p < 0.05, overall_pass=True | 2 | Evidencia positiva de H1 |
| **weak** | 0.10 ≤ EDI < 0.30, p < 0.05 | 1 | Señal macro sub-umbral H1 |
| **suggestive** | EDI > 0.01, p < 0.05 | 3 | Señal estadística, resolución insuficiente |
| **trend** | EDI > 0, p ≥ 0.05 | 7 | Tendencia positiva sin confirmación |
| **null** | EDI ≤ 0 o sin señal | 13 | Sin constricción macro detectable |
| **falsification** | Controles negativos diseñados | 3 | Correctamente rechazados |
| **Total** | | **29** | |

### Clasificación por Resultado

#### Casos con Emergencia Fuerte (strong) — overall_pass=True

| Caso | EDI | p-perm | CR | BC | Interpretación |
|------|----:|-------:|---:|:---|:---|
| 16 Deforestación | **0.633** | 0.000 | 1.017 | full | ODE von Thünen: frontera agrícola capturada. 63% reducción RMSE |
| 24 Microplásticos | **0.427** | 0.000 | 1.002 | none | Modelo Jambeck: acumulación persistente. Sin BC necesario |

Estos dos casos satisfacen H1 completamente: EDI > 0.30 con significancia estadística (p < 0.001), protocolo C1-C5 completo, y las 11 condiciones simultáneas. Representan evidencia de **constricción macro efectiva** en sistemas con inercia material.

#### Caso con Emergencia Débil (weak)

| Caso | EDI | p-perm | CR | BC | Interpretación |
|------|----:|-------:|---:|:---|:---|
| 28 Fuga de Cerebros | **0.183** | 0.001 | 1.008 | bias_only | Docquier-Rapoport: migración de capital humano. Señal significativa pero sub-umbral H1 |

#### Casos con Señal Sugestiva (suggestive)

| Caso | EDI | p-perm | CR | Interpretación |
|------|----:|-------:|---:|:---|
| 09 Finanzas | 0.040 | 0.000 | 0.000 | Señal estadística, magnitud insuficiente |
| 17 Océanos | 0.053 | 0.000 | 1.334 | Proxy WMO, señal detectable |
| 29 IoT | 0.020 | 0.000 | 1.053 | Señal se atenúa en datos reales |

Señal estadísticamente significativa (p < 0.05 y EDI > 0.01) pero de magnitud insuficiente para afirmaciones ontológicas.

#### Casos con Tendencia no Significativa (trend)

| Caso | EDI | p-perm | Interpretación |
|------|----:|-------:|:---|
| 01 Clima | 0.010 | 0.591 | ODE Budyko-Sellers insuficiente |
| 11 Movilidad | 0.003 | 0.361 | Señal marginal |
| 13 Políticas | 0.011 | 0.719 | Señal débil |
| 14 Postverdad | 0.001 | 0.030 | Marginal |
| 18 Urbanización | 0.000 | 0.220 | Señal nula en práctica |
| 21 Salinización | 0.027 | 0.724 | Proxy inadecuado |
| 27 Riesgo Biológico | 0.105 | 0.365 | Señal no significativa |

#### Casos sin Evidencia (null)

13 casos con EDI ≤ 0 o sin señal detectable: Conciencia (-0.024), Contaminación (-0.000), Energía (-0.003), Epidemiología (0.000), Justicia (0.000), Paradigmas (0.000), Wikipedia (0.000), Acidificación (-0.000), Kessler (-0.420), Fósforo (-1.000), Erosión Dialéctica (-1.000), Acuíferos (-0.179), Starlink (-1.000). En estos casos, la constricción macro no mejora (o empeora) la predicción del ABM.

#### Controles de Falsación (3/3 correctamente rechazados)
- 06 Falsación Exogeneidad: ruido sin estructura → rechazado (EDI=0.055, categoría falsification).
- 07 Falsación No-Estacionariedad: deriva temporal sin causalidad → rechazado (EDI=-1.000).
- 08 Falsación Observabilidad: límites de medición micro → rechazado (EDI=-1.000).

### Métricas Globales de Robustez

| Métrica | Valor | Descripción |
|---------|-------|-------------|
| **Significancia** (p<0.05 + EDI>0.01) | 6/29 | Casos con señal estadística |
| **Estabilidad numérica** (ns_stable) | 25/29 | Fallan: 05, 12, 13, 18 |
| **Persistencia** (std < 5× ratio) | 27/29 | Fallan: 11 (ratio=9.65), 20 (ratio=276777) |
| **Bias Correction aplicado** | 17/29 | {full:5, bias_only:12, none:10, reverted:2} |
| **Reproducibilidad** | 100% | seed=42, 999 permutaciones |

## Análisis de Selectividad

### Distribución de modos de fallo (24 rechazados genuinos)

De los 26 casos genuinos (excluyendo 3 falsaciones), 24 son rechazados. La distribución de fallos revela los filtros más selectivos:

| Criterio | Descripción |
|----------|-------------|
| **Emergence (EDI < 0.30)** | Filtro primario: la mayoría no alcanzan el umbral de eficacia causal |
| **C1 (Convergencia)** | Segundo filtro: modelos ODE inadecuados producen baja convergencia ABM-datos |
| **Symploké** | Cohesión interna insuficiente en dominios con datos ruidosos |

### Diversidad de Dominios
Los 29 casos cubren dominios físicos (clima, energía, océanos, acidificación), biológicos (deforestación, fósforo, riesgo biológico, epidemiología), económicos (finanzas), tecnológicos (Starlink, IoT, Kessler), culturales (paradigmas, erosión dialéctica, conciencia), sociales (urbanización, fuga de cerebros, movilidad, justicia, postverdad), hídricos (acuíferos, salinización), materiales (microplásticos, contaminación) y de gobernanza (políticas estratégicas, Wikipedia).

### La Paradoja de la Inercia — Resuelta

Los dos únicos casos con emergencia fuerte (Deforestación EDI=0.633 y Microplásticos EDI=0.427) son sistemas con **inercia material**: la frontera agrícola se desplaza lentamente (deforestación) y los plásticos se acumulan persistentemente en océanos. El caso con emergencia débil (Fuga de Cerebros EDI=0.183) también exhibe inercia demográfica.

Esto confirma la hipótesis de que el marco detecta **estabilidad de flujo informacional** en sistemas donde la constricción macro opera sobre sustratos con inercia física o biológica. Los sistemas con alta reflexividad (finanzas), alta volatilidad (clima regional), o datos indirectos (conciencia, postverdad) no alcanzan el umbral, consistente con las limitaciones teóricas del modelo híbrido.

### Diagnóstico: ¿Por Qué la Mayoría No Muestra Emergencia?

1. **Modelos ODE inadecuados:** La ODE no captura la dinámica macro del dominio, generando una señal que interfiere con el ABM en lugar de mejorarlo.
2. **No-estacionariedad:** La ODE se ajusta bien en entrenamiento pero la relación se degrada en validación por cambios estructurales.
3. **Coupling destructivo:** El sesgo del ODE destruye información útil. El Bias Correction resolvió esto para Deforestación; otros casos persisten.
4. **Señal-ruido insuficiente (3 suggestive):** La señal macro existe (p < 0.05) pero el ruido domina, produciendo EDI < 0.10. Límite del SNR de los datos, no del marco.

---

## Diálogo Dialéctico y Falsación del Marco

El rigor del marco no reside en la validación universal, sino en su capacidad de establecer fronteras de rechazo.

### 1. El Dilema del Caso Clima (EDI=0.010 vs Umbral 0.30)
**Crítica:** La hipótesis (H1) exige EDI > 0.30, pero el caso paradigmático (Clima) obtiene EDI=0.010 (trend).
**Defensa:** La tesis admite la no-emergencia del clima regional bajo el modelo Budyko-Sellers con resolución de datos actual. Esto no invalida el marco, sino que refina la taxonomía: el clima regional no opera como un atractor fuerte independiente bajo estas condiciones de modelado. El umbral 0.30 actúa como Navaja de Ockham: si el EDI es bajo, la capa macro es una restricción débil. El rigor se demuestra al no ajustar resultados para que el clima "encaje".

### 2. Información Efectiva (EI) y sus Limitaciones
**Crítica:** El EI produce valores negativos en sistemas socio-técnicos.
**Defensa:** La EI negativa indica que los residuos del modelo completo son más entrópicos que los del modelo reducido — una propiedad esperable cuando el macro extrae la señal estructurada. El EDI permanece como métrica principal porque mide eficacia predictiva sin supuestos sobre la entropía residual. La EI opera como indicador complementario, no como condición de H1.

### 3. El Problema de la Masa Crítica (Resolución 20×20)
**Crítica:** 400 agentes son insuficientes para simular hiperobjetos planetarios.
**Defensa:** El motor HybridModel es un framework de prueba de concepto. La resolución 20×20 es el límite inferior para que surja la Symploké. Pruebas de escalamiento (100 a 1600 agentes) muestran que EDI y CR se estabilizan rápidamente, sugiriendo que la lógica de hiperobjeto es invariante a la escala por encima del umbral de masa crítica mínima.

### 4. Circularidad en la Calibración
**Crítica:** La calibración y el nudging son "ventriloquismo" del programador.
**Defensa:** La circularidad se rompe mediante la separación estricta de fases: calibración en ventana de entrenamiento, validación en ventana de prueba con `assimilation_strength=0.0`. Si el sistema retiene eficacia causal cuando el programador "suelta los controles", la emergencia es real. Los 2 casos validados demuestran precisamente esto.

---

## Conclusiones

### Estado actual: H1 parcialmente confirmada — marco operativo y selectivo

El resultado principal es **2/29 overall_pass** bajo el pipeline con evaluación estricta (zero-nudging, sin data leakage, 999 permutaciones). La hipótesis H1 (EDI > 0.30 + protocolo C1-C5) se confirma en dos casos con emergencia fuerte:

- **Deforestación** (EDI=0.633): constricción macro de la frontera agrícola, verificada con datos World Bank.
- **Microplásticos** (EDI=0.427): acumulación persistente, verificada con datos OWID.

Adicionalmente, 4 casos muestran señal estadísticamente significativa (weak + suggestive), y 7 presentan tendencias positivas no confirmadas.

### Valor epistemológico del resultado

1. **El marco es falsable:** La corrección del data leakage colapsó los EDI inflados de versiones anteriores, demostrando que el protocolo no es un rubber-stamp.
2. **Los controles de falsación funcionan:** Los 3 controles (06-08) son correctamente rechazados con categoría falsification.
3. **La selectividad es alta:** Solo 2/26 casos genuinos pasan (7.7%), descartando la posibilidad de inflación sistemática.
4. **El espectro es informativo:** La taxonomía de 6 categorías (strong → falsification) produce un mapa de evidencia más rico que el binario pasa/no pasa.

### Reformulación de H1

La tesis se reformula desde "todos los hiperobjetos muestran emergencia" hacia: **"El protocolo EDI + C1-C5 discrimina efectivamente entre sistemas con constricción macro genuina y sistemas sin ella. Ciertos fenómenos con inercia material (deforestación, microplásticos) demuestran constricción macro que resiste eliminación, satisfaciendo el criterio de patrón macro real."**

La honestidad de reportar 2/29 — distinguiendo el espectro completo de evidencia — es la mejor demostración de rigor científico del marco.

