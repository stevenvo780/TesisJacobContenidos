# Ejercicio Critico Gladiadores - Partida 1 (20 rondas)

**Proposito**
Consolidar de forma exhaustiva todo lo aprendido, discutido, probado y corregido durante el ejercicio Gladiadores (Partida 1). Este documento reemplaza notas dispersas y sirve como referencia unica para auditoria academica.

---

## 1. Contexto y reglas operativas

**Objetivo**
Evaluar la validez del marco ABM+ODE para sostener la Hipotesis H1 y sus criterios (EDI, C1-C5, CR) bajo debate adversarial con trazabilidad.

**Reglas de la dinamica**
- Turnos por equipos: defensor, critico, jueces.
- Los jueces moderan: exigen evidencia, detectan falacias y mantienen trazabilidad.
- Cada afirmacion tecnica debe apuntar a ruta/archivo/fase.
- Se prohiben ataques personales; cualquier imputacion requiere prueba documental.

**Estructura de partida**
- 20 rondas (R1-R20) con iteraciones y comentarios de jueces.
- Se habilito una “Resolucion Especial” por unificacion de repositorio (R18c): la defensa pudo corregir R18 con data completa y el critico rehacer su ataque.

---

## 2. Hallazgos tecnicos verificados

**Trazabilidad v8**
- `repos/Simulaciones/mega_run_v8_traceability.json` existe y contiene rutas/MD5/metrics por caso.
- La tabla de 29 casos genuinos vs 32 totales aparece en `TesisFinal/Tesis.md` y `TesisDesarrollo/02_Modelado_Simulacion/02_Modelado_Simulacion.md`.

**Consistencia de EDI en tablas**
- `repos/scripts/verificar_consistencia.py` reporta consistencia de EDI entre tablas y `metrics.json`, con advertencias por rutas legacy.

**Resultados cuantitativos centrales**
- 32 casos ejecutados: 29 genuinos + 3 falsaciones.
- 24/29 genuinos validados (83%), 5 genuinos rechazados.
- 3 controles de falsacion correctamente rechazados.

**Dominance share**
- En validados: ~0.0025 (1/400) indica influencia uniforme (no-localidad fuerte).
- En falsacion 07: dominance_share mayor (0.00264), indicando heterogeneidad.

**Forcing scale**
- En outputs oficiales del repositorio unificado: forcing_scale <= 0.99 por A6.
- Los valores discrepantes detectados pertenecian a repositorios legacy/no unificados.

---

## 3. Cambios doctrinales y correcciones documentales

**CR (Cohesion Ratio)**
- Se reclasifico CR como **indicador complementario**, no condicion de H1.
- Actualizado en: `TesisFinal/Tesis.md`, `TesisDesarrollo/00_Marco_Conceptual/00_00_Marco_Conceptual.md`, `02_Modelado_Simulacion.md`, `03_Validacion_Praxis.md`.

**H1 (definicion operativa)**
- H1 queda: **EDI > 0.30 + C1–C5** como criterio operativo.
- EDI definido por ablacion ABM completo vs ABM reducido.

**EI (Effective Information)**
- Bug EI=0.0 detectado y corregido (C5).
- EI queda como indicador complementario, no criterio de rechazo.

---

## 4. Controversias resueltas

**Gating sintetico**
- C2–C4 gatean fase real; C1 sintetico puede fallar sin invalidar real.
- Documentado en `hybrid_validator.py` (gating explicitado).

**ODE no actua sobre ABM**
- ABM y ODE se simulan por separado; ODE es benchmark, no driver.
- EDI compara ABM completo vs reducido (sin ODE).

**Tautologia del macro_coupling**
- Refutada por casos con mc alto y EDI bajo/negativo (Wikipedia, falsaciones).
- Ablacion muestra degradacion fuerte en validados y baja en rechazados.

---

## 5. Controversias no resueltas

**Emergencia espacial / fronteras**
- CR ≈ 1.0 en la mayoria; no se prueba frontera nítida.
- Arquitectura isotropica homogeniza; falta topologia heterogenea.

**Reproducibilidad total**
- Persisten rutas legacy (`caso_clima` vs `01_caso_clima`).
- Se requiere replay completo con hashes y outputs en git.

**Ontologia fuerte vs operativa**
- El marco prueba constriccion macro efectiva, no ontologia fuerte.
- Debe aclararse el alcance: realismo operativo debil.

---

## 6. Errores repetitivos detectados (R1-R20)

**Del critico**
- Afirmaciones sin trazabilidad.
- Circularidad: repetir ataques sin evidencia nueva.
- Confusion de fuentes (outputs vs copias en TesisDesarrollo).
- Lenguaje descalificatorio sin pruebas.

**De la defensa**
- Afirmaciones cuantitativas sin extractos.
- Cambios doctrinales comunicados sin actualizar todos los documentos.
- Outputs no versionados en etapas intermedias.

---

## 7. Veredictos del tribunal (sintesis)

**Juez de Complejidad**
- Validez muy condicionada: evidencia temporal, no espacial.

**Juez de Filosofia de la Ciencia**
- Aceptacion solo bajo realismo operativo debil.

**Juez de Modelado/Validacion**
- Reproducibilidad parcial; requiere replay total.

**Dictamen final**
- Aprobacion muy condicionada. La tesis es aceptable como marco operacional, no como ontologia fuerte.

---

## 8. Condiciones obligatorias para cierre academico

1. Replay total reproducible (todas las simulaciones) con logs y hashes.
2. Eliminacion de rutas legacy y unificacion de nomenclatura.
3. Consistencia documental completa en TesisFinal y TesisDesarrollo.
4. Declaracion ontologica explicita: constriccion macro efectiva, no ontologia fuerte.

---

## 9. Estado final de la partida

- Partida 1 completada con 20 rondas.
- Dictamen final emitido y registrado.
- Toda la evidencia, correcciones y trazabilidad consolidadas en esta carpeta.

