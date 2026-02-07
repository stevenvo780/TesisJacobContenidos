# Arquitectura de Modelos — Urbanizacion Global

## Conceptual
- Hiperobjeto: urbanizacion global como atractor macro que constriñe patrones
  de migracion a escala local.
- Mecanismo: la tendencia secular de urbanizacion genera un forcing descendente
  sobre las decisiones individuales de migracion rural-urbana.
- Delimitacion: frontera funcional basada en cohesion interna vs externa.
- Señal extremadamente suave — caso ideal de hiperobjeto.

## Formal

### Capa macro (ODE)
- Estado macro: porcentaje de poblacion urbana media global `U_bar`.
- Dinamica: `dU/dt = alpha * (F(t) - beta * U) + noise`
  - `F(t)`: forcing exogeno (industrializacion, infraestructura, politicas).
  - `alpha`: tasa de respuesta del sistema.
  - `beta`: coeficiente de saturacion urbana.
- Asimilacion de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Agentes: celdas en grilla NxN representando regiones/localidades.
- Estado por celda: indice de urbanizacion `u_i`.
- Regla de actualizacion por celda por paso:
  1. Difusion espacial (vecinos 4-conectados).
  2. Forcing externo (atraccion urbana).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocastico.

### Acoplamiento
- Variable puente: `U_bar` acopla macro → micro; media micro → macro.
- Parametro clave: `macro_coupling` controla la intensidad del acople.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta tipo balance agregado.
- Simulacion: pasos discretos con semillas controladas.
- Fuente de datos: World Bank API — `SP.URB.TOTL.IN.ZS` (1960–2022).

## Validacion
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Metricas: EDI, CR, EI, RMSE, correlacion (ver `indicadores_metricas.md`).
- Umbrales de rechazo: EDI < 0.30 o EDI > 0.90 → RECHAZO.
