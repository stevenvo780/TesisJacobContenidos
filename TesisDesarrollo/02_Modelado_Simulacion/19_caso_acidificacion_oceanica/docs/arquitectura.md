# Arquitectura de Modelos — Acidificación Oceánica

## Conceptual
- Hiperobjeto: acidificación oceánica global como proceso macro distribuido.
- Mecanismo: Las emisiones antropogénicas de CO₂ incrementan la pCO₂ atmosférica, que se disuelve en los océanos alterando el equilibrio carbonato-bicarbonato y reduciendo el pH marino a escala global.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: pH medio oceánico global.
- Dinámica: `dX/dt = α*(F(t) - β*X) + revelle_correction + noise`
  - Modelo específico: revelle_factor + mean_reversion.
  - Parámetros: α (tasa de absorción), β (buffer carbonato), factor de Revelle.
- Modelo basado en el factor de Revelle: captura la respuesta no-lineal del sistema carbonato oceánico a la absorción de CO₂.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan parcelas oceánicas con pH local, acopladas por difusión y forzadas por gradiente de pCO₂.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: pH medio oceánico global.
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (revelle_factor + mean_reversion).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: World Bank (proxy CO₂ emissions) + calibración SOCAT/GLODAPv2.
- Indicador: `EN.ATM.CO2E.PC (CO₂ per capita)`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: -0.000008 → Nivel 0.
- Overall pass: ❌ No.
