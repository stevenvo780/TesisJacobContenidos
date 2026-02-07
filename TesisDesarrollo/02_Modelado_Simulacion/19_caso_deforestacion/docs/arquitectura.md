# Arquitectura de Modelos — Deforestacion Global

## Conceptual
- Hiperobjeto: deforestacion global como proceso macro distribuido.
- Mecanismo: politicas macro (internacionales, nacionales) constriñen decisiones
  locales de uso de suelo, generando una tendencia secular de declive.
- Delimitacion: frontera funcional basada en cohesion interna vs externa.
- La deforestacion actua como atractor macro sobre la dinamica micro de parcelas.

## Formal

### Capa macro (ODE)
- Estado macro: cobertura forestal media global `D_bar`.
- Dinamica: `dD/dt = alpha * (F(t) - beta * D) + noise`
  - `F(t)`: forcing exogeno (presion demografica, politicas ambientales).
  - `alpha`: tasa de respuesta del sistema.
  - `beta`: coeficiente de restauracion/degradacion.
- Asimilacion de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Agentes: celdas en grilla NxN representando parcelas de uso de suelo.
- Estado por celda: indice de cobertura forestal `d_i`.
- Regla de actualizacion por celda por paso:
  1. Difusion espacial (vecinos 4-conectados).
  2. Forcing externo (presion de deforestacion).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocastico.

### Acoplamiento
- Variable puente: `D_bar` acopla macro → micro; media micro → macro.
- Parametro clave: `macro_coupling` controla la intensidad del acople.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta tipo balance agregado.
- Simulacion: pasos discretos con semillas controladas.
- Fuente de datos: World Bank API — `AG.LND.FRST.ZS` (1990–2022).

## Validacion
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Metricas: EDI, CR, EI, RMSE, correlacion (ver `indicadores_metricas.md`).
- Umbrales de rechazo: EDI < 0.30 o EDI > 0.90 → RECHAZO.
