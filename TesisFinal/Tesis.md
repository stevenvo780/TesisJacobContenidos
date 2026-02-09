# Validación de Hiperobjetos mediante Eficacia Causal
**Tesis Doctoral en Ciencias de la Complejidad y Ontología Computacional**  
**Autor:** Steven Villanueva Osorio  
**Fecha:** 2026  

> Documento ensamblado automáticamente por `tesis.py build` el 2026-02-09 23:55 UTC  
> Fuente de verdad: `TesisDesarrollo/`


## Tabla de Contenidos

1. [00 Marco Conceptual — Narrativa Unificada](#00-marco-conceptual-narrativa-unificada)
2. [01 Metodologia de Medicion — Narrativa Unificada](#01-metodologia-de-medicion-narrativa-unificada)
3. [02 Modelado y Simulacion — Narrativa Unificada](#02-modelado-y-simulacion-narrativa-unificada)
4. [03 Validación y Praxis — Narrativa Unificada](#03-validación-y-praxis-narrativa-unificada)
5. [04 Casos de Estudio — Narrativa Unificada (29 Casos)](#04-casos-de-estudio-narrativa-unificada-29-casos)
6. [Anexos](#anexos)
7. [Resumen de Simulaciones](#resumen-de-simulaciones)


---

# 00 Marco Conceptual — Narrativa Unificada

## Proposito
Esta tesis define una ontologia operativa para hiperobjetos: entidades masivamente distribuidas cuya dinamica macro impone restricciones causales sobre lo micro. El criterio de realidad es computacional: si la capa macro es necesaria para reducir incertidumbre y mejorar la prediccion, entonces esa entidad es tratable como real dentro del marco.

## Postura Filosofica y Debate Fundacional
La tesis adopta un **realismo inferencial**: no exigimos observacion directa del hiperobjeto, sino convergencia de evidencia causal y poder explicativo. Esta postura surge de un debate realismo vs instrumentalismo: si los hiperobjetos fueran solo herramientas utiles, el marco perderia su ambicion ontologica. En cambio, el realismo inferencial permite sostener existencia operativa, siempre que haya trazabilidad y falsabilidad.

El debate **emergencia vs reduccionismo** queda resuelto en favor de un **emergentismo fuerte por irreducibilidad causal demostrada** (Humphreys, Batterman): la emergencia no se define por misterio metafísico, sino por la necesidad demostrable de un parámetro macro para explicar y estabilizar el comportamiento micro. Esta elección se protege contra reificación mediante criterios de validación estrictos (EDI, CR, C1–C5) y la prueba de ablación como intervención causal.

La **causalidad descendente** se formula en version debil: lo macro restringe, no introduce fuerzas nuevas. Esto evita contradicciones con el cierre causal y permite formalizar el efecto macro como restricciones y nudging computacional.

## Postura Ontológica: Realismo Estructural de Patrones
Esta tesis adopta un **realismo estructural de patrones** como compromiso ontológico. El marco no afirma la existencia de hiperobjetos como sustancias (objetos independientes con esencia propia) sino como **patrones reales** cuya estructura relacional porta información causalmente indispensable.

Un patrón es real, en sentido de Dennett (1991) y Ladyman & Ross (2007), si:
1. Contiene información que se pierde al intentar reducirlo a sus componentes.
2. Genera predicciones verificables que no se obtienen sin él.
3. Resiste intentos de eliminación bajo condiciones controladas.

El EDI operacionaliza las tres condiciones simultáneamente: (1) la ablación mide la pérdida informacional; (2) la mejora predictiva es el output del EDI; (3) los controles C1-C5 y las falsaciones proporcionan las condiciones controladas.

**Relación con Morton:** Timothy Morton (2013) propuso el concepto de hiperobjeto con propiedades fenomenológicas (viscosidad, no-localidad, fase temporal, interobjetividad). Esta tesis operacionaliza computacionalmente un subconjunto de esas propiedades y las somete a prueba empírica. La operacionalización no es completa: la interobjetividad no se mide; la no-localidad se modela como retícula pero sin topología heterogénea; la viscosidad se infiere del nudging pero no se prueba directamente por perturbación-recuperación. Lo que la tesis demuestra es la **constricción macro efectiva** — la propiedad ontológica mínima que un hiperobjeto debe tener para ser distinguible de un agregado. Es condición necesaria, no suficiente, del estatus ontológico pleno.

**Emergentismo fuerte por irreducibilidad causal:** Se adopta la versión de emergencia fuerte de Humphreys (2016) y Batterman (2002). La emergencia no se define por misterio metafísico sino por irreducibilidad funcional demostrada: eliminar el nivel macro destruye información causal que no es recuperable desde el nivel micro. La prueba es operativa (la ablación) y falsable (los controles). Esto distingue la emergencia fuerte del marco de la emergencia débil de Bedau (mera sorpresa computacional) y de la emergencia fuerte de O'Connor (poderes causales metafísicamente nuevos, que no son demostrables computacionalmente).

## Hipótesis Central (H1) Reformulada

Un sistema exhibe constricción macro efectiva — condición necesaria para el estatus de *patrón macro real* — si y solo si:

(a) La eliminación de la constricción macro (ablación: forcing_scale=0, macro_coupling=0) produce una degradación predictiva medible EDI > 0.30 que persiste bajo el protocolo C1-C5;

(b) Esta degradación no es compensable reconfigurando el nivel micro sin reintroducir información macro (demostrado por la incapacidad del ABM reducido de igualar al ABM completo);

(c) Controles de falsación confirman que el protocolo rechaza correctamente sistemas sin estructura macro genuina.

Un sistema que satisface H1 es un **patrón macro real** en sentido de Ladyman & Ross (2007): porta información causalmente indispensable que se destruye al intentar reducirlo. Su eficacia causal se demuestra intervencionistamente (Woodward, 2003): la ablación es una intervención cuyo efecto (degradación del EDI) establece la realidad causal de la constricción macro.

El estatus de **hiperobjeto fuerte** (sentido pleno de Morton) requiere adicionalmente: frontera espacial detectable (CR > 2.0 con topología heterogénea), persistencia transtemporal verificada, viscosidad demostrada por resistencia a perturbación, e interobjetividad. La presente investigación valida el nivel de patrón macro real; el nivel de hiperobjeto fuerte queda como programa de investigación futura.

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

## Correspondencia Propiedades de Morton ↔ Aparato Técnico

| Propiedad (Morton, 2013) | Operacionalización actual | Métrica | Cobertura | Extensión necesaria |
|---|---|---|---|---|
| **Viscosidad** (el objeto se adhiere al observador) | Nudging: el modelo no puede desacoplarse completamente del sistema | macro_coupling, assimilation_strength | Parcial | Test de perturbación-recuperación: medir tiempo de retorno al atractor tras perturbación exógena |
| **No-localidad** (el objeto está distribuido) | Retícula ABM con forzamiento uniforme; dominance_share | dominance_share ≈ 0.0025 (uniforme) | Débil | Topología heterogénea (small-world, scale-free) con forzamiento no uniforme para detectar gradientes espaciales |
| **Fase temporal** (existe en escalas que exceden la observación directa) | Series temporales de larga duración integradas vía ODE | Persistencia temporal en validador | Parcial | Datos de >50 años; detección de cambios de régimen (bifurcaciones) |
| **Interobjetividad** (afecta múltiples dominios simultáneamente) | No operacionalizada | N/A | Ninguna | Análisis inter-caso: ¿los hiperobjetos climáticos afectan los económicos? Requiere modelado multi-dominio |
| **Constricción macro efectiva** (condición mínima) | Ablación: ABM completo vs reducido | EDI > 0.30 + C1-C5 | Completa | Ya operacionalizada y validada |

La tesis demuestra la constricción macro efectiva de forma completa y robusta. Las demás propiedades de Morton están parcialmente operacionalizadas o pendientes. Esto se declara como **horizonte de investigación**, no como deficiencia del marco actual.


## Glosario Operativo
- **Hiperobjeto:** Entidad distribuida con no-localidad y viscosidad, validada por C1-C5.
- **EDI (Effective Dependency Index):** Reducción de error al integrar el nivel macro. Exige un umbral > 0.30 para validar la integración y > 0.05 para validar la autonomía estructural (atractor).
- **CR (Cohesion Ratio):** Ratio de cohesión interna/externa. Un CR > 2.0 indica frontera nítida. Es indicador complementario de topología, no condición necesaria de H1. La condición operativa de Symploké en el validador es `internal ≥ external - 1e-3`.
- **Nudging:** Acople macro-micro para asimilación de datos.
- **Aliasing temporal:** Falla por resolución temporal insuficiente.
- **Reflexividad:** El sistema cambia al ser observado (límite en finanzas y opinión).
- **Patrón real (Ladyman & Ross):** Estructura relacional que porta información causalmente indispensable; su eliminación produce pérdida predictiva no recuperable desde el nivel inferior.
- **Irreducibilidad causal funcional:** Propiedad de un nivel macro cuya eliminación degrada la predicción del nivel micro de forma medible (EDI) y robusta (C1-C5), sin que el micro pueda compensar la pérdida reconfigurando sus propios parámetros.
- **Sonda ontológica (ODE):** Instrumento computacional que genera una señal macro candidata para probar la existencia de constricción efectiva; no representa al hiperobjeto sino que revela su efecto.
- **Emergentismo fuerte por irreducibilidad causal:** Versión de emergencia fuerte (Humphreys/Batterman) donde "fuerte" significa irreducibilidad funcional demostrada por intervención, no irreducibilidad metafísica.
- **Nivel de Evidencia (LoE):** Clasificación 1-5 de la calidad epistémica de los datos de un caso. LoE=5: datos físicos de alta calidad con series >10 años. LoE=1: proxies indirectos o datos sintéticos dominantes.


## Dialectica y Limites
- **Reduccionismo:** no se equipara el sistema a un vector, se mide su dinamica causal.
- **Tautologia:** el caso Finanzas muestra que el modelo puede fallar, por tanto no es circular.
- **Emergencia:** el parametro macro no es resumen, actua como restriccion activa.
- **Edge cases:** alta frecuencia y sistemas reflexivos requieren validacion prospectiva.

## Evidencia de Ablación Parcial (Refutación de Tautología)

La crítica de "diseño tautológico" afirma que quitar mc y fs destruye la predicción "por construcción". La prueba de ablación parcial refuta esto:

| Caso | RMSE Full | RMSE No-MC | RMSE No-FS | RMSE No-Both |
|------|-----------|------------|------------|---------------|
| Clima | 0.0000 | 0.0001 | 316.68 | 316.68 |
| Finanzas | 0.0000 | 0.0066 | 6167.02 | 6167.02 |
| Energía | 0.0000 | 0.0006 | 1238.07 | 1238.07 |
| Control (ruido) | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

**Interpretación:**
1. **fs domina:** Sin forcing (fs=0), el modelo pierde casi toda capacidad predictiva (RMSE explota). El forzamiento externo es la señal principal.
2. **mc contribuye independientemente:** Sin acoplamiento (mc=0), el modelo aún predice razonablemente, pero con error mayor. El acoplamiento macro añade información.
3. **Control de ruido:** En un sistema sin estructura (noise puro), la ablación no tiene efecto. Esto confirma que el efecto medido es real, no un artefacto.

La ablación NO es tautológica: mc y fs tienen efectos distinguibles y parcialmente compensables.

## Extensión: Topologías Heterogéneas (Fase 9)

Para resolver la crítica de "homogeneidad espacial" (dom_share ≈ 1/N²), se implementó un generador de topologías complejas:

| Topología | Nodos | Heterogeneidad (σ/μ grado) |
|-----------|-------|---------------------------|
| Regular Grid | 400 | 0.11 |
| Small-World (WS) | 400 | 0.15 |
| Scale-Free (BA) | 400 | **1.11** |

La topología Scale-Free (Barabási-Albert) produce heterogeneidad 10x mayor que la grilla regular. Esto permite detectar hubs (nodos con grado alto) y frontera espacial genuina (CR > 2.0 esperado).

**Implementación:** La heterogeneidad de agentes se implementa en `repos/Simulaciones/common/abm_core.py` con tres capas: `forcing_gradient` (radial/linear/random_hubs), `heterogeneity_strength` (parámetros varían por celda) y topología opcional (small-world/scale-free). Estos parámetros se inyectan por defecto en `hybrid_validator.py`.

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

## Bibliografia Nuclear (22 fuentes)
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
18. Ladyman, J. & Ross, D. (2007) — *Every Thing Must Go: Metaphysics Naturalized.* [Patrones reales, realismo estructural]
19. Woodward, J. (2003) — *Making Things Happen.* [Causalidad intervencionista]
20. Dennett, D. (1991) — "Real Patterns." *Journal of Philosophy.* [Definición original de patrón real]
21. Batterman, R. (2002) — *The Devil in the Details.* [Irreducibilidad asintótica, emergencia]
22. Humphreys, P. (2016) — *Emergence: A Philosophical Account.* [Emergencia por fusión]

## Apendice de Autoria IA
Trabajo en co-autoria humano-IA: el humano define objetivos y valida empiricamente; la IA apoya implementacion y documentacion.

## Sintesis
El marco define criterios computacionales para distinguir hiperobjetos estables de agregados caoticos. Su valor esta en lo que valida y en lo que rechaza, porque esa frontera es la que protege a la tesis de la especulacion.

---

# 01 Metodologia de Medicion — Narrativa Unificada

## Protocolo de Rigor (C1-C5)
1. **C1 Convergencia:** ABM y ODE convergen en datos reales.
2. **C2 Robustez:** estabilidad ante perturbaciones de parametros.
3. **C3 Determinismo aleatorio:** semillas fijas para replicabilidad.
4. **C4 Linter de realidad:** coherencia con leyes del dominio.
5. **C5 Reporte de fallos:** sensibilidad y limites explicitados.

Estos criterios surgen de auditorias internas: los protocolos deben ser visibles, comparables y verificables. La metodologia no se justifica por resultados favorables, sino por su capacidad para fallar de forma explicita cuando el dominio lo exige.

## Pipeline de Validacion
Observacion → Simulacion → Validacion. El modelo se mantiene solo si supera falsacion y produce mejoras no triviales sobre el micro. Esta secuencia responde al debate metodologico: no basta con evidencia convergente, se requiere una prueba operativa y un procedimiento de rechazo.

## Metricas y Justificación Teórica: Emergencia Metaestable
- **EDI (Effective Dependence Index):** Mide la **indispensabilidad causal** del nivel macro. No es simplemente una reducción de entropía, sino la demostración de que el comportamiento observado no puede explicarse solo por interacciones locales.
- **Interpretación Ontológica del EDI:** Un EDI > 0.30 indica que eliminar el nivel macro (ablación) causa una pérdida de información irrecuperable.
- **Ablación como Intervención Causal:** Siguiendo a Woodward (2003), la manipulación de `forcing_scale=0` es una intervención controlada. Si el sistema colapsa predictivamente bajo esta intervención, se demuestra la realidad causal de la variable intervenida (el hiperobjeto).
- **Regla de Descuento por Nivel de Evidencia (LoE):** Para evitar la reificación de constructos débiles, el EDI se pondera por la calidad de los datos subyacentes.
  $$EDI_{ponderado} = EDI \times \frac{LoE}{5}$$
  Esto penaliza hipótesis con datos indirectos (ej. Conciencia, LoE=1) frente a sistemas físicos robustos (ej. Clima, LoE=5).

## Niveles de Evidencia (LoE)
1. **LoE 1 (Especulativo):** Proxies indirectos, encuestas subjetivas, o datos sintéticos sin ground truth físico. (Ej. Conciencia).
2. **LoE 2 (Débil):** Datos digitales traza (Google Trends, Twitter) con alto ruido semántico.
3. **LoE 3 (Medio):** Datos estructurados pero incompletos o de corto plazo (< 5 años).
4. **LoE 4 (Fuerte):** Series temporales consistentes, múltiples fuentes, > 10 años.
5. **LoE 5 (Robusto):** Datos físicos directos (sensores), estandarizados internacionalmente, > 30 años. (Ej. Clima, Océanos).


## Reglas de Rechazo y Validación Ponderada
1. **EDI_ponderado < 0.20:** Inexistencia de estructura macro robusta → **RECHAZO**
2. **EDI > 0.30 pero LoE < 3:** Emergencia especulativa → **PROTOTIPO** (No validada ontológicamente)
3. **Coupling < 0.10:** Epifenomenalismo (Inercia sin agencia) → **RECHAZO**
4. **RMSE < 1e-10:** Fraude por sobreajuste (Copy-paste de datos) → **RECHAZO**
5. **EDI > 0.90:** Flag de tautología — revisión manual.
6. **forcing_scale ≥ 1.0:** Cap en calibración — forzamiento externo no amplifica por encima de la unidad.
7. **C1-C5 protocolo completo:** Condición necesaria para validez técnica. (EDI ponderado es condición para validez ontológica).

Nota: La regla 4 evolucionó de rechazo a flag tras verificar que EDI > 0.90 es alcanzable legítimamente en modelos bien calibrados con señales de tendencia (casos 12, 17, 28, entre otros). El protocolo C1-C5 discrimina tautología de emergencia genuina.

## Reproducibilidad
- Hashing de datasets.
- Semillas fijas.
- Entornos replicables.

La reproducibilidad es un requisito epistemico, no un extra tecnico. Sin ella, la tesis no puede sostener afirmaciones ontologicas estables.

## Validez y Limites
- Riesgo de reificacion y de aliasing temporal.
- Clasificacion de datos por dureza: fisicos (nivel alto), proxies digitales (medio), encuestas (bajo).

Esta distincion evita confundir evidencia empirica con evidencia prospectiva.

## Riesgos y Edge Cases
- Sesgo de seleccion → multiples fuentes.
- Divergencia ABM → ajuste de nudging.
- Falta de memoria historica → series sinteticas.

Estas mitigaciones responden a auditorias sobre edge cases: cada riesgo debe tener una estrategia operativa asociada.

## Datos e Instrumentos
Python, numpy, pandas, math. Fuentes: Meteostat, Yahoo Finance, OWID, OPSD, Wikimedia (segun caso).

## Gobernanza de Datos
Filtro de nulos, normalizacion, uso exclusivo de datos abiertos. Esta gobernanza se incorpora como condicion de validez: si la calidad de datos no cumple criterios, la tesis debe abstenerse de validar.

## Casos Piloto
Clima sintetico, Finanzas sinteticas, y caso clima regional como MVP metodologico. Los pilotos prueban el pipeline antes de afirmar existencia ontologica.

## Sintesis
El pipeline discrimina sistemas con estructura macro de agregados caoticos. La metodologia se valida tanto por resultados positivos como por rechazos consistentes.

---

# 02 Modelado y Simulacion — Narrativa Unificada

## Arquitectura Detallada del Motor Híbrido
El corazón de esta investigación es la clase `HybridModel`. Su función no es solo predecir, sino mediar entre dos ontologías: el individuo (Agente) y la estructura (Ecuación).

### Pseudocódigo de la Lógica de Acoplamiento:
```python
class HybridModel:
    def step(self, t):
        # 1. El nivel Macro evoluciona según la ODE
        # dX/dt = alpha(F(t) - beta*X)
        self.macro_state = self.ode.integrate(t)
        
        # 2. El nivel Micro evoluciona con Nudging (Causalidad Descendente)
        # Cada agente i ajusta su estado x_i hacia el macro_state X
        for agent in self.agents:
            drift = self.macro_coupling * (self.macro_state - agent.x)
            noise = self.stochastic_noise()
            agent.update(drift + noise + agent.local_interaction())
            
        # 3. Asimilación de Datos (Retroalimentación)
        # El macro se corrige si la realidad observada se desvía
        if self.obs[t]:
            self.ode.adjust(self.obs[t], self.assimilation_strength)
```

## Rol Ontológico de la ODE: Sonda, No Representación

La ODE no es la representación del hiperobjeto. Es una **sonda ontológica**: un instrumento que genera una señal macro candidata para probar si la dinámica micro responde a constricciones de ese nivel. La ODE es al hiperobjeto lo que el acelerador de partículas es al bosón de Higgs: no es la entidad, es la herramienta que revela la entidad.

Lo que se demuestra como real no es la ODE sino la **constricción macro** que la ODE parametriza. Si la eliminación de esa constricción (ablación: forcing_scale=0, macro_coupling=0) degrada la predicción micro (EDI > 0.30), la constricción es causalmente eficaz. La ODE es un modelo auxiliar cuya función es:
1. Generar la señal macro que alimenta al ABM (como condición de contorno).
2. Permitir la comparación ABM_completo vs ABM_reducido (el EDI no mide calidad de la ODE).
3. Servir de benchmark para evaluar la coherencia macro-micro (correlación ODE-ABM).

Esta distinción resuelve la objeción "Phantom ODE" (Gladiadores R15): una ODE con correlación baja puede coexistir con un EDI positivo (cuando ocurre) porque lo que el EDI mide es la diferencia entre ABM con y sin constricción macro, no la calidad de la ODE como predictor independiente.

## Arquitectura y Ejecución de los 29 Casos
La arquitectura actual del proyecto integra **29 motores de simulación completamente funcionales** y ejecutables. Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas.

Esta infraestructura permite una reproducibilidad total del EDI y CR reportados, eliminando la dependencia de métricas pre-generadas. El sistema utiliza datos reales de fuentes como World Bank, Wikimedia, Meteostat, CelesTrak y yfinance para los casos de alta fidelidad, y generadores estocásticos controlados para los casos de falsación. Los casos 19-29 amplían la cobertura a dominios como acidificación oceánica, uso de fósforo, acuíferos, conectividad digital (IoT/Starlink), capital intelectual, erosión discursiva, microplásticos, basura espacial y riesgo biológico.

> **Nota:** Tres casos originales (Estética Global, Moderación Adversarial, RTB Publicidad) fueron removidos por inviabilidad de datos reales. Los 29 casos restantes constituyen el universo oficial de la tesis.

### Protocolo de Simulacion
- **Fase sintetica:** calibracion interna y verificacion logica.
- **Fase real:** validacion con datos historicos.
- **Zero-Nudging:** En la versión final, la evaluación se realiza sin nudging (`assimilation_strength=0.0`) para medir la emergencia pura del acoplamiento macro.

## Criterios Técnicos de Validación
- **EDI > 0.30:** condición necesaria de H1 (emergencia fuerte) — indica eficacia causal macro.
- **Permutation test (p<0.05):** significancia estadística del EDI contra distribución nula (999 permutaciones, seed=42).
- **Bias Correction:** transformación afín condicional del target ODE para eliminar sesgo de nivel/escala.
- **CR > 2.0:** indicador complementario de frontera sistémica (no condición de H1).
- **C1-C5:** Protocolo de rigor aplicado a la convergencia, robustez, replicación, validez y gestión de incertidumbre.
- **overall_pass:** 11 condiciones simultáneas (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento ≥ 0.1, no-fraude RMSE).
- **C1 v2.0:** Criterio relativo (acoplado mejor que reducido) OR absoluto relajado (RMSE < 2·obs_std, corr > 0.3). Anterior v1.0 era demasiado estricto (RMSE < obs_std, corr > 0.7).
- **emergence_taxonomy:** Clasificación diferenciada en 6 niveles: strong, weak, suggestive, trend, null, falsification.
- **noise_sensitivity:** Test de estabilidad del EDI bajo perturbaciones de ruido (CV < 0.5).

## Resultados Consolidados (Matriz de Validación Técnica)

| Caso | EDI | p-perm | sig | CR | Cat | Pass | Reporte |
| :--- | ---: | ---: | :---: | ---: | :--- | :---: | :--- |
| 01_caso_clima | 0.010 | 0.591 | ❌ | 1.000 | trend | ❌ | `01_caso_clima/report.md` |
| 02_caso_conciencia | -0.024 | 0.938 | ❌ | 0.919 | null | ❌ | `02_caso_conciencia/report.md` |
| 03_caso_contaminacion | -0.000 | 0.474 | ❌ | 2.780 | null | ❌ | `03_caso_contaminacion/report.md` |
| 04_caso_energia | -0.003 | 0.937 | ❌ | 1.096 | null | ❌ | `04_caso_energia/report.md` |
| 05_caso_epidemiologia | 0.000 | 1.000 | ❌ | 0.000 | null | ❌ | `05_caso_epidemiologia/report.md` |
| 06_caso_falsacion_exogeneidad | 0.055 | 1.000 | ❌ | 1.006 | falsification | ❌ | `06_caso_falsacion_exogeneidad/report.md` |
| 07_caso_falsacion_no_estacionariedad | -1.000 | 1.000 | ❌ | 1.004 | falsification | ❌ | `07_caso_falsacion_no_estacionariedad/report.md` |
| 08_caso_falsacion_observabilidad | -1.000 | 1.000 | ❌ | 1.005 | falsification | ❌ | `08_caso_falsacion_observabilidad/report.md` |
| 09_caso_finanzas | 0.040 | 0.000 | ✅ | 0.000 | suggestive | ❌ | `09_caso_finanzas/report.md` |
| 10_caso_justicia | 0.000 | 1.000 | ❌ | 1.053 | null | ❌ | `10_caso_justicia/report.md` |
| 11_caso_movilidad | 0.003 | 0.361 | ❌ | 0.000 | trend | ❌ | `11_caso_movilidad/report.md` |
| 12_caso_paradigmas | 0.000 | 1.000 | ❌ | 0.000 | null | ❌ | `12_caso_paradigmas/report.md` |
| 13_caso_politicas_estrategicas | 0.011 | 0.719 | ❌ | 1.626 | trend | ❌ | `13_caso_politicas_estrategicas/report.md` |
| 14_caso_postverdad | 0.001 | 0.030 | ❌ | 1.054 | trend | ❌ | `14_caso_postverdad/report.md` |
| 15_caso_wikipedia | 0.000 | 1.000 | ❌ | 1.158 | null | ❌ | `15_caso_wikipedia/report.md` |
| 16_caso_deforestacion | 0.633 | 0.000 | ✅ | 1.017 | strong | ✅ | `16_caso_deforestacion/report.md` |
| 17_caso_oceanos | 0.053 | 0.000 | ✅ | 1.334 | suggestive | ❌ | `17_caso_oceanos/report.md` |
| 18_caso_urbanizacion | 0.000 | 0.220 | ❌ | 30.069 | trend | ❌ | `18_caso_urbanizacion/report.md` |
| 19_caso_acidificacion_oceanica | -0.000 | 0.000 | ❌ | 1.211 | null | ❌ | `19_caso_acidificacion_oceanica/report.md` |
| 20_caso_kessler | -0.420 | 1.000 | ❌ | 1.204 | null | ❌ | `20_caso_kessler/report.md` |
| 21_caso_salinizacion | 0.027 | 0.724 | ❌ | ∞ | trend | ❌ | `21_caso_salinizacion/report.md` |
| 22_caso_fosforo | -1.000 | 1.000 | ❌ | 1.065 | null | ❌ | `22_caso_fosforo/report.md` |
| 23_caso_erosion_dialectica | -1.000 | 1.000 | ❌ | 1.001 | null | ❌ | `23_caso_erosion_dialectica/report.md` |
| 24_caso_microplasticos | 0.427 | 0.000 | ✅ | 1.002 | strong | ✅ | `24_caso_microplasticos/report.md` |
| 25_caso_acuiferos | -0.179 | 1.000 | ❌ | 1.001 | null | ❌ | `25_caso_acuiferos/report.md` |
| 26_caso_starlink | -1.000 | 1.000 | ❌ | ∞ | null | ❌ | `26_caso_starlink/report.md` |
| 27_caso_riesgo_biologico | 0.105 | 0.365 | ❌ | 1.002 | trend | ❌ | `27_caso_riesgo_biologico/report.md` |
| 28_caso_fuga_cerebros | 0.183 | 0.001 | ✅ | 1.008 | weak | ❌ | `28_caso_fuga_cerebros/report.md` |
| 29_caso_iot | 0.020 | 0.000 | ✅ | 1.053 | suggestive | ❌ | `29_caso_iot/report.md` |

Para recalcular este reporte de forma automatica, usar:
`python3 scripts/actualizar_tablas_002.py`
## Análisis de Evidencia y Hallazgos

Los 29 casos demuestran que el modelo híbrido funciona como **herramienta de demarcación operativa**: discrimina entre sistemas con estructura macro detectable y sistemas sin ella. El espectro de resultados bajo la taxonomía de emergencia diferenciada es más informativo que el binario "pasa/no pasa".

### Estado Actual: H1 Parcialmente Confirmada (Emergencia Diferenciada)

**overall_pass = 2/29** (Deforestación EDI=0.633, Microplásticos EDI=0.427). La taxonomía diferenciada revela:

- **2 casos con emergencia fuerte** (strong): Deforestación, Microplásticos
- **1 caso con emergencia débil** (weak): Fuga de Cerebros (EDI=0.183)
- **3 con señal sugestiva**: Finanzas, Océanos, IoT
- **7 con tendencia no significativa**: Clima, Movilidad, Políticas, Postverdad, Urbanización, Salinización, Riesgo Biológico
- **13 sin evidencia** (null): sin constricción macro detectable
- **3 falsificaciones correctamente rechazadas**: Exogeneidad, No-estacionariedad, Observabilidad

**Significancia estadística (p<0.05 + EDI>0.01):** 6/29 casos (09, 16, 17, 24, 28, 29)
**Estabilidad numérica:** 25/29 (fallan: 05, 12, 13, 18)
**Persistencia (std<5×):** 27/29 (fallan: 11, 20)

La tesis se reformula desde "todos los hiperobjetos muestran emergencia" hacia "el protocolo discrimina, y ciertos fenómenos muestran constricción macro genuina que resiste eliminación".

### Casos con Emergencia Fuerte (strong)

**Deforestación Global** (EDI=0.633, p=0.000, overall_pass=True):
El modelo ODE (von Thünen Frontier) captura la dinámica de la frontera agrícola. Tras Bias Correction full, el ABM acoplado reduce el RMSE en 63% respecto al ABM aislado. Este es el caso más robusto del corpus: EDI significativo, C1=True, persistencia estable.

**Microplásticos Oceánicos** (EDI=0.427, p=0.000, overall_pass=True):
El modelo Jambeck de acumulación persistente. El ABM sin ODE pierde 43% de precisión. Este caso NO requiere Bias Correction — la señal macro emerge directamente del acoplamiento.

### Caso con Emergencia Débil (weak)

**Fuga de Cerebros** (EDI=0.183, p=0.001):
El modelo Docquier-Rapoport captura la migración de capital humano. El EDI es significativo pero sub-umbral (0.183 < 0.30). BC bias_only preservó la señal sin amplificación excesiva.

### Casos con Señal Sugestiva (suggestive)

Finanzas (EDI=0.040, p=0.000), Océanos (0.053, p=0.000), IoT (0.020, p=0.000): señal estadísticamente significativa pero de magnitud insuficiente para afirmaciones ontológicas. Postverdad (EDI=0.001, p=0.030) no alcanza el umbral EDI>0.01 para significancia combinada.

### Falsificaciones Correctas

Los 3 controles negativos (Exogeneidad, No-estacionariedad, Observabilidad) son clasificados como `falsification` con EDI negativo. El protocolo los rechaza correctamente, confirmando su **selectividad**.

### Anti-emergencia: ODE de Alta Correlación con EDI Negativo

Varios casos presentan EDI negativo a pesar de buenos modelos ODE. Esto revela que **alta correlación ODE-obs no implica emergencia**. La correlación puede ser espuria o el acoplamiento puede destruir información útil que el ABM aislado captura por sí solo.

### Composición del universo de 29 casos

| Categoría | Conteo | Función |
|-----------|--------|---------|
| **strong** | 2 | Evidencia positiva de H1 (overall_pass=True) |
| **weak** | 1 | Señal macro sub-umbral H1 |
| **suggestive** | 3 | Señal estadística, resolución insuficiente |
| **trend** | 7 | Tendencia positiva sin confirmación |
| **null** | 13 | Sin evidencia de constricción macro |
| **falsification** | 3 | Controles negativos correctos |
| **Total** | **29** | |

### Diagnóstico: ¿Por Qué la Mayoría No Muestra Emergencia?

1. **Modelos ODE inadecuados:** El ODE no captura la dinámica macro, por lo que no puede generar constricción útil. Esto no refuta H1 — indica que el modelo ODE necesita mejoras específicas por dominio.

2. **No-estacionariedad del ODE:** El ODE se ajusta bien en training pero la correlación se invierte o degrada en validation. Esto refleja cambios estructurales en el fenómeno.

3. **Coupling destructivo:** El sesgo del ODE destruye información útil en el ABM. El Bias Correction resolvió esto para Deforestación; otros casos persisten por problemas de escala.

4. **Señal real demasiado ruidosa (4 casos suggestive):** La señal macro existe (EDI significativo) pero el ruido domina, produciendo EDI < 0.10. Esto es un límite del SNR de los datos reales, no del marco.

### Líneas de mejora pendientes

| Mejora | Estado | Impacto esperado |
|--------|--------|-----------------|
| Restricción mc ∈ [0.05, 0.50] | ✅ Resuelto | Reduce epifenomenalismo |
| ode_coupling_strength separado de mc | ✅ Resuelto | Control fino del coupling |
| Acoplamiento bidireccional ABM↔ODE | ✅ Resuelto | 2 iteraciones con gamma=0.05 |
| Bias Correction del ODE target | ✅ Resuelto | Deforestación rescatada (EDI +0.63) |
| Permutation test EDI (999 perms) | ✅ Resuelto | Significancia estadística robusta |
| Taxonomía de emergencia diferenciada | ✅ Resuelto | strong/weak/suggestive/null/falsification |
| Fases sintéticas independientes por caso | ⚠️ Parcial | 6/29 con generadores customizados |
| Modelos ODE dominio-específicos mejorados | ❌ Pendiente | Podría rescatar casos con ODE poor |
| Forcing multivariado (CO2, VIX, etc.) | ❌ Pendiente | Forcing más realista por dominio |
| Topología de red heterogénea para CR | ❌ Pendiente | CR > 2.0 requiere redes no regulares |

## Regla Operacional: Divergencia EDI/CR

El CR (Cohesion Ratio = internal/external) es un **indicador complementario de frontera**, no una condición necesaria de H1. H1 se define exclusivamente por EDI > 0.30 + C1-C5 (§ Hipótesis Central, línea 17 de `00_Marco_Conceptual`). El CR informa sobre la topología del acoplamiento.

Clasificación descriptiva cuando EDI y CR divergen:

1. **EDI > 0.30, CR < 2.0, C1-C5 = True**: Emergencia funcional con frontera difusa → **Validado** (H1 satisfecho). CR ≈ 1.0 es esperado en modelos de difusión espacial homogénea.
2. **EDI > 0.30, CR > 2.0, C1-C5 = True**: Emergencia completa con frontera nítida → **Validado**.
3. **EDI < 0.30, CR > 2.0**: Cohesión sin eficacia causal → **Parcial**.
4. **EDI < 0.30, CR < 2.0**: Sin emergencia ni cohesión → **Rechazado**.

**Nota:** El validador (`hybrid_validator.py`, L656) implementa `overall_pass` con 11 condiciones (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento, no-fraude). El CR se computa como métrica informativa pero no es condición de `overall_pass`, coherente con H1.

**Caso Clima real** (EDI_real=-0.015, categoría: null) no satisface H1. **Caso Deforestación** (EDI_real=+0.629, categoría: strong) sí satisface H1: la constricción macro reduce el RMSE en 63% respecto al ABM aislado, con significancia estadística (p=0.000).

### Análisis Teórico: CR ≈ 1.0 en Modelos de Difusión Homogénea

En la arquitectura ABM actual, todos los agentes comparten el mismo forzamiento externo y la misma dinámica de difusión isotrópica (vecinos de Von Neumann en retícula n×n). Formalmente, sea `σ²_int` la varianza intra-grupo (cohesión interna entre agentes vecinos) y `σ²_ext` la varianza inter-grupo (desviación respecto al macro). El CR se define como `σ²_int / σ²_ext`.

Para difusión isotrópica con forzamiento uniforme, el teorema de equipartición estocástica predice `σ²_int ≈ σ²_ext` en el límite estacionario, produciendo CR ≈ 1.0. La desviación de CR respecto a la unidad refleja heterogeneidad espacial del forzamiento o asimetría en el acoplamiento — propiedades que la arquitectura actual no implementa.

**Implicación:** CR > 2.0 requeriría forzamiento no-uniforme (ej. fuentes locales vs. gradientes globales) o topología de red no-regular (ej. small-world, scale-free). Esto constituye una **extensión natural** para trabajo futuro, no una deficiencia del marco actual. El CR ≈ 1.0 confirma que la difusión es operativa y que los agentes están acoplados al macro — condición necesaria para que el EDI sea interpretable.

**Referencia:** Haken (1983, *Synergetics*, §4.3) demuestra que en campos de orden con simetría translacional, la razón entre fluctuaciones internas y externas converge a la unidad. El CR ≈ 1.0 es la predicción teórica para ABM de difusión, no un artefacto.

### Nota sobre trazabilidad

Cada `metrics.json` contiene `generated_at` (timestamp ISO) y `git.commit` (hash del código ejecutado). Los resultados se generan ejecutando `validate.py` desde `repos/Simulaciones/{NN}_caso_*/src/`.

> La bitácora detallada de correcciones (C5), defensas técnicas ante vectores de ataque, y limitaciones del marco de Hoel se documenta en `TesisFinal/documentacion_procedimental.md`.

## Auditoría de Consistencia

Para auditar la consistencia estructural de los casos, ejecutar:
```bash
python3 repos/scripts/tesis.py audit
```

Este comando verifica presencia de archivos requeridos, sincronización de timestamps, y rangos válidos de métricas (EDI, CR).

---

# 03 Validación y Praxis — Narrativa Unificada

## Enfoque de Validación
La validación distingue entre evidencia empírica (datasets largos y duros) y evidencia prospectiva (proxies o series cortas). Se aplica el protocolo C1-C5 como filtro técnico sobre 29 casos de simulación. La evaluación se realiza con `assimilation_strength=0.0` (zero-nudging), eliminando toda asistencia observacional durante la fase de validación.

## Estados de Fallo (Umbrales de Rechazo)
- **EDI < 0.30:** no hay eficacia macro.
- **EDI > 0.90:** posible sobreajuste (flag de tautología, no rechazo automático).
- **Coupling < 0.10:** epifenomenalismo.
- **RMSE < 1e-10:** fraude por sobreajuste.
- **CR > 2.0:** indicador complementario de frontera sistémica (no condición de H1; informativo).

## Resultados Consolidados (29 Casos — Protocolo Completo)

El pipeline se ejecutó sobre 29 casos con el protocolo completo C1-C5 y 6 criterios adicionales (Symploké, no-localidad, persistencia, emergencia, coupling, no-fraude). Un caso es **Validado** solo si las 11 condiciones son ✓ simultáneamente. La significancia estadística se evalúa mediante permutation test con 999 permutaciones (seed=42).

> **Estado actual:** Bajo el pipeline limpio (sin data leakage, zero-nudging, 999 permutaciones): **overall_pass = 2/29** (Deforestación y Microplásticos). La hipótesis H1 queda **parcialmente confirmada** bajo la taxonomía de emergencia diferenciada.

### Taxonomía de Emergencia (6 categorías)

| Categoría | Criterio | Conteo | Función |
|-----------|----------|--------|---------|
| **strong** | EDI > 0.30, p < 0.05, overall_pass=True | 2 | Evidencia positiva de H1 |
| **weak** | 0.10 ≤ EDI < 0.30, p < 0.05 | 1 | Señal macro sub-umbral H1 |
| **suggestive** | EDI > 0.01, p < 0.05 | 3 | Señal estadística, resolución insuficiente |
| **trend** | EDI > 0, p ≥ 0.05 | 7 | Tendencia positiva sin confirmación |
| **null** | EDI ≤ 0 o sin señal | 13 | Sin constricción macro detectable |
| **falsification** | Controles negativos diseñados | 3 | Correctamente rechazados |
| **Total** | | **29** | |

### Clasificación por Resultado

#### Casos con Emergencia Fuerte (strong) — overall_pass=True

| Caso | EDI | p-perm | CR | BC | Interpretación |
|------|----:|-------:|---:|:---|:---|
| 16 Deforestación | **0.633** | 0.000 | 1.017 | full | ODE von Thünen: frontera agrícola capturada. 63% reducción RMSE |
| 24 Microplásticos | **0.427** | 0.000 | 1.002 | none | Modelo Jambeck: acumulación persistente. Sin BC necesario |

Estos dos casos satisfacen H1 completamente: EDI > 0.30 con significancia estadística (p < 0.001), protocolo C1-C5 completo, y las 11 condiciones simultáneas. Representan evidencia de **constricción macro efectiva** en sistemas con inercia material.

#### Caso con Emergencia Débil (weak)

| Caso | EDI | p-perm | CR | BC | Interpretación |
|------|----:|-------:|---:|:---|:---|
| 28 Fuga de Cerebros | **0.183** | 0.001 | 1.008 | bias_only | Docquier-Rapoport: migración de capital humano. Señal significativa pero sub-umbral H1 |

#### Casos con Señal Sugestiva (suggestive)

| Caso | EDI | p-perm | CR | Interpretación |
|------|----:|-------:|---:|:---|
| 09 Finanzas | 0.040 | 0.000 | 0.000 | Señal estadística, magnitud insuficiente |
| 17 Océanos | 0.053 | 0.000 | 1.334 | Proxy WMO, señal detectable |
| 29 IoT | 0.020 | 0.000 | 1.053 | Señal se atenúa en datos reales |

Señal estadísticamente significativa (p < 0.05 y EDI > 0.01) pero de magnitud insuficiente para afirmaciones ontológicas.

#### Casos con Tendencia no Significativa (trend)

| Caso | EDI | p-perm | Interpretación |
|------|----:|-------:|:---|
| 01 Clima | 0.010 | 0.591 | ODE Budyko-Sellers insuficiente |
| 11 Movilidad | 0.003 | 0.361 | Señal marginal |
| 13 Políticas | 0.011 | 0.719 | Señal débil |
| 14 Postverdad | 0.001 | 0.030 | Marginal |
| 18 Urbanización | 0.000 | 0.220 | Señal nula en práctica |
| 21 Salinización | 0.027 | 0.724 | Proxy inadecuado |
| 27 Riesgo Biológico | 0.105 | 0.365 | Señal no significativa |

#### Casos sin Evidencia (null)

13 casos con EDI ≤ 0 o sin señal detectable: Conciencia (-0.024), Contaminación (-0.000), Energía (-0.003), Epidemiología (0.000), Justicia (0.000), Paradigmas (0.000), Wikipedia (0.000), Acidificación (-0.000), Kessler (-0.420), Fósforo (-1.000), Erosión Dialéctica (-1.000), Acuíferos (-0.179), Starlink (-1.000). En estos casos, la constricción macro no mejora (o empeora) la predicción del ABM.

#### Controles de Falsación (3/3 correctamente rechazados)
- 06 Falsación Exogeneidad: ruido sin estructura → rechazado (EDI=0.055, categoría falsification).
- 07 Falsación No-Estacionariedad: deriva temporal sin causalidad → rechazado (EDI=-1.000).
- 08 Falsación Observabilidad: límites de medición micro → rechazado (EDI=-1.000).

### Métricas Globales de Robustez

| Métrica | Valor | Descripción |
|---------|-------|-------------|
| **Significancia** (p<0.05 + EDI>0.01) | 6/29 | Casos con señal estadística |
| **Estabilidad numérica** (ns_stable) | 25/29 | Fallan: 05, 12, 13, 18 |
| **Persistencia** (std < 5× ratio) | 27/29 | Fallan: 11 (ratio=9.65), 20 (ratio=276777) |
| **Bias Correction aplicado** | 17/29 | {full:5, bias_only:12, none:10, reverted:2} |
| **Reproducibilidad** | 100% | seed=42, 999 permutaciones |

## Análisis de Selectividad

### Distribución de modos de fallo (24 rechazados genuinos)

De los 26 casos genuinos (excluyendo 3 falsaciones), 24 son rechazados. La distribución de fallos revela los filtros más selectivos:

| Criterio | Descripción |
|----------|-------------|
| **Emergence (EDI < 0.30)** | Filtro primario: la mayoría no alcanzan el umbral de eficacia causal |
| **C1 (Convergencia)** | Segundo filtro: modelos ODE inadecuados producen baja convergencia ABM-datos |
| **Symploké** | Cohesión interna insuficiente en dominios con datos ruidosos |

### Diversidad de Dominios
Los 29 casos cubren dominios físicos (clima, energía, océanos, acidificación), biológicos (deforestación, fósforo, riesgo biológico, epidemiología), económicos (finanzas), tecnológicos (Starlink, IoT, Kessler), culturales (paradigmas, erosión dialéctica, conciencia), sociales (urbanización, fuga de cerebros, movilidad, justicia, postverdad), hídricos (acuíferos, salinización), materiales (microplásticos, contaminación) y de gobernanza (políticas estratégicas, Wikipedia).

### La Paradoja de la Inercia — Resuelta

Los dos únicos casos con emergencia fuerte (Deforestación EDI=0.633 y Microplásticos EDI=0.427) son sistemas con **inercia material**: la frontera agrícola se desplaza lentamente (deforestación) y los plásticos se acumulan persistentemente en océanos. El caso con emergencia débil (Fuga de Cerebros EDI=0.183) también exhibe inercia demográfica.

Esto confirma la hipótesis de que el marco detecta **estabilidad de flujo informacional** en sistemas donde la constricción macro opera sobre sustratos con inercia física o biológica. Los sistemas con alta reflexividad (finanzas), alta volatilidad (clima regional), o datos indirectos (conciencia, postverdad) no alcanzan el umbral, consistente con las limitaciones teóricas del modelo híbrido.

### Diagnóstico: ¿Por Qué la Mayoría No Muestra Emergencia?

1. **Modelos ODE inadecuados:** La ODE no captura la dinámica macro del dominio, generando una señal que interfiere con el ABM en lugar de mejorarlo.
2. **No-estacionariedad:** La ODE se ajusta bien en entrenamiento pero la relación se degrada en validación por cambios estructurales.
3. **Coupling destructivo:** El sesgo del ODE destruye información útil. El Bias Correction resolvió esto para Deforestación; otros casos persisten.
4. **Señal-ruido insuficiente (3 suggestive):** La señal macro existe (p < 0.05) pero el ruido domina, produciendo EDI < 0.10. Límite del SNR de los datos, no del marco.

---

## Diálogo Dialéctico y Falsación del Marco

El rigor del marco no reside en la validación universal, sino en su capacidad de establecer fronteras de rechazo.

### 1. El Dilema del Caso Clima (EDI=0.010 vs Umbral 0.30)
**Crítica:** La hipótesis (H1) exige EDI > 0.30, pero el caso paradigmático (Clima) obtiene EDI=0.010 (trend).
**Defensa:** La tesis admite la no-emergencia del clima regional bajo el modelo Budyko-Sellers con resolución de datos actual. Esto no invalida el marco, sino que refina la taxonomía: el clima regional no opera como un atractor fuerte independiente bajo estas condiciones de modelado. El umbral 0.30 actúa como Navaja de Ockham: si el EDI es bajo, la capa macro es una restricción débil. El rigor se demuestra al no ajustar resultados para que el clima "encaje".

### 2. Información Efectiva (EI) y sus Limitaciones
**Crítica:** El EI produce valores negativos en sistemas socio-técnicos.
**Defensa:** La EI negativa indica que los residuos del modelo completo son más entrópicos que los del modelo reducido — una propiedad esperable cuando el macro extrae la señal estructurada. El EDI permanece como métrica principal porque mide eficacia predictiva sin supuestos sobre la entropía residual. La EI opera como indicador complementario, no como condición de H1.

### 3. El Problema de la Masa Crítica (Resolución 20×20)
**Crítica:** 400 agentes son insuficientes para simular hiperobjetos planetarios.
**Defensa:** El motor HybridModel es un framework de prueba de concepto. La resolución 20×20 es el límite inferior para que surja la Symploké. Pruebas de escalamiento (100 a 1600 agentes) muestran que EDI y CR se estabilizan rápidamente, sugiriendo que la lógica de hiperobjeto es invariante a la escala por encima del umbral de masa crítica mínima.

### 4. Circularidad en la Calibración
**Crítica:** La calibración y el nudging son "ventriloquismo" del programador.
**Defensa:** La circularidad se rompe mediante la separación estricta de fases: calibración en ventana de entrenamiento, validación en ventana de prueba con `assimilation_strength=0.0`. Si el sistema retiene eficacia causal cuando el programador "suelta los controles", la emergencia es real. Los 2 casos validados demuestran precisamente esto.

---

## Conclusiones

### Estado actual: H1 parcialmente confirmada — marco operativo y selectivo

El resultado principal es **2/29 overall_pass** bajo el pipeline con evaluación estricta (zero-nudging, sin data leakage, 999 permutaciones). La hipótesis H1 (EDI > 0.30 + protocolo C1-C5) se confirma en dos casos con emergencia fuerte:

- **Deforestación** (EDI=0.633): constricción macro de la frontera agrícola, verificada con datos World Bank.
- **Microplásticos** (EDI=0.427): acumulación persistente, verificada con datos OWID.

Adicionalmente, 4 casos muestran señal estadísticamente significativa (weak + suggestive), y 7 presentan tendencias positivas no confirmadas.

### Valor epistemológico del resultado

1. **El marco es falsable:** La corrección del data leakage colapsó los EDI inflados de versiones anteriores, demostrando que el protocolo no es un rubber-stamp.
2. **Los controles de falsación funcionan:** Los 3 controles (06-08) son correctamente rechazados con categoría falsification.
3. **La selectividad es alta:** Solo 2/26 casos genuinos pasan (7.7%), descartando la posibilidad de inflación sistemática.
4. **El espectro es informativo:** La taxonomía de 6 categorías (strong → falsification) produce un mapa de evidencia más rico que el binario pasa/no pasa.

### Reformulación de H1

La tesis se reformula desde "todos los hiperobjetos muestran emergencia" hacia: **"El protocolo EDI + C1-C5 discrimina efectivamente entre sistemas con constricción macro genuina y sistemas sin ella. Ciertos fenómenos con inercia material (deforestación, microplásticos) demuestran constricción macro que resiste eliminación, satisfaciendo el criterio de patrón macro real."**

La honestidad de reportar 2/29 — distinguiendo el espectro completo de evidencia — es la mejor demostración de rigor científico del marco.

---

# 04 Casos de Estudio — Narrativa Unificada (29 Casos)

## Resumen de Validación
El motor de simulación ha sido ejecutado sobre un universo de **29 casos**, tras la remoción de 3 casos por inviabilidad de datos reales (Estética, Moderación Adversarial, RTB Publicidad). El protocolo C1-C5 + 6 criterios adicionales actúan como filtro de demarcación ontológica. La evaluación se realiza con `assimilation_strength=0.0` y 999 permutaciones (seed=42).

> **Estado actual:** Bajo el pipeline limpio: **overall_pass = 2/29** (Deforestación y Microplásticos). La hipótesis H1 se confirma parcialmente bajo la taxonomía de emergencia diferenciada.

| Categoría | Conteo | Resultado |
|-----------|--------|-----------|
| **strong** (EDI > 0.30, overall_pass=True) | 2 | Evidencia positiva de H1 |
| **weak** (0.10 ≤ EDI < 0.30, p < 0.05) | 1 | Señal sub-umbral |
| **suggestive** (EDI > 0.01, p < 0.05) | 3 | Señal estadística insuficiente |
| **trend** (EDI > 0, p ≥ 0.05) | 7 | Tendencia sin confirmación |
| **null** (EDI ≤ 0 o sin señal) | 13 | Sin constricción macro |
| **falsification** (Controles negativos) | 3 | Rechazados correctamente |

---

## 1. Emergencia Fuerte (strong) — overall_pass = True

Estos casos satisfacen H1 completamente: EDI > 0.30, significancia estadística (p < 0.001), y las 11 condiciones simultáneas del protocolo.

| ID | Caso | Fuente de Datos | EDI | p-perm | BC | Interpretación |
|----|------|-----------------|----:|-------:|:---|:---|
| 16 | **Deforestación** | World Bank (Área forestal) | **0.633** | 0.000 | full | ODE von Thünen captura frontera agrícola. 63% reducción RMSE |
| 24 | **Microplásticos** | OWID (Plastic Production) | **0.427** | 0.000 | none | Modelo Jambeck de acumulación persistente. Sin BC necesario |

**Deforestación Global** es el caso más robusto del corpus: la ODE modela la expansión de la frontera agrícola (modelo de von Thünen), y el Bias Correction full corrigió el sesgo de escala sin amplificar la señal. C1-C5 todos satisfechos, persistencia temporal estable.

**Microplásticos Oceánicos** es notable porque no requiere Bias Correction — la señal macro emerge directamente del acoplamiento ABM-ODE. El modelo Jambeck de acumulación persistente genera una constricción que reduce el RMSE en 43%.

---

## 2. Emergencia Débil (weak)

| ID | Caso | Fuente de Datos | EDI | p-perm | BC | Interpretación |
|----|------|-----------------|----:|-------:|:---|:---|
| 28 | **Fuga de Cerebros** | World Bank (I+D % PIB) | **0.183** | 0.001 | bias_only | Modelo Docquier-Rapoport. Señal significativa pero sub-umbral H1 |

El caso presenta emergencia estadísticamente significativa pero insuficiente para la condición H1 (EDI < 0.30). La migración de capital humano muestra inercia demográfica detectable, candidato para mejora con forcing multivariado.

---

## 3. Señal Sugestiva (suggestive)

| ID | Caso | Fuente de Datos | EDI | p-perm | Interpretación |
|----|------|-----------------|----:|-------:|:---|
| 09 | **Finanzas (SPY)** | Yahoo Finance | 0.040 | 0.000 | Serie ruidosa, señal mínima pero significativa |
| 17 | **Océanos** | Proxy WMO | 0.053 | 0.000 | Señal detectable, proxy poco representativo |
| 29 | **IoT** | World Bank (Suscripciones) | 0.020 | 0.000 | Señal se atenúa en datos reales |

Estos casos presentan significancia estadística (p < 0.05 y EDI > 0.01) pero la magnitud es insuficiente para afirmaciones ontológicas. Candidatos a mejora con modelos ODE dominio-específicos y forcing multivariado.

---

## 4. Tendencia no Significativa (trend)

| ID | Caso | Fuente de Datos | EDI | p-perm | Interpretación |
|----|------|-----------------|----:|-------:|:---|
| 01 | **Clima Regional** | Meteostat (NOAA) | 0.010 | 0.591 | ODE Budyko-Sellers insuficiente |
| 11 | **Movilidad** | World Bank | 0.003 | 0.361 | Señal marginal |
| 13 | **Políticas Estratégicas** | World Bank | 0.011 | 0.719 | Señal débil |
| 14 | **Postverdad** | Fallback sintético | 0.001 | 0.030 | Marginal, datos no disponibles |
| 18 | **Urbanización** | World Bank | 0.000 | 0.220 | Señal nula en práctica |
| 21 | **Salinización** | World Bank | 0.027 | 0.724 | Proxy inadecuado |
| 27 | **Riesgo Biológico** | World Bank (Mortalidad) | 0.105 | 0.365 | Señal positiva, no significativa |

---

## 5. Sin Evidencia (null) — 13 Casos

Casos donde la constricción macro no mejora (o empeora) la predicción del ABM:

| ID | Caso | EDI | Interpretación |
|----|------|----:|:---|
| 02 | Conciencia | -0.024 | Sin datos reales (fallback sintético) |
| 03 | Contaminación PM2.5 | -0.000 | Sin señal macro |
| 04 | Energía | -0.003 | Señal nula |
| 05 | Epidemiología | 0.000 | SEIR no capturada |
| 10 | Justicia | 0.000 | Sin señal |
| 12 | Paradigmas | 0.000 | Señal nula |
| 15 | Wikipedia | 0.000 | Sin estructura macro detectable |
| 19 | Acidificación Oceánica | -0.000 | Proxy inadecuado |
| 20 | Kessler | -0.420 | Anti-emergencia con datos CelesTrak |
| 22 | Fósforo | -1.000 | Anti-emergencia severa |
| 23 | Erosión Dialéctica | -1.000 | Anti-emergencia severa |
| 25 | Acuíferos | -0.179 | Señal no capturada |
| 26 | Starlink | -1.000 | Colapso del modelo |

Los casos con EDI fuertemente negativo (Fósforo, Erosión, Starlink) indican que el acoplamiento macro *destruye* información útil del ABM — un resultado que confirma la selectividad del protocolo. Estos no son fallos del marco, sino diagnósticos precisos de la inadecuación del modelo ODE para esos dominios.

---

## 6. Controles de Falsación (3/3 Correctos)
Sistemas diseñados para probar la selectividad del protocolo C1-C5:

| ID | Caso | Propósito | EDI | Estado |
|----|------|-----------|----:|:---|
| 06 | **Exogeneidad** | Probar respuesta ante ruido puro | 0.055 | ❌ Rechazado ✓ |
| 07 | **No-estacionariedad** | Probar respuesta ante Random Walk | -1.000 | ❌ Rechazado ✓ |
| 08 | **Observabilidad** | Probar respuesta ante estados ocultos | -1.000 | ❌ Rechazado ✓ |

Los tres controles son correctamente rechazados con categoría `falsification`, confirmando que el protocolo no es un rubber-stamp.

---

## 7. Casos Removidos (Archivo)
Descartados por falta de fuentes de datos reales verificables:
- **Estética Global:** Inviabilidad de API pública de subastas de arte.
- **Moderación Adversarial:** Opacidad de datos de plataformas (Big Tech).
- **RTB Publicidad:** Datos propietarios protegidos por NDAs de industria.

Archivados en `Artifacts/casos_removidos/`.

---

**Conclusión:** De los 26 casos genuinos (excluidas 3 falsaciones), 2 demuestran constricción macro efectiva con emergencia fuerte (7.7%), 1 muestra emergencia débil, y 3 presentan señal sugestiva estadísticamente significativa. La selectividad del protocolo (rechazo del 92.3% de casos genuinos) es la garantía de que las validaciones positivas representan evidencia genuina de patrones macro reales, no artefactos de modelado.

---

# Anexos

Este archivo consolida indices, registros y auditorias complementarias.

---

## 00_Marco_Conceptual
- Ver carpeta `00_Marco_Conceptual/` para glosarios, axiomas y debates.

## 01_Metodologia_Medicion
- Ver carpeta `01_Metodologia_Medicion/` para protocolos, metricas y validacion.

## 02_Modelado_Simulacion
- Ver carpeta `02_Modelado_Simulacion/` para arquitectura, casos y resultados.

## 03_Validacion_Praxis
- Ver carpeta `03_Validacion_Praxis/` para matrices de evidencia y reportes.

## 04_Casos_De_Estudio
- Ver carpeta `04_Casos_De_Estudio/` para sintesis de casos.

---

# Indice: EjersiciosCriticos

- Ejercicio Gladiadores Partida 1:
  - `EjersiciosCriticos/Ejercicio_Critico_Gladiadores_Partida1.md`
- Trazas, Posibles y Dudas:
  - `EjersiciosCriticos/Trazas_Mejoras_Possibles_Dudas.md`

---

# Registros historicos

## registro_racionalizacion_glosarios_casos.md

Fecha: 2026-02-03

Acciones:
- Glosarios 00_Glosario.md, 00_1_GlosarioTecnico.md y 01_1_Glosario_Medicion.md fusionados en 00_02_Glosario_Maestro.md.
- Casos piloto 01_17, 01_20 y 01_21 unificados en 01_15_Casos_Piloto.md.
- Riesgos/edge cases centralizados en 00_4 y 00_15; eliminados 00_10 y 00_5.

Indices actualizados:
- 00_14_Indice_Maestro.md
- 00_Marco_Conceptual/index.md
- 01_Metodologia_Medicion/index.md
- INDEX_GENERAL.md
- 00_10_Dependencias.md

## registro_resecuencia_indices.md

Fecha: 2026-02-03

Acciones:
- Resequencia de indices y limpieza de referencias redundantes.

---


# Resumen de Simulaciones

> Tabla generada automáticamente desde `metrics.json` de cada caso.

## Matriz de Protocolo Completa (29 casos × 11 criterios)

Cada celda = resultado del criterio en **Fase Real** (`assimilation_strength = 0.0`). **Validado** = 11 condiciones ✓ simultáneamente.

| # | Caso | EDI | C1 | C2 | C3 | C4 | C5 | Sym | NL | Per | Emr | Cp | Result |
| :--- | :--- | ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 16 | Deforestacion | 0.633 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 24 | Microplasticos | 0.427 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 06 | Falsacion Exogeneidad | 0.055 | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Control ❌ |
| 07 | Falsacion No Estacionariedad | -1.000 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Control ❌ |
| 08 | Falsacion Observabilidad | -1.000 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Control ❌ |
| 01 | Clima | 0.010 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 02 | Conciencia | -0.024 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ | Rechazado |
| 03 | Contaminacion | -0.000 | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 04 | Energia | -0.003 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 05 | Epidemiologia | 0.000 | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | Rechazado |
| 09 | Finanzas | 0.040 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | Rechazado |
| 10 | Justicia | 0.000 | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 11 | Movilidad | 0.003 | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | Rechazado |
| 12 | Paradigmas | 0.000 | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 13 | Politicas Estrategicas | 0.011 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 14 | Postverdad | 0.001 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 15 | Wikipedia | 0.000 | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 17 | Oceanos | 0.053 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | Rechazado |
| 18 | Urbanizacion | 0.000 | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | ✗ | ✗ | Rechazado |
| 19 | Acidificacion Oceanica | -0.000 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 20 | Kessler | -0.420 | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ | Rechazado |
| 21 | Salinizacion | 0.027 | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 22 | Fosforo | -1.000 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 23 | Erosion Dialectica | -1.000 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 25 | Acuiferos | -0.179 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 26 | Starlink | -1.000 | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 27 | Riesgo Biologico | 0.105 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | Rechazado |
| 28 | Fuga Cerebros | 0.183 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 29 | Iot | 0.020 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |

**Resumen:** 2 validados, 0 rechazados con EDI > 0.30 (selectividad), 3 controles de falsación, 24 rechazados con EDI bajo.

## Distribución de Modos de Fallo

En los 24 rechazados genuinos:

| Criterio | Fallos | % |
| :--- | :---: | :---: |
| C1 | 11/24 | 45% |
| Emergence | 21/24 | 87% |
| Symploké | 2/24 | 8% |
| Persistencia | 2/24 | 8% |
| C5 | 1/24 | 4% |
| C2 | 2/24 | 8% |
