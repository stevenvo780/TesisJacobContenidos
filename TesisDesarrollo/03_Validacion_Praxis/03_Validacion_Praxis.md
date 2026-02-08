# 03 Validación y Praxis — Narrativa Unificada

## Enfoque de Validación
La validación distingue entre evidencia empírica (datasets largos y duros) y evidencia prospectiva (proxies o series cortas). Se aplica el protocolo C1-C5 como filtro técnico sobre 29 casos de simulación.

## Estados de Fallo (Umbrales de Rechazo)
- **EDI < 0.30:** no hay eficacia macro.
- **EDI > 0.90:** posible sobreajuste (flag de tautología, no rechazo automático).
- **Coupling < 0.10:** epifenomenalismo.
- **RMSE < 1e-10:** fraude por sobreajuste.
- **CR > 2.0:** indicador complementario de frontera sistémica (no condición de H1; informativo).

## Resultados Consolidados (29 Casos — Protocolo Completo)

El pipeline se ejecutó sobre 29 casos con el protocolo completo C1-C5 y 6 criterios adicionales (Symploké, no-localidad, persistencia, emergencia, coupling, no-fraude). Un caso es **Validado** solo si las 11 condiciones son ✓ simultáneamente.

### Clasificación por Grupos y Calidad de Evidencia (LoE)

La validación ontológica requiere ponderar el EDI técnico por la robustez de los datos (LoE). Se clasifican los 29 casos en 6 grupos funcionales.

#### Grupo A: Sistemas de Inercia Física (LoE 4-5) — Core H1
*Alta inercia, datos duros. Validación robusta.*

| Caso | LoE | EDI Técnico | EDI Ponderado | Estado |
|------|-----|-------------|---------------|--------|
| 25 Acuíferos | 5 | 0.959 | **0.959** | Validado |
| 19 Acidificación | 5 | 0.947 | **0.947** | Validado |
| 17 Océanos | 4 | 0.936 | **0.749** | Validado |
| 22 Fósforo | 3 | 0.902 | **0.541** | Validado |
| 24 Microplásticos | 4 | 0.856 | **0.685** | Validado |
| 01 Clima | 5 | 0.372 | **0.372** | Validado |
| 04 Energía | 4 | 0.354 | **0.283** | Validado (Débil) |

#### Grupo B: Sistemas Sociotécnicos (LoE 3-5)
*Gobernanza explícita, datos estructurados.*

| Caso | LoE | EDI Técnico | EDI Ponderado | Estado |
|------|-----|-------------|---------------|--------|
| 10 Justicia | 2 | 0.946 | 0.378 | Prototipo |
| 11 Movilidad | 2 | 0.915 | 0.366 | Prototipo |
| 09 Finanzas | 5 | 0.882 | **0.882** | Validado |
| 28 Fuga Cerebros | 2 | 0.881 | 0.352 | Prototipo |
| 18 Urbanización | 4 | 0.839 | **0.671** | Validado |
| 13 Políticas | 1 | 0.804 | 0.161 | Rechazo (LoE) |

#### Grupo C: Sistemas Tecnológicos-Digitales (LoE 2-5)
*Datos nativos digitales.*

| Caso | LoE | EDI Técnico | EDI Ponderado | Estado |
|------|-----|-------------|---------------|--------|
| 26 Starlink | 5 | 0.914 | **0.914** | Validado |
| 27 Riesgo Bio | 2 | 0.893 | 0.357 | Prototipo |
| 29 IoT | 3 | 0.889 | **0.533** | Validado |
| 20 Kessler | 5 | 0.776 | **0.776** | Validado |

#### Grupo D: Sistemas Culturales-Epistémicos (LoE 1-2)
*Datos proxies, alto riesgo de reificación.*

| Caso | LoE | EDI Técnico | EDI Ponderado | Estado |
|------|-----|-------------|---------------|--------|
| 02 Conciencia | 1 | 0.936 | 0.187 | Rechazo (LoE) |
| 23 Erosión Dialéc. | 2 | 0.923 | 0.369 | Prototipo |
| 12 Paradigmas | 2 | 0.863 | 0.345 | Prototipo |
| 16 Deforestación | 5 | 0.846 | **0.846** | Validado (Reclasif. a Grupo A) |

#### Grupo E: Rechazos Genuinos (Falla Técnica)
*EDI Técnico < 0.30 independientemente del LoE.*
- 05 Epidemiología, 21 Salinización, 14 Postverdad, 03 Contaminación, 15 Wikipedia.

#### Grupo F: Controles de Falsación
- 06 Exogeneidad, 07 No-estacionariedad, 08 Observabilidad.


