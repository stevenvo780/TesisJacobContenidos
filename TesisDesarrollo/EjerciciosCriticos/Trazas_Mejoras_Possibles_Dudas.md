# Trazas de mejoras, Posibles y Dudas (Partida 1)

## Trazas de mejoras (registradas)
- Correccion EI=0.0 por bug KDE (C5).
- Forzado `assimilation_strength=0.0` en evaluacion.
- Cap `forcing_scale <= 0.99` (Axioma A6).
- Unificacion de repositorio; outputs/metrics.json versionados.
- Reclasificacion CR como indicador complementario.
- Tabla 29 genuinos vs 32 totales con falsaciones excluidas.
- Archivo `mega_run_v8_traceability.json` con MD5 y rutas.

## Posibles (plan de mejora)
**Tecnico**
- Replay total determinista con logs y hashes por caso.
- Eliminar rutas legacy (`caso_clima` vs `01_caso_clima`).
- Script de regeneracion y verificacion MD5 integral.
- Topologias no regulares (small-world/scale-free) para evaluar CR>2.0.
- Metricas espaciales adicionales (entropia, variogramas).

**Documentacion**
- Seccion de reproducibilidad con outputs esperados.
- Consolidar tablas con referencia directa a metrics.json.
- Historial de cambios doctrinales (CR, H1, EI) con fechas y commits.

**Escritura**
- Clarificar diferencia entre causalidad descendente y constriccion efectiva.
- Evitar terminos ontologicamente fuertes sin respaldo.
- Explicitar limites del ABM isotropico.

## Dudas (ontologicas y definicionales)
- Si CR no es condicion necesaria, cual es el umbral minimo para hablar de frontera.
- Diferencia entre constriccion macro efectiva y causalidad descendente fuerte.
- Alcance del termino “hiperobjeto” bajo realismo operativo debil.
- Rol de la ODE como benchmark: que prueba exactamente en lo ontologico.
- Validez de la emergencia cuando la dinamica es altamente homogenea.
- Criterios para distinguir tendencia macro de entidad real.

