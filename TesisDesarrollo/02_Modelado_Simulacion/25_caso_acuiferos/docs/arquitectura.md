# Arquitectura de Modelos — Agotamiento de Acuíferos

## Conceptual
- Hiperobjeto: agotamiento global de acuíferos como proceso macro distribuido.
- Mecanismo: La sobreexplotación de aguas subterráneas genera un descenso secular del nivel freático (proxy: Ogallala). El macro-proceso constriñe la disponibilidad hídrica local en cada celda/región.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: H (anomalía de almacenamiento hídrico subterráneo, GWSA).
- Dinámica: `dH/dt = α*(F(t) - β*H) + noise`
  - Modelo específico: accumulation_decay (aquifer_balance variant).
  - Parámetros: α (tasa de respuesta, ~0.08), β (equilibrio de extracción, ~0.03).
- Modelo accumulation_decay adaptado: el estado H representa el nivel del acuífero, con recarga (precipitación) menos extracción.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan parcelas de terreno sobre el acuífero, con nivel freático local acoplado por difusión lateral y forzado por macro.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: H (anomalía de almacenamiento hídrico subterráneo, GWSA).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (accumulation_decay (aquifer_balance variant)).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: World Bank: AG.LND.PRCP.MM (precipitación, USA) + ER.H2O.FWTL.ZS (extracción hídrica) — proxy GRACE/USGS Ogallala.
- Indicador: `AG.LND.PRCP.MM + ER.H2O.FWTL.ZS (USA)`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: -0.178754 → Nivel 0.
- Overall pass: ❌ No.
