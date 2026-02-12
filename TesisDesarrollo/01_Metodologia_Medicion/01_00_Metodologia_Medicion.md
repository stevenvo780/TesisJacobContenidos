# 01 Metodología de Medición

## El Emergentómetro en la Práctica

El sistema de medición de esta tesis — que llamamos **Emergentómetro** — opera como cualquier instrumento científico: tiene un protocolo de uso, métricas estandarizadas y condiciones de rechazo. La diferencia es que no mide temperatura o voltaje, sino *cuánta emergencia operativa* exhibe un fenómeno de gran escala.

En términos intuitivos: el Emergentómetro toma un fenómeno complejo (como la deforestación global), construye dos modelos — uno que incluye la "visión de conjunto" (macro) y otro que solo mira los componentes individuales (micro) — y mide cuánto empeora la predicción cuando eliminamos la visión de conjunto. Si empeora mucho y de forma robusta (protocolo C1-C5), el fenómeno tiene cierre operativo alto.

## Protocolo de Rigor (C1-C5)

El Emergentómetro exige que cada medición supere cinco filtros de calidad:

1. **C1 Convergencia:** El modelo completo (ABM+ODE) debe predecir mejor que el modelo reducido (ABM solo) en datos reales. Si no mejora, no hay señal.

2. **C2 Robustez:** La mejora debe mantenerse aunque variemos los parámetros. Si pequeños cambios destruyen la señal, la medición es inestable.

3. **C3 Determinismo aleatorio:** Semillas fijas (seed=42) para garantizar que cualquier investigador obtenga exactamente los mismos resultados.

4. **C4 Linter de realidad:** Los resultados deben ser coherentes con las leyes del dominio (no violar física básica, economía elemental, etc.).

5. **C5 Reporte de fallos:** Sensibilidad y límites explicitados. El instrumento debe reportar honestamente qué no pudo medir.

```mermaid
flowchart LR
    C1[C1: Convergencia] --> C2[C2: Robustez]
    C2 --> C3[C3: Replicabilidad]
    C3 --> C4[C4: Validez]
    C4 --> C5[C5: Incertidumbre]
    C5 --> Pass{¿Todo OK?}
    Pass -->|Sí| Valid[Nivel 4: Objeto Operativo]
    Pass -->|No| Reject[Clasificación Nivel 0-3]

    style C1 fill:#e1f5fe,stroke:#01579b
    style C2 fill:#e1f5fe,stroke:#01579b
    style C3 fill:#e1f5fe,stroke:#01579b
    style C4 fill:#e1f5fe,stroke:#01579b
    style C5 fill:#e1f5fe,stroke:#01579b
    style Pass fill:#fff9c4,stroke:#fbc02d
    style Valid fill:#c8e6c9,stroke:#2e7d32,stroke-width:3px
    style Reject fill:#ffebee,stroke:#c62828
```

Estos criterios surgen de auditorías internas y responden a la tradición de rigor metodológico de Popper (1959) — falsabilidad como condición demarcatoria — y Lakatos (1978) — programas de investigación que toleran anomalías mientras el núcleo progrese. La metodología no se justifica por resultados favorables, sino por su capacidad para discriminar fenómenos de forma explícita y reproducible.

## Pipeline de Validación
Observación → Simulación → Clasificación. El Emergentómetro asigna un grado de cierre operativo (EDI) que posiciona al fenómeno en el paisaje de emergencia. El pipeline no "valida" o "invalida" — **clasifica** en un gradiente.

```mermaid
stateDiagram-v2
    [*] --> Datos: WorldBank, OWID, etc.
    Datos --> Sintetico: Fase de Calibración
    Sintetico --> Real: Fase de Validación (Zero-Nudging)
    Real --> Protocolo: C1-C5 + EDI
    Protocolo --> Clasificacion: Nivel 0-4
    Clasificacion --> [*]
```

## Métricas y su Interpretación bajo Irrealismo Operativo

### EDI (Effective Dependence Index) — "El termómetro de emergencia"
El EDI mide el **grado de cierre operativo** de un fenómeno. No mide "existencia" ni "realidad" del hiperobjeto — mide cuánta información predictiva se pierde al eliminar la constricción macro.

En lenguaje accesible: imagine que tiene dos médicos — uno que ve al paciente completo (historial, síntomas, contexto) y otro que solo ve análisis de sangre aislados. El EDI mide cuánto peor diagnostica el segundo. Si el EDI es 0.38, el médico sin visión de conjunto se equivoca un 38% más.

