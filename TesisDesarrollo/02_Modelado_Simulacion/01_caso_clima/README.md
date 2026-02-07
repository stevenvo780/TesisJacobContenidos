# Caso Clima Regional (Modelo y Simulacion)

Este caso implementa dos modelos no isomorfos para dinamica climatica regional:
- Modelo micro (ABM/lattice) con interaccion local y acople macro.
- Modelo macro (ODE/energy-balance agregado) con forcing exogeno.

El objetivo es cumplir criterios del marco 00/01/02:
- Capas completas (conceptual, formal, computacional, validacion).
- Modelos alternativos no isomorfos.
- Reglas de aceptacion y C1-C5.

## Estructura
- `docs/arquitectura.md`: capas y supuestos.
- `docs/protocolo_simulacion.md`: protocolo y criterio de paro.
- `docs/indicadores_metricas.md`: indicadores, metricas y reglas.
- `docs/validacion_c1_c5.md`: validacion operativa.
- `docs/reproducibilidad.md`: versionado, entorno y sensibilidad.
- `src/`: implementacion.
- `outputs/`: reportes de corrida.

## Como correr

```bash
pip install -r requirements.txt
python3 src/validate.py
```

Genera:
- `outputs/metrics.json`
- `outputs/report.md`

## Datos sinteticos y reales
- Fase sintetica: calibracion y verificacion interna con serie sintetica.
- Fase real: evaluacion final con datos regionales (Meteostat, CONUS) en el periodo 1990-2024.
El script cachea los datos reales en `data/regional_monthly_tavg.csv`.

## Validacion
- Split entrenamiento/validacion sintetica: 2000-2009 / 2010-2019.
- Split entrenamiento/validacion real: 1990-2010 / 2011-2024.
- Nudging con observacion rezagada (t-1) para evaluacion de corto plazo.

## Resultados

<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.687 | 0.434 |
| CR      | 1.000 | 1.000 |
| RMSE ABM| 2.1139 | 0.5626 |
| RMSE ODE| 1.8845 | 1.5087 |
| Corr ABM| 0.9994 | 0.8233 |
| Corr ODE| 0.9997 | -0.0542 |
| C1      | ✅ | ✅ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | VALIDADO | VALIDADO |
<!-- AUTO:RESULTS:END -->
