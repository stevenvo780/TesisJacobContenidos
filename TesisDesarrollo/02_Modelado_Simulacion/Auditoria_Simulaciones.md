# Auditoria de Simulaciones

Criterios: consistencia documental, presencia de metricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | CR | Estado | Hallazgos |
| :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 0.425 | 1.002 | True | OK |
| 02_caso_conciencia | 0.477 | 2.119 | False | OK |
| 03_caso_contaminacion | 0.124 | 1.365 | False | OK |
| 04_caso_energia | 0.351 | 1.116 | True | OK |
| 05_caso_epidemiologia | -395.634 | -19429.308 | False | CR <= 0 (revisar); EDI fuera de rango esperado (revisar) |
| 06_caso_estetica | 0.363 | 1.646 | False | OK |
| 07_caso_falsacion_exogeneidad | -2.513 | 1.005 | False | OK |
| 08_caso_falsacion_no_estacionariedad | 0.009 | 1.002 | False | OK |
| 09_caso_falsacion_observabilidad | n/a | n/a | False | EDI no disponible (n/a); CR no disponible (n/a) |
| 10_caso_finanzas | 0.769 | 1.078 | False | OK |
| 11_caso_justicia | 0.619 | 2.001 | False | OK |
| 12_caso_moderacion_adversarial | -0.179 | 1.069 | False | OK |
| 13_caso_movilidad | 0.072 | 1.148 | False | OK |
| 14_caso_paradigmas | 0.248 | 1.353 | False | OK |
| 15_caso_politicas_estrategicas | -0.209 | 1.264 | False | OK |
| 16_caso_postverdad | 0.313 | 1.887 | False | OK |
| 17_caso_rtb_publicidad | 0.088 | 6.937 | False | OK |
| 18_caso_wikipedia | 0.562 | 2.888 | False | OK |

## Recomendaciones
- Si EDI o CR es n/a, revisar el pipeline de calculo y los datos fuente.
- Si CR <= 0 o EDI fuera de rango, revisar la etapa de normalizacion o parametros.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
