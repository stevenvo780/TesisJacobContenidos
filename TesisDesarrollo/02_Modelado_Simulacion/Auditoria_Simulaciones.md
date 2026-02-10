# Auditoría de Simulaciones

Criterios: consistencia documental, presencia de métricas y señales de posibles anomalías sin forzar resultados.

| Caso | EDI | p-perm | sig | CR | C1 | Categoría | Nivel | NS | Per | Pass | Hallazgos |
| :--- | ---: | ---: | :---: | ---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- |
| 01_caso_clima | 0.010 | 0.591 | ❌ | 1.000 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 02_caso_conciencia | -0.024 | 0.938 | ❌ | 0.919 | ✅ | null | 0 | ✅ | ✅ | ❌ | OK |
| 03_caso_contaminacion | -0.000 | 0.474 | ❌ | 2.780 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 04_caso_energia | -0.003 | 0.937 | ❌ | 1.096 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 05_caso_epidemiologia | 0.000 | 1.000 | ❌ | 0.000 | ❌ | null | 0 | ❌ | ✅ | ❌ | OK |
| 06_caso_falsacion_exogeneidad | 0.055 | 1.000 | ❌ | 1.006 | ✅ | falsification | — | ✅ | ✅ | ❌ | OK |
| 07_caso_falsacion_no_estacionariedad | -1.000 | 1.000 | ❌ | 1.004 | ❌ | falsification | — | ✅ | ✅ | ❌ | OK |
| 08_caso_falsacion_observabilidad | -1.000 | 1.000 | ❌ | 1.005 | ❌ | falsification | — | ✅ | ✅ | ❌ | OK |
| 09_caso_finanzas | 0.040 | 0.000 | ✅ | 0.000 | ✅ | suggestive | 2 | ✅ | ✅ | ❌ | OK |
| 10_caso_justicia | 0.000 | 1.000 | ❌ | 1.053 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 11_caso_movilidad | 0.003 | 0.361 | ❌ | 0.000 | ✅ | trend | 1 | ✅ | ❌ | ❌ | OK |
| 12_caso_paradigmas | 0.000 | 1.000 | ❌ | 0.000 | ❌ | null | 0 | ❌ | ✅ | ❌ | OK |
| 13_caso_politicas_estrategicas | 0.011 | 0.719 | ❌ | 1.626 | ✅ | trend | 1 | ❌ | ✅ | ❌ | OK |
| 14_caso_postverdad | 0.001 | 0.030 | ❌ | 1.054 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 15_caso_wikipedia | 0.000 | 1.000 | ❌ | 1.158 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 16_caso_deforestacion | 0.633 | 0.000 | ✅ | 1.017 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 17_caso_oceanos | 0.053 | 0.000 | ✅ | 1.334 | ✅ | suggestive | 2 | ✅ | ✅ | ❌ | OK |
| 18_caso_urbanizacion | 0.000 | 0.220 | ❌ | 30.069 | ✅ | trend | 1 | ❌ | ✅ | ❌ | OK |
| 19_caso_acidificacion_oceanica | -0.000 | 0.000 | ❌ | 1.211 | ❌ | null | 0 | ✅ | ✅ | ❌ | docs/ incompleto (4 faltantes) |
| 20_caso_kessler | -0.420 | 1.000 | ❌ | 1.204 | ❌ | null | 0 | ✅ | ❌ | ❌ | OK |
| 21_caso_salinizacion | 0.027 | 0.724 | ❌ | ∞ | ✅ | trend | 1 | ✅ | ✅ | ❌ | CR=∞ (ext≈0) |
| 22_caso_fosforo | -1.000 | 1.000 | ❌ | 1.065 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 23_caso_erosion_dialectica | -1.000 | 1.000 | ❌ | 1.001 | ❌ | null | 0 | ✅ | ✅ | ❌ | OK |
| 24_caso_microplasticos | 0.427 | 0.000 | ✅ | 1.002 | ✅ | strong | 4 | ✅ | ✅ | ✅ | OK |
| 25_caso_acuiferos | -0.179 | 1.000 | ❌ | 1.001 | ✅ | null | 0 | ✅ | ✅ | ❌ | OK |
| 26_caso_starlink | -1.000 | 1.000 | ❌ | ∞ | ❌ | null | 0 | ✅ | ✅ | ❌ | CR=∞ (ext≈0) |
| 27_caso_riesgo_biologico | 0.105 | 0.365 | ❌ | 1.002 | ✅ | trend | 1 | ✅ | ✅ | ❌ | OK |
| 28_caso_fuga_cerebros | 0.183 | 0.001 | ✅ | 1.008 | ✅ | weak | 3 | ✅ | ✅ | ❌ | OK |
| 29_caso_iot | 0.020 | 0.000 | ✅ | 1.053 | ✅ | suggestive | 2 | ✅ | ✅ | ❌ | OK |

## Resumen

| Métrica | Valor |
| :--- | :--- |
| Total de casos | 29 |
| overall_pass (EDI∈[0.30,0.90]) | 2/29 |
| Significancia (p<0.05 + EDI>0.01) | 6/29 |
| Estabilidad numérica | 25/29 |
| Persistencia (std_ratio<5) | 27/29 |

### Distribución por categoría

| Categoría | Nivel | Casos |
| :--- | :---: | ---: |
| strong | 4 | 2 |
| weak | 3 | 1 |
| suggestive | 2 | 3 |
| trend | 1 | 7 |
| null | 0 | 13 |
| falsification | — | 3 |

## Recomendaciones

- Si EDI o CR es n/a, revisar el pipeline de cálculo y los datos fuente.
- CR=∞ indica acoplamiento externo nulo: la macro no recibe señal del entorno.
- Si reportes carecen de resultados, completar con los hallazgos del metrics.json.
