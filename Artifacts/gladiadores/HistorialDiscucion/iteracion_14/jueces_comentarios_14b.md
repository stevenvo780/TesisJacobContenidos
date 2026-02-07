# Iteración 14 — Equipo Jueces — Comentarios al Defensor

## ✅ Verificable vs. documentación
- Los scripts citados por la defensa **existen** en `repos/Simulaciones/19_caso_deforestacion/src/` y sus MD5 coinciden con lo reportado.  
- Los valores de `forcing_scale` para Clima/Paradigmas/Fuga Cerebros aparecen en `metrics.json` (fase real), con rutas verificables.

## ⚠️ Observaciones críticas (moderación)
- **NC1 = C1**: La defensa afirma que C1 ya implementa NC1 en escala Z; esto es plausible por la normalización en `hybrid_validator.py`, pero debe documentarse formalmente en la tesis para evitar ambigüedad.
- **Tabla sin extractos**: Las tablas de RMSE_z/threshold_z/NC1_z requieren extractos por caso y fase en `metrics.json`; de lo contrario, quedan como afirmaciones no verificables.
- **Persisten inconsistencias documentales**: la regla EDI/CR en `02_Modelado_Simulacion.md` sigue contradiciendo la etiqueta “Validado” para CR ≈ 1.0. Esto debe corregirse antes de cerrar debate.

## 🔎 Requerimientos al defensor
1. Añadir en documentación oficial (TesisDesarrollo/TesisFinal) una nota explícita de que C1 opera en escala Z y equivale a NC1_z.  
2. Adjuntar extractos (ruta + fase) que respalden los valores de RMSE_z/threshold_z por caso.  
3. Resolver la contradicción EDI/CR vs “Validado” en tablas.

**Conteo de falacias/problemas argumentativos (esta intervención):**
- Equipo defensor: 1 (afirmaciones cuantitativas sin extractos verificables).
- Equipo crítico: 0.

**Solicitud explícita:** mover las clarificaciones al texto de tesis y adjuntar trazabilidad por caso.
