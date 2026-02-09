# Variables Faltantes por Caso — Estado Final

> **Commit**: `e0c2293` (scripts corregidos + docs actualizados)  
> **Datos**: `eeb3001` (4 fixes técnicos + regeneración 29 casos)  
> **Fecha**: 2026-02-09  
> **overall_pass**: 2/29 · **per**: 27/29 · **sig**: 6/29 · **ns**: 25/29

---

## 1. Resumen Ejecutivo

**Cero variables faltantes.** Todos los campos requeridos están presentes en los 29 metrics.json (verificado con `_audit_fresh.py`) y todos los parámetros necesarios están declarados en los 29 validate.py.

| Categoría | Valor | Estado |
|-----------|:-----:|:------:|
| `driver_cols` sin campo | **0** | ✅ |
| `driver_cols` lista vacía | 10 | ✅ Correcto (univariados) |
| `driver_cols` con contenido | 19 | ✅ |
| `persistence` sin campo | **0** | ✅ |
| `emergence_taxonomy` sin campo | **0** | ✅ |
| `bias_correction` sin campo | **0** | ✅ |
| `noise_sensitivity` sin campo | **0** | ✅ |
| `symploke` sin campo | **0** | ✅ |
| `non_locality` sin campo | **0** | ✅ |
| `edi.permutation_pvalue` sin campo | **0** | ✅ |
| `edi.permutation_significant` sin campo | **0** | ✅ |
| `edi.ci_lo` / `edi.ci_hi` sin campo | **0** | ✅ |

---

## 2. driver_cols — Detalle por Caso

### 2.1 Con contenido (19/29)

Valores extraídos de cada `validate.py` (los `driver_cols` indican las columnas del dataset usadas como forzamiento externo en el ABM).

| # | Caso | driver_cols |
|---|------|-------------|
| 01 | Clima | `["co2", "tsi", "ohc", "aod"]` |
| 02 | Conciencia | `["suicide_rate", "tertiary_enrollment"]` |
| 04 | Energía | `["tavg", "price"]` |
| 05 | Epidemiología | `["deaths", "vaccinated", "stringency"]` |
| 06 | Falsación-Exogeneidad | `["unrelated_driver"]` |
| 07 | Falsación-NoEstacionariedad | `["spurious_trend"]` |
| 08 | Falsación-Observabilidad | `["insufficient_driver"]` |
| 09 | Finanzas | `["vix", "fedfunds", "inflation", "credit_spread", "volume"]` |
| 11 | Movilidad | `["gdp_per_capita", "air_departures"]` |
| 12 | Paradigmas | `["journal_articles", "patent_residents"]` |
| 14 | Postverdad | `["mobile_subs", "literacy"]` |
| 21 | Salinización | `["freshwater_withdrawal"]` |
| 23 | Erosión Dialéctica | `["literacy"]` |
| 24 | Microplásticos | `["mismanaged_waste", "river_discharge"]` |
| 25 | Acuíferos | `["precip", "extraction_usgs", "withdrawal"]` |
| 26 | Starlink | `["launches", "collision_events", "debris_new"]` |
| 27 | Riesgo Biológico | `["hiv_incidence", "immunization_coverage"]` |
| 28 | Fuga Cerebros | `["researchers", "enrollment", "remittances", "gdp_pc", "net_migration"]` |
| 29 | IoT | `["internet_users", "broadband", "gdp_pc", "gdp_growth", "secure_servers"]` |

**Nota**: Casos 06–08 son falsificaciones; sus driver_cols contienen variables diseñadas para **no** producir emergencia (exógenas irrelevantes, tendencias espurias, observabilidad insuficiente).

### 2.2 Lista vacía (10/29) — Correcto para univariados

Estos casos usan una sola serie temporal como observable y no requieren drivers externos. El ABM se fuerza únicamente con la serie principal.

| # | Caso | Razón |
|---|------|-------|
| 03 | Contaminación | Serie PM2.5 global |
| 10 | Justicia | Índice de percepción único |
| 13 | Políticas Estratégicas | Índice global único |
| 15 | Wikipedia | Serie de ediciones climáticas |
| 16 | Deforestación | Serie de pérdida forestal (World Bank) |
| 17 | Océanos | Serie de temperatura oceánica |
| 18 | Urbanización | Serie de tasa de urbanización |
| 19 | Acidificación Oceánica | Serie de pH oceánico |
| 20 | Kessler | Serie de objetos orbitales |
| 22 | Fósforo | Serie de consumo de fertilizantes |

---

## 3. persistence — Detalle

### Pasan (27/29)

Todos con std_ratio < 5.0. Valores representativos:

| # | Caso | std_ratio | Categoría |
|---|------|-----------|-----------|
| 01 | Clima | < 5.0 | trend |
| 09 | Finanzas | 3.09 | suggestive |
| 16 | Deforestación | 2.97 | strong |
| 24 | Microplásticos | 4.20 | strong |

### Fallan (2/29)

| # | Caso | std_ratio | Diagnóstico |
|---|------|-----------|-------------|
| 11 | Movilidad | 9.65 | ABM amplifica ~10× la variabilidad respecto a datos |
| 20 | Kessler | 276,777 | Crecimiento exponencial en ABM vs. datos suaves |

---

## 4. Fuentes de datos — Todos los casos tienen CSV cacheado

Los 29 casos tienen un archivo CSV en su directorio `data/`. No hay dependencia de APIs externas en tiempo de ejecución.

| Tipo de archivo | Casos |
|----------------|-------|
| `dataset.csv` (genérico) | 02, 10, 11, 12, 13, 14, 17, 19, 20, 23, 25, 27, 28, 29 |
| CSV con nombre específico | 01 (`conus_monthly`), 03 (`pm25_world`), 04 (`opsd_*`), 05 (`owid_covid`), 06 (`memetic`), 07 (`crypto`), 08 (`sparse_happiness`), 09 (`spy_monthly`), 15 (`wiki_climate`), 16 (`wb_deforestation`), 18 (`wb_urbanization`), 21 (`wb_arable_land`), 22 (`wb_fertilizer_consumption`), 24 (`mismanaged_waste`+otros), 26 (`satcat_starlink`+otros) |

---

## 5. Conclusión

### ✅ No hay variables faltantes

Todos los campos del protocolo C1–C5 están presentes y correctamente tipados en los 29 metrics.json:
- `edi` (value, ci_lo, ci_hi, permutation_pvalue, permutation_significant)
- `bias_correction` (mode)
- `emergence_taxonomy` (category)
- `persistence` (pass, std_ratio)
- `noise_sensitivity` (stable)
- `symploke` (pass, cr)
- `non_locality` (pass)
- `overall_pass`

No quedan acciones técnicas pendientes en esta categoría.

---

*Datos verificados con `repos/scripts/_audit_fresh.py` — 29/29 campos completos*  
*driver_cols extraídos de `repos/Simulaciones/XX_caso_*/src/validate.py`*
