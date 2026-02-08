# Dinámica Auditoría de Escritura - Tesis de Hiperobjetos

**Propósito**
Simular un proceso de revisión editorial y defensa narrativa de la tesis. A diferencia de "Gladiadores" (que debate la validez científica), esta dinámica se enfoca exclusivamente en la **calidad del texto**: claridad, coherencia, flujo argumental, estilo y rigor académico.

**Participantes**
1. **Auditor de Escritura:** Crítico implacable de la forma y el fondo narrativo. Busca ambigüedades, redundancias, falta de definiciones y desconexiones lógicas en el texto.
2. **Defensor de Escritura:** Justifica las decisiones estilísticas y narrativas, propone reescrituras y defiende la complejidad necesaria del texto.

**Contexto base de la tesis (Resumen para Escritura)**
- La tesis es un documento complejo que une Filosofía (Realismo Especulativo), Ciencia de Sistemas (Sinergética) y Computación (Simulación Multiagente).
- El desafío principal es mantener la legibilidad sin sacrificar la precisión técnica de tres dominios distintos.
- Se debe cuidar especialmente la definición de términos (Glosario) y la trazabilidad de argumentos.

**Reglas de juego (por rondas)**
- Se juega en rondas de interacción directa entre el Auditor y el Defensor.
- **Turno Auditor:** Selecciona una sección, párrafo o concepto y lanza una crítica estructurada (Sintaxis, Claridad, Coherencia, Tono).
- **Turno Defensor:** Responde a la crítica aceptando el cambio (proponiendo nueva redacción) o justificando la versión actual.
- **Objetivo:** Llegar a un consenso de redacción ("Versión Consensuada") para la sección en disputa.

**Entrega y trazabilidad**
- Toda intervención debe quedar en `Artifacts/auditoria_escritura/HistorialDiscucion/ronda_N/`.
- Nombre de archivos sugerido:
    - `01_auditor_critica_[tema].md`
    - `02_defensor_respuesta_[tema].md`
    - `03_auditor_replica_[tema].md`
    - `04_acuerdo_final_[tema].md`
- Las propuestas de reescritura deben ser explícitas (bloques de código o diffs).

**Archivo de turnos**
- Archivo simple para ver y actualizar el turno: `Artifacts/auditoria_escritura/turno.txt`.

**Perfiles**
- `Artifacts/auditoria_escritura/perfiles/auditor_escritura/perfil.md`
- `Artifacts/auditoria_escritura/perfiles/defensor_escritura/perfil.md`
