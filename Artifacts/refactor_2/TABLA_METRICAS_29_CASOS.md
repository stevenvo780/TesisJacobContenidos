# Tabla Maestra de Metricas — 29 Casos (Fase Real)

Actualizado: 2026-02-08

| # | Caso | EDI | EDI valid | ODE corr | ABM corr | mc | fs | Tipo Dato | C1 | Pass | Flags |
|---|------|-----|-----------|----------|----------|-----|-----|-----------|-----|------|-------|
| 01 | Clima Regional (CONUS) | 0.000 | false | -0.021 | 0.008 | 0.10 | 0.99 | REAL | false | false | ODE fantasma |
| 02 | Conciencia Colectiva | -0.375 | false | nan | 0.000 | 0.93 | 0.99 | SINT | false | false | mc>0.5, Sint |
| 03 | Contaminación PM2.5 | 0.000 | false | -0.153 | -0.149 | 0.10 | 0.76 | REAL | false | false | ODE fantasma |
| 04 | Energía (OPSD GB Grid) | 0.000 | false | 0.417 | 0.415 | 0.10 | 0.85 | REAL | false | false |  |
| 05 | Epidemiología (COVID-19 SEIR) | -0.163 | false | 0.361 | 0.005 | 0.81 | 0.99 | REAL | false | false | mc>0.5 |
| 06 | Falsación: Exogeneidad | 0.469 | true | -0.368 | -0.452 | 0.62 | 0.99 | REAL | false | false | ODE fantasma, mc>0.5 |
| 07 | Falsación: No-Estacionariedad | -0.211 | false | 0.783 | 0.001 | 1.00 | 0.79 | REAL | false | false | mc>0.5 |
| 08 | Falsación: Observabilidad Escasa | 0.000 | false | N/A | N/A | N/A | N/A | REAL | false | false |  |
| 09 | Finanzas (SPY) | 0.000 | false | 0.981 | 0.990 | 0.11 | 0.71 | REAL | true | false |  |
| 10 | Justicia Algorítmica | -0.225 | false | 0.062 | 0.058 | 1.00 | 0.48 | REAL | false | false | mc>0.5 |
| 11 | Movilidad Urbana | -0.373 | false | 0.000 | -0.131 | 1.00 | 0.80 | REAL | false | false | mc>0.5 |
| 12 | Cambio de Paradigmas Científicos | -2.008 | false | nan | 0.000 | 0.19 | 0.82 | REAL | false | false |  |
| 13 | Políticas Estratégicas Globales | -2.496 | false | 0.703 | 0.073 | 1.00 | 0.99 | REAL | false | false | mc>0.5 |
| 14 | Postverdad y Desinformación | -0.465 | false | nan | 0.000 | 0.43 | 0.99 | SINT | false | false | Sint |
| 15 | Wikipedia Clima | 0.003 | false | -0.590 | -0.662 | 0.77 | 0.49 | REAL | false | false | ODE fantasma, mc>0.5 |
| 16 | Deforestación Global | -1.640 | false | 0.868 | 0.886 | 0.77 | 0.94 | REAL | false | false | mc>0.5 |
| 17 | Temperatura Oceánica Global | -0.451 | false | 0.011 | 0.024 | 0.83 | 0.64 | REAL* | false | false | mc>0.5, Proxy |
| 18 | Urbanización Global | -0.057 | false | 0.994 | 0.996 | 0.45 | 0.97 | REAL | false | false |  |
| 19 | Acidificación Oceánica | -0.451 | false | -0.015 | 0.023 | 0.83 | 0.64 | REAL* | false | false | ODE fantasma, mc>0.5, Proxy |
| 20 | Síndrome de Kessler | -3.532 | false | 1.000 | 1.000 | 0.47 | 0.96 | REAL* | false | false | Proxy |
| 21 | Salinización de Suelos | -1.930 | false | 0.802 | 0.003 | 0.86 | 0.99 | REAL* | false | false | mc>0.5, Proxy |
| 22 | Ciclo del Fósforo | -2.293 | false | 0.869 | 0.879 | 0.63 | 0.98 | REAL | false | false | mc>0.5 |
| 23 | Erosión Dialéctica | -5.471 | false | 0.992 | 0.988 | 1.00 | 0.97 | REAL | false | false | mc>0.5 |
| 24 | Contaminación por Microplásticos | -0.618 | false | 0.994 | 0.994 | 0.84 | 0.49 | REAL* | false | false | mc>0.5, Proxy |
| 25 | Nivel Freático de Acuíferos | -0.197 | false | 0.954 | 0.980 | 1.00 | 0.99 | REAL* | false | false | mc>0.5, Proxy |
| 26 | Constelaciones Satelitales (Starlink) | -2.754 | false | 0.999 | 1.000 | 0.47 | 0.96 | REAL* | false | false | Proxy |
| 27 | Contaminación por Microplásticos | 0.856 | false | 0.994 | 0.994 | 0.52 | 0.55 | REAL | true | false | mc>0.5 |
| 27 | Riesgo Biológico Global | -0.769 | false | 0.967 | 0.974 | 0.73 | 0.96 | REAL | false | false | mc>0.5 |
| 28 | Fuga de Cerebros Global | -0.049 | false | 0.891 | 0.428 | 1.00 | 0.96 | REAL | false | false | mc>0.5 |
| 29 | Ecosistema IoT Global | -0.002 | false | 0.927 | 0.945 | 0.11 | 0.99 | REAL | false | false |  |

## Conteos

| Métrica | Valor |
|---------|-------|
| EDI válido (0.30-0.90) | 1 |
| EDI > 0.90 (tautológico) | 0 |
| Datos sintéticos (fallback) | 2 |
| Datos con proxy (REAL*) | 7 |
| mc > 0.5 | 19 |
| ODE corr negativa | 5 |
| overall_pass = true | 0 |
