# Variables Faltantes por Caso — Oportunidades de Mejora

> **Actualizado:** 2026-02-12 (post commit e3db5c7 — T1-T8 fixes + revert regresiones, overall_pass=1/29)

Este documento lista las variables reales disponibles que podrian integrarse para mejorar
cada simulacion. Solo se incluyen fuentes gratuitas y programaticamente accesibles.

> **Estado global:** **16/26** casos no-falsificación tienen `driver_cols` con variables reales declaradas en sus `validate.py` (T1, commit 23214c0). La infraestructura `driver_cols` en `hybrid_validator.py` está activa y los drivers se integran vía OLS en la construcción de forcing.
>
> **8 casos con lista vacía []:** 03 (Contaminación), 10 (Justicia), 13 (Políticas), 15 (Wikipedia), 17 (Océanos), 18 (Urbanización), 19 (Acidificación), 20 (Kessler).
> **2 sin campo driver_cols:** 16 (Deforestación), 22 (Fósforo).
> **3 falsificación:** 06, 07, 08 (drivers de control por diseño).
>
> ✅ **Regresiones revertidas (e3db5c7):** Drivers problemáticos en casos 24 (mismanaged_share) y 27 (3 drivers extras) fueron eliminados. EDI restaurado a valores pre-T1.

---

## CASOS CON DATOS REALES (mejorar con variables adicionales) — 16/26 con driver_cols

> **Estado:** 16/26 casos no-falsificación tienen `driver_cols` con contenido en `validate.py` (T1, commit 23214c0, revert e3db5c7). Los drivers se usan en la construcción de forcing vía OLS.

### 01_caso_clima — ✅ driver_cols declarados
**Actual:** Temperatura media mensual (Meteostat)
**ODE:** ✅ Budyko-Sellers implementado en `ode_models.py`
**driver_cols:** `["co2", "tsi", "ohc", "aod"]` ✔️ declarados en validate.py
**Agregar variables:** ✅ Declaradas (pendiente verificar que data.py las sirve)
| Variable | Fuente | API | Impacto |
|----------|--------|-----|---------|
| CO2 atmosferico | NOAA ESRL Mauna Loa | `ftp://aftp.cmdl.noaa.gov/products/trends/co2/co2_mm_mlo.txt` | CRITICO — forcing real del clima |
| Irradiancia solar (TSI) | LASP/SORCE | `http://lasp.colorado.edu/data/sorce/tsi_data/` | ALTO — ciclo solar |
| OHC (calor oceanico) | NOAA NCEI | `https://www.ncei.noaa.gov/data/oceans/` | ALTO — inercia termica |
| **ODE recomendada:** Balance radiativo `dT/dt = (S*(1-a)/4 - e*sigma*T^4) / C + noise` |

### 04_caso_energia
**Actual:** Carga electrica GB mensual (OPSD)
**Agregar:**
| Variable | Fuente | API |
|----------|--------|-----|
| Temperatura GB | Meteostat | Ya disponible en el repo |
| Precio electricidad | ENTSOE Transparency | `https://transparency.entsoe.eu/api` |
| Generacion renovable | OPSD | Mismo CSV, columnas wind/solar |

### 05_caso_epidemiologia
**Actual:** Casos COVID semanales globales (OWID)
**Agregar:**
| Variable | Fuente | API |
|----------|--------|-----|
| Muertes COVID | OWID | Mismo CSV: `new_deaths_smoothed` |
| Vacunacion | OWID | Mismo CSV: `people_vaccinated` |
| Stringency index | OxCGRT | `https://github.com/OxCGRT/covid-policy-tracker` |
| **ODE recomendada:** Ya tiene modelo SEIR — es el unico caso bueno |

### 09_caso_finanzas — ✅ driver_cols declarados
**Actual:** Log(SPY) mensual
**ODE:** ✅ Heston implementado en `ode_models.py`
**driver_cols:** `["vix", "fedfunds", "inflation", "credit_spread", "volume"]` ✔️ declarados
**Agregar variables:** ✅ Declaradas
| Variable | Fuente | API |
|----------|--------|-----|
| VIX (volatilidad) | Yahoo Finance | `yfinance.download("^VIX")` |
| Fed Funds Rate | FRED | `https://fred.stlouisfed.org/series/FEDFUNDS` |
| Volumen SPY | Yahoo Finance | Ya en descarga actual |
| **ODE recomendada:** Heston `dv = kappa*(theta-v)dt + xi*sqrt(v)dW` |

