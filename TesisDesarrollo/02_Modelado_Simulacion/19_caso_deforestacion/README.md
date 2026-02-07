# Caso Deforestacion Global (Modelo y Simulacion)

Este caso implementa dos modelos no isomorfos para la dinamica de deforestacion global:
- Modelo micro (ABM/lattice) con interaccion local y acople macro.
- Modelo macro (ODE/balance agregado) con forcing exogeno.

La deforestacion global opera como un proceso macro distribuido que constriñe
las decisiones locales de uso de suelo. La señal secular de declive en cobertura
forestal (% area forestal) refleja politicas macro que actuan como atractor.

## Fuente de datos
- **API:** World Bank — Indicador `AG.LND.FRST.ZS` (% area forestal)
- **Rango:** 1990–2022, frecuencia anual
- **Clave de serie:** `d`

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
cd repos/Simulaciones/caso_deforestacion/src && python3 validate.py
```
