# Caso Emisiones CO2 Oceanos (Modelo y Simulacion)

Este caso implementa dos modelos no isomorfos para la dinamica de emisiones
de CO2 a escala global:
- Modelo micro (ABM/lattice) con interaccion local y acople macro.
- Modelo macro (ODE/balance agregado) con forcing exogeno.

Las emisiones globales de CO2 constituyen el hiperobjeto por excelencia
(Morton, 2013). La acumulacion de CO2 opera como forcing macro sobre la
actividad economica local, generando un acoplamiento descendente.

## Fuente de datos
- **API:** World Bank — Indicador `EN.ATM.CO2E.KT` (emisiones CO2 en kt)
- **Rango:** 1960–2022, frecuencia anual
- **Clave de serie:** `e`

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
cd repos/Simulaciones/caso_oceanos/src && python3 validate.py
```
