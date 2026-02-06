# 03_10 Validacion Caso Contaminacion (Ejecucion)

## Objetivo
- Validar el caso contaminacion con dos fases: sintetica (verificacion interna) y real (evaluacion final).

## Indicadores y umbrales
- C1 Convergencia: RMSE por debajo de `0.6 * sigma` y correlacion >= 0.7.
- C2 Robustez: estabilidad ante perturbaciones +/-10%.
- C3 Replicacion: estabilidad bajo semillas distintas.
- C4 Validez: respuesta detectable a forcing alterno.
- C5 Incertidumbre: sensibilidad acotada.
- Persistencia: varianza del modelo < 5x la varianza observada (serie anual).

## Datos y fases
- Fase sintetica: 1980-01-01 a 2019-01-01, split 2000-01-01.
- Fase real: 1990-01-01 a 2022-01-01, split 2006-01-01 (World Bank PM2.5, WLD).

## Resultados resumidos
- Fase sintetica: `overall_pass = True`.
- Fase real: `overall_pass = True`.
- Errores y umbrales documentados en `02_Modelado_Simulacion/caso_contaminacion/metrics.json`.

## Auditoria y trazabilidad
- Reporte completo en `02_Modelado_Simulacion/caso_contaminacion/report.md`.
- Metricas completas y parametros en `02_Modelado_Simulacion/caso_contaminacion/metrics.json`.
- Semillas y configuracion quedan registradas en el reporte.

## Criterio de cierre
- La validacion queda aceptada si ambas fases pasan C1-C5 y los indicadores.
