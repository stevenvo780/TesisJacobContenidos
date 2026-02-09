# Auditoria de Simulaciones

Criterios: consistencia documental, presencia de metricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | CR | Estado | Hallazgos |
| :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | -0.609 | 1.071 | False | OK |
| 02_caso_conciencia | 0.432 | 0.928 | False | OK |
| 03_caso_contaminacion | -0.000 | 4.287 | False | OK |
| 04_caso_energia | -0.014 | -1.115 | False | CR <= 0 (revisar) |
| 05_caso_epidemiologia | 0.674 | -0.000 | False | CR <= 0 (revisar) |
| 06_caso_falsacion_exogeneidad | -0.185 | 2.815 | False | OK |
| 07_caso_falsacion_no_estacionariedad | -0.243 | 1.146 | False | OK |
| 08_caso_falsacion_observabilidad | -0.345 | 1.227 | False | OK |
| 09_caso_finanzas | 0.041 | 0.000 | False | CR <= 0 (revisar) |
| 10_caso_justicia | 0.000 | 1.065 | False | OK |
| 11_caso_movilidad | -1.077 | n/a | False | CR no disponible (n/a) |
| 12_caso_paradigmas | -0.167 | n/a | False | CR no disponible (n/a) |
| 13_caso_politicas_estrategicas | -0.012 | -1.465 | False | CR <= 0 (revisar) |
| 14_caso_postverdad | 0.005 | 1.055 | False | OK |
| 15_caso_wikipedia | 0.000 | -1.158 | False | CR <= 0 (revisar) |
| 16_caso_deforestacion | 0.345 | -0.575 | False | CR <= 0 (revisar) |
| 17_caso_oceanos | 0.124 | -1.244 | False | CR <= 0 (revisar) |
| 18_caso_urbanizacion | -0.001 | 1.472 | False | OK |
| 19_caso_acidificacion_oceanica | -0.023 | 1.157 | False | docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 20_caso_kessler | -3.037 | 1.173 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 21_caso_salinizacion | -1.096 | -17.969 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; CR <= 0 (revisar) |
| 22_caso_fosforo | 0.180 | 1.016 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 23_caso_erosion_dialectica | 0.293 | -2.116 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; CR <= 0 (revisar) |
| 24_caso_microplasticos | 0.856 | 1.000 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 25_caso_acuiferos | 0.334 | -0.137 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; CR <= 0 (revisar) |
| 26_caso_starlink | -928.866 | n/a | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; CR no disponible (n/a); EDI fuera de rango esperado (revisar) |
| 27_caso_riesgo_biologico | 0.770 | 1.003 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 28_caso_fuga_cerebros | 0.457 | 0.967 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |
| 29_caso_iot | 0.167 | 1.085 | False | docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante |

## Recomendaciones
- Si EDI o CR es n/a, revisar el pipeline de calculo y los datos fuente.
- Si CR <= 0 o EDI fuera de rango, revisar la etapa de normalizacion o parametros.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
