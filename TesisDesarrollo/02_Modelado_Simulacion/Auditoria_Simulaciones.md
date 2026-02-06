# Auditoria de Simulaciones

Criterios: consistencia documental, presencia de metricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | CR | Estado | Hallazgos |
| :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 0.074 | 1.102 | False | OK |
| 02_caso_conciencia | 1.000 | 1.382 | True | OK |
| 03_caso_contaminacion | 0.423 | 2.472 | True | OK |
| 04_caso_energia | 1.000 | 1.824 | True | OK |
| 05_caso_epidemiologia | 1.000 | n/a | True | CR no disponible (n/a) |
| 06_caso_estetica | 1.000 | 1.073 | True | OK |
| 07_caso_falsacion_exogeneidad | -2.513 | 1.005 | False | OK |
| 08_caso_falsacion_no_estacionariedad | 0.009 | 1.002 | False | OK |
| 09_caso_falsacion_observabilidad | n/a | n/a | False | EDI no disponible (n/a); CR no disponible (n/a) |
| 10_caso_finanzas | -0.020 | 1.437 | False | OK |
| 11_caso_justicia | 1.000 | 1.262 | True | OK |
| 12_caso_moderacion_adversarial | -0.179 | 1.069 | False | OK |
| 13_caso_movilidad | 0.740 | 5.273 | True | OK |
| 14_caso_paradigmas | 1.000 | 2.283 | True | OK |
| 15_caso_politicas_estrategicas | -0.209 | 1.264 | False | OK |
| 16_caso_postverdad | 1.000 | 1.061 | True | OK |
| 17_caso_rtb_publicidad | 0.088 | 6.937 | False | OK |
| 18_caso_wikipedia | 1.000 | 5.302 | True | OK |

## Recomendaciones
- Si EDI o CR es n/a, revisar el pipeline de calculo y los datos fuente.
- Si CR <= 0 o EDI fuera de rango, revisar la etapa de normalizacion o parametros.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
