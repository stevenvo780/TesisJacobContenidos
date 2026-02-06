# Caso Finanzas Globales (Modelo y Simulacion)

Este caso implementa dos modelos no isomorfos para dinamica de precios en un indice bursatil:
- Modelo micro (ABM/lattice) con agentes de tendencia y fundamentalistas.
- Modelo macro (ODE agregado) con forzamiento externo.

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
- Fase real: evaluacion final con datos de mercado reales (SPY, 1990-2024).
El script cachea los datos reales en `data/spy_monthly.csv`.

## Validacion
- Split entrenamiento/validacion sintetica: 2000-2009 / 2010-2019.
- Split entrenamiento/validacion real: 1990-2010 / 2011-2024.
- Nudging con observacion rezagada (t-1) para evaluacion de corto plazo.

## Resultados

<!-- AUTO:RESULTS:START -->
| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.235 | 0.769 |
| CR      | 1.152 | 1.078 |
| RMSE ABM| 2.0193 | 0.5282 |
| RMSE ODE| 1.0968 | 1.2264 |
| Corr ABM| 0.9951 | 0.9462 |
| Corr ODE| 0.9923 | 0.9626 |
| C1      | ❌ | ❌ |
| C2      | ✅ | ✅ |
| C3      | ✅ | ✅ |
| C4      | ✅ | ✅ |
| C5      | ✅ | ✅ |
| Estado  | NO VALIDADO | NO VALIDADO |
<!-- AUTO:RESULTS:END -->
