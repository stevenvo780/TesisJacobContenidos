# Auditoria de Simulaciones

Criterios: consistencia documental, presencia de metricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | CR | Estado | Hallazgos |
| :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 0.425 | 1.002 | True | OK |
| 02_caso_conciencia | -0.320 | 0.999 | False | OK |
| 03_caso_contaminacion | 0.124 | 1.365 | False | OK |
| 04_caso_energia | 0.351 | 1.116 | True | OK |
| 05_caso_epidemiologia | -395.634 | -19429.308 | False | CR <= 0 (revisar); EDI fuera de rango esperado (revisar) |
| 06_caso_estetica | -1096.608 | -16987.385 | False | CR <= 0 (revisar); EDI fuera de rango esperado (revisar) |
| 06_caso_falsacion_exogeneidad | -1.649 | 1.000 | False | OK |
| 06_caso_falsacion_no_estacionariedad | -2.204 | 0.984 | False | OK |
| 06_caso_falsacion_observabilidad | n/a | n/a | False | EDI no disponible (n/a); CR no disponible (n/a) |
| 06_caso_finanzas | 0.879 | 1.248 | True | OK |
| 06_caso_justicia | -0.237 | 1.001 | False | OK |
| 12_caso_moderacion_adversarial | -274616.823 | -1291.556 | False | CR <= 0 (revisar); EDI fuera de rango esperado (revisar) |
| 06_caso_movilidad | 0.072 | 1.148 | False | OK |
| 12_caso_paradigmas | 0.657 | 1.001 | True | OK |
| 06_caso_politicas_estrategicas | 0.296 | 1.012 | False | OK |
| 12_caso_postverdad | 0.311 | 1.000 | False | OK |
| 17_caso_rtb_publicidad | 0.426 | 1.030 | True | OK |
| 06_caso_wikipedia | 0.017 | 1.151 | False | OK |
| 12_caso_acidificacion_oceanica | n/a | n/a | n/a | README.md faltante; report.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; metrics.json faltante o ilegible |
| 12_caso_deforestacion | n/a | n/a | n/a | report.md sin seccion de resultados clara; metrics.json faltante o ilegible |
| 17_caso_oceanos | n/a | n/a | n/a | report.md sin seccion de resultados clara; metrics.json faltante o ilegible |
| 06_caso_kessler | n/a | n/a | n/a | README.md faltante; report.md faltante; docs/arquitectura.md faltante; docs/protocolo_simulacion.md faltante; docs/indicadores_metricas.md faltante; docs/reproducibilidad.md faltante; docs/validacion_c1_c5.md faltante; metrics.json faltante o ilegible |
| 06_caso_urbanizacion | n/a | n/a | n/a | report.md sin seccion de resultados clara; metrics.json faltante o ilegible |

## Recomendaciones
- Si EDI o CR es n/a, revisar el pipeline de calculo y los datos fuente.
- Si CR <= 0 o EDI fuera de rango, revisar la etapa de normalizacion o parametros.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
