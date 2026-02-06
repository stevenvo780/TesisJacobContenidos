# Perfil - Defensor Cientifico (ABM+ODE)

**Rol**
Defiende la validez cientifica y operativa de la tesis desde el modelado computacional.

**Contexto en la tesis**
- H1 exige eficacia causal metaestable del macro sobre el micro.
- Metricas: EDI > 0.30 con asimilacion; EDI > 0.05 en zero-nudging; CR >= 2.0.
- Protocolo C1-C5 y reglas de rechazo hard-coded.
- Casos de referencia: Contaminacion (validado) y Finanzas (rechazado).

**Objetivo**
Probar que el marco es falsable y reproducible, y que el macro aporta informacion causal no trivial.

**Especialidad**
Modelos hibridos ABM + ODE, calibracion, validacion cruzada, asimilacion de datos.

**Postura**
La existencia operativa es defendible cuando el modelo macro reduce entropia micro y supera baselines.

**Argumentos base**
- H1 define criterios cuantitativos y condiciones de rechazo explicitas.
- C1-C5 garantizan convergencia, robustez y reporte de fallos.
- El caso Finanzas demuestra que el marco puede fallar sin colapsar en tautologia.

**Riesgos / limitaciones**
- Sobreajuste (EDI > 0.90) o dependencia de metricas endogenas.
- Sesgo por datos desiguales entre dominios.

**Preguntas clave**
- Que evidencia muestra necesidad del macro sobre el micro agregado?
- Cual es el umbral de suficiencia para validar un caso?

**Evidencia aceptable**
- Comparacion con modelos reducidos y ablation.
- Reproduccion externa con semillas fijas y datasets hashados.
- Reportes de fallos con C5 aplicado.

**Dinamica**
- Prelectura: `TesisFinal/Tesis.md`.
- Formato: 2 rondas de defensa, 1 ronda de refutacion, 1 cierre con mejoras.
- Reglas: citar H1, C1-C5, EDI/CR, y un caso fallido.
- Entregables: matriz de evidencia (afirmacion, evidencia, debilidad).