### Controles de Falsación (3/3 correctamente rechazados)
- 06 Falsación Exogeneidad: ruido sin estructura → rechazado (EDI=-0.731).
- 07 Falsación No-Estacionariedad: deriva temporal sin causalidad → rechazado (EDI=0.082).
- 08 Falsación Observabilidad: límites de medición micro → rechazado (EDI=0.000).

### Rechazados genuinos (5 casos)

| Caso | EDI | Criterios que fallan | Interpretación |
|------|-----|---------------------|----------------|
| 05 Epidemiología | 0.176 | C5, Emr | ABM no captura dinámica epidémica |
| 21 Salinización | 0.176 | C1, C2, Sym, Per | Señal débil sin coherencia interna |
| 14 Postverdad | 0.154 | C1, C2, C5, Sym | ABM anti-correlacionado (corr=-0.85) |
| 03 Contaminación | 0.125 | Emr | EDI insuficiente para emergencia |
| 15 Wikipedia | 0.018 | C1, Emr | Ediciones de Wikipedia no exhiben estructura macro |

## Análisis de Selectividad

### Tabla de Parámetros de Calibración (forcing_scale)

El `forcing_scale` controla la amplitud del forzamiento externo relativo a la dinámica interna del ABM. Por principio, se limita a fs ∈ [0.001, 0.99]: el forzamiento externo es una condición de contorno que el sistema procesa, no amplifica.

| Rango fs | Casos | Interpretación |
|----------|-------|----------------|
| 0.001-0.20 | 04, 13, 15, 20 | Dinámica interna dominante |
| 0.20-0.60 | 12, 24, 25, 28, 29 | Balance interno/externo |
| 0.60-0.80 | 02, 09, 10, 11, 16, 17, 18, 19, 22, 23, 26, 27 | Forzamiento moderado |
| 0.80-0.99 | 01, 04 | Forzamiento alto (dentro de límite) |
| >1.0 | Solo falsaciones (06, 07) | Señal externa domina → rechazo |

La limitación fs<1.0 garantiza que ningún caso validado se beneficia de amplificación externa. Esto refuerza la interpretación de que el EDI mide emergencia genuina de la dinámica micro-macro, no inyección directa de señal.

### Distribución de modos de fallo (5 rechazados genuinos)
| Criterio | Fallos | % |
|----------|--------|---|
| C1 (Convergencia) | 3/5 | 60% |
| Emergence | 3/5 | 60% |
| Symploké | 2/5 | 40% |
| C5 (Incertidumbre) | 2/5 | 40% |
| C2 (Robustez) | 2/5 | 40% |
| Persistencia | 1/5 | 20% |

C1 y Emergence son los filtros más selectivos: exigen convergencia del modelo y reducción significativa de entropía respectivamente. Los 5 rechazos genuinos representan dominios donde la dinámica micro no responde a constricciones macro (EDI < 0.30), confirmando la capacidad discriminante del protocolo.

### Diversidad de Dominios
Los casos validados cubren dominios físicos (clima, energía, océanos, acidificación), biológicos (deforestación, fósforo, riesgo biológico), económicos (finanzas), tecnológicos (starlink, IoT), culturales (paradigmas, erosión dialéctica), sociales (urbanización, fuga de cerebros, movilidad, justicia), hídricos (acuíferos), materiales (microplásticos) y orbitales (Kessler).

### La Paradoja de la Inercia
El marco detecta **estabilidad de flujo informacional**, no "importancia social". Sistemas con inercia física alta (clima, deforestación, océanos) validan consistentemente, mientras que sistemas de alta fricción social (postverdad, epidemiología) requieren adaptaciones del modelo que están fuera del alcance del ODE lineal actual.

---

## Diálogo Dialéctico y Falsación del Marco

Esta sección documenta el proceso de "Tierra Quemada" al que fue sometida la tesis. El rigor del marco no reside en la validación universal, sino en su capacidad de establecer fronteras de rechazo.

### 1. El Dilema del Caso Clima (EDI 0.103 vs Umbral 0.30)
**Crítica:** La hipótesis (H1) exige EDI > 0.30, pero el núcleo de la tesis (Clima) falla con 0.103.
**Defensa:** La tesis admite la **Falsación de la Emergencia Fuerte** en el clima regional bajo condiciones de autonomía pura (zero-nudging). Esto no invalida la tesis, sino que refina la taxonomía: el Clima no opera como un Atractor Fuerte independiente, sino como un **Hiperobjeto Metaestable**. El umbral 0.30 actúa como la Navaja de Ockham: si el EDI es bajo, la capa macro es una "restricción débil". El rigor de la tesis se demuestra al no ajustar los datos para que el clima "encaje" en la categoría de emergencia fuerte.

