# Reporte total — Estado de Simulaciones (29 casos)

- **Fecha (UTC):** 2026-02-12 02:24 UTC
- **Fuente:** `repos/Simulaciones/*/outputs/metrics.json` (fase real)
- **overall_pass=True:** 9/29
- **Casos validados:** 05_caso_epidemiologia, 11_caso_movilidad, 13_caso_politicas_estrategicas, 14_caso_postverdad, 15_caso_wikipedia, 18_caso_urbanizacion, 20_caso_kessler, 22_caso_fosforo, 27_caso_riesgo_biologico

## Veredicto científico (tesis)
- **Sí, es científicamente válido como instrumento de clasificación**: el pipeline discrimina (no fuerza), tiene controles negativos (06–08), usa zero-nudging en evaluación y reporta fallos (C2/C4/p-valor) en vez de “arreglarlos”.
- **Suficiencia**: el estado actual es estable (9/29) y suficiente para sostener el argumento central de “paisaje” + selectividad; los casos que fallan lo hacen por razones explícitas (robustez, validez o significancia), lo cual fortalece la tesis.

## Distribución de clasificación (por EDI/p, no por overall_pass)
- **Nivel 0 (null):** 7
- **Nivel 1 (trend / no significativo):** 6
- **Nivel 2 (suggestive):** 2
- **Nivel 3 (weak / componente funcional):** 6
- **Nivel 4* (strong por magnitud):** 5
- **control (falsificación):** 3

## Tabla maestra (fase real)
> Columnas: EDI, p-perm (999), C1–C5 + criterios extra, y nota de fallo.

