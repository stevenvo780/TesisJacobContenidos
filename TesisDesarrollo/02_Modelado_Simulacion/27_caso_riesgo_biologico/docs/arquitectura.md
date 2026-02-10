# Arquitectura de Modelos — Riesgo Biológico Global

## Conceptual
- Hiperobjeto: riesgo biológico global (bioseguridad) como proceso macro distribuido.
- Mecanismo: La combinación de urbanización, deforestación y comercio global incrementa el riesgo de eventos biológicos (pandemias, zoonosis). El macro-proceso constriñe la vulnerabilidad local de cada región.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: R (índice global de riesgo biológico).
- Dinámica: `dR/dt = α*(F(t) - β*R) + γ_bio*F*R + noise`
  - Modelo específico: mean_reversion + amplificación biológica.
  - Parámetros: α (~0.05), β (~0.02), γ_bio (amplificación biológica).
- Modelo mean_reversion con término de amplificación biológica: dR/dt = α*(f - β*R) + γ_bio*f*R, donde el término γ_bio captura la retroalimentación riesgo-exposición.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan regiones con índice de riesgo biológico local, acopladas por difusión (conectividad global) y forzadas por macro-riesgo.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: R (índice global de riesgo biológico).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (mean_reversion + amplificación biológica).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: Proxy compuesto: indicadores World Bank de salud + urbanización + deforestación.
- Indicador: `Proxy compuesto multi-indicador (synthetic_fallback → cache)`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: 0.105111 → Nivel 1.
- Overall pass: ❌ No.
