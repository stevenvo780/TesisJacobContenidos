# Caso Urbanizacion Global (Modelo y Simulacion)

Este caso implementa dos modelos no isomorfos para la dinamica de urbanizacion
global:
- Modelo micro (ABM/lattice) con interaccion local y acople macro.
- Modelo macro (ODE/balance agregado) con forcing exogeno.

La urbanizacion masiva opera como una señal macro extremadamente suave que
actua como atractor, constriniendo los patrones de migracion micro. La
tendencia secular es tan estable que constituye un caso ideal de hiperobjeto.

## Fuente de datos
- **API:** World Bank — Indicador `SP.URB.TOTL.IN.ZS` (% poblacion urbana)
- **Rango:** 1960–2022, frecuencia anual
- **Clave de serie:** `u`

## Estructura
- `docs/arquitectura.md`: capas y supuestos del modelo hibrido.
- `docs/protocolo_simulacion.md`: protocolo de simulacion y criterio de paro.
- `docs/indicadores_metricas.md`: indicadores, metricas y reglas de rechazo.
- `docs/validacion_c1_c5.md`: validacion operativa C1–C5.
- `docs/reproducibilidad.md`: versionado, entorno y sensibilidad.
- `metrics.json`: metricas de validacion computadas.
- `report.md`: reporte narrativo de resultados.

## Ejecucion
```bash
cd repos/Simulaciones/caso_urbanizacion/src && python3 validate.py
```
