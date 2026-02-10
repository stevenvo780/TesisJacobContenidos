# Arquitectura de Modelos — Fuga de Cerebros (Brain Drain)

## Conceptual
- Hiperobjeto: fuga de cerebros global como proceso macro distribuido.
- Mecanismo: La concentración de oportunidades en economías desarrolladas genera flujos migratorios de capital humano que empobrecen las periferias, creando un macro-proceso de acumulación desigual que constriñe la dinámica local.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: H (índice compuesto de capital humano global).
- Dinámica: `dH/dt = α*(F(t) - β*H) + noise`
  - Modelo específico: accumulation_decay (capital humano).
  - Parámetros: α (~0.06, acumulación capital humano), β (~0.02, tasa de fuga).
- Modelo de acumulación de capital humano: dH/dt = α*(f - β*H) + noise, con α~6%/año (formación) y β~2%/año (emigración).
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas en grilla 25×25 representan regiones con capital humano local, acopladas por difusión migratoria y forzadas por macro-concentración.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: H (índice compuesto de capital humano global).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (accumulation_decay (capital humano)).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: World Bank (multi-indicador): SE.XPD.TOTL.GD.ZS (gasto educativo), SM.POP.NETM (migración neta), IP.PAT.RESD (patentes residentes), SE.TER.ENRR (matrícula terciaria), SP.POP.SCIE.RD.P6 (investigadores/millón).
- Indicador: `SE.XPD.TOTL.GD.ZS + SM.POP.NETM + IP.PAT.RESD + SE.TER.ENRR + SP.POP.SCIE.RD.P6`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: 0.182896 → Nivel 3.
- Overall pass: ❌ No.
