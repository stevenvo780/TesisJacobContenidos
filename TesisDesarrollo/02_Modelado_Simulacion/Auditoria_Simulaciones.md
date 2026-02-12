# Auditoría de Simulaciones

Criterios: consistencia documental, presencia de métricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | p-perm | sig | CR | C1 | Categoría | Nivel | NS | Per | Pass | Hallazgos |
| :--- | ---: | ---: | :---: | ---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01_caso_clima | 0.002 | 1.000 | ❌ | 1.006 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 02_caso_conciencia | 0.123 | 0.231 | ❌ | 1.006 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 03_caso_contaminacion | -0.011 | 0.737 | ❌ | 1.022 | ✅ | null | 0 | ✅ | ✅ | ❌ | OK |
| 04_caso_energia | 0.409 | 0.070 | ❌ | 1.001 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 05_caso_epidemiologia | 0.129 | 0.000 | ✅ | 1.009 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 06_caso_falsacion_exogeneidad | 0.055 | 1.000 | ❌ | 1.006 | ✅ | falsification | — | ✅ | ✅ | ❌ | OK |
| 07_caso_falsacion_no_estacionariedad | -0.890 | 1.000 | ❌ | 1.006 | ❌ | falsification | — | ✅ | ✅ | ❌ | OK |
| 08_caso_falsacion_observabilidad | -1.000 | 1.000 | ❌ | 1.005 | ❌ | falsification | — | ✅ | ✅ | ❌ | OK |
| 09_caso_finanzas | 0.081 | 0.000 | ✅ | 2.616 | ✅ | suggestive | 2 | ✅ | ✅ | ❌ | OK |
| 10_caso_justicia | 0.227 | 0.477 | ❌ | 1.038 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 11_caso_movilidad | 0.128 | 0.002 | ✅ | 1.004 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 12_caso_paradigmas | -0.006 | 0.000 | ❌ | 1.003 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 13_caso_politicas_estrategicas | 0.288 | 0.001 | ✅ | 1.009 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 14_caso_postverdad | 0.325 | 0.000 | ✅ | 1.009 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 15_caso_wikipedia | 0.160 | 0.000 | ✅ | 1.060 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 16_caso_deforestacion | 0.589 | 0.000 | ✅ | 1.016 | ✅ | strong | 4 | ✅ | ✅ | ❌ | OK |
| 17_caso_oceanos | -0.032 | 1.000 | ❌ | 1.002 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 18_caso_urbanizacion | 0.151 | 0.000 | ✅ | 1.001 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 19_caso_acidificacion_oceanica | -0.000 | 0.000 | ❌ | 1.214 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 20_caso_kessler | 0.381 | 0.000 | ✅ | 1.005 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 21_caso_salinizacion | 0.070 | 0.005 | ✅ | ∞ | ✅ | suggestive | 2 | ✅ | ✅ | ❌ | CR=∞ (ext≈0) |
| 22_caso_fosforo | 0.376 | 0.000 | ✅ | 1.002 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 23_caso_erosion_dialectica | -1.000 | 1.000 | ❌ | 1.002 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 24_caso_microplasticos | 0.656 | 0.000 | ✅ | 1.000 | ✅ | strong | 4 | ✅ | ✅ | ❌ | OK |
| 25_caso_acuiferos | -0.126 | 1.000 | ❌ | 1.002 | ✅ | null | 0 | ✅ | ✅ | ❌ | OK |
| 26_caso_starlink | 0.837 | 1.000 | ❌ | 1.805 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 27_caso_riesgo_biologico | 0.266 | 0.003 | ✅ | 1.066 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 28_caso_fuga_cerebros | 0.059 | 0.780 | ❌ | 1.007 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 29_caso_iot | -0.218 | 0.885 | ❌ | 1.037 | ❌ | null | 0 | ✅ | ❌ | ❌ | OK |

## Resumen

| Métrica | Valor |
| :--- | :--- |
| Total de casos | 29 |
| overall_pass (EDI∈[0.30,0.90]) | 9/29 |
| Significancia (p<0.05 + EDI>0.01) | 13/29 |
| Estabilidad numérica | 29/29 |
| Persistencia (std_ratio<5) | 28/29 |

### Distribución por categoría

| Categoría | Nivel | Casos |
| :--- | :---: | ---: |
| strong | 4 | 11 |
| suggestive | 2 | 2 |
| trend | 1 | 6 |
| null | 0 | 7 |
| falsification | — | 3 |

## Recomendaciones

- Si EDI o CR es n/a, revisar el pipeline de cálculo y los datos fuente.
- CR=∞ indica acoplamiento externo nulo: la macro no recibe señal del entorno.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
