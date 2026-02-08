# Variables Faltantes por Caso — Oportunidades de Mejora

Este documento lista las variables reales disponibles que podrian integrarse para mejorar
cada simulacion. Solo se incluyen fuentes gratuitas y programaticamente accesibles.

---

## CASOS CON DATOS REALES (mejorar con variables adicionales)

### 01_caso_clima
**Actual:** Solo temperatura media mensual (Meteostat)
**Agregar:**
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

### 09_caso_finanzas
**Actual:** Solo log(SPY) mensual
**Agregar:**
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

### 17_caso_oceanos (PRIORIDAD MAXIMA — datos disponibles)
**Actual:** Sintetico (ODE+ruido)
**Reemplazo:**
| Variable | Fuente | API | Formato |
|----------|--------|-----|---------|
| SST (Sea Surface Temperature) | NOAA ERSST v5 | `https://psl.noaa.gov/data/gridded/data.noaa.ersst.v5.html` | NetCDF mensual desde 1854 |
| Nivel del mar | NASA PODAAC | `https://podaac.jpl.nasa.gov/` | Mensual desde 1993 |
| **Esfuerzo:** BAJO — datos CSV/NetCDF publicos, solo cambiar data.py |

### 19_caso_acidificacion (PRIORIDAD MAXIMA)
**Actual:** Sintetico
**Reemplazo:**
| Variable | Fuente | API |
|----------|--------|-----|
| pH oceanico | Hawaii Ocean Time-series | `http://hahana.soest.hawaii.edu/hot/` |
| pCO2 oceano | SOCAT v2023 | `https://www.socat.info/index.php/data-access/` |
| CO2 atmosferico | Mauna Loa | Mismo que clima |
| **Esfuerzo:** BAJO — datos desde 1988, CSV |

### 25_caso_acuiferos (PRIORIDAD ALTA)
**Actual:** Sintetico
**Reemplazo:**
| Variable | Fuente | API |
|----------|--------|-----|
| Almacenamiento agua (GRACE) | NASA GRACE-FO | `https://grace.jpl.nasa.gov/data/get-data/` |
| Niveles piezometricos | USGS NWIS | `https://waterdata.usgs.gov/nwis` |
| **Esfuerzo:** MEDIO — requiere procesamiento de grids GRACE |

### 12_caso_paradigmas (PRIORIDAD MEDIA)
**Actual:** Sintetico
**Reemplazo:**
| Variable | Fuente | API |
|----------|--------|-----|
| Citaciones por campo | OpenAlex | `https://api.openalex.org/works?group_by=publication_year` |
| Papers publicados | Semantic Scholar | `https://api.semanticscholar.org/` |
| **Esfuerzo:** MEDIO — requiere definir campos/paradigmas y queries |

### 28_caso_fuga_cerebros (FACIL)
**Actual:** Sintetico
**Reemplazo:** World Bank `GB.XPD.RSDV.GD.ZS` (gasto R&D % PIB), `SM.POP.NETM` (migracion neta)
**Esfuerzo:** BAJO — solo cambiar indicador en data.py

### 29_caso_iot (FACIL)
**Actual:** Sintetico
**Reemplazo:** World Bank `IT.CEL.SETS.P2` (suscripciones moviles per capita)
**Esfuerzo:** BAJO

### 13_caso_politicas (FACIL)
**Actual:** Sintetico
**Reemplazo:** World Bank `MS.MIL.XPND.GD.ZS` (gasto militar % PIB) + `GC.TAX.TOTL.GD.ZS` (ingresos fiscales)
**Esfuerzo:** BAJO

### 27_caso_riesgo_biologico (FACIL)
**Actual:** Sintetico
**Reemplazo:** World Bank `SH.DYN.MORT` (mortalidad infantil per 1000) + GHS Index
**Esfuerzo:** BAJO

### 11_caso_movilidad (FACIL)
**Actual:** Sintetico
**Reemplazo:** World Bank `IS.VEH.NVEH.P3` (vehiculos per 1000 personas)
**Esfuerzo:** BAJO

### 10_caso_justicia (FACIL)
**Actual:** Sintetico
**Reemplazo:** World Bank `RL.EST` (Rule of Law Index, WGI)
**Esfuerzo:** BAJO

### 14_caso_postverdad (MEDIO)
**Actual:** Sintetico
**Reemplazo:** Google Trends para "fake news" + "misinformation"
**Esfuerzo:** MEDIO — Google Trends API tiene limitaciones de rate

### 24_caso_microplasticos (MEDIO)
**Actual:** Sintetico
**Reemplazo:** Produccion global de plasticos (PlasticsEurope annual reports, manual)
**Esfuerzo:** MEDIO — datos anuales, requiere digitalizacion manual

### 23_caso_erosion_dialectica (FACIL)
**Actual:** Sintetico
**Reemplazo:** World Bank `SE.ADT.LITR.ZS` (alfabetizacion adultos %)
**Esfuerzo:** BAJO

### ~~02_caso_conciencia (DIFICIL)~~ [IMPLEMENTADO]
**Actual:** Google Trends ("global news") validado como proxy de atencion.
**Estado:** Completado en Refactor Fase 2.


---

## PROXIES INADECUADOS — REEMPLAZO URGENTE

### 20_caso_kessler
**Actual:** Salidas aereas (IS.AIR.DPRT) — NO es debris orbital
**Reemplazo:** CelesTrak TLE catalog count (objetos rastreados en orbita)
```
https://celestrak.org/NORAD/elements/
```
**Alternativa:** ESA DISCOS database o Space-Track.org (requiere registro)

### 26_caso_starlink
**Actual:** Usuarios de internet (IT.NET.USER.ZS) — NO es Starlink
**Reemplazo:** CelesTrak Starlink TLE count + SpaceX launch manifest
**Alternativa:** Jonathan's Space Report (publicaciones semanales de lanzamientos)

### 21_caso_salinizacion
**Actual:** Tierra arable % — proxy muy indirecto de salinidad
**Reemplazo:** FAO AQUASTAT + GLASOD soil degradation data
**Alternativa:** World Bank AG.LND.IRIG.AG.ZS (irrigated land %) como proxy menos malo
