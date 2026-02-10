# Arquitectura de Modelos — Erosión de Suelos (Dialéctica Institucional)

## Conceptual
- Hiperobjeto: erosión global de suelos como proceso macro con retroalimentación institucional.
- Mecanismo: La presión agrícola global degrada suelos, generando una retroalimentación dialéctica: la degradación intensifica la presión por más tierra, lo que acelera la erosión. El estado del macro-sistema constriñe las parcelas locales.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: X (índice global de erosión).
- Dinámica: `dX/dt = α*(F(t) - β*X) + 0.3*X*α + noise`
  - Modelo específico: mean_reversion + retroalimentación positiva.
  - Parámetros: α (tasa de respuesta, ~0.03), β (restauración, ~0.01), amplificación=0.3.
- Modelo mean_reversion con término de amplificación proporcional al estado (0.3*x): modela retroalimentación positiva institucional.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan parcelas de uso de suelo con índice de erosión, acopladas por difusión y forzadas por presión macro global.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: X (índice global de erosión).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (mean_reversion + retroalimentación positiva).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: Proxy sintético calibrado a datos FAO/GLASOD de degradación de suelos.
- Indicador: `Proxy: índice compuesto de degradación (synthetic_fallback)`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: -1.000000 → Nivel 0.
- Overall pass: ❌ No.