- **Interpretación técnica:** Un EDI de 0.579 (Deforestación) significa que eliminar el constructo macro degrada la predicción en 57.9%. Esto es una medición operativa, no una afirmación ontológica.
- **Ablación como intervención:** Siguiendo a Woodward (2003), la manipulación de `forcing_scale=0` es una intervención controlada. El efecto medido (degradación del EDI) establece la indispensabilidad operativa del constructo macro, no su "realidad causal" en sentido metafísico.

### Regla de Descuento por Nivel de Evidencia (LoE)
Para evitar la sobreinterpretación de constructos con datos débiles, el EDI se pondera por la calidad epistémica de los datos:
$$EDI_{ponderado} = EDI \times \frac{LoE}{5}$$
Esto penaliza fenómenos con datos indirectos (ej. Conciencia, LoE=1) frente a sistemas con datos físicos robustos (ej. Clima, LoE=5).

## Niveles de Evidencia (LoE)
1. **LoE 1 (Especulativo):** Proxies indirectos, encuestas subjetivas, o datos sintéticos sin ground truth físico.
2. **LoE 2 (Débil):** Datos digitales traza con alto ruido semántico.
3. **LoE 3 (Medio):** Datos estructurados pero incompletos o de corto plazo (< 5 años).
4. **LoE 4 (Fuerte):** Series temporales consistentes, múltiples fuentes, > 10 años.
5. **LoE 5 (Robusto):** Datos físicos directos (sensores), estandarizados internacionalmente, > 30 años.

## Reglas de Clasificación
Los umbrales **clasifican** fenómenos en el gradiente de emergencia:

1. **EDI < 0.01:** Sin señal detectable → Nivel 0 (null)
2. **EDI > 0.01, p < 0.05:** Señal sugestiva → Nivel 2
3. **0.10 ≤ EDI < 0.30, p < 0.05:** Componente funcional → Nivel 3 (weak)
4. **EDI ≥ 0.30, overall_pass=True:** Objeto operativo → Nivel 4 (strong)
5. **Coupling < 0.10:** Epifenomenalismo — señal espuria sin acoplamiento → flag
6. **RMSE < 1e-10:** Fraude por sobreajuste → flag
7. **EDI > 0.90:** Flag de tautología — revisión manual
8. **forcing_scale ≥ 1.0:** Cap en calibración — dominancia exógena
9. **C1-C5 protocolo completo:** Condición necesaria para Nivel 4

La clasificación de 6 categorías (strong, weak, suggestive, trend, null, falsification) es el **resultado principal** del Emergentómetro, no un filtro binario.

## EI (Información Efectiva) — Indicador Complementario
La EI (Hoel, 2017), fundamentada en la teoría de la información de Shannon (1948), mide la ganancia informacional teórica del nivel macro. Opera como indicador de calidad informacional, no como condición de clasificación. En sistemas con ruido no-gaussiano, la EI puede ser transitoriamente negativa sin invalidar el grado de cierre operativo medido por EDI.

## Reproducibilidad
- Hashing de datasets.
- Semillas fijas (seed=42 global).
- 999 permutaciones para significancia estadística.
- Entornos replicables.

La reproducibilidad es requisito epistémico: sin ella, el gradiente de cierre operativo no es verificable.

## Validez y Límites
- Riesgo de sobreinterpretación mitigado por irrealismo: nunca afirmamos "es" un hiperobjeto.
- Aliasing temporal: resolución insuficiente puede clasificar fenómenos en nivel incorrecto.
- Clasificación de datos por dureza (LoE) evita confundir evidencia empírica con prospectiva.

## Datos e Instrumentos
Python, numpy, pandas, math. La asimilación de datos sigue principios del filtro de Kalman por ensambles (Evensen, 2009), adaptados a nuestra arquitectura híbrida con zero-nudging en evaluación. Fuentes: World Bank, Meteostat, Yahoo Finance, OWID, OPSD, Wikimedia, CelesTrak (según caso). Todos los datasets cacheados en CSV local.

## Gobernanza de Datos
Filtro de nulos, normalización, uso exclusivo de datos abiertos. La gobernanza se incorpora como condición de reproducibilidad: si la calidad de datos no cumple criterios (LoE), se ajusta la interpretación del EDI, no se fuerza el resultado.

## Casos Piloto
Clima sintético, Finanzas sintéticas, y caso clima regional como MVP metodológico. Los pilotos prueban el pipeline antes de clasificar fenómenos en el paisaje de emergencia.

## Síntesis
El Emergentómetro clasifica fenómenos en un gradiente de cierre operativo. La metodología se valida por la diversidad de sus resultados (8 null, 4 trend, 3 suggestive, 6 weak, 5 strong, 3 controles de falsación) y por la coherencia del gradiente con las propiedades de los dominios evaluados.
