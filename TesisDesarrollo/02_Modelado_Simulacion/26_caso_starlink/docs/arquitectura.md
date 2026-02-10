# Arquitectura de Modelos — Mega-constelaciones Satelitales (Starlink)

## Conceptual
- Hiperobjeto: proliferación de mega-constelaciones satelitales como proceso macro.
- Mecanismo: El despliegue masivo de satélites (Starlink et al.) crea un macro-fenómeno que afecta la dinámica orbital local, la astronomía y el entorno de LEO.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: N (número total de satélites operativos).
- Dinámica: `dN/dt = α*(F(t) - β*N) + noise`
  - Modelo específico: accumulation_decay.
  - Parámetros: α (tasa de despliegue, ~0.18), β (decaimiento orbital, ~0.015).
- Modelo accumulation_decay: acumulación de satélites proporcional a la tasa de lanzamiento menos el decaimiento orbital.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas en grilla 25×25 representan regiones orbitales con densidad satelital local, acopladas por difusión y forzadas por macro-despliegue.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: N (número total de satélites operativos).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (accumulation_decay).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: Datos públicos de despliegue Starlink (satélites operativos mensuales).
- Indicador: `Conteo mensual de satélites Starlink operativos (cache local)`.

## Nota numérica
Serie con 352/385 valores en cero (Starlink no existía antes de 2019). La ventana de validación está dominada por ceros, lo que genera RMSE_no_ode ≈ 0 y EDI = -1.0 (artefacto de datos, no error del modelo). El caso demuestra correctamente que la sonda no detecta clausura operativa.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: -1.000000 → Nivel 0.
- Overall pass: ❌ No.
