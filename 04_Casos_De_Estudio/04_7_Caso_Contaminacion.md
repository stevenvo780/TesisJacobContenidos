# 04_7 Caso de Estudio: Contaminacion PM2.5 (Ejecutado)

## Contexto
- Fenomeno: contaminacion del aire persistente con shocks externos.
- Justificacion: evidencia distribuida y patrones globales sostenidos.

## Datos
- Fase sintetica: serie controlada 1980-2019 con tendencia.
- Fase real: World Bank PM2.5 (WLD), 1990-2022.
- Archivos de resultados: `02_Modelado_Simulacion/caso_contaminacion/report.md` y `02_Modelado_Simulacion/caso_contaminacion/metrics.json`.

## Modelado
- Modelo micro: ABM lattice 2D con difusion local y acople macro.
- Modelo macro: ODE de balance agregado para contaminacion.
- Variable puente: `P` (contaminacion agregada) acopla micro y macro.

## Resultados
- Fase sintetica: `overall_pass = True`.
- Fase real: `overall_pass = True`.
- Convergencia en ambas fases bajo umbral `0.6 * sigma`.
- Symploke interna > externa, no-localidad funcional y persistencia verificadas.
- Emergencia: el modelo reducido degrada el error por encima del umbral.

## Criterio de aceptacion
- Cumplimiento C1-C5 y reglas de indicadores en ambas fases.

## Limites y criterio de paro
- Limites: resolucion anual y cobertura global agregada.
- Criterio de paro: estabilidad de patrones y costo marginal > beneficio.