### 16_caso_deforestacion
**Actual:** Forest area % global (World Bank)
**Agregar:**
| Variable | Fuente | API |
|----------|--------|-----|
| Incendios (fire counts) | NASA FIRMS | `https://firms.modaps.eosdis.nasa.gov/api/` |
| Precipitacion tropical | NOAA GPCC | Descarga directa |
| Poblacion rural | World Bank SP.RUR.TOTL | Ya integrado |

---

## CASOS SINTETICOS — MIGRACION A DATOS REALES

### 17_caso_oceanos (PRIORIDAD MAXIMA — datos disponibles) — ✅ DATOS REALES CACHEADOS
**Actual:** Datos reales cacheados en `data/dataset.csv` (35 filas, cols: date,value). Fuente: NOAA SST/ERSST.
**ODE:** ✅ `ocean_thermal` implementado
**Acción requerida:** Diagnosticar fallo WMO o usar descarga directa CSV de NOAA ERSST
**Reemplazo:**
| Variable | Fuente | API | Formato |
|----------|--------|-----|---------|
| SST (Sea Surface Temperature) | NOAA ERSST v5 | `https://psl.noaa.gov/data/gridded/data.noaa.ersst.v5.html` | NetCDF mensual desde 1854 |
| Nivel del mar | NASA PODAAC | `https://podaac.jpl.nasa.gov/` | Mensual desde 1993 |
| **Esfuerzo:** BAJO — datos CSV/NetCDF publicos, solo cambiar data.py |

### 19_caso_acidificacion (PRIORIDAD MAXIMA) — ✅ DATOS REALES CACHEADOS
**Actual:** Datos reales cacheados en `data/dataset.csv` (32 filas, cols: date,value). Fuente: PMEL/NOAA.
**ODE:** ✅ `acidification` implementado
**Acción requerida:** Diagnosticar fallo API o usar descarga directa HOT CSV
**Reemplazo:**
| Variable | Fuente | API |
|----------|--------|-----|
| pH oceanico | Hawaii Ocean Time-series | `http://hahana.soest.hawaii.edu/hot/` |
| pCO2 oceano | SOCAT v2023 | `https://www.socat.info/index.php/data-access/` |
| CO2 atmosferico | Mauna Loa | Mismo que clima |
| **Esfuerzo:** BAJO — datos desde 1988, CSV |

### 25_caso_acuiferos (PRIORIDAD ALTA) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **GRAVIS + USGS + WorldBank** (obs_mean=85.74, dataset.csv presente)
**ODE:** ✅ `aquifer_balance` implementado
**Reemplazo:**
| Variable | Fuente | API |
|----------|--------|-----|
| Almacenamiento agua (GRACE) | NASA GRACE-FO | `https://grace.jpl.nasa.gov/data/get-data/` |
| Niveles piezometricos | USGS NWIS | `https://waterdata.usgs.gov/nwis` |
| **Esfuerzo:** MEDIO — requiere procesamiento de grids GRACE |

### 12_caso_paradigmas (PRIORIDAD MEDIA) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **OpenAlex citations + WorldBank R&D** (obs_mean=34,343)
**Reemplazo original:**
| Variable | Fuente | API |
|----------|--------|-----|
| Citaciones por campo | OpenAlex | `https://api.openalex.org/works?group_by=publication_year` |
| Papers publicados | Semantic Scholar | `https://api.semanticscholar.org/` |
| **Esfuerzo:** MEDIO — requiere definir campos/paradigmas y queries |

### 28_caso_fuga_cerebros (FACIL) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **WorldBank GB.XPD.RSDV.GD.ZS** (obs_mean=2.10, dataset.csv presente)
**Reemplazo original:** World Bank `GB.XPD.RSDV.GD.ZS` (gasto R&D % PIB), `SM.POP.NETM` (migracion neta)
**Esfuerzo:** BAJO — solo cambiar indicador en data.py

### 29_caso_iot (FACIL) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **WorldBank IT.CEL.SETS.P2** (obs_mean=36.88, dataset.csv presente)
**Reemplazo original:** World Bank `IT.CEL.SETS.P2` (suscripciones moviles per capita)
**Esfuerzo:** BAJO

### 13_caso_politicas (FACIL) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **WorldBank MS.MIL.XPND.GD.ZS** (obs_mean=2.75, dataset.csv presente)
**Reemplazo original:** World Bank `MS.MIL.XPND.GD.ZS` (gasto militar % PIB) + `GC.TAX.TOTL.GD.ZS` (ingresos fiscales)
**Esfuerzo:** BAJO