| # | Caso | overall | EDI | p | C1 | C2 | C3 | C4 | C5 | Sym | NL | Per | Emr | Cp | Clasificación | Nota |
|---:|---|:---:|---:|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|---|---|
| 1 | 01_caso_clima | — | 0.002 | 1.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 1 (trend / no significativo) |  |
| 2 | 02_caso_conciencia | — | 0.123 | 0.231 | Si | Si | Si | Si | Si | Si | No | Si | Si | Si | Nivel 1 (trend / no significativo) | sin significancia (p≥0.05) |
| 3 | 03_caso_contaminacion | — | -0.011 | 0.737 | Si | Si | Si | Si | Si | Si | Si | Si | No | Si | Nivel 0 (null) |  |
| 4 | 04_caso_energia | — | 0.360 | 0.061 | Si | No | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 1 (trend / no significativo) | falla C2 (robustez); sin significancia (p≥0.05) |
| 5 | 05_caso_epidemiologia | ✓ | 0.129 | 0.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 3 (weak / componente funcional) |  |
| 6 | 06_caso_falsacion_exogeneidad | — | 0.055 | 1.000 | Si | No | Si | No | Si | Si | Si | Si | No | Si | control (falsificación) | control negativo (esperado: rechazar); falla C2 (robustez); falla C4 (validez); sin significancia (p≥0.05) |
| 7 | 07_caso_falsacion_no_estacionariedad | — | -0.890 | 1.000 | No | No | Si | Si | Si | Si | Si | Si | Si | Si | control (falsificación) | control negativo (esperado: rechazar); falla C2 (robustez) |
| 8 | 08_caso_falsacion_observabilidad | — | -1.000 | 1.000 | No | No | Si | Si | Si | Si | Si | Si | Si | Si | control (falsificación) | control negativo (esperado: rechazar); falla C2 (robustez) |
| 9 | 09_caso_finanzas | — | 0.081 | 0.000 | Si | Si | Si | No | Si | Si | Si | Si | Si | Si | Nivel 2 (suggestive) | falla C4 (validez) |
| 10 | 10_caso_justicia | — | 0.227 | 0.477 | Si | Si | Si | Si | Si | Si | Si | Si | No | Si | Nivel 1 (trend / no significativo) | sin significancia (p≥0.05) |
| 11 | 11_caso_movilidad | ✓ | 0.128 | 0.002 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 3 (weak / componente funcional) |  |
| 12 | 12_caso_paradigmas | — | -0.006 | 0.000 | No | Si | Si | Si | Si | Si | Si | Si | No | Si | Nivel 0 (null) |  |
| 13 | 13_caso_politicas_estrategicas | ✓ | 0.288 | 0.001 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 3 (weak / componente funcional) |  |
| 14 | 14_caso_postverdad | ✓ | 0.325 | 0.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 4* (strong por magnitud) |  |
| 15 | 15_caso_wikipedia | ✓ | 0.160 | 0.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 3 (weak / componente funcional) |  |
| 16 | 16_caso_deforestacion | — | 0.579 | 0.000 | Si | No | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 4* (strong por magnitud) | falla C2 (robustez) |
| 17 | 17_caso_oceanos | — | -0.032 | 1.000 | No | Si | Si | Si | Si | Si | Si | Si | No | Si | Nivel 0 (null) |  |
| 18 | 18_caso_urbanizacion | ✓ | 0.151 | 0.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 3 (weak / componente funcional) |  |
| 19 | 19_caso_acidificacion_oceanica | — | -0.000 | 0.000 | No | Si | Si | Si | Si | Si | Si | Si | No | Si | Nivel 0 (null) |  |
| 20 | 20_caso_kessler | ✓ | 0.381 | 0.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 4* (strong por magnitud) |  |
| 21 | 21_caso_salinizacion | — | 0.058 | 0.004 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 2 (suggestive) |  |
| 22 | 22_caso_fosforo | ✓ | 0.376 | 0.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 4* (strong por magnitud) |  |
| 23 | 23_caso_erosion_dialectica | — | -0.988 | 1.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 0 (null) |  |
| 24 | 24_caso_microplasticos | — | 0.656 | 0.000 | Si | No | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 4* (strong por magnitud) | falla C2 (robustez) |
| 25 | 25_caso_acuiferos | — | -0.126 | 1.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 0 (null) |  |
| 26 | 26_caso_starlink | — | 0.837 | 1.000 | Si | No | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 1 (trend / no significativo) | falla C2 (robustez); sin significancia (p≥0.05) |
| 27 | 27_caso_riesgo_biologico | ✓ | 0.257 | 0.003 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 3 (weak / componente funcional) |  |
| 28 | 28_caso_fuga_cerebros | — | 0.059 | 0.780 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | Nivel 1 (trend / no significativo) | sin significancia (p≥0.05) |
| 29 | 29_caso_iot | — | -0.919 | 1.000 | No | No | Si | Si | Si | Si | Si | No | Si | Si | Nivel 0 (null) | falla C2 (robustez) |

## Casos clave (lectura “sin forzar”)
- **16 Deforestación** y **24 Microplásticos**: EDI alto y significativo, pero **falla C2** → exactamente el tipo de “strong sin overall_pass” que sirve para argumentar selectividad (no rubber-stamp).
- **04 Energía**: EDI alto pero p≈0.06 (no significativo) y sensibilidad C2. En estado actual **se fuerza A6 (forcing_scale≤0.99)**, evitando dominancia exógena.
- **09 Finanzas** y **21 Salinización**: señal estadística pequeña (Nivel 2) pero límites de validez/interpretación → útiles para explicar límites del instrumento.
- **06–08 (falsificaciones)**: rechazadas como corresponde → refuerzan la falsabilidad del protocolo.

## Qué se hizo (mejoras técnicas relevantes)
- **Robustez C2 sin sesgo de borde**: `perturb_params()` usa **reflexión en clamps** para evitar perturbación asimétrica cuando un parámetro calibrado cae en el límite.
- **Clamps configurables por caso**: soporte de `calibration.refinement_clamps` en `case_config.json` (vía `config_loader.py`) para ampliar el espacio de refinamiento solo donde hace falta, sin afectar otros casos.
- **A6 respetado donde aplica**: en `04_caso_energia` se fuerza `forcing_scale≤0.99` para evitar dominancia exógena.

## Recomendaciones de cierre
- Si el objetivo es “estado final para escritura”, **sí: es suficiente**. Congelar este estado, regenerar tablas y construir `TesisFinal/`.
