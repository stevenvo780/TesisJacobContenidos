# Iteración 4 — Equipo Jueces — Preguntas

## 🧭 Juez de Complejidad
1. Usted afirma que la calibración actual produce `macro_coupling > 0.8` y que la Symploké es operativa. ¿Puede señalar el archivo y las claves exactas en `metrics.json` (ruta completa) donde se ve el valor de `macro_coupling` en **fase real** para Movilidad y Contaminación con el código actual?
2. Si el canal operativo principal es `macro_coupling` y no `forcing_scale`, ¿qué evidencia cuantitativa muestra irreductibilidad macro→micro más allá de la simple mejora del RMSE (p. ej., cambio de régimen o transición de fase) en la fase real?
3. Para Clima real usted reporta `CR = 4.82` y `EDI = 0.002`. ¿Cómo justifica “restricción descendente” cuando el EDI es prácticamente nulo? ¿Cuál es el criterio operativo cuando EDI y CR divergen?

## 🧠 Juez de Filosofía de la Ciencia
1. Si EI fue un bug y ahora se corrige, ¿qué estatus tiene EI en el marco conceptual? ¿Sigue siendo condición informacional fuerte o queda como métrica secundaria? Cite capítulo o sección aplicable.
2. Usted afirma que el crítico atacó “métricas fósiles”. ¿Qué regla metodológica evita el moving target? ¿Cómo se preserva la falsabilidad si los criterios cambian tras cada auditoría?
3. En Contaminación real el EDI negativo lleva a rechazo. ¿Cómo se justifica ontológicamente que un mismo dominio pase o falle dependiendo de recalibraciones si la “existencia operativa” debe ser estable?

## 📐 Juez de Modelado y Validación
1. Indique la ruta exacta y el fragmento de `metrics.json` donde se vea `assimilation_strength = 0.0` en **evaluación** para Movilidad y Contaminación (fase real). Necesito la evidencia textual concreta, no un resumen.
2. ¿Dónde quedaron documentadas (C5) la corrección de EI y la re‑ejecución? Especifique el archivo en `TesisDesarrollo` o `repos/Simulaciones` y la sección.
3. Usted presenta valores “frescos” para EDI/CR/mc. ¿Existe un script reproducible y un commit o hash de ejecución que garantice que cualquiera pueda replicar esos números? Proporcione ubicación exacta.

**Nota del equipo de jueces:** no emitimos veredicto hasta recibir trazabilidad verificable de los tres puntos anteriores.
