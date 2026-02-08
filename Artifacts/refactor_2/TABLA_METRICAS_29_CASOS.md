# Tabla Maestra de Metricas — 29 Casos (Fase Real)

| # | Caso | EDI | EDI valid | ODE corr | ABM corr | mc | fs | Tipo Dato | C1 | Pass | Flags |
|---|------|-----|-----------|----------|----------|-----|-----|-----------|-----|------|-------|
| 01 | Clima | 0.372 | true | -0.027 | 0.837 | 0.10 | 0.99 | REAL | true | **false** | ODE fantasma |
| 02 | Conciencia | 0.936 | **false** | 0.983 | 0.983 | 0.49 | 0.63 | SINT | true | true | TAUTOLOGICO |
| 03 | Contaminacion | 0.125 | false | -0.192 | 0.712 | 1.00 | 0.76 | REAL | true | **false** | Rechazado |
| 04 | Energia | 0.354 | true | 0.414 | 0.800 | 1.00 | 0.85 | REAL | true | true | mc=1.0 |
| 05 | Epidemiologia | 0.176 | false | -0.004 | 0.750 | 0.64 | 0.72 | REAL | true | **false** | Rechazado |
| 06 | Falsac.Exog | -0.401 | false | 0.678 | 0.706 | 0.97 | 0.99 | REAL | **false** | **false** | Falsacion OK |
| 07 | Falsac.NoEst | 0.090 | false | 0.893 | 0.847 | 1.00 | 0.99 | REAL | **false** | **false** | Falsacion OK |
| 08 | Falsac.Obs | 0.000 | false | N/A | N/A | N/A | N/A | REAL | **false** | **false** | Falsacion OK |
| 09 | Finanzas | 0.882 | true | 0.986 | 0.996 | 1.00 | 0.68 | REAL | true | true | mc=1.0 |
| 10 | Justicia | 0.946 | **false** | 0.985 | 0.985 | 0.56 | 0.63 | SINT | true | true | TAUTOLOGICO |
| 11 | Movilidad | 0.915 | **false** | 0.989 | 0.987 | 0.70 | 0.60 | SINT | true | true | TAUTOLOGICO |
| 12 | Paradigmas | 0.863 | true | 0.993 | 0.993 | 0.39 | 0.52 | SINT | true | true | OK sintetico |
| 13 | Politicas | 0.804 | true | 0.994 | 0.993 | 0.55 | 0.43 | SINT | true | true | mc>0.5 |
| 14 | Postverdad | 0.154 | false | 0.988 | -0.853 | 0.80 | 0.59 | SINT | **false** | **false** | ABM diverge |
| 15 | Wikipedia | 0.018 | false | 0.518 | 0.304 | 1.00 | 0.49 | REAL | **false** | **false** | Rechazado |
| 16 | Deforestacion | 0.846 | true | 0.894 | 0.920 | 0.10 | 0.63 | REAL | true | true | **MEJOR CASO** |
| 17 | Oceanos | 0.936 | **false** | 0.990 | 0.989 | 0.57 | 0.63 | SINT | true | true | TAUTOLOGICO |
| 18 | Urbanizacion | 0.839 | true | 0.999 | 0.999 | 0.58 | 0.64 | REAL | true | true | mc>0.5 |
| 19 | Acidificacion | 0.947 | **false** | 0.992 | 0.992 | 0.57 | 0.63 | SINT | true | true | TAUTOLOGICO |
| 20 | Kessler | 0.776 | true | 0.984 | 0.985 | 0.54 | 0.47 | REAL* | true | true | Proxy debil |
| 21 | Salinizacion | 0.176 | false | 0.802 | -0.295 | 0.85 | 0.71 | REAL* | **false** | **false** | Proxy debil |
| 22 | Fosforo | 0.902 | **false** | 0.883 | 0.881 | 0.64 | 0.65 | REAL | true | true | TAUTOLOGICO |
| 23 | Erosion | 0.923 | **false** | 0.989 | 0.987 | 0.19 | 0.63 | SINT | true | true | TAUTOLOGICO |
| 24 | Microplasticos | 0.856 | true | 0.994 | 0.994 | 0.73 | 0.54 | SINT | true | true | mc>0.5 |
| 25 | Acuiferos | 0.959 | **false** | 0.990 | 0.989 | 0.64 | 0.60 | SINT | true | true | TAUTOLOGICO |
| 26 | Starlink | 0.914 | **false** | 0.994 | 0.994 | 0.46 | 0.68 | REAL* | true | true | TAUT+proxy nulo |
| 27 | Riesgo Biol | 0.893 | true | 0.981 | 0.981 | 0.52 | 0.63 | SINT | true | true | mc>0.5 |
| 28 | Fuga Cerebros | 0.881 | true | 0.992 | 0.992 | 0.65 | 0.52 | SINT | true | true | mc>0.5 |
| 29 | IoT | 0.889 | true | 0.991 | 0.991 | 0.10 | 0.56 | SINT | true | true | OK sintetico |

## Leyenda
- **SINT** = datos sinteticos (ODE+ruido)
- **REAL** = datos reales de API
- **REAL*** = datos reales pero proxy inadecuado
- **TAUTOLOGICO** = EDI > 0.90 (regla de rechazo no aplicada en overall_pass)
- **mc** = macro_coupling
- **fs** = forcing_scale

## Conteos

| Metrica | Valor |
|---------|-------|
| EDI en rango valido 0.30-0.90 + datos reales + pass=true | **4 casos** |
| EDI > 0.90 (tautologico) | 9 casos |
| Datos sinteticos | 12 casos |
| mc > 0.5 | 22 casos |
| ODE corr negativa | 3 casos |
| Controles falsacion correctos | 3 casos |
| Rechazados | 5 casos |