### 27_caso_riesgo_biologico (FACIL) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **WorldBank SH.DYN.MORT** (obs_mean=52.03, dataset.csv presente)
**Reemplazo original:** World Bank `SH.DYN.MORT` (mortalidad infantil per 1000) + GHS Index
**Esfuerzo:** BAJO

### 11_caso_movilidad (FACIL) — ✅ DATOS REALES CACHEADOS
**Actual:** Datos reales cacheados en `data/dataset.csv` (54 filas, cols: year,date,value,gdp_per_capita,air_departures). Fuente: WorldBank.
**Reemplazo original:** World Bank `IS.VEH.NVEH.P3` (vehiculos per 1000 personas)
**Esfuerzo:** BAJO

### 10_caso_justicia (FACIL) — ✅ DATOS REALES CACHEADOS
**Actual:** Datos reales cacheados en `data/dataset.csv` (62 filas, cols: date,value). Fuente: WorldBank RL.EST.
**Reemplazo original:** World Bank `RL.EST` (Rule of Law Index, WGI)
**Esfuerzo:** BAJO

### 14_caso_postverdad (MEDIO) — ✅ DATOS REALES CACHEADOS
**Actual:** Datos reales cacheados en `data/dataset.csv` (20 filas, cols: year,date,value,mobile_subs,literacy). Fuente: WorldBank + proxies.
**Reemplazo original:** Google Trends para "fake news" + "misinformation"
**Esfuerzo:** MEDIO — Google Trends API tiene limitaciones de rate

### 24_caso_microplasticos (MEDIO) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **OWID plastic production + WorldBank** (obs_mean=42.23, dataset.csv presente)
**Reemplazo original:** Produccion global de plasticos (PlasticsEurope annual reports, manual)
**Esfuerzo:** MEDIO — datos anuales, requiere digitalizacion manual

### 23_caso_erosion_dialectica (FACIL) — ✅ MIGRADO
**Actual:** ~~Sintetico~~ → **WorldBank SE.ADT.LITR.ZS** (obs_mean=85.35, dataset.csv presente)
**Reemplazo original:** World Bank `SE.ADT.LITR.ZS` (alfabetizacion adultos %)
**Esfuerzo:** BAJO

### ~~02_caso_conciencia (DIFICIL)~~ [IMPLEMENTADO] — ✅ driver_cols declarados
**Actual:** Google Trends ("global news") validado como proxy de atencion.
**driver_cols:** `["suicide_rate", "tertiary_enrollment"]` ✔️ declarados
**Estado:** Código completado, **pytrends no instalado** → cae a fallback sintético en ejecución.


---

## PROXIES INADECUADOS — REEMPLAZO URGENTE

### 20_caso_kessler — ✅ RESUELTO
**Actual:** ~~Salidas aereas (IS.AIR.DPRT) — NO es debris orbital~~ → **CelesTrak SATCAT** (objetos orbitales rastreados, obs_mean=7187)
**Reemplazo implementado:** CelesTrak TLE catalog count (objetos rastreados en orbita)
```
https://celestrak.org/NORAD/elements/
```
**Alternativa:** ESA DISCOS database o Space-Track.org (requiere registro)

### 26_caso_starlink — ✅ RESUELTO
**Actual:** ~~Usuarios de internet (IT.NET.USER.ZS) — NO es Starlink~~ → **CelesTrak SATCAT filtrado STARLINK** (obs_mean=4774)
**Reemplazo implementado:** CelesTrak Starlink TLE count + SpaceX launch manifest
**Alternativa:** Jonathan's Space Report (publicaciones semanales de lanzamientos)

### 21_caso_salinizacion — ⚠️ MEJORADO (T3, commit 23214c0)
**Actual:** ~~Tierra arable %~~ → **Tierra irrigada % (AG.LND.IRIG.AG.ZS)** + **freshwater_withdrawal (ER.H2O.FWTL.ZS)** como driver
**driver_cols:** `["freshwater_withdrawal"]` ✔️
**Reemplazo ideal pendiente:** FAO AQUASTAT + GLASOD soil degradation data
**Nota T3:** data.py reescrito con `_fetch_indicator()` helper + API fallback. EDI bajó de 0.154 a 0.027 (sigue trend).
**Alternativa:** World Bank AG.LND.IRIG.AG.ZS (irrigated land %) como proxy menos malo
