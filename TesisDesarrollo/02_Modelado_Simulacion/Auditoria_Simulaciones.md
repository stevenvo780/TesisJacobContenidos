# Auditoria de Simulaciones

> **Actualizado: 2026-02-09** — Post Bias Correction + Emergencia Diferenciada (commit 54234d6)

Criterios: consistencia documental, presencia de metricas, taxonomía de emergencia, calidad ODE y señales de posibles anomalías.

| Caso | EDI | CR | Categoría | ODE Qual. | BC | Estado | sig | Hallazgos |
| :--- | ---: | ---: | :--- | :--- | :--- | :--- | :---: | :--- |
| 01_caso_clima | -0.015 | 1.000 | null | poor | none | False | — | OK |
| 02_caso_conciencia | -0.046 | 0.935 | null | poor | bias_only | False | — | OK |
| 03_caso_contaminacion | -0.000 | 2.780 | null | moderate | none | False | — | OK |
| 04_caso_energia | -0.003 | 1.096 | null | moderate | none | False | — | OK |
| 05_caso_epidemiologia | 0.000 | 0.000 | null | moderate | none | False | — | CR=0 (señal plana) |
| 06_caso_falsacion_exogeneidad | 0.055 | 1.006 | falsification | poor | bias_only | False | — | Rechazo correcto ✓ |
| 07_caso_falsacion_no_estacionariedad | -4.924 | 1.003 | falsification | moderate | bias_only | False | — | Rechazo correcto ✓ |
| 08_caso_falsacion_observabilidad | -2.144 | 1.004 | falsification | poor | bias_only | False | — | Rechazo correcto ✓ |
| 09_caso_finanzas | 0.026 | 0.000 | suggestive | good | none | False | ✓ | CR=0; señal significativa |
| 10_caso_justicia | 0.000 | 1.053 | null | poor | bias_only | False | — | OK |
| 11_caso_movilidad | 0.003 | 0.000 | trend | poor | none | False | — | CR=0; tendencia no significativa |
| 12_caso_paradigmas | 0.000 | 0.000 | null | good | none | False | — | CR=0; ODE anticorrelada |
| 13_caso_politicas_estrategicas | 0.011 | 1.626 | trend | poor | full | False | — | OK |
| 14_caso_postverdad | 0.001 | 1.054 | suggestive | moderate | bias_only | False | ✓ | Señal significativa débil |
| 15_caso_wikipedia | 0.000 | 1.158 | null | moderate | none | False | — | OK |
| **16_caso_deforestacion** | **0.629** | **1.018** | **strong** | **good** | **full** | **False** | **✓** | **BC rescató (EDI -0.29→+0.63)** |
| 17_caso_oceanos | 0.053 | 1.334 | suggestive | good | bias_only | False | ✓ | Señal significativa |
| 18_caso_urbanizacion | 0.000 | 30.069 | trend | poor | full | False | — | CR anómalo alto |
| 19_caso_acidificacion_oceanica | -0.002 | 1.168 | null | poor | none | False | ✓ | EDI sig. pero negativo |
| 20_caso_kessler | -0.161 | 1.510 | null | good | bias_only | False | ✓ | ODE escala absurda |
| 21_caso_salinizacion | 0.088 | 1.054 | trend | good | none | False | — | OK |
| 22_caso_fosforo | -3.069 | 1.090 | null | good | full | False | — | Corr invierte train→val |
| 23_caso_erosion_dialectica | -5.931 | 0.999 | null | good | none | False | — | Corr train≠val |
| **24_caso_microplasticos** | **0.439** | **1.002** | **strong** | **good** | **none** | **False** | **✓** | **Emergencia genuina (sin BC)** |
| 25_caso_acuiferos | -0.182 | 1.001 | null | good | none | False | — | Corr train=-1.0 |
| 26_caso_starlink | -545.736 | ∞ | null | poor | none | False | — | EDI fuera de rango |
| 27_caso_riesgo_biologico | -0.077 | 1.002 | null | poor | full | False | — | OK |
| **28_caso_fuga_cerebros** | **0.190** | **1.009** | **weak** | **good** | **bias_only** | **False** | **✓** | **Emergencia débil (BC preservó)** |
| 29_caso_iot | 0.007 | 1.056 | suggestive | good | none | False | ✓ | Señal significativa |

### Resumen Taxonómico

| Categoría | N | % |
|-----------|---|---|
| strong | 2 | 6.9% |
| weak | 1 | 3.4% |
| suggestive | 4 | 13.8% |
| trend | 4 | 13.8% |
| null | 15 | 51.7% |
| falsification | 3 | 10.3% |

### Distribución por Calidad ODE

| ODE Quality | strong | weak | suggestive | trend | null | falsification | Total |
|-------------|--------|------|------------|-------|------|---------------|-------|
| good | 2 | 1 | 3 | 1 | 5 | 0 | 12 |
| moderate | 0 | 0 | 1 | 0 | 5 | 1 | 7 |
| poor | 0 | 0 | 0 | 3 | 5 | 2 | 10 |

## Recomendaciones
- Los 2 casos **strong** (Deforestación, Microplásticos) constituyen evidencia robusta de emergencia macro.
- El caso **weak** (Fuga de Cerebros) merece investigación adicional — el EDI podría alcanzar el umbral con modelos ODE mejorados.
- Los 4 casos **suggestive** tienen señal significativa: mejorar resolución del forcing podría rescatarlos.
- Los 5 casos con ODE good + null (12, 20, 22, 23, 25) tienen modelos ODE que no generalizan train→val.
- Si CR=0, revisar si la serie real tiene varianza insuficiente para calcular cohesión.
