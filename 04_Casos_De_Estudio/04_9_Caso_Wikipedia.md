# 04_9 Caso de Estudio: Wikipedia (Ejecutado)

## Contexto
- Fenomeno: atencion colectiva persistente con shocks externos.
- Justificacion: evidencia distribuida y patrones recurrentes de interes.

## Datos
- Fase sintetica: serie controlada 2000-2019 con estacionalidad.
- Fase real: Wikimedia Pageviews (cluster de articulos), 2015-2024.
- Archivos de resultados: `02_Modelado_Simulacion/caso_wikipedia/report.md` y `02_Modelado_Simulacion/caso_wikipedia/metrics.json`.

## Modelado
- Modelo micro: ABM lattice 2D con contagio local y acople macro.
- Modelo macro: ODE de balance agregado para atencion.
- Variable puente: `W` (atencion agregada) acopla micro y macro.

## Resultados
- Fase sintetica: `overall_pass = True`.
- Fase real: `overall_pass = True`.
- Convergencia en ambas fases bajo umbral `0.6 * sigma`.
- Symploke interna > externa, no-localidad funcional y persistencia verificadas.
- Emergencia: el modelo reducido degrada el error por encima del umbral.

## Criterio de aceptacion
- Cumplimiento C1-C5 y reglas de indicadores en ambas fases.

## Limites y criterio de paro
- Limites: depende de coverage de pageviews y seleccion de articulos.
- Criterio de paro: estabilidad de patrones y costo marginal > beneficio.