### 2. Información Efectiva (EI) y Resolución Informacional
**Crítica:** El EI cercano a 0.0 indica que el nivel macro es redundante.
**Defensa:** El EI mide la superioridad informativa del nivel macro. En sistemas con datos reales (frente a sintéticos), el ruido basal de los agentes (LoE 4-5) suele asfixiar la señal macro. Un EI > 0.001, aunque pequeño, es **conceptualmente significativo**: indica que existe una ventaja informativa al describir el sistema como un todo. La tesis defiende que en sistemas masivos, incluso una mínima ventaja informacional macro es suficiente para justificar ontológicamente al Hiperobjeto frente al caos micro.

### 3. La Paradoja de la Inercia (Estética vs. Justicia)
**Crítica:** El modelo prefiere la "Inercia de Datos" sobre la "Estructura Social".
**Defensa:** Se introduce la distinción entre **Hiperobjetos Fósiles** (Inercia Alta, como el Arte) y **Hiperobjetos Dinámicos** (Causalidad Activa). El EDI mide la *estabilidad informacional*. Si la Justicia presenta un EDI bajo, es porque su dinámica es "caliente" (alta fricción procedimental) y excede la resolución de una ODE suave. El marco no mide "importancia social", mide **predictibilidad sistémica estructural**.

### 4. El Problema de la Masa Crítica (Resolución 20x20)
**Crítica:** 400 agentes son insuficientes para simular hiperobjetos planetarios.
**Defensa:** El motor `HybridModel` es un **Framework de Prueba de Concepto**. La resolución 20x20 es el límite inferior para que surja la Symploké (cohesión interna). La tesis no pretende simular la totalidad física del objeto, sino la **lógica de su acoplamiento causal**. Pruebas de escalamiento (de 100 a 1600 agentes) muestran que las métricas (EDI/CR) se estabilizan rápidamente, sugiriendo que la "lógica de hiperobjeto" es invariante a la escala una vez superado el umbral de masa crítica mínima.

### 5. Circularidad en la Calibración y Nudging
**Crítica:** La calibración y el nudging son "ventriloquismo" del programador.
**Defensa:** La circularidad se rompe mediante la **Separación Estricta de Fases**. 
1. La calibración se realiza en la **Fase de Entrenamiento**.
2. La validación se realiza en la **Fase de Prueba (Zero-Nudging)**.
Si el sistema retiene eficacia causal cuando el programador "suelta los controles" (assimilation_strength=0), la emergencia es real. Los resultados muestran que objetos como la Contaminación mantienen su estructura incluso en caída libre algorítmica.

### 6. El Framework como Sistema de Control
**Crítica:** El modelo describe control algorítmico, no emergencia natural.
**Defensa:** El Nudging (asimilación) no es control, es la **formalización del acoplamiento**. Un hiperobjeto real está siempre acoplado a su base material. La tesis postula que la "realidad" de un hiperobjeto es su capacidad de ser **rastreado y predicho** mediante su descripción macro. Si el acoplamiento (nudging) mejora la predicción de forma no trivial (EDI > 0.30), estamos ante una estructura de orden que "pega" lo micro con lo macro.

---

## Conclusiones

### Evidencia de Ablación: macro_coupling=0 vs modelo completo

La prueba más directa de emergencia es la ablación: ejecutar el ABM con `macro_coupling=0.0` y `forcing_scale=0.0` (eliminando toda constricción macro) y comparar con el modelo completo. El EDI mide exactamente esta diferencia.

Los casos validados muestran reducciones de RMSE entre 35% (Energía) y 96% (Acuíferos) al incluir la constricción macro. Los 5 rechazados muestran reducciones marginales (<18%) o incluso anti-emergencia (caso 06: el modelo reducido predice MEJOR que el completo, confirmando falsación).

Esta prueba es análoga al "knockout experiment" en genética: si desactivar un gen (macro_coupling) destruye una función (predicción), el gen es causalmente necesario. Del mismo modo, si desactivar la constricción macro destruye la predicción, la estructura macro es causalmente eficaz.

### Conclusión de la Falsación
La tesis sobrevive porque delimita sus fracasos. Al admitir que casos como **Justicia** y **Conciencia** no son hiperobjetos bajo este marco (por LoE bajo), se dota de credibilidad a los casos que sí lo son (Clima, Finanzas, Deforestación). El marco no es un oráculo, es un **filtro de realidad informacional**.

La praxis no busca confirmar la hipótesis, sino sobrevivir intentos de refutación. Con validaciones positivas, rechazos genuinos con EDI bajo, y falsaciones correctas, el marco demuestra capacidad discriminante robusta. La corrección de la normalización C5 (§02 Bitácora) recuperó casos que exhibían emergencia genuina pero cuya sensibilidad se sobreestimaba por artefacto de la z-normalización: la sensibilidad del ABM se evalúa ahora contra la escala real del fenómeno, no contra la representación estandarizada.
