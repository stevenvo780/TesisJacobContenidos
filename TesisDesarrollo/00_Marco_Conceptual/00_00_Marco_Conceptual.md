# 00 Marco Conceptual — Narrativa Unificada

## Proposito
Esta tesis define una ontologia operativa para hiperobjetos: entidades masivamente distribuidas cuya dinamica macro impone restricciones causales sobre lo micro. El criterio de realidad es computacional: si la capa macro es necesaria para reducir incertidumbre y mejorar la prediccion, entonces esa entidad es tratable como real dentro del marco.

## Postura Filosofica y Debate Fundacional
La tesis adopta un **realismo inferencial**: no exigimos observacion directa del hiperobjeto, sino convergencia de evidencia causal y poder explicativo. Esta postura surge de un debate realismo vs instrumentalismo: si los hiperobjetos fueran solo herramientas utiles, el marco perderia su ambicion ontologica. En cambio, el realismo inferencial permite sostener existencia operativa, siempre que haya trazabilidad y falsabilidad.

El debate **emergencia vs reduccionismo** queda resuelto en favor de un **emergentismo fuerte** operativo: la emergencia no se define por misterio, sino por la necesidad demostrable de un parametro macro para explicar y estabilizar el comportamiento micro. Esta eleccion se protege contra reificacion mediante criterios de validacion estrictos (EDI, CR, C1–C5).

La **causalidad descendente** se formula en version debil: lo macro restringe, no introduce fuerzas nuevas. Esto evita contradicciones con el cierre causal y permite formalizar el efecto macro como restricciones y nudging computacional.

## Hipótesis Central (H1)
Un **Hiperobjeto** es ontológicamente real si y solo si su modelo macroscópico (ODE) demuestra una **Eficacia Causal Metaestable** sobre sus componentes microscópicos (ABM). 

Esta eficacia se formaliza mediante una condición principal y un indicador complementario:
1.  **Condición Principal — Autonomía de Atractor:** El sistema debe mantener una reducción de incertidumbre microscópica significativa (**EDI > 0.30**) bajo condiciones de **Acoplamiento Mínimo** (Zero-Nudging), demostrando la realidad ontológica del atractor macro. Esta es la condición necesaria y suficiente para H1, junto con el protocolo C1-C5.
2.  **Indicador Complementario — Información Efectiva (EI):** El sistema acoplado idealmente posee una **Información Efectiva (EI)** positiva ($EI_{macro} > EI_{micro\_agg}$), demostrando que el nivel macro es causalmente más informativo que la suma de sus partes. La EI opera como indicador de calidad informacional, no como condición de rechazo. En sistemas socio-técnicos con ruido no-gaussiano, la EI puede ser transitoriamente negativa sin invalidar la emergencia (Hoel, 2017, § Limitaciones). El EDI mide la **eficacia causal operativa**; la EI mide la **ganancia informacional teórica**. Ambos son complementarios, pero solo el EDI define H1.

---

## Presupuestos Filosoficos
- **P1 Realismo de Sistemas (Bunge):** los sistemas macro poseen propiedades sistémicas reales, no meros agregados descriptivos.
- **P2 Symploke (Bueno):** no todo esta conectado con todo, pero nada esta aislado; la realidad se evalúa como una red con limites funcionales.
- **P3 Materialismo Emergentista:** las propiedades macro emergen de interacciones y persisten como patrones causales.

## Axiomas Operativos del Modelado Hibrido
- **A1 Incompletitud del nivel unico:** ABM u ODE por separado suelen ser insuficientes para capturar la complejidad del hiperobjeto.
- **A2 Primacia del parametro de orden:** el macro estabiliza y restringe al micro.
- **A3 Invarianza estructural (C3):** el mecanismo macro-micro debe mostrar estabilidad ante condiciones iniciales distintas.
- **A4 Falsabilidad por saturación:** si EDI < 0.30 (con asimilación) o EDI < 0.05 (en autonomía pura/zero-nudging), la capa macro se descarta. Este umbral representa la "Ventaja de Hoel": el punto donde la descripción macro es causalmente más informativa que la micro, superando el ruido estocástico del nivel basal.
- **A5 Clausura computacional:** solo afirmaciones expresables como reglas algoritmicas son evaluadas.
- **A6 Principio de sub-grid:** el forzamiento externo (forcing_scale) se limita a [0, 1.0); la señal macro es procesada por la dinámica micro, no amplificada. fs ≥ 1.0 indica dominancia exógena incompatible con emergencia.

