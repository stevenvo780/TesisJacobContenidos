# Arquitectura de Modelos — Ciclo del Fósforo

## Conceptual
- Hiperobjeto: alteración global del ciclo biogeoquímico del fósforo.
- Mecanismo: El uso masivo de fertilizantes fosfatados altera los flujos biogeoquímicos globales del fósforo, generando eutrofización y zonas muertas como efecto macro distribuido.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: P (carga global de fósforo reactivo).
- Dinámica: `dP/dt = α*(F(t) - β*P) + noise`
  - Modelo específico: accumulation_decay.
  - Parámetros: α (tasa de acumulación, ~0.07), β (secuestro, ~0.02).
- Modelo accumulation_decay: acumulación de fósforo reactivo proporcional al consumo de fertilizantes menos el secuestro sedimentario.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas representan cuencas hidrográficas con carga de fósforo local, acopladas por difusión fluvial y forzadas por aplicación global.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: P (carga global de fósforo reactivo).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (accumulation_decay).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: World Bank — AG.CON.FERT.ZS (consumo de fertilizantes, kg/ha).
- Indicador: `AG.CON.FERT.ZS (Fertilizer consumption kg/ha of arable land)`.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: -1.000000 → Nivel 0.
- Overall pass: ❌ No.
