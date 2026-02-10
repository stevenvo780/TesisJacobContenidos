# Arquitectura de Modelos — Contaminación por Microplásticos

## Conceptual
- Hiperobjeto: acumulación global de microplásticos como proceso macro distribuido.
- Mecanismo: La producción masiva de plástico genera partículas micro que se acumulan en los ecosistemas (modelo Jambeck). El macro-proceso constriñe la dinámica local de contaminación en cada cuenca/región.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: M (índice global de concentración de microplásticos).
- Dinámica: `dM/dt = α*(F(t) - β*M) + noise`
  - Modelo específico: accumulation_decay (Jambeck).
  - Parámetros: α (tasa de ingreso, ~0.09), β (degradación, ~0.003 — muy lento).
- Modelo accumulation_decay: acumulación de microplásticos proporcional a la producción plástica menos degradación ambiental (extremadamente lenta).
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan regiones costeras/fluviales con concentración local de microplásticos, acopladas por difusión oceánica.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: M (índice global de concentración de microplásticos).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (accumulation_decay (Jambeck)).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: OWID (plastic waste) + World Bank (ER.H2O.INTR.K3 — recursos hídricos internos).
- Indicador: `OWID plastic waste + ER.H2O.INTR.K3`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: 0.426505 → Nivel 4.
- Overall pass: ✅ Sí.
