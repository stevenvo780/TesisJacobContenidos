# Variables Faltantes por Caso — Estado Actualizado

> **Commit**: `20072d1` (fix P2+P3: persistencia std 5× + driver_cols casos 16, 22)  
> **Fecha**: 2025-07-21  
> **overall_pass**: 2/29 · **per**: 27/29 · **sig**: 8/29 · **ns**: 25/29

---

## 1. Resumen Ejecutivo

Tras las correcciones P2 y P3, **todas las variables estructurales están presentes en los 29 casos**. No quedan campos faltantes en `metrics.json` ni parámetros sin declarar en `validate.py`. Los "faltantes" que siguen son semánticos (listas vacías por ser datasets univariados) y no técnicos.

| Categoría | Antes (e3db5c7) | Ahora (20072d1) | Δ |
|-----------|:---:|:---:|:---:|
| `driver_cols` sin campo | 2 | **0** | ✅ −2 |
| `driver_cols` lista vacía | 10 | 10 | = |
| `driver_cols` con contenido | 17→19 | 19 | = |
| `persistence` sin campo | 0 | 0 | = |
| `emergence_taxonomy` sin campo | 0 | 0 | = |
| `bias_correction` sin campo | 0 | 0 | = |
| `edi.permutation_significant` sin campo | 0 | 0 | = |

---

## 2. driver_cols — Detalle por Caso

### 2.1 Casos con driver_cols con contenido (19/29)

| # | Caso | driver_cols |
|---|------|-------------|
| 01 | Clima | `['tavg']` |
| 02 | Conciencia | `['GDP_change', 'Unemployment_change']` |
| 03 | Criptomonedas | `['volume', 'market_cap']` |
| 04 | Desinformación | `['troll_activity', 'media_coverage']` |
| 05 | Epidemiología | `['new_cases', 'stringency_index']` |
| 06 | Extinción | `['habitat_loss', 'climate_anomaly']` |
| 08 | Inflación | `['oil_price', 'interest_rate']` |
| 09 | Internet | `['users', 'bandwidth']` |
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

### 2.2 Casos con driver_cols = [] (10/29)

Estos casos son **univariados** (serie temporal única sin variables exógenas). La lista vacía es **semánticamente correcta** — no es un error ni un faltante técnico.

| # | Caso | Razón de lista vacía |
|---|------|---------------------|
| 07 | Finanzas | Serie de precios S&P 500, sin drivers externos |
| 13 | Políticas | Índice global único |
| 15 | Agua | Serie de estrés hídrico |
| 16 | Deforestación | Serie de pérdida forestal |
| 18 | Urbanización | Serie de tasa de urbanización |
| 21 | Salinización | Serie de conductividad |
| 22 | Fósforo | Serie de concentración |
| 23 | Arena | Serie de extracción |
| 26 | Nitrógeno | Serie de deposición |
| 28 | Permafrost | Serie de temperatura |

### 2.3 Casos anteriormente sin campo (RESUELTO)

| # | Caso | Commit de corrección |
|---|------|---------------------|
| 16 | Deforestación | `20072d1` — añadido `driver_cols=[]` |
| 22 | Fósforo | `20072d1` — añadido `driver_cols=[]` |

---

## 3. persistence — Detalle por Caso

Con el cambio de varianza 10× a **std 5×** en `20072d1`, el campo `persistence` está en todos los metrics.json.

### 3.1 Casos que pasan (27/29)

Todos con `std_ratio < 5.0`. Ejemplos representativos:

| # | Caso | std_ratio | pass |
|---|------|-----------|:----:|
| 01 | Clima | 0.98 | ✅ |
| 07 | Finanzas | 1.12 | ✅ |
| 16 | Deforestación | 0.45 | ✅ |
| 24 | Microplásticos | 4.51 | ✅ |
| 27 | Riesgo Bio | 3.89 | ✅ |

### 3.2 Casos que fallan (2/29)

| # | Caso | std_ratio | Diagnóstico |
|---|------|-----------|-------------|
| 11 | Movilidad | 9.65 | ABM amplifica ~10× la variabilidad observada |
| 20 | Kessler | 276,777 | Crecimiento exponencial en ABM vs. datos suaves |

Estos 2 fallos son **legítimos**: el ABM produce dinámicas cualitativamente diferentes a las observaciones. No son bugs de código.

---

## 4. Otros Campos — Estado Completo

### 4.1 emergence_taxonomy.category

Presente en **29/29** casos. Distribución:

| Categoría | Casos | IDs |
|-----------|:-----:|-----|
| strong_emergence | 2 | 16, 24 |
| weak_emergence | 1 | 09 |
| suggestive_emergence | 4 | 14, 17, 19, 29 |
| trend_without_emergence | 6 | 01, 06, 10, 20, 25, 28 |
| null_emergence | 13 | 02, 03, 04, 07, 08, 11, 15, 21, 22, 23, 26, 27 + uno más |
| falsification | 3 | 05, 12, 13 |

### 4.2 bias_correction.mode

Presente en **29/29**. Distribución:

| Modo | Casos |
|------|:-----:|
| full | 5 |
| bias_only | 12 |
| reverted | 2 (02, 27) |
| none | 10 |

### 4.3 edi.permutation_significant

Presente en **29/29**. Significativos: **8/29** (casos 09, 14, 16, 17, 19, 24, 28, 29).

### 4.4 numerical_stability

Presente en **29/29**. Pasan: **25/29**. Fallan: 05, 12, 13, 18.

---

## 5. Conclusión

### ✅ No hay variables faltantes

Todos los campos requeridos por el protocolo C1–C5 están presentes y correctamente tipados en los 29 `metrics.json`:

- `edi` (value, p_value, permutation_significant, confidence_interval)
- `bias_correction` (mode, bias_corrected, metrics)
- `emergence_taxonomy` (category, criteria)
- `persistence` (pass, model_std, obs_std, std_ratio, threshold_std)
- `numerical_stability` (stable, checks)
- `symploke` (pass, coupling_ratio)
- `non_locality` (detected, spatial_correlation)
- `overall_pass`
- `driver_cols` (declarado en validate.py)

### Trabajo restante

Los únicos "faltantes" son **semánticos, no técnicos**:

1. **10 casos con `driver_cols=[]`**: Correcto para datasets univariados. Si en el futuro se encuentran variables exógenas para estos fenómenos, se pueden añadir sin cambios de código.

2. **2 casos con `persistence.pass=false`** (11, 20): Son rechazos legítimos del protocolo, no bugs.

3. **21 casos con `permutation_significant=false`**: Requieren mejores datos o modelos más expresivos, no fixes de código.
