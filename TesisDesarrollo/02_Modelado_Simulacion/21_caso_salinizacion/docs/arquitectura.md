# Arquitectura de Modelos — Salinización de Suelos

## Conceptual
- Hiperobjeto: salinización global de suelos agrícolas como proceso macro distribuido.
- Mecanismo: La irrigación intensiva y la extracción de agua subterránea elevan la concentración salina de los suelos agrícolas, un proceso macro que constriñe la productividad local.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: S (índice de salinización global).
- Dinámica: `dS/dt = α*(F(t) - β*S) + noise`
  - Modelo específico: accumulation_decay.
  - Parámetros: α (tasa de salinización, ~0.05), β (lixiviación natural, ~0.015), ode_inflow=0.05, ode_decay=0.015.
- Modelo accumulation_decay: acumulación salina proporcional a la irrigación menos disipación natural.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan parcelas agrícolas con concentración salina local, acopladas por difusión lateral y forzadas por macro-salinización.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: S (índice de salinización global).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (accumulation_decay).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: World Bank — AG.LND.IRIG.AG.ZS (irrigated land %) + ER.H2O.FWTL.ZS (freshwater withdrawal).
- Indicador: `AG.LND.IRIG.AG.ZS (% tierras bajo riego)`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: 0.026546 → Nivel 1.
- Overall pass: ❌ No.