## Interpretacion de Resultados (No Forzar el Marco)
Este marco no fuerza validaciones. Un caso puede **divergir** como hiperobjeto y aun asi aportar conocimiento: señala limites de escala, problemas de datos o dominios con reflexividad alta. En lugar de ajustar resultados para que “encajen”, se reportan las divergencias como parte del criterio de demarcacion. La mejora del marco se interpreta asi:
- Si EDI/CR no aparecen o son inestables, se revisa el pipeline de medicion y la calidad de datos.
- Si hay alta variabilidad entre fases (sintetica vs real), se examinan supuestos de modelado.
- Si el dominio es reflexivo, se acepta que la validacion puede ser prospectiva y no empirica.

## Delimitacion del Objeto: Viscosidad y No-localidad
Siguiendo a Timothy Morton, los hiperobjetos poseen propiedades que desafían el modelado clásico:
1. **Viscosidad:** El hiperobjeto parece "pegarse" a cualquier agente que intente medirlo. En nuestra tesis, esto se traduce en el **Acoplamiento Activo (Nudging)**: no podemos simular el clima sin ser parte de su flujo de información.
2. **No-localidad:** El objeto está distribuido espacialmente. El ABM captura esta dispersión en la grilla, mientras que la ODE captura la unidad no-local que los organiza.
3. **Fase-temporal:** El objeto existe en escalas de tiempo que exceden la observación humana directa. Nuestro modelo híbrido intenta abordar esto mediante la integración de series históricas de larga duración.

Esta base conceptual justifica por qué un modelo puramente local (ABM) suele presentar limitaciones ante un hiperobjeto: carece de la representación de la **"viscosidad macro"** que una ecuación diferencial proporciona.


## Glosario Operativo (Reducido)
- **Hiperobjeto:** entidad distribuida con no-localidad y viscosidad, validada por C1-C5.
- **EDI (Effective Dependency Index):** Reducción de error al integrar el nivel macro. Exige un umbral > 0.30 para validar la integración y > 0.05 para validar la autonomía estructural (atractor).
- **CR (Cohesion Ratio):** Ratio de cohesión interna/externa. Un CR > 2.0 indica frontera nítida. Es indicador complementario de topología, no condición necesaria de H1. La condición operativa de Symploké en el validador es `internal ≥ external - 1e-3`.
- **Nudging:** acople macro-micro para asimilacion de datos.
- **Aliasing temporal:** falla por resolucion temporal insuficiente.
- **Reflexividad:** el sistema cambia al ser observado (limite en finanzas y opinion).

## Dialectica y Limites
- **Reduccionismo:** no se equipara el sistema a un vector, se mide su dinamica causal.
- **Tautologia:** el caso Finanzas muestra que el modelo puede fallar, por tanto no es circular.
- **Emergencia:** el parametro macro no es resumen, actua como restriccion activa.
- **Edge cases:** alta frecuencia y sistemas reflexivos requieren validacion prospectiva.

## Riesgos y Mitigacion
- **Reificacion:** describir dinamicas, no “cosas”; todo debe pasar por métricas.
- **Sobreajuste:** EDI demasiado alto es sospechoso; se exige robustez y reporte de fallos.
- **Falta de datos:** fase sintetica antes de datos reales.

## Mapa de la Tesis
```mermaid
graph TD
    A[00 Marco Conceptual] -->|Axiomas| B[01 Metodologia]
    B -->|Protocolos| C[02 Modelado]
    C -->|Datos| D[03 Validacion]
    D -->|Resultados| E[04 Casos]
    E -->|Retroalimentacion| A
```

## Dependencias Teoricas (Resumen)
Realismo estructural, teoria de sistemas, termodinamica no lineal, estadistica bayesiana y filosofia analitica como marco de prueba y refutacion.

## Bibliografia Nuclear (17 fuentes)
1. Morton (2013) — Hyperobjects.
2. Harman (2018) — OOO.
3. Latour (2017) — Facing Gaia.
4. Bennett (2010) — Vibrant Matter.
5. Bunge (1979) — Ontology II.
6. Bueno (1978) — Ensayos materialistas.
7. Popper (1959) — Logic of Scientific Discovery.
8. Lakatos (1978) — Research Programmes.
9. Luhmann (1995) — Social Systems.
10. Haken (1983) — Synergetics.
11. Shannon (1948) — Information Theory.
12. Holland (1995) — CAS.
13. Schelling (1978) — Micro/Macro.
14. Strogatz (2014) — Nonlinear Dynamics.
15. Soros (1987) — Reflexividad.
16. Taleb (2012) — Antifragile.
17. Evensen (2009) — Data Assimilation.

## Apendice de Autoria IA
Trabajo en co-autoria humano-IA: el humano define objetivos y valida empiricamente; la IA apoya implementacion y documentacion.

## Sintesis
El marco define criterios computacionales para distinguir hiperobjetos estables de agregados caoticos. Su valor esta en lo que valida y en lo que rechaza, porque esa frontera es la que protege a la tesis de la especulacion.
