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

> **Estado actual (2026-02-09):** Tras la corrección de data leakage, la inclusión de `edi_valid` en `overall_pass`, y la evaluación con `assimilation_strength=0.0`: **overall_pass = 0/29**. La hipótesis H1 queda **no confirmada** bajo criterios estrictos.

### Clasificación por Resultado

#### Casos con señal parcial en fase real (EDI_real > 0)

Estos casos muestran algún indicio de constricción macro, aunque insuficiente para pasar el protocolo completo:

| Caso | EDI_syn | EDI_real | Notas |
|------|---------|----------|-------|
| 24 Microplásticos | 0.679 | **0.586** | Mejor caso: OWID plastic production |
| 27 Riesgo Biológico | 0.409 | **0.414** | WorldBank mortalidad — señal consistente |
| 28 Fuga Cerebros | 0.491 | 0.213 | WorldBank I+D — señal débil |
| 17 Océanos | 0.110 | 0.119 | Proxy WMO — marginal |
| 09 Finanzas | -0.000 | 0.051 | Yahoo Finance SPY — casi nulo |
| 29 IoT | 0.414 | 0.014 | WorldBank — señal se pierde en real |
| 11 Movilidad | 0.020 | 0.003 | WorldBank — marginal |
| 14 Postverdad | 0.000 | 0.003 | Fallback sintético — marginal |

Solo los casos **24 (Microplásticos)** y **27 (Riesgo Biológico)** alcanzan EDI_real > 0.30, el umbral de H1. Sin embargo, fallan otros criterios del protocolo de 11 condiciones.

#### Casos con anti-emergencia (EDI_real < 0)

En estos casos, el ABM reducido (sin constricción macro) predice **mejor** que el ABM completo:

| Caso | EDI_real | Interpretación |
|------|----------|---------------|
| 26 Starlink | -546.587 | Colapso total del modelo con datos reales |
| 23 Erosión Dialéctica | -9.084 | Anti-emergencia severa |
| 22 Fósforo | -4.269 | Anti-emergencia severa |
| 08 Falsac. Observabilidad | -3.771 | Control correctamente rechazado |
| 20 Kessler | -3.419 | Anti-emergencia con datos CelesTrak |
| 21 Salinización | -1.378 | Proxy inadecuado |
| 16 Deforestación | -1.001 | Anti-emergencia |
| 06 Falsac. Exogeneidad | -0.615 | Control correctamente rechazado |
| 07 Falsac. No-Estacionariedad | -7.837 | Control correctamente rechazado |
| 01 Clima | -0.299 | ODE Budyko-Sellers insuficiente |
| 25 Acuíferos | -0.272 | Señal real no capturada |

#### Controles de Falsación (3/3 correctamente rechazados)
- 06 Falsación Exogeneidad: ruido sin estructura → rechazado (EDI=-0.615).
- 07 Falsación No-Estacionariedad: deriva temporal sin causalidad → rechazado (EDI=-7.837).
- 08 Falsación Observabilidad: límites de medición micro → rechazado (EDI=-3.771).

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
Los 29 casos cubren dominios físicos (clima, energía, océanos, acidificación), biológicos (deforestación, fósforo, riesgo biológico, epidemiología), económicos (finanzas), tecnológicos (starlink, IoT, Kessler), culturales (paradigmas, erosión dialéctica, conciencia), sociales (urbanización, fuga de cerebros, movilidad, justicia, postverdad), hídricos (acuíferos, salinización), materiales (microplásticos, contaminación) y de gobernanza (políticas estratégicas, Wikipedia).

### La Paradoja de la Inercia — Revisada
Con el pipeline limpio, la paradoja se disuelve parcialmente: los dos únicos casos con EDI real positivo significativo son **Microplásticos** (EDI=0.586, datos OWID) y **Riesgo Biológico** (EDI=0.414, WorldBank mortalidad). Ambos son sistemas con inercia material/biológica moderada, consistente con la hipótesis de que el marco detecta **estabilidad de flujo informacional** en sistemas con inercia física o biológica.

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

### Estado actual: H1 no confirmada, marco falsable

El resultado principal es negativo: **overall_pass = 0/29**. La hipótesis H1 (EDI > 0.30 + protocolo C1-C5) no se confirma bajo el pipeline actual con evaluación estricta (zero-nudging, sin data leakage, `edi_valid` en `overall_pass`).

Sin embargo, este resultado negativo es **epistemológicamente valioso**:

1. **El marco es falsable:** La corrección del data leakage produjo un colapso de los EDI, demostrando que el protocolo no es un rubber-stamp.
2. **Los controles de falsación funcionan:** Los 3 controles (06-08) son correctamente rechazados con EDI negativo.
3. **Hay señal parcial:** Los casos 24 (Microplásticos, EDI=0.586) y 27 (Riesgo Biológico, EDI=0.414) muestran EDI real en rango válido, sugiriendo que la mejora del pipeline (mc restringido, acoplamiento bidireccional, variables multivariadas) podría rescatar la hipótesis en dominios específicos.

### Evidencia de Ablación: resultado invertido

La prueba de ablación (macro_coupling=0, forcing_scale=0) produce un resultado inesperado: en la mayoría de los casos reales, el ABM reducido predice **igual o mejor** que el ABM completo. Esto indica que la constricción macro actual (ODE→ABM unidireccional, mc excesivo) no captura emergencia genuina, sino que introduce una señal que interfiere con la dinámica micro.

### Conclusión de la Falsación — Revisada
La tesis sobrevive como **marco metodológico**: el protocolo de demarcación (EDI + C1-C5 + 6 criterios) es operativo y discriminante. Pero la hipótesis sustantiva (los hiperobjetos son computacionalmente reales vía constricción macro) queda **pendiente de confirmación** hasta que se resuelvan las mejoras pendientes (restricción mc < 0.5, acoplamiento bidireccional, fases sintéticas independientes).

La honestidad de reportar 0/29 — cuando el pipeline anterior inflado reportaba 24/29 — es la mejor evidencia de rigor científico.
