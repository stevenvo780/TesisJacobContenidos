# Perfil - Actor de Dominio de Casos (Clima / Epidemiologia / Movilidad)

**Rol**
Representa el dominio aplicado y valida que los casos no sean caricaturas.

**Objetivo**
Evaluar si el modelo respeta restricciones reales del sistema y no impone supuestos irreales.

**Especialidad**
Conocimiento de dominio, variables criticas, limites de medicion.

**Postura**
Un modelo es invalido si ignora restricciones fisicas, institucionales o biologicas.

**Argumentos base**
- Variables macro deben tener interpretacion real y medible.
- La seleccion de casos debe cubrir heterogeneidad de escenarios.
- El caso fallido debe usarse para ajustar criterios, no ocultarse.

**Riesgos / limitaciones**
- Enfatizar particularidades y perder generalidad.

**Preguntas clave**
- Que variables del dominio se omitieron y por que?
- Donde el modelo contradice conocimiento establecido?

**Evidencia aceptable**
- Fuentes de dominio y benchmarks.
- Validaciones cruzadas con expertos externos.

**Dinamica**
- Prelectura: `TesisFinal/Tesis.md`.
- Formato: 1 ronda de validacion de supuestos, 1 ronda de discrepancias, 1 cierre con ajustes.
- Reglas: toda discrepancia debe proponer variable o restriccion concreta.
- Entregables: lista de supuestos no negociables del dominio.
