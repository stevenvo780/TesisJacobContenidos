# Iteración 15 — Equipo Jueces — Comentarios al Crítico (Rondas 1–15)

## ✅ Verificable vs. documentación (R15)
- En `TesisDesarrollo/02_Modelado_Simulacion/01_caso_clima/metrics.json` (fase real) se observa:
  - `correlations.abm_obs = 0.8218` y `correlations.ode_obs = -0.0266`
  - `forcing_scale = 1.494`
  Esto **sostiene parcialmente** la observación del crítico sobre la ODE en Clima, pero requiere análisis técnico, no descalificatorio.

## ⚠️ Patrones circulares detectados (R1–R15)
1. **Afirmaciones sin trazabilidad** repetidas: múltiples rondas citan valores/experimentos sin rutas, extractos o scripts verificables.
2. **Objetivo móvil (moving target)**: se exige CR como condición necesaria pese a que el marco lo define como indicador; cuando se corrige, se cambia el criterio sin enmienda documental.
3. **Acusaciones personales** (“fraude”, “mentira”, “voodú”) sin evidencia documental completa.
4. **Reciclaje de ataques** (gating, forcing>1.0, timestamps) sin nuevas pruebas o propuesta metodológica concreta.
5. **Sesgo de fase**: se citan valores sintéticos o reales de forma parcial sin reportar ambas fases.

## ✅ Mejores aportes del crítico (para conservar)
- Señalar discrepancias reales en correlaciones (Clima) y tensionar el rol de la ODE.
- Proponer un criterio alternativo (NC1), aunque debe integrarse formalmente con C1–C5.

## 🔎 Exigencias de mejora para próximas críticas
1. **Evidencia con rutas y extractos**: cada cifra debe venir con `metrics.json` y fase.
2. **Evitar ataques personales**: formular en términos verificables.
3. **Proponer alternativas concretas**: si se impugna C1 o gating, proponer regla nueva compatible con protocolo.
4. **No circularidad**: no repetir el mismo ataque sin evidencia nueva o refutación formal del diseño.

**Conteo de falacias/problemas argumentativos (esta intervención):**
- Equipo crítico: 1 (lenguaje descalificatorio).
- Equipo defensor: 0.

**Solicitud explícita:** concentrarse en puntos técnicos claros y verificables; dejar de atacar por atacar.
