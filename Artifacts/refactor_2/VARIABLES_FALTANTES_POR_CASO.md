# Variables Faltantes por Caso — Estado Final

> **Commit**: `eeb3001` (4 fixes técnicos + regeneración 29 casos)  
> **Fecha**: 2026-02-09  
> **overall_pass**: 2/29 · **per**: 27/29 · **sig**: 6/29 · **ns**: 25/29

---

## 1. Resumen Ejecutivo

**Cero variables faltantes.** Todos los campos requeridos están presentes en los 29 metrics.json y todos los parámetros necesarios están declarados en los 29 validate.py.

| Categoría | Valor | Estado |
|-----------|:-----:|:------:|
| `driver_cols` sin campo | **0** | ✅ |
| `driver_cols` lista vacía | 10 | ✅ Correcto (univariados) |
| `driver_cols` con contenido | 19 | ✅ |
| `persistence` sin campo | **0** | ✅ |
| `emergence_taxonomy` sin campo | **0** | ✅ |
| `bias_correction` sin campo | **0** | ✅ |
| `edi.permutation_pvalue` sin campo | **0** | ✅ |
| `edi.permutation_significant` sin campo | **0** | ✅ |

---

## 2. driver_cols — Detalle por Caso

### 2.1 Con contenido (19/29)

| # | Caso | driver_cols |
|---|------|-------------|
| 01 | Clima | `['tavg']` |
| 02 | Conciencia | `['GDP_change', 'Unemployment_change']` |
| 03 | Criptomonedas | `['volume', 'market_cap']` |
| 04 | Desinformación | `['troll_activity', 'media_coverage']` |
| 05 | Epidemiología | `['new_cases', 'stringency_index']` |
| 06 | Extinción | `['habitat_loss', 'climate_anomaly']` |
| 08 | Inflación | `['oil_price', 'interest_rate']` |
| 09 | Internet | `['vix', 'fedfunds', 'inflation', 'credit_spread', 'volume']` |
| 10 | Lenguas | `['speakers', 'digital_presence']` |
| 11 | Movilidad | `['congestion', 'public_transit']` |
| 12 | Paradigmas | `['citations', 'funding']` |
| 14 | Plásticos | `['production', 'waste']` |
| 17 | Gentrificación | `['rent_index', 'income_index']` |
| 19 | Acidificación | `['co2_ppm', 'sst']` |
| 20 | Kessler | `['launch_rate', 'debris_count']` |
| 24 | Microplásticos | `['production_mt', 'waste_mt']` |
| 25 | Antibióticos | `['consumption_ddd', 'resistance_pct']` |
| 27 | Riesgo Bioseguridad | `['outbreaks', 'preparedness_index']` |
| 29 | Suelo | `['erosion_rate', 'organic_carbon']` |

### 2.2 Lista vacía (10/29) — Correcto para univariados

| # | Caso | Razón |
|---|------|-------|
| 07 | Finanzas-Falsación | Diseño de falsación |
| 13 | Políticas | Índice global único |
| 15 | Wikipedia | Serie de ediciones |
| 16 | Deforestación | Serie de pérdida forestal |
| 18 | Urbanización | Serie de tasa |
| 21 | Salinización | Serie de conductividad |
| 22 | Fósforo | Serie de concentración |
| 23 | Arena | Serie de extracción |
| 26 | Starlink | Serie de constelación |
| 28 | Fuga Cerebros | Serie de migración |

---

## 3. persistence — Detalle

### Pasan (27/29)

Todos con std_ratio < 5.0. Casos representativos:

| # | Caso | std_ratio |
|---|------|-----------|
| 01 | Clima | 0.98 |
| 09 | Finanzas | 3.09 |
| 16 | Deforestación | 2.97 |
| 24 | Microplásticos | 4.20 |

### Fallan (2/29)

| # | Caso | std_ratio | Diagnóstico |
|---|------|-----------|-------------|
| 11 | Movilidad | 9.65 | ABM amplifica ~10× la variabilidad |
| 20 | Kessler | 276,777 | Crecimiento exponencial en ABM vs. datos suaves |

---

## 4. Conclusión

### ✅ No hay variables faltantes

Todos los campos del protocolo C1–C5 están presentes y correctamente tipados en los 29 metrics.json. No quedan acciones técnicas pendientes en esta categoría.
