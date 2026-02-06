# 03_9 Validacion Caso Movilidad (Ejecucion)

## Objetivo
- Validar el caso movilidad con dos fases: sintetica (verificacion interna) y real (evaluacion final).

## Indicadores y umbrales
- C1 Convergencia: RMSE por debajo de `0.6 * sigma` (piso sigma 0.3) y correlacion >= 0.3.
- C2 Robustez: estabilidad ante perturbaciones +/-10%.
- C3 Replicacion: estabilidad bajo semillas distintas.
- C4 Validez: respuesta detectable a forcing alterno.
- C5 Incertidumbre: sensibilidad acotada.
- Indicadores adicionales: symploke, no-localidad, persistencia y emergencia.

## Datos y fases
- Fase sintetica: 2000-01-01 a 2019-12-01, split 2010-01-01.
- Fase real: 2020-03-01 a 2024-12-31, split 2023-01-01 (MTA Subway, mensual).

## Resultados resumidos
- Fase sintetica: `overall_pass = True`.
- Fase real: `overall_pass = True`.
- Errores y umbrales documentados en `02_Modelado_Simulacion/caso_movilidad/metrics.json`.

## Auditoria y trazabilidad
- Reporte completo en `02_Modelado_Simulacion/caso_movilidad/report.md`.
- Metricas completas y parametros en `02_Modelado_Simulacion/caso_movilidad/metrics.json`.
- Semillas y configuracion quedan registradas en el reporte.

## Criterio de cierre
- La validacion queda aceptada si ambas fases pasan C1-C5 y los indicadores.
