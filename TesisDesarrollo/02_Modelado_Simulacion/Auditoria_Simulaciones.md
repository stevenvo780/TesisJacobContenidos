# Auditoria de Simulaciones

Criterios: consistencia documental, presencia de metricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | CR | C1 | Cat | NS | Estado | Hallazgos |
| :--- | ---: | ---: | :---: | :--- | :---: | :--- | :--- |
| 01_caso_clima | -0.225 | 1.000 | ✅ | trend | ✅ | False | OK |
| 02_caso_conciencia | 0.402 | 0.919 | ✅ | null | ✅ | False | OK |
| 03_caso_contaminacion | -0.000 | 2.780 | ❌ | null | ✅ | False | OK |
| 04_caso_energia | -0.012 | -1.096 | ❌ | null | ✅ | False | CR <= 0 (revisar) |
| 05_caso_epidemiologia | 0.674 | -0.000 | ❌ | null | ❌ | False | CR <= 0 (revisar) |
| 06_caso_falsacion_exogeneidad | 0.005 | 1.006 | ✅ | falsification | ✅ | False | OK |
| 07_caso_falsacion_no_estacionariedad | 0.148 | 1.004 | ❌ | falsification | ✅ | False | OK |
| 08_caso_falsacion_observabilidad | 0.140 | 1.005 | ❌ | falsification | ✅ | False | OK |
| 09_caso_finanzas | 0.030 | 0.000 | ✅ | suggestive | ✅ | False | CR <= 0 (revisar) |
| 10_caso_justicia | 0.000 | 1.053 | ❌ | null | ✅ | False | OK |
| 11_caso_movilidad | -1.137 | n/a | ✅ | trend | ✅ | False | CR no disponible (n/a) |
| 12_caso_paradigmas | -0.167 | n/a | ❌ | null | ❌ | False | CR no disponible (n/a) |
| 13_caso_politicas_estrategicas | 0.021 | -1.626 | ✅ | trend | ❌ | False | CR <= 0 (revisar) |
| 14_caso_postverdad | 0.003 | 1.054 | ✅ | suggestive | ✅ | False | OK |
| 15_caso_wikipedia | 0.000 | -1.158 | ❌ | null | ✅ | False | CR <= 0 (revisar) |
| 16_caso_deforestacion | 0.879 | 1.017 | ✅ | strong | ✅ | True | OK |
| 17_caso_oceanos | 0.058 | -1.334 | ✅ | suggestive | ✅ | False | CR <= 0 (revisar) |
| 18_caso_urbanizacion | -0.001 | -30.069 | ✅ | trend | ❌ | False | CR <= 0 (revisar) |
| 19_caso_acidificacion_oceanica | -0.021 | 1.211 | ❌ | null | ✅ | False | docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 20_caso_kessler | -0.351 | 1.204 | ❌ | null | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 21_caso_salinizacion | 0.027 | n/a | ✅ | trend | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; CR no disponible (n/a) |
| 22_caso_fosforo | 0.481 | 1.065 | ❌ | null | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 23_caso_erosion_dialectica | 0.598 | 1.001 | ❌ | null | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 24_caso_microplasticos | -1.302 | 1.002 | ✅ | strong | ✅ | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 25_caso_acuiferos | 0.383 | 1.001 | ✅ | null | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 26_caso_starlink | -576.760 | n/a | ❌ | null | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; CR no disponible (n/a); EDI fuera de rango esperado (revisar) |
| 27_caso_riesgo_biologico | 0.659 | 1.002 | ✅ | trend | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 28_caso_fuga_cerebros | 0.437 | 1.008 | ✅ | weak | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 29_caso_iot | 0.169 | 1.053 | ✅ | suggestive | ✅ | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |

## Recomendaciones
- Si EDI o CR es n/a, revisar el pipeline de calculo y los datos fuente.
- Si CR <= 0 o EDI fuera de rango, revisar la etapa de normalizacion o parametros.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
