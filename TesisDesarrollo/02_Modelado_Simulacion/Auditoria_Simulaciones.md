# Auditoria de Simulaciones

Criterios: consistencia documental, presencia de metricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | CR | Estado | Hallazgos |
| :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 0.372 | 1.000 | True | OK |
| 02_caso_conciencia | 0.936 | 1.000 | True | OK |
| 03_caso_contaminacion | 0.125 | 1.365 | False | OK |
| 04_caso_energia | 0.354 | 1.118 | True | OK |
| 05_caso_epidemiologia | 0.176 | 1.000 | False | OK |
| 06_caso_estetica | 0.949 | 1.000 | True | OK |
| 06_caso_falsacion_exogeneidad | -0.401 | -49.492 | False | CR <= 0 (revisar) |
| 07_caso_falsacion_no_estacionariedad | 0.090 | -31.846 | False | CR <= 0 (revisar) |
| 08_caso_falsacion_observabilidad | n/a | n/a | False | EDI no disponible (n/a); CR no disponible (n/a) |
| 09_caso_finanzas | 0.882 | 1.250 | True | OK |
| 10_caso_justicia | 0.946 | 1.000 | True | OK |
| 11_caso_movilidad | 0.915 | 1.000 | True | OK |
| 12_caso_moderacion_adversarial | 0.950 | 1.000 | True | OK |
| 12_caso_paradigmas | 0.863 | 1.000 | True | OK |
| 13_caso_politicas_estrategicas | 0.804 | 1.000 | True | OK |
| 14_caso_postverdad | 0.154 | -33.426 | False | CR <= 0 (revisar) |
| 15_caso_wikipedia | 0.018 | 1.147 | False | OK |
| 16_caso_deforestacion | 0.846 | 1.000 | True | OK |
| 17_caso_oceanos | 0.936 | 1.000 | True | OK |
| 17_caso_rtb_publicidad | 0.950 | 1.000 | True | OK |
| 18_caso_urbanizacion | 0.839 | 1.000 | True | OK |
| 19_caso_acidificacion_oceanica | 0.947 | 1.000 | True | docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 20_caso_kessler | 0.776 | 1.001 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 21_caso_salinizacion | 0.176 | -26.257 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; CR <= 0 (revisar) |
| 22_caso_fosforo | 0.902 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 23_caso_erosion_dialectica | 0.923 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 24_caso_microplasticos | 0.856 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 25_caso_acuiferos | 0.959 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 26_caso_starlink | 0.914 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 27_caso_riesgo_biologico | 0.893 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 28_caso_fuga_cerebros | 0.881 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 29_caso_iot | 0.889 | 1.000 | True | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |

## Recomendaciones
- Si EDI o CR es n/a, revisar el pipeline de calculo y los datos fuente.
- Si CR <= 0 o EDI fuera de rango, revisar la etapa de normalizacion o parametros.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
