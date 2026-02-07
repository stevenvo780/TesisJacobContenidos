# Trazas de mejoras, Posibles y Dudas

**Trazas de mejoras (hechas y registradas)**
- Correccion de EI=0.0 (KDE) y registro en C5.
- `assimilation_strength=0.0` en evaluacion para evitar leakage.
- Cap `forcing_scale <= 0.99` (Axioma A6).
- Unificacion de repositorio y tracking de `outputs/metrics.json`.
- Reclasificacion de CR como indicador complementario (no condicion de H1).
- Tabla 29 genuinos vs 32 totales con falsaciones excluidas.
- Incorporacion de `mega_run_v8_traceability.json` con MD5 y rutas.

**Posibles (plan de mejoras tecnicas, escritura, documentacion)**
- Ejecutar **rebuild total determinista** de todos los casos con logs y hashes publicados.
- Eliminar rutas legacy y unificar nomenclatura (`caso_clima` vs `01_caso_clima`).
- Añadir script de reproduccion que regenere outputs y compare MD5.
- Incluir seccion de reproducibilidad con outputs esperados en la tesis.
- Añadir topologias no regulares (small-world, scale-free) para evaluar CR>2.0.
- Implementar metricas de heterogeneidad espacial (entropia, variogramas).
- Publicar analisis de sensibilidad de EDI a forcing_scale y macro_coupling.
- Clarificar el rol de ODE como benchmark y no como driver del ABM.
- Consolidar tablas en TesisFinal con fuentes directas a metrics.json.
- Mejorar redaccion y consistencia terminologica (hiperobjeto, constriccion, causalidad).

**Dudas (problemas ontologicos/definicionales a resolver)**
- Si CR no es condicion necesaria, cual es el criterio minimo de frontera para hablar de "objeto".
- Diferencia entre constriccion macro efectiva y causalidad descendente fuerte.
- Alcance ontologico de la tesis: realismo operativo debil vs realismo fuerte.
- Si la emergencia es temporal y agregada, hasta donde puede llamarse hiperobjeto.
- Como tratar series monotónicas donde corr ~1.0 no implica explicacion causal.
- Que evidencia adicional permitiria pasar de "tendencia macro" a "entidad".
