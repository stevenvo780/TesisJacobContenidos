# Arquitectura de Modelos — Internet de las Cosas (IoT — Bass-Metcalfe)

## Conceptual
- Hiperobjeto: expansión global del IoT como proceso macro distribuido.
- Mecanismo: La adopción masiva de dispositivos IoT sigue un modelo Bass (difusión de innovación) amplificado por efectos de red Metcalfe. El macro-proceso de conectividad global constriñe la adopción local en cada región.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: N (índice compuesto de penetración IoT global).
- Dinámica: `dN/dt = α*(F(t) - β*N) + γ_net*F*N + noise`
  - Modelo específico: mean_reversion + efecto de red (Bass-Metcalfe).
  - Parámetros: α (~0.05), β (~0.02), γ_net (efecto de red Metcalfe).
- Modelo mean_reversion con término de efecto de red: dN/dt = α*(f - β*N) + γ_net*f*N, donde γ_net captura el efecto Metcalfe.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan regiones con densidad IoT local, acopladas por difusión de conectividad y forzadas por macro-adopción global.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: N (índice compuesto de penetración IoT global).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (mean_reversion + efecto de red (Bass-Metcalfe)).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: World Bank (multi-indicador): IT.NET.BBND.P2 (banda ancha fija), IT.CEL.SETS.P2 (suscripciones móviles), IT.NET.USER.ZS (uso de Internet), TX.VAL.TECH.MF.ZS (exportaciones high-tech), EG.ELC.ACCS.ZS (acceso eléctrico).
- Indicador: `IT.NET.BBND.P2 + IT.CEL.SETS.P2 + IT.NET.USER.ZS + TX.VAL.TECH.MF.ZS + EG.ELC.ACCS.ZS`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: 0.020387 → Nivel 2.
- Overall pass: ❌ No.
