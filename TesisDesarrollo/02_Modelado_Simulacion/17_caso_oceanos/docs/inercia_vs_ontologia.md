# Argumento: Inercia Térmica vs. Emergencia Ontológica

## El problema

El océano presenta **inercia térmica**: un sistema con alta capacidad calorífica responde lentamente a perturbaciones externas (radiación, gases). Esto genera una objeción natural:

> ¿El EDI detecta una propiedad emergente real del hiperobjeto "Océano", o simplemente la persistencia mecánica de un sistema con baja difusividad térmica?

Si la inercia sola explica la estructura macro, el hiperobjeto "Océano calentándose" sería **epifenomenal**: el macro no añade nada que la física de transporte no contenga ya.

## Resolución: tres líneas de evidencia

### 1. La inercia no es gratuita ontológicamente

La inercia térmica oceánica es un **fenómeno de escala**: emerge de la distribución de masas de agua, termohalinas, circulación y estratificación. No es una constante física fundamental como la velocidad de la luz; es un **patrón macroscópico** que requiere:

- ≈ 1.335 × 10⁹ km³ de agua distribuidos en capas con gradientes térmicos
- Circulación meridional (AMOC) que redistribuye calor globalmente  
- Estratificación vertical que limita mezcla convectiva

La inercia **es** la propiedad emergente. El hecho de que sea "predecible" no la hace epifenomenal — la regularidad macro que reduce la entropía micro es exactamente lo que el EDI mide.

### 2. Criterio de ablación (EDI) va más allá de persistencia

El protocolo C1–C5 compara un modelo ABM con acoplamiento macro vs. sin acoplamiento:

| Modelo | Significado |
|--------|------------|
| ABM completo | Agentes locales + forzamiento + acoplamiento con estado macro global |
| ABM reducido | Mismos agentes, **sin** acoplamiento macro (macro_coupling=0, forcing_scale=0) |

Si la inercia fuera "todo lo que hay", el ABM reducido debería predecir igual de bien que el completo (la difusión local replica la inercia). Un **EDI > 0.30** demuestra que hay estructura macro que la difusión local sola no captura:

- La corrección del estado macro (ODE de temperatura) reduce el RMSE del ABM en >30%
- Esto implica que la distribución micro de celdas es **más informativa** cuando se condiciona al estado global

### 3. Distinción escala temporal: inercia ≠ persistencia ≠ emergencia

| Concepto | Definición | Medición |
|----------|-----------|----------|
| **Inercia** | Resistencia al cambio por capacidad calorífica | τ_relajación ~ 10-100 años |
| **Persistencia** | Autocorrelación temporal de la serie | C5: variance_ratio > 1.0 |
| **Emergencia** | Estructura macro que reduce incertidumbre micro | C2: EDI > 0.30 |

La inercia genera persistencia, pero **no toda persistencia implica emergencia**. Los casos de falsación (06, 07, 08) demuestran que un sistema con alta inercia pero sin estructura macro real produce EDI < 0.30.

## Criterio operativo

El argumento materialista es:

1. Si EDI < 0.30 a pesar de inercia → la inercia es reducible a física de transporte (caso epifenomenal)
2. Si EDI ∈ [0.30, 0.90] → la inercia es necesaria pero no suficiente; hay estructura macro irreducible
3. Si EDI > 0.90 → tautología (circularidad)

Para el caso 17 (Calentamiento Oceánico), el EDI empírico establece en qué régimen se encuentra. El **protocolo de ablación** es precisamente el mecanismo que distingue inercia-como-reducible de inercia-como-emergente.

## Nota sobre la navaja de Ockham

Por convención del marco teórico (§00_03): no se reclama emergencia si la inercia sola explica los datos. El EDI está diseñado como test conservador — la carga de la prueba recae en quien afirma la emergencia, no en quien la niega.

---

*Referencia cruzada*: Glosario §00_02 ("Epifenomenalismo", "Descendencia Causal"), Protocolo C2 (EDI), Caso 06 (Falsación por exogeneidad).
