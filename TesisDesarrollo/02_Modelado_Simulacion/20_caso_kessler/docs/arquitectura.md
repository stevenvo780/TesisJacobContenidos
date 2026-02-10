# Arquitectura de Modelos — Síndrome de Kessler (Basura Espacial)

## Conceptual
- Hiperobjeto: cascada colisional de basura espacial como proceso macro distribuido.
- Mecanismo: La acumulación de objetos en órbita terrestre baja (LEO) genera colisiones que producen fragmentos adicionales, creando un bucle de retroalimentación positiva (síndrome de Kessler) que constriñe la dinámica orbital local.
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: N (número total de objetos orbitales rastreables).
- Dinámica: `dN/dt = L + α*N² - β*N`
  - Modelo específico: kessler_liou (cuadrático).
  - Parámetros: L (tasa de lanzamiento), α (coeficiente colisional ~2e-10), β (decaimiento atmosférico ~0.02).
- Modelo de Kessler-Liou con término cuadrático de colisión: dN/dt = L + α*N² - β*N, donde el término cuadrático captura la cascada colisional.
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- Celdas en grilla 25×25 representan regiones orbitales, con difusión de fragmentos entre sectores y acoplamiento macro hacia densidad global.
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: N (número total de objetos orbitales rastreables).
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta (kessler_liou (cuadrático)).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: ESA Space Debris Office / NASA Orbital Debris Program (catálogo público).
- Indicador: `Conteo total de objetos rastreables en LEO (1960-2023)`.

## Nota sobre transformación
- Se aplica `log_transform=True` debido a la escala exponencial de los datos.

## Nota numérica
Escala exponencial (60 → 40,500 objetos). Se aplica log_transform=True para estabilizar la calibración. El RMSE alto en escala absoluta refleja la magnitud del fenómeno, no un error del modelo.

## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: -0.420251 → Nivel 0.
- Overall pass: ❌ No.
