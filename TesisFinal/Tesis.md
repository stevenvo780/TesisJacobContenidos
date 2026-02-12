# Irrealismo Operativo de Hiperobjetos: Clasificación de Fenómenos por Grado de Cierre Operativo
**Tesis Doctoral en Ciencias de la Complejidad y Filosofía de la Simulación**  
**Autor:** Steven Villanueva Osorio  
**Fecha:** 2026  

> Documento ensamblado automáticamente por `tesis.py build` el 2026-02-12 04:22 UTC  
> Fuente de verdad: `TesisDesarrollo/`


## Tabla de Contenidos

- [Irrealismo Operativo de Hiperobjetos: Clasificación de Fenómenos por Grado de Cierre Operativo](#irrealismo-operativo-de-hiperobjetos-clasificación-de-fenómenos-por-grado-de-cierre-operativo)
  - [Tabla de Contenidos](#tabla-de-contenidos)
- [00 Marco Conceptual](#00-marco-conceptual)
  - [Propósito](#propósito)
    - [En lenguaje accesible](#en-lenguaje-accesible)
  - [Postura Filosófica: Irrealismo Operativo](#postura-filosófica-irrealismo-operativo)
    - [El problema pre-ontológico](#el-problema-pre-ontológico)
    - [Fundamentos del irrealismo](#fundamentos-del-irrealismo)
    - [Consecuencia central](#consecuencia-central)
  - [Emergentismo Gradual con Niveles](#emergentismo-gradual-con-niveles)
    - [Analogía: La escala Richter de la emergencia](#analogía-la-escala-richter-de-la-emergencia)
    - [Anclaje teórico](#anclaje-teórico)
  - [Hipótesis Central (H1)](#hipótesis-central-h1)
    - [La analogía del ribosoma](#la-analogía-del-ribosoma)
    - [Condición de "hiperobjeto con límites"](#condición-de-hiperobjeto-con-límites)
  - [Relación con Morton y la Tradición OOO](#relación-con-morton-y-la-tradición-ooo)
  - [Posición frente a la causalidad descendente](#posición-frente-a-la-causalidad-descendente)
  - [Presupuestos Filosóficos](#presupuestos-filosóficos)
  - [Axiomas Operativos del Modelado Híbrido](#axiomas-operativos-del-modelado-híbrido)
  - [Interpretación de Resultados (No Forzar el Marco)](#interpretación-de-resultados-no-forzar-el-marco)
  - [Delimitación del Objeto de Estudio](#delimitación-del-objeto-de-estudio)
  - [Evidencia de Ablación Parcial (Refutación de Tautología)](#evidencia-de-ablación-parcial-refutación-de-tautología)
  - [Extensión: Topologías Heterogéneas (Fase 9)](#extensión-topologías-heterogéneas-fase-9)
  - [Glosario Operativo](#glosario-operativo)
  - [Dialéctica y Límites](#dialéctica-y-límites)
  - [Riesgos y Mitigación](#riesgos-y-mitigación)
  - [Mapa de la Tesis](#mapa-de-la-tesis)
  - [Dependencias Teóricas (Resumen)](#dependencias-teóricas-resumen)
  - [Apéndice de Autoría IA](#apéndice-de-autoría-ia)
  - [Síntesis](#síntesis)
- [01 Metodología de Medición](#01-metodología-de-medición)
  - [El Emergentómetro en la Práctica](#el-emergentómetro-en-la-práctica)
  - [Protocolo de Rigor (C1-C5)](#protocolo-de-rigor-c1-c5)
  - [Pipeline de Validación](#pipeline-de-validación)
  - [Métricas y su Interpretación bajo Irrealismo Operativo](#métricas-y-su-interpretación-bajo-irrealismo-operativo)
    - [EDI (Effective Dependence Index) — "El termómetro de emergencia"](#edi-effective-dependence-index--el-termómetro-de-emergencia)
    - [Regla de Descuento por Nivel de Evidencia (LoE)](#regla-de-descuento-por-nivel-de-evidencia-loe)
  - [Niveles de Evidencia (LoE)](#niveles-de-evidencia-loe)
  - [Reglas de Clasificación](#reglas-de-clasificación)
  - [EI (Información Efectiva) — Indicador Complementario](#ei-información-efectiva--indicador-complementario)
  - [Reproducibilidad](#reproducibilidad)
  - [Validez y Límites](#validez-y-límites)
  - [Datos e Instrumentos](#datos-e-instrumentos)
  - [Gobernanza de Datos](#gobernanza-de-datos)
  - [Casos Piloto](#casos-piloto)
  - [Síntesis](#síntesis-1)
- [02 Modelado y Simulación](#02-modelado-y-simulación)
  - [El Motor del Emergentómetro](#el-motor-del-emergentómetro)
  - [Arquitectura Detallada del Motor Híbrido](#arquitectura-detallada-del-motor-híbrido)
    - [Pseudocódigo de la Lógica de Acoplamiento:](#pseudocódigo-de-la-lógica-de-acoplamiento)
  - [Rol Instrumental de la ODE: Sonda Operativa](#rol-instrumental-de-la-ode-sonda-operativa)
  - [Implementación de los 29 Casos](#implementación-de-los-29-casos)
    - [Protocolo de Simulación](#protocolo-de-simulación)
  - [Criterios Técnicos de Clasificación](#criterios-técnicos-de-clasificación)
  - [Trazabilidad y Resultados](#trazabilidad-y-resultados)
    - [Regla Operacional: Divergencia EDI/CR](#regla-operacional-divergencia-edicr)
  - [Auditoría de Consistencia](#auditoría-de-consistencia)
- [03 Validación y Praxis: Resultados del Emergentómetro](#03-validación-y-praxis-resultados-del-emergentómetro)
  - [Resumen ejecutivo: Lo que el Emergentómetro encontró](#resumen-ejecutivo-lo-que-el-emergentómetro-encontró)
  - [Enfoque de Clasificación Operativa](#enfoque-de-clasificación-operativa)
  - [Umbrales de Clasificación (no de rechazo)](#umbrales-de-clasificación-no-de-rechazo)
  - [Especificación de Modelos por Dominio](#especificación-de-modelos-por-dominio)
  - [Resultados Consolidados (29 Casos — Protocolo Completo)](#resultados-consolidados-29-casos--protocolo-completo)
    - [Taxonomía de Emergencia con Niveles Operativos](#taxonomía-de-emergencia-con-niveles-operativos)
- [Resumen de Simulaciones](#resumen-de-simulaciones)
  - [Matriz de Clasificación Operativa (29 casos × 13 criterios + Nivel)](#matriz-de-clasificación-operativa-29-casos--13-criterios--nivel)
  - [Distribución de Modos de Fallo](#distribución-de-modos-de-fallo)
    - [Clasificación por Resultado](#clasificación-por-resultado)
      - [Nivel 4 — Cierre Operativo Fuerte (overall\_pass=True)](#nivel-4--cierre-operativo-fuerte-overall_passtrue)
      - [Nivel 3 — Componentes Funcionales (weak)](#nivel-3--componentes-funcionales-weak)
      - [Nivel 2 — Señal Sugestiva](#nivel-2--señal-sugestiva)
      - [Nivel 1 — Tendencia no Significativa](#nivel-1--tendencia-no-significativa)
      - [Nivel 0 — Sin Señal Operativa (8 Casos)](#nivel-0--sin-señal-operativa-8-casos)
      - [Controles de Falsación (3/3 Correctos)](#controles-de-falsación-33-correctos)
    - [Métricas Globales de Robustez](#métricas-globales-de-robustez)
  - [Análisis de Selectividad](#análisis-de-selectividad)
    - [Distribución del paisaje (26 casos genuinos)](#distribución-del-paisaje-26-casos-genuinos)
    - [Diversidad de Dominios](#diversidad-de-dominios)
    - [El Patrón de la Inercia Material](#el-patrón-de-la-inercia-material)
    - [Diagnóstico: ¿Por Qué Algunos Casos se Clasifican en Nivel 0-1?](#diagnóstico-por-qué-algunos-casos-se-clasifican-en-nivel-0-1)
  - [Diálogo Dialéctico y Falsación del Instrumento](#diálogo-dialéctico-y-falsación-del-instrumento)
    - [1. El Caso Clima (EDI=0.011 vs Umbral 0.30)](#1-el-caso-clima-edi0011-vs-umbral-030)
    - [2. Información Efectiva (EI) y sus Limitaciones](#2-información-efectiva-ei-y-sus-limitaciones)
    - [3. Resolución 20×20 (400 agentes)](#3-resolución-2020-400-agentes)
    - [4. Circularidad en la Calibración](#4-circularidad-en-la-calibración)
  - [Conclusiones](#conclusiones)
    - [Resultado principal: Paisaje de Emergencia Operativa completamente mapeado](#resultado-principal-paisaje-de-emergencia-operativa-completamente-mapeado)
    - [Valor epistemológico bajo irrealismo operativo](#valor-epistemológico-bajo-irrealismo-operativo)
    - [H1 — Hipótesis Central](#h1--hipótesis-central)
- [04 Casos de Estudio: El Emergentómetro en Acción](#04-casos-de-estudio-el-emergentómetro-en-acción)
  - [Paisaje de Emergencia Operativa](#paisaje-de-emergencia-operativa)
  - [1. Casos de Cierre Operativo Fuerte (Nivel 4 — overall\_pass=True)](#1-casos-de-cierre-operativo-fuerte-nivel-4--overall_passtrue)
  - [2. Componentes Funcionales (Nivel 3 — weak)](#2-componentes-funcionales-nivel-3--weak)
  - [3. Señales Sugestivas (Nivel 2)](#3-señales-sugestivas-nivel-2)
  - [4. Otros Fenómenos del Paisaje (Niveles 0-1)](#4-otros-fenómenos-del-paisaje-niveles-0-1)
  - [5. Controles de Falsación (3/3 Correctos)](#5-controles-de-falsación-33-correctos)
  - [6. Casos Removidos (Archivo)](#6-casos-removidos-archivo)
  - [Conclusión: El Paisaje como Resultado Principal](#conclusión-el-paisaje-como-resultado-principal)
- [Anexos](#anexos)
  - [00\_Marco\_Conceptual](#00_marco_conceptual)
  - [01\_Metodologia\_Medicion](#01_metodologia_medicion)
  - [02\_Modelado\_Simulacion](#02_modelado_simulacion)
  - [03\_Validacion\_Praxis](#03_validacion_praxis)
  - [04\_Casos\_De\_Estudio](#04_casos_de_estudio)
  - [05\_Bibliografia](#05_bibliografia)
- [Indice: EjerciciosCriticos](#indice-ejercicioscriticos)
- [Registros historicos](#registros-historicos)
  - [registro\_racionalizacion\_glosarios\_casos.md](#registro_racionalizacion_glosarios_casosmd)
  - [registro\_resecuencia\_indices.md](#registro_resecuencia_indicesmd)
- [05 Bibliografía Nuclear](#05-bibliografía-nuclear)
  - [Bibliografía Nuclear (37 fuentes)](#bibliografía-nuclear-37-fuentes)
  - [Fuentes de Datos (Repositorios Principales)](#fuentes-de-datos-repositorios-principales)


---

# 00 Marco Conceptual

## Propósito
Esta tesis construye un marco computacional para evaluar fenómenos de gran escala — candidatos a "hiperobjetos" en terminología de Morton (2013) — según su grado de cierre operativo. El marco no afirma ni niega la existencia metafísica de tales entidades: mide, clasifica y ordena su comportamiento en un gradiente de emergencia operativa.

### En lenguaje accesible

Imagine que existe una pregunta fundamental en filosofía y ciencia: **¿los fenómenos de gran escala (el clima, la economía global, una pandemia) son "algo más" que la suma de sus partes, o basta con conocer las partes para predecirlo todo?** Esta tesis no intenta responderla con argumentos filosóficos — la responde con un *instrumento de medición*.

Ese instrumento es el **Emergentómetro**: un sistema computacional que mide cuánta información predictiva se pierde si ignoramos el nivel macro de un fenómeno y solo miramos las partes individuales. Si la pérdida es grande y robusta, el fenómeno tiene *cierre operativo* — se comporta como una entidad funcional con reglas propias. Si no, los componentes individuales bastan para explicarlo.

```mermaid
flowchart LR
    F["🌍 Fenómeno\n(clima, economía, pandemia)"] --> E["🔬 Emergentómetro\n(ODE + ABM + C1-C5)"]
    E --> G["📊 Grado de Emergencia\n(EDI: 0 a 1)"]
    G --> N4["Nivel 4: El todo ES más\nque las partes"]
    G --> N0["Nivel 0: Las partes\nbastan"]
    
    style E fill:#e1f5fe,stroke:#01579b,stroke-width:3px
    style N4 fill:#c8e6c9,stroke:#388e3c,stroke-width:2px
    style N0 fill:#ffebee,stroke:#c62828
```

Así como un termómetro mide temperatura sin que eso implique una teoría sobre "qué es el calor", el Emergentómetro mide emergencia operativa sin afirmar que los hiperobjetos "existan" como entidades metafísicas. Esta postura se llama **irrealismo operativo**: medir sin reificar.

## Postura Filosófica: Irrealismo Operativo

### El problema pre-ontológico
La tesis adopta un **irrealismo operativo**: lo pre-ontológico — la realidad anterior a todo marco teórico — no tiene forma particular ni estructura predeterminada. Todo marco teórico impone estructura sobre una materia ontológicamente indeterminada. Esta posición se distingue de:

- **Realismo fuerte** (Bunge, 1979; Ladyman & Ross, 2007): que afirma que la estructura descubierta preexiste al marco.
- **Instrumentalismo puro** (van Fraassen, 1980): que reduce los constructos a herramientas predictivas sin contenido ontológico.
- **Realismo inferencial** (Psillos, 1999): que infiere existencia desde eficacia predictiva.

El irrealismo operativo ocupa una posición intermedia: nuestros constructos son **operativamente suficientes** para tratar fenómenos de gran escala, sin que esa suficiencia implique existencia metafísica. Un "hiperobjeto" es un objeto del entendimiento — un constructo que el marco detecta, mide y clasifica — cuya utilidad operativa se demuestra por su capacidad de reducir incertidumbre predictiva de forma robusta y falsable.

### Fundamentos del irrealismo
1. **Indeterminación pre-ontológica:** Lo que existe antes de la medición no tiene la estructura que el marco le impone. La estructura emerge del acto de modelar, no del fenómeno en sí. Esto no es antirrealismo (negación de la realidad externa), sino agnosticismo estructural: la realidad impone restricciones (los datos resisten la arbitrariedad), pero no dicta la forma del modelo.
2. **Suficiencia operativa:** Un marco es operativamente suficiente si: (a) produce predicciones verificables, (b) resiste intentos de falsación, (c) discrimina entre fenómenos, y (d) genera un gradiente medible de propiedades. El framework ABM+ODE satisface las cuatro condiciones.
3. **Objetos del entendimiento:** Los hiperobjetos de esta tesis son constructos operativos, análogos a lo que Kant (1781) llamó "objetos de la experiencia posible" — no cosas-en-sí, sino estructuras que el entendimiento impone y que los datos validan o rechazan.

### Consecuencia central
La tesis no afirma "el clima es un hiperobjeto real". Afirma: "bajo este marco, el fenómeno de deforestación global exhibe un grado de cierre operativo de 0.580 (EDI), estadísticamente significativo (p<0.001), que resiste ablación, falsación y perturbación. Esto lo clasifica como objeto operativo de alto grado de emergencia."

## Emergentismo Gradual con Niveles

Esta tesis adopta un **emergentismo gradual por niveles de cierre operativo**. Los grados de emergencia no son categorías metafísicas sino posiciones en un continuo medido.

### Analogía: La escala Richter de la emergencia
Así como la escala Richter no dice "este terremoto es real" — mide su magnitud —, los niveles del Emergentómetro miden *cuánta emergencia operativa* exhibe un fenómeno. Un terremoto de magnitud 2 no es un "fracaso": es un dato. Del mismo modo, un fenómeno clasificado en Nivel 0 no es un "hiperobjeto fallido" — es un fenómeno donde el instrumento no detecta cierre operativo con la sonda elegida.

```mermaid
graph LR
    N0[Nivel 0: Null] --> N1[Nivel 1: Trend]
    N1 --> N2[Nivel 2: Suggestive]
    N2 --> N3[Nivel 3: Weak]
    N3 --> N4[Nivel 4: Strong]
    N4 --> N5[Nivel 5: Hiperobjeto]
    
    style N0 fill:#eeeeee,stroke:#999,stroke-width:1px,color:#666
    style N1 fill:#fff9c4,stroke:#fbc02d,stroke-width:1px
    style N2 fill:#ffe0b2,stroke:#f57c00,stroke-width:1px
    style N3 fill:#e3f2fd,stroke:#1976d2,stroke-width:2px
    style N4 fill:#c8e6c9,stroke:#388e3c,stroke-width:3px
    style N5 fill:#d1c4e9,stroke:#512da8,stroke-width:4px
```

| Nivel | Categoría | Criterio operativo | Interpretación |
|:-----:|-----------|-------------------|----------------|
| 0 | **null** | EDI ≤ 0 o sin señal | Sin cierre operativo. El fenómeno no presenta constricción macro detectable. No es un objeto sino una agregación sin estructura identificable por este instrumento. |
| 1 | **trend** | EDI > 0, p ≥ 0.05 | Tendencia macro sin significancia estadística. Indicios de estructura, evidencia insuficiente. |
| 2 | **suggestive** | EDI > 0.01, p < 0.05 | Señal estadística sin magnitud suficiente. Constricción detectable pero débil. Componente funcional sin autonomía. |
| 3 | **weak** | 0.10 ≤ EDI < 0.30, p < 0.05 | Constricción significativa sub-umbral de cierre. "Componente funcional" con influencia pero sin autonomía plena — análogo a un ribosoma: tiene función pero no es un organismo. |
| 4 | **strong** | EDI > 0.30, p < 0.05, overall_pass=True | **Cierre operativo alto.** Constricción macro irreducible, significativa y robusta. Objeto operativo del entendimiento con límites identificables. |
| 5 | **hiperobjeto fuerte** | Nivel 4 + CR > 2.0, topología heterogénea, persistencia transtemporal, viscosidad verificada | Cierre máximo con frontera espacial. Programa de investigación futura. |

### Anclaje teórico
- **Chalmers (2006):** Distingue emergencia débil (inesperada pero deducible) de emergencia fuerte (no deducible desde lo micro). Nuestro gradiente operacionaliza esta distinción: los Niveles 0-2 corresponden a ausencia o emergencia débil; los Niveles 3-4 muestran irreducibilidad funcional demostrada.
- **Bedau (1997):** La emergencia débil es el "estado por defecto" de los sistemas complejos — computable pero no predecible en la práctica. Nuestros 8 casos null + 4 trend habitan este territorio.
- **Kim (1999):** La exclusión causal amenaza toda emergencia que afirme causalidad descendente fuerte. Bajo irrealismo operativo, esquivamos esta objeción: no afirmamos que lo macro *cause* — afirmamos que el constructo macro reduce incertidumbre de forma no eliminable. Es una constatación epistémica, no una afirmación causal metafísica.
- **Humphreys (2016):** La "fusión emergente" produce propiedades nuevas no atribuibles a componentes. Nuestro Nivel 4 captura exactamente esto: la constricción macro genera información predictiva que desaparece al eliminarla y no es recuperable desde el nivel micro.
- **O'Connor & Wong (2005):** Distinguen emergencia ontológica (propiedades genuinamente nuevas) de emergencia epistemológica (limitaciones del conocimiento). Nuestro marco se sitúa explícitamente en la emergencia epistemológica: medimos limitaciones del nivel micro para explicar el fenómeno, no afirmamos propiedades ontológicamente nuevas.

## Hipótesis Central (H1)

Un fenómeno exhibe **cierre operativo de grado G** si y solo si:

(a) La eliminación de la constricción macro (ablación: forcing_scale=0, macro_coupling=0) produce una degradación predictiva medible EDI = G que persiste bajo el protocolo C1-C5;

(b) Esta degradación no es compensable reconfigurando el nivel micro sin reintroducir información macro (demostrado por la incapacidad del ABM reducido de igualar al ABM completo);

(c) Controles de falsación confirman que el protocolo rechaza correctamente sistemas sin estructura macro genuina.

**Clasificación resultante:**
- Si G ≥ 0.30 con significancia estadística y protocolo C1-C5 completo: **objeto operativo con cierre alto** (Nivel 4).
- Si 0.10 ≤ G < 0.30 con significancia: **componente funcional** (Nivel 3).
- Si G > 0.01 con significancia: **señal sugestiva** (Nivel 2).
- Si G > 0 sin significancia: **tendencia** (Nivel 1).
- Si G ≤ 0: **sin cierre operativo** (Nivel 0).

H1 no afirma "este fenómeno es un hiperobjeto real". H1 mide y clasifica el grado de cierre operativo. El **resultado** de la tesis es el paisaje completo de 29 fenómenos clasificados, no solo los que alcanzan Nivel 4.

```mermaid
flowchart TD
    A[Modelo Completo ABM + ODE] -->|Error RMSE_full| C{Comparación}
    B[Modelo Reducido ABM solo] -->|Error RMSE_reduced| C
    C -->|Calculo EDI| D[EDI = 1 - RMSE_full/RMSE_reduced]
    
    D -->|EDI > 0.30| E[Nivel 4: Emergencia Fuerte]
    D -->|0.01 < EDI < 0.30| G[Nivel 2-3: Emergencia Débil]
    D -->|EDI < 0.01| F[Nivel 0-1: Sin Señal]
    
    style A fill:#e1f5fe,stroke:#01579b
    style B fill:#fff3e0,stroke:#e65100
    style E fill:#c8e6c9,stroke:#2e7d32,stroke-width:3px
    style G fill:#fff9c4,stroke:#fbc02d
    style F fill:#ffebee,stroke:#c62828
```

### La analogía del ribosoma
Los fenómenos de Nivel 2-3 (suggestive, weak) son análogos a **ribosomas** en biología: componentes funcionales imprescindibles para la célula, pero que por sí solos no constituyen un organismo. La deforestación (Nivel 4) es análoga a una célula completa: tiene cierre operativo suficiente para ser tratada como unidad funcional autónoma. Un caso null es análogo a moléculas dispersas en solución: materia sin organización detectable.

### Condición de "hiperobjeto con límites"
Para que un fenómeno merezca el título de "hiperobjeto con límites" (Nivel 5), se requieren condiciones estrictas que van más allá del cierre operativo:
1. **EDI > 0.30** con overall_pass=True (Nivel 4 satisfecho)
2. **CR > 2.0** con topología heterogénea (frontera espacial nítida)
3. **Persistencia transtemporal** verificada en múltiples ventanas
4. **Viscosidad** demostrada por test de perturbación-recuperación
5. **Interobjetividad** verificada por análisis inter-caso

Ningún caso del corpus actual alcanza el Nivel 5. Esto es consistente con el irrealismo operativo: afirmar "hiperobjeto fuerte" requiere más evidencia de la que un modelo ABM+ODE homogéneo puede proporcionar.

## Relación con Morton y la Tradición OOO
Timothy Morton (2013) propuso el concepto de hiperobjeto con propiedades fenomenológicas (viscosidad, no-localidad, fase temporal, interobjetividad). Dentro de la Ontología Orientada a Objetos (OOO), Harman (2018) sostiene que los objetos se retiran de todo acceso directo, mientras que Latour (2017) y Bennett (2010) enfatizan la agencia distribuida de los no-humanos. Luhmann (1995) aporta la noción de sistemas autopoiéticos con cierre operativo — una analogía directa con nuestro concepto de cierre medido por EDI. La presente tesis:

1. **Acepta** la utilidad del concepto como heurística para identificar fenómenos candidatos.
2. **Rechaza** la pretensión ontológica fuerte: no afirmamos que los hiperobjetos *existan* como entidades autónomas.
3. **Operacionaliza parcialmente** un subconjunto de propiedades (constricción macro, no-localidad en retícula, persistencia temporal).
4. **Mide** el grado en que cada fenómeno candidato exhibe comportamiento compatible con dichas propiedades.
5. **Clasifica** los resultados en un gradiente de emergencia operativa, donde solo los fenómenos con cierre alto merecen un tratamiento diferenciado.

| Propiedad (Morton, 2013) | Operacionalización | Métrica | Cobertura |
|---|---|---|---|
| **Viscosidad** | Nudging: acoplamiento modelo-datos | macro_coupling, assimilation_strength | Parcial |
| **No-localidad** | Retícula ABM con forzamiento uniforme | dominance_share ≈ 1/N² | Débil (homogénea) |
| **Fase temporal** | Series temporales de larga duración vía ODE | Persistencia temporal | Parcial |
| **Interobjetividad** | No operacionalizada | N/A | Ninguna |
| **Constricción macro** | Ablación: ABM completo vs reducido | EDI + C1-C5 | Completa |

## Posición frente a la causalidad descendente
La tesis adopta una versión **deflacionaria** de la causalidad descendente: lo macro no "causa" en sentido fuerte (no introduce fuerzas nuevas ni viola el cierre causal físico). Lo macro **restringe** — limita el espacio de estados accesible al nivel micro. Siguiendo la metodología intervencionista de Woodward (2003), esta restricción es:

- **Operativamente detectable:** la ablación (intervención controlada sobre el forzamiento macro) la revela.
- **Cuantitativamente medible:** el EDI (Effective Dependence Index), inspirado en el marco de Información Efectiva de Hoel (2017), la cuantifica.
- **Falsable:** los controles de falsación la discriminan de artefactos.

Pero **no es ontológicamente interpretable** como causalidad fuerte. Bajo irrealismo operativo, la pregunta "¿lo macro realmente causa algo?" es una pregunta mal planteada. La pregunta correcta es: "¿eliminar el constructo macro degrada la predicción de forma robusta?"

## Presupuestos Filosóficos
- **P1 Indeterminación pre-ontológica:** Lo que existe antes de la modelización no tiene la estructura que el marco le impone.
- **P2 Symploké (Bueno, 1978):** No todo está conectado con todo (caos), pero nada está aislado (monadismo); la realidad se evalúa como una red con límites funcionales.

```mermaid
graph TD
    subgraph Caos[Caos: Hiperconexión]
        A[Agente] <--> B[Agente]
        B <--> C[Agente]
        C <--> A
    end
    
    subgraph Monadismo[Monadismo: Aislamiento]
        D[Agente]
        E[Agente]
        F[Agente]
    end
    
    subgraph Symploke[Symploké: Límites Operativos]
        G[Agente] --- H[Agente]
        H --- I[Agente]
        I --- G
        style Symploke fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    end
    
    Caos ---|RECHAZO| X((Objeto))
    Monadismo ---|RECHAZO| X
    Symploke -->|ACEPTACIÓN| X
    
    style X fill:#6f6,stroke:#333,stroke-width:4px
```

- **P3 Emergentismo gradual:** Las propiedades de nivel macro se clasifican en un continuo de cierre operativo. No hay un salto discreto entre "emergente" y "no emergente", sino un gradiente medible.
- **P4 Suficiencia operativa:** El marco no necesita afirmar existencia metafísica para ser científicamente válido. Basta con producir predicciones verificables, falsables y discriminativas.

## Axiomas Operativos del Modelado Híbrido
- **A1 Incompletitud del nivel único:** ABM u ODE por separado suelen ser insuficientes para capturar la complejidad de fenómenos de gran escala.
- **A2 Primacía del parámetro de orden:** El macro estabiliza y restringe al micro. Esto es una hipótesis operativa, no una afirmación ontológica.
- **A3 Invarianza estructural (C3):** El mecanismo macro-micro debe mostrar estabilidad ante condiciones iniciales distintas.
- **A4 Falsabilidad por saturación:** Si EDI < 0.30, el fenómeno no alcanza cierre operativo alto. Si EDI < 0.01, no hay señal detectable. Estos umbrales representan la "Ventana de Hoel" (Hoel, 2017): el punto donde la descripción macro es operativamente más informativa que la micro.
- **A5 Clausura computacional:** Solo afirmaciones expresables como reglas algorítmicas son evaluadas.
- **A6 Principio de sub-grid:** El forzamiento externo (forcing_scale) se limita a [0, 0.99]; la señal macro es procesada por la dinámica micro, no amplificada. fs ≥ 1.0 indica dominancia exógena incompatible con emergencia.

## Interpretación de Resultados (No Forzar el Marco)
Este marco no fuerza validaciones. Un caso con EDI bajo o negativo **no es un fracaso** — es un dato en el paisaje de emergencia operativa. Señala que, bajo este instrumento, el fenómeno no presenta cierre operativo detectable. Esto puede deberse a:
- Ausencia real de estructura macro (null genuino)
- Modelo ODE inadecuado para el dominio
- Datos insuficientes o ruidosos
- Reflexividad del sistema (el fenómeno cambia al ser observado)

Bajo irrealismo operativo, la distinción entre estas causas es **epistémica, no ontológica**: no afirmamos "no es un hiperobjeto", sino "este instrumento no detecta cierre operativo en este fenómeno".

## Delimitación del Objeto de Estudio
Siguiendo a Morton (2013), los hiperobjetos poseen propiedades que desafían el modelado clásico:
1. **Viscosidad:** Se traduce en acoplamiento activo (nudging). El modelo no puede desacoplarse completamente del sistema. En evaluación, assimilation_strength=0 simula el máximo desacoplamiento posible.
2. **No-localidad:** El ABM captura la dispersión espacial; la ODE captura la unidad funcional que los organiza.
3. **Fase temporal:** Series históricas de larga duración integradas vía ODE.

Estas propiedades justifican por qué un modelo puramente local (ABM solo) presenta limitaciones: carece de la representación de la "viscosidad macro" que una ecuación diferencial proporciona.

## Evidencia de Ablación Parcial (Refutación de Tautología)

La crítica de "diseño tautológico" afirma que quitar mc y fs destruye la predicción "por construcción". La prueba de ablación parcial refuta esto:

| Caso | RMSE Full | RMSE No-MC | RMSE No-FS | RMSE No-Both |
|------|-----------|------------|------------|---------------|
| Clima | 0.0000 | 0.0001 | 316.68 | 316.68 |
| Finanzas | 0.0000 | 0.0066 | 6167.02 | 6167.02 |
| Energía | 0.0000 | 0.0006 | 1238.07 | 1238.07 |
| Control (ruido) | 0.0000 | 0.0000 | 0.0000 | 0.0000 |

**Interpretación:**
1. **fs domina:** Sin forcing (fs=0), el modelo pierde casi toda capacidad predictiva. El forzamiento externo es la señal principal.
2. **mc contribuye independientemente:** Sin acoplamiento (mc=0), el modelo aún predice razonablemente, pero con error mayor.
3. **Control de ruido:** En un sistema sin estructura, la ablación no tiene efecto. Esto confirma que el efecto medido no es artefacto.

## Extensión: Topologías Heterogéneas (Fase 9)

Para resolver la crítica de "homogeneidad espacial" (dom_share ≈ 1/N²), se implementó un generador de topologías complejas:

| Topología | Nodos | Heterogeneidad (σ/μ grado) |
|-----------|-------|---------------------------|
| Regular Grid | 400 | 0.11 |
| Small-World (WS) | 400 | 0.15 |
| Scale-Free (BA) | 400 | **1.11** |

La topología Scale-Free produce heterogeneidad 10× mayor que la grilla regular. Alcanzar Nivel 5 (hiperobjeto con límites) requeriría esta heterogeneidad verificada.

## Glosario Operativo
- **Emergentómetro:** Nombre operativo del instrumento de medición completo: motor híbrido (ODE+ABM), protocolo C1-C5, test de permutación (999 reps) y métrica EDI. Así como un termómetro mide temperatura, el Emergentómetro mide el grado de emergencia operativa de un fenómeno. No es una metáfora — es el nombre funcional del pipeline computacional.
- **Hiperobjeto (operativo):** Constructo del entendimiento que designa un fenómeno de gran escala con cierre operativo alto (Nivel 4+). No implica existencia metafísica.
- **Cierre operativo:** Propiedad de un fenómeno cuya constricción macro es irreducible, significativa y robusta bajo el protocolo C1-C5. Medido por EDI.
- **EDI (Effective Dependence Index):** Grado de cierre operativo. Mide la degradación predictiva al eliminar la constricción macro. En términos pedagógicos: "si quito la visión de conjunto, ¿cuánto empeora mi predicción?". Rango: EDI ∈ [-1, 1]. Un EDI de 0.30 (Kessler) significa que ignorar el patrón macro degrada la predicción en 30%.
- **CR (Cohesion Ratio):** Indicador complementario de frontera funcional. CR > 2.0 sugiere frontera espacial nítida. No es condición de H1.
- **Nudging:** Acople macro-micro para asimilación de datos. Desactivado (=0) en evaluación.
- **Componente funcional:** Fenómeno de Nivel 2-3 que exhibe constricción detectable pero insuficiente para cierre. Análogo a ribosomas en biología.
- **Objeto operativo:** Fenómeno de Nivel 4 que exhibe cierre operativo alto. Tratado como unidad funcional autónoma dentro del marco.
- **Sonda ontológica (ODE):** Instrumento computacional que genera una señal macro candidata (ej. modelos de Budyko-Sellers para clima, von Thünen para deforestación, Jambeck para microplásticos o Docquier-Rapoport para migración). No representa al fenómeno; revela su grado de cierre operativo mediante el acoplamiento con el nivel micro.
- **Paisaje de emergencia:** El conjunto ordenado de los 29 fenómenos clasificados por su grado de cierre operativo. Es el resultado principal de la tesis.
- **Irrealismo operativo:** Postura filosófica que no afirma ni niega existencia metafísica, sino que mide suficiencia operativa de constructos.
- **Nivel de Evidencia (LoE):** Clasificación 1-5 de la calidad epistémica de los datos. LoE=5: datos físicos directos, >30 años. LoE=1: proxies indirectos.

## Dialéctica y Límites
- **Reduccionismo:** No se equipara el sistema a un vector; se mide el grado de cierre operativo del nivel macro.
- **Tautología:** Los controles de falsación (3/3 correctamente rechazados) y la diversidad de resultados (8 null, 4 trend, 3 suggestive, 6 weak, 5 strong, 3 controles) refutan la circularidad.
- **Instrumentalismo:** El irrealismo operativo va más allá del instrumentalismo puro: no reduce los constructos a "herramientas útiles" — les asigna un grado medible de cierre funcional que puede ser mayor o menor. Un instrumento puro no tiene grados.
- **Reificación:** Bajo irrealismo, el riesgo de reificación se minimiza: nunca afirmamos que algo "es" un hiperobjeto; afirmamos que "exhibe cierre operativo de grado G".
- **Edge cases:** Alta frecuencia y sistemas reflexivos requieren validación prospectiva.

## Riesgos y Mitigación
- **Sobreajuste:** EDI > 0.90 es flag de tautología. Protocolo C1-C5 discrimina.
- **Falta de datos:** Fase sintética antes de datos reales. LoE pondera la calidad.
- **Fragilidad del modelo:** Siguiendo a Taleb (2012), los sistemas complejos son vulnerables a perturbaciones no anticipadas. C2 (robustez) prueba explícitamente esta vulnerabilidad.
- **Patrones reales vs. aparentes:** Dennett (1991) argumenta que los "patrones reales" existen en la medida en que permiten compresión predictiva. Nuestro EDI operacionaliza esta noción: un patrón macro es "real" operativamente si su eliminación degrada la predicción.
- **Asimetrías inter-nivel:** Batterman (2002) muestra que el razonamiento asintótico revela propiedades emergentes invisibles a la descripción micro. El gradiente EDI captura estas asimetrías.
- **Homogeneidad espacial:** CR ≈ 1.0 es la predicción teórica para agentes acoplados en sistemas con simetría translacional y difusión isotrópica (Haken, 1983, §4.3). El CR > 2.0 (Nivel 5) requiere romper esta simetría mediante topologías heterogéneas.
- **Circularidad BC:** Bias Correction aplica solo en fase de corrección. Evaluación usa assimilation_strength=0. Modo 'reverted' protege contra circularidad (verificado: 9 puntos de forzado en hybrid_validator.py).

## Mapa de la Tesis
```mermaid
graph TD
    A[00 Marco Conceptual<br/>Irrealismo Operativo] -->|Axiomas| B[01 Metodología]
    B -->|Protocolos| C[02 Modelado]
    C -->|Datos| D[03 Validación]
    D -->|Paisaje de Emergencia| E[04 Casos]
    E -->|Retroalimentación| A
```

## Dependencias Teóricas (Resumen)
Irrealismo operativo, emergentismo gradual, teoría de sistemas, termodinámica no lineal, estadística bayesiana y filosofía analítica como marco de prueba y refutación.



## Apéndice de Autoría IA
Trabajo en co-autoría humano-IA: el humano define objetivos y valida empíricamente; la IA apoya implementación y documentación.

## Síntesis
El marco define un gradiente computacional de cierre operativo para fenómenos de gran escala. Su valor está en el paisaje completo que produce: no solo en los casos que alcanzan Nivel 4, sino en los 29 puntos que mapean el continuo de emergencia. Este paisaje es el resultado principal de la tesis. La frontera entre "objeto operativo" (Nivel 4) y "componente funcional" (Nivel 3) o "agregación sin cierre" (Nivel 0) es la contribución que protege a la tesis de la especulación ontológica.

---

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

---

# 02 Modelado y Simulación

## El Motor del Emergentómetro

El Emergentómetro necesita un "motor" que simule fenómenos a dos escalas simultáneamente: la escala individual (micro) y la escala del fenómeno completo (macro). Ese motor es el **modelo híbrido ODE+ABM**.

En términos accesibles: imagine una colonia de hormigas. Cada hormiga sigue reglas simples (modelo micro, ABM), pero la colonia como un todo parece tener "comportamiento propio" — rutas eficientes, arquitectura del hormiguero, defensa coordinada. La ODE captura ese patrón de conjunto. El Emergentómetro entonces pregunta: **¿si eliminamos la influencia del patrón de conjunto sobre las hormigas individuales, la predicción empeora?** Si la respuesta es "sí, y mucho", hay emergencia operativa.

## Arquitectura Detallada del Motor Híbrido
El corazón de esta investigación es la clase `HybridModel`. Su función es mediar entre dos niveles descriptivos: el individuo (Agente) y la estructura (Ecuación). No presupone que la estructura "exista" ontológicamente — solo que su inclusión modifica las predicciones de forma medible.

### Pseudocódigo de la Lógica de Acoplamiento:
```python
class HybridModel:
    def step(self, t):
        # 1. El nivel Macro evoluciona según la ODE
        # dX/dt = alpha(F(t) - beta*X)
        self.macro_state = self.ode.integrate(t)
        
        # 2. El nivel Micro evoluciona con Nudging (acoplamiento descendente)
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

```mermaid
graph TD
    subgraph Macro[Nivel Macro: ODE]
        M1[dX/dt] --> M2[Estado X]
    end
    
    subgraph Micro[Nivel Micro: ABM]
        A1[Agente i] --> A2[Acción local]
        A2 --> A3[Estado x_i]
    end
    
    M2 -->|Nudging / Causalidad Descendente| Micro
    A3 -->|Agregación / Causalidad Ascendente| Macro
    D[Datos Reales] -->|Asimilación| Macro
    
    style Macro fill:#e1f5fe,stroke:#01579b,stroke-width:2px
    style Micro fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style D fill:#c8e6c9,stroke:#2e7d32
```

## Rol Instrumental de la ODE: Sonda Operativa

La ODE no es la representación del hiperobjeto. Es una **sonda operativa**: un instrumento que genera una señal macro candidata para probar si la dinámica micro responde a constricciones de ese nivel. Bajo irrealismo operativo, lo que se mide no es "existencia" sino **grado de cierre operativo**. Si la eliminación de la constricción macro (ablación: forcing_scale=0, macro_coupling=0) degrada la predicción micro (EDI > 0.30), el constructo macro es operativamente indispensable.

La ODE es un modelo auxiliar cuya función es:
1. Generar la señal macro que alimenta al ABM (como condición de contorno).
2. Permitir la comparación ABM_completo vs ABM_reducido (el EDI no mide calidad de la ODE).
3. Servir de benchmark para evaluar la coherencia macro-micro (correlación ODE-ABM).

Esta distinción resuelve la objeción "Phantom ODE": una ODE con correlación baja puede coexistir con un EDI positivo porque lo que el EDI mide es la diferencia entre ABM con y sin constricción macro, no la calidad de la ODE como predictor independiente.

```mermaid
flowchart LR
    subgraph Exterior[Entorno]
        FS[Forzamiento Externo: fs]
    end
    
    subgraph Sistema[Hiperobjeto Operativo]
        MC[Acoplamiento Macro: mc]
        ABM[Dinámica Micro]
    end
    
    FS -->|Señal Exógena| ABM
    MC -->|Constricción Macro| ABM
    ABM -->|Respuesta| Obs[Observación]
    
    style Exterior fill:#f5f5f5,stroke:#333
    style Sistema fill:#fff3e0,stroke:#e65100,stroke-width:2px
    style MC fill:#c8e6c9,stroke:#2e7d32
    style FS fill:#e1f5fe,stroke:#01579b
```

## Implementación de los 29 Casos
La arquitectura actual integra **29 motores de simulación completamente funcionales**. La lógica ABM sigue la tradición de modelos basados en agentes de Holland (1995) y Schelling (1978), donde reglas micro simples producen patrones macro complejos. La dinámica ODE se fundamenta en sistemas no lineales (Strogatz, 2014). Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas. Se utilizan datos reales de fuentes como World Bank, Meteostat, Yahoo Finance, OWID, Wikimedia y CelesTrak.

### Protocolo de Simulación
- **Fase sintética:** calibración interna y verificación lógica.
- **Fase real:** clasificación con datos históricos.
- **Zero-Nudging:** En la versión final, la evaluación se realiza sin nudging (`assimilation_strength=0.0`) para medir el cierre operativo puro del acoplamiento macro.

## Criterios Técnicos de Clasificación
- **EDI ≥ 0.30:** Nivel 4 (cierre operativo fuerte).
- **Permutation test (p<0.05):** significancia estadística (999 permutaciones).
- **Bias Correction:** transformación afín condicional del target ODE para eliminar sesgo.
- **CR > 2.0:** indicador complementario de frontera sistémica.
- **overall_pass:** 13 condiciones simultáneas (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento, no-fraude, EDI válido, EDI significativo).

## Trazabilidad y Resultados
Los resultados detallados de la ejecución de estos 29 casos se consolidan exclusivamente en la sección **03 Validación y Praxis**. La arquitectura permite una trazabilidad total: cada simulación genera un archivo `metrics.json` con el timestamp y el hash del commit.

Para recalcular el reporte completo:
`python3 repos/scripts/actualizar_tablas_002.py`

### Regla Operacional: Divergencia EDI/CR
El CR (Cohesion Ratio) es un indicador complementario de frontera. CR ≈ 1.0 es la predicción teórica para agentes acoplados en sistemas con simetría translacional y difusión isotrópica (Haken, 1983).

## Auditoría de Consistencia
Para auditar la consistencia estructural de los casos, ejecutar:
```bash
python3 repos/scripts/tesis.py audit
```

---

# 03 Validación y Praxis: Resultados del Emergentómetro

## Resumen ejecutivo: Lo que el Emergentómetro encontró

El Emergentómetro se aplicó a **29 fenómenos de gran escala** de dominios tan diversos como el clima, las pandemias, los mercados financieros, la deforestación y la basura espacial. El resultado no es un veredicto binario ("existe/no existe") sino un **mapa de emergencia**: un paisaje donde cada fenómeno tiene un grado medido de cierre operativo.

De los 29 fenómenos medidos:
- **5 exhiben cierre operativo alto y robusto** (overall_pass=True): eliminar la "visión de conjunto" degrada la predicción entre 32.2% y 80.6%, de forma estable y significativa.
- **6 son componentes funcionales** (weak, Nivel 3): señal significativa (p < 0.05) con EDI entre 0.10 y 0.30 pero sin cierre pleno.
- **3 presentan señal sugestiva**: el instrumento detecta algo, pero no suficiente para confirmar.
- **4 muestran tendencia sin significancia**: indicios sin confirmación estadística.
- **8 no presentan señal**: el instrumento no detecta cierre operativo con la sonda elegida.
- **3 controles de falsación** funcionan correctamente: ruido puro, random walk y estados ocultos son rechazados.

Este paisaje es el resultado principal de la tesis — no solo los casos "exitosos", sino la distribución completa.

## Enfoque de Clasificación Operativa
La validación bajo irrealismo operativo no busca "confirmar" ni "refutar" la existencia de hiperobjetos. Clasifica fenómenos en un **gradiente de cierre operativo** (Niveles 0-5) según la indispensabilidad del constructo macro para predecir el comportamiento micro. Se aplica el protocolo C1-C5 como filtro técnico sobre 29 casos de simulación. La evaluación se realiza con `assimilation_strength=0.0` (zero-nudging), eliminando toda asistencia observacional durante la fase de validación.

## Umbrales de Clasificación (no de rechazo)
- **EDI < 0.01:** Nivel 0 — sin señal operativa detectable.
- **EDI > 0.01, p < 0.05:** Nivel 2 — señal sugestiva.
- **0.10 ≤ EDI < 0.30, p < 0.05:** Nivel 3 — componente funcional (analogía: ribosoma).
- **EDI ≥ 0.30, overall_pass=True:** Nivel 4 — cierre operativo fuerte.
- **Coupling < 0.10:** flag de epifenomenalismo.
- **RMSE < 1e-10:** flag de sobreajuste.
- **EDI > 0.90:** flag de tautología (revisión manual).
- **CR > 2.0:** indicador complementario de frontera sistémica (no condición de clasificación).

## Especificación de Modelos por Dominio

Cada caso de simulación utiliza un par de modelos (ODE/ABM) específicos para su dominio, evitando soluciones genéricas. A continuación se detallan los núcleos matemáticos implementados:

| Caso | Dominio | Modelo ODE (Macro) | Modelo ABM (Micro) |
| :--- | :--- | :--- | :--- |
| **01 Clima** | Ciencias Climáticas | **Balance Energético Linealizado** (Budyko-Sellers) | **Difusión Espacial Vectorizada** (Watts-Strogatz) |
| **02 Conciencia** | Cognitivo-Social | **Atención-Decaimiento** (Logística Forzada) | **Global Workspace Theory** (16 Módulos) |
| **03 Contaminación** | Ambiental | **Acumulación-Disipación** (Box Model EPA) | **Pluma Gaussiana** (AERMOD Simplificado) |
| **04 Energía** | Sistemas Eléctricos | **Lotka-Volterra** (Competencia Energética) | **Adopción Tecnológica** (Tipo TIMES) |
| **05 Epidemiología** | Salud Pública | **SEIR** (Kermack-McKendrick) | **SEIR en Red** (Scale-Free Barabási) |
| **06 Falsación Exog.** | Control Negativo | *Random Walk* (Movimiento Browniano) | *N/A* (Incidencia Sintética) |
| **07 Falsación Trend** | Control Negativo | *Random Walk* (Control) | *N/A* (Tendencia Lineal) |
| **08 Falsación Obs.** | Control Negativo | *Constante* (Control de Ruido) | *N/A* (Confounder Sintético) |
| **09 Finanzas** | Mercados Financieros | **Heston Simplificado** (Volatilidad Estocástica) | **Heterogeneous Agent Model** (Brock-Hommes) |
| **10 Justicia** | Sociología Legal | **Logística Forzada** (Adopción de Normas) | **Deffuant Bounded Confidence** (Espacial) |
| **11 Movilidad** | Tráfico Urbano | **Diagrama Fundamental Macroscópico** (MFD) | **Tráfico en Red** (Greenshields/Dijkstra) |
| **12 Paradigmas** | Sociología Ciencia | **Landau-Ginzburg** (Transición de Fase) | **Ising Model** (Red Scale-Free) |
| **13 Políticas** | Ciencias Políticas | **Inercia Institucional** (North 1990) | **Difusión Bass** (Red Barabási-Albert) |
| **14 Postverdad** | Comunicación | **SIS de Campo Medio** | **SIS en Red** (Misinformación) |
| **15 Wikipedia** | Colaboración Online | **Lotka-Volterra** (Calidad vs Controversia) | **Modelo Cultural Axelrod** (Fragmentación) |
| **16 Deforestación** | Ecología Global | **Accumulation-Decay** (Von Thünen) | **Gradiente Radial** (Von Thünen Frontier) |
| **17 Océanos** | Oceanografía | **Modelo de Caja de Stommel** (Termohalina) | **Circulación Termohalina** (Grilla 2D) |
| **18 Urbanización** | Geografía Urbana | **Logística + Atracción Económica** | **Preferential Attachment** (Simon-Yule) |
| **19 Acidificación** | Biogeoquímica | **Revelle Factor** (Buffering Oceánico) | **Calcificadores Marinos** (Respuesta Bio) |
| **20 Kessler** | Espacio Orbital | **Ecuación Kessler-Liou** (Cascada Cuadrática)| **NASA LEGEND-inspired** (Campo de Debris) |
| **21 Salinización** | Agricultura | **Richards-Convección** (Transporte Solutos) | **Gradiente Hídrico** (Parcelas Agrícolas) |
| **22 Fósforo** | Ciclos Globales | **Carpenter Biogeochemical P Cycle** | **Gradiente de Fertilización** (Polos Agrícolas)|
| **23 Erosión Dialéctica**| Lingüística | **Abrams-Strogatz** (Competition 2003) | **Gradiente de Centros Culturales** |
| **24 Microplásticos** | Contaminación Marina| **Jambeck Persistent Accumulation** | **Transporte Marino** (Gradiente Fluvial) |
| **25 Acuíferos** | Hidrología | **Balance Hídrico Darcy-Theis** | **Flujo Lateral Darcy** (Gradiente Radial) |
| **26 Starlink** | Infraestructura | **Dinámica Orbital Kessler-Lewis** | **Constelación** (Gradiente Orbital) |
| **27 Riesgo Bio** | One Health | **Woolhouse Zoonotic Cascade** (Bilineal) | **Focos Zoonóticos** (Random Hubs) |
| **28 Fuga Cerebros** | Economía Desarrollo | **Dinámica Capital Humano** (Docquier) | **Polos Académicos/Tecnológicos** |
| **29 IoT** | Tecnología Digital | **Bass-Metcalfe** (Efectos de Red) | **Difusión Tecnológica** (Goldenberg) |

## Resultados Consolidados (29 Casos — Protocolo Completo)

El pipeline se ejecutó sobre 29 casos con el protocolo completo C1-C5 y 8 criterios adicionales (Symploké, no-localidad, persistencia, emergencia, coupling, no-fraude, EDI válido, EDI significativo). Un caso alcanza **Nivel 4** solo si las 13 condiciones se cumplen simultáneamente. La significancia estadística se evalúa mediante permutation test con 999 permutaciones (seed=42).

> **Estado actual:** Bajo el pipeline afinado (sin data leakage, zero-nudging, 999 permutaciones, EDI ≥ 0.30): **5/29 overall_pass=True** (Energía, Deforestación, Urbanización, Fósforo, Microplásticos). 6 casos clasificados como weak (Nivel 3). El paisaje de emergencia queda completamente mapeado.

```mermaid
pie title Distribución del Paisaje de Emergencia (29 Casos)
    "Nivel 4: Cierre Fuerte" : 5
    "Nivel 3: Componente Funcional" : 6
    "Nivel 2: Señal Sugestiva" : 3
    "Nivel 0-1: Tendencia/Sin Señal" : 12
    "Controles de Falsación" : 3
```

### Taxonomía de Emergencia con Niveles Operativos

| Categoría | Nivel | Criterio | Conteo | Función en el paisaje |
|-----------|:-----:|----------|--------|----------------------|
| **strong** | 4 | EDI ≥ 0.30, p < 0.05, overall_pass=True | 5 | Cierre operativo fuerte |
| **weak** | 3 | 0.10 ≤ EDI < 0.30, p < 0.05 | 6 | Componente funcional |
| **suggestive** | 2 | EDI > 0.01, p < 0.05 | 3 | Señal detectable |
| **trend** | 1 | EDI > 0, p ≥ 0.05 | 4 | Tendencia no confirmada |
| **null** | 0 | EDI ≤ 0 o sin señal | 8 | Sin señal operativa |
| **falsification** | — | Controles negativos diseñados | 3 | Correctamente rechazados |
| **Total** | | | **29** | |


# Resumen de Simulaciones

> Tabla generada automáticamente desde `metrics.json` de cada caso.

## Matriz de Clasificación Operativa (29 casos × 13 criterios + Nivel)

Cada celda = resultado del criterio en **Fase Real** (`assimilation_strength = 0.0`). **Nivel** = grado de cierre operativo (0–4, control = —). **Validado** = 13 condiciones se cumplen simultáneamente (incluye EDI válido y EDI significativo).

| # | Caso | EDI | C1 | C2 | C3 | C4 | C5 | Sym | NL | Per | Emr | Cp | Nivel | Result |
| :--- | :--- | ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 24 | Microplasticos | 0.806 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 4 | **Validado** |
| 04 | Energia | 0.650 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 4 | **Validado** |
| 16 | Deforestacion | 0.580 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 4 | **Validado** |
| 18 | Urbanizacion | 0.337 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 4 | **Validado** |
| 22 | Fosforo | 0.322 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 4 | **Validado** |
| 06 | Falsacion Exogeneidad | 0.055 | Si | Si | Si | No | Si | Si | Si | Si | No | Si | — | Control (Rechazado) |
| 07 | Falsacion No Estacionariedad | -0.882 | No | Si | Si | Si | Si | Si | Si | Si | Si | Si | — | Control (Rechazado) |
| 08 | Falsacion Observabilidad | -1.000 | No | Si | Si | Si | Si | Si | Si | Si | Si | Si | — | Control (Rechazado) |
| 26 | Starlink | 0.690 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 1 | Rechazado |
| 01 | Clima | 0.011 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 1 | Rechazado |
| 02 | Conciencia | -0.116 | Si | Si | Si | Si | Si | No | No | Si | Si | Si | 0 | Rechazado |
| 03 | Contaminacion | -0.004 | Si | Si | Si | Si | Si | Si | Si | Si | No | Si | 0 | Rechazado |
| 05 | Epidemiologia | 0.129 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 3 | Rechazado |
| 09 | Finanzas | 0.081 | Si | Si | Si | No | Si | Si | Si | Si | Si | Si | 2 | Rechazado |
| 10 | Justicia | 0.227 | Si | No | Si | Si | Si | Si | Si | Si | No | Si | 1 | Rechazado |
| 11 | Movilidad | 0.128 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 3 | Rechazado |
| 12 | Paradigmas | -0.006 | No | Si | Si | Si | Si | Si | Si | Si | No | Si | 0 | Rechazado |
| 13 | Politicas Estrategicas | 0.288 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 3 | Rechazado |
| 14 | Postverdad | 0.252 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 3 | Rechazado |
| 15 | Wikipedia | 0.080 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 2 | Rechazado |
| 17 | Oceanos | -0.043 | No | Si | Si | Si | Si | Si | Si | Si | No | Si | 0 | Rechazado |
| 19 | Acidificacion Oceanica | -0.000 | No | Si | Si | Si | Si | Si | Si | Si | No | Si | 0 | Rechazado |
| 20 | Kessler | 0.299 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 3 | Rechazado |
| 21 | Salinizacion | 0.058 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 2 | Rechazado |
| 23 | Erosion Dialectica | -1.000 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 0 | Rechazado |
| 25 | Acuiferos | -0.020 | Si | Si | Si | Si | Si | Si | Si | Si | Si | No | 0 | Rechazado |
| 27 | Riesgo Biologico | 0.294 | Si | Si | Si | Si | Si | Si | Si | Si | Si | Si | 3 | Rechazado |
| 28 | Fuga Cerebros | 0.025 | Si | No | Si | Si | Si | Si | Si | Si | Si | Si | 1 | Rechazado |
| 29 | Iot | -0.899 | No | Si | Si | Si | Si | Si | Si | No | Si | Si | 0 | Rechazado |

**Resumen:** 5 validados (Nivel 4), 1 rechazados con EDI > 0.30 (selectividad), 3 controles de falsación, 20 rechazados con EDI bajo (Nivel 0–1).

## Distribución de Modos de Fallo

En los 21 rechazados genuinos:

| Criterio | Fallos | % |
| :--- | :---: | :---: |
| C1 | 4/21 | 19% |
| Emergence | 5/21 | 23% |
| Symploké | 1/21 | 4% |
| Persistencia | 1/21 | 4% |
| C5 | 0/21 | 0% |
| C2 | 2/21 | 9% |


### Clasificación por Resultado

#### Nivel 4 — Cierre Operativo Fuerte (overall_pass=True)

| Caso | EDI | p-perm | CR | BC | Interpretación operativa |
|------|----:|-------:|---:|:---|:---|
| 24 Microplásticos | **0.806** | 0.000 | 1.000 | bias_only | Jambeck Accumulation: acumulación persistente con fuerte constricción macro |
| 04 Energía | **0.650** | 0.000 | 1.002 | bias_only | Lotka-Volterra: competencia energética con fuerte constricción macro |
| 16 Deforestación | **0.580** | 0.000 | 1.023 | full | Von Thünen Frontier: inercia de frontera agrícola |
| 18 Urbanización | **0.337** | 0.000 | 1.003 | full | Logística urbana: atracción económica |
| 22 Fósforo | **0.322** | 0.000 | 1.003 | full | Carpenter P Cycle: ciclo biogeoquímico |

Estos cinco casos alcanzan overall_pass=True: las 13 condiciones se cumplen simultáneamente. El constructo macro es operativamente indispensable. Eliminar la constricción macro degrada la predicción entre 32.2% y 80.6%. Bajo irrealismo operativo, esto no afirma que "existan" como entidades autónomas — afirma que el instrumento detecta cierre operativo robusto.

#### Nivel 3 — Componentes Funcionales (weak)

| Caso | EDI | p-perm | CR | Interpretación operativa |
|------|----:|-------:|---:|:---|
| 20 Kessler | 0.299 | 0.000 | 1.003 | Cascada Kessler-Liou: señal fuerte, marginalmente sub-umbral (0.30) |
| 27 Riesgo Biológico | 0.294 | 0.003 | 1.001 | Woolhouse Zoonotic: cascada bilineal significativa |
| 13 Políticas | 0.289 | 0.000 | 1.009 | Inercia Institucional North: señal significativa sub-umbral |
| 14 Postverdad | 0.252 | 0.000 | 1.009 | SIS Campo Medio: cascada de desinformación significativa |
| 05 Epidemiología | 0.129 | 0.000 | 1.009 | SEIR Kermack-McKendrick: señal significativa pero sub-umbral |
| 11 Movilidad | 0.128 | 0.002 | 1.004 | MFD: constricción detectable pero sub-umbral |

Estos seis casos presentan señal estadísticamente significativa (p < 0.05) y EDI entre 0.10 y 0.30. Son "componentes funcionales" — análogos a ribosomas en biología: contribuyen al sistema pero no constituyen unidades autónomas con cierre operativo pleno. Nótese que Kessler, Riesgo Biológico y Políticas están marginalmente por debajo del umbral 0.30 — candidatos prioritarios para refinamiento de modelos.

#### Nivel 2 — Señal Sugestiva

| Caso | EDI | p-perm | CR | Interpretación operativa |
|------|----:|-------:|---:|:---|
| 09 Finanzas | 0.081 | 0.000 | 2.616 | Señal estadísticamente significativa, falla C4 |
| 15 Wikipedia | 0.080 | 0.000 | 1.020 | Lotka-Volterra: señal significativa pero EDI bajo |
| 21 Salinización | 0.058 | 0.004 | 1.000 | Señal detectable, magnitud insuficiente |

El instrumento detecta señal estadística (p < 0.05 y EDI > 0.01) pero la magnitud no alcanza para atribuir cierre operativo pleno y/o fallan criterios técnicos adicionales. Son candidatos, no diagnósticos.

#### Nivel 1 — Tendencia no Significativa

| Caso | EDI | p-perm | Interpretación operativa |
|------|----:|-------:|:---|
| 01 Clima | 0.011 | 0.999 | ODE Budyko-Sellers insuficiente para este dominio |
| 10 Justicia | 0.227 | 0.477 | Señal no significativa |
| 26 Starlink | 0.690 | 1.000 | EDI alto pero sin significancia estadística |
| 28 Fuga Cerebros | 0.025 | 0.998 | Señal no significativa |

Estos casos muestran EDI positivo sin significancia estadística. El instrumento no detecta cierre operativo confirmado — esto puede reflejar inadecuación del modelo ODE o varianza excesiva en la muestra.

> **Nota importante:** El caso Starlink (EDI=0.690) presenta un EDI nominalmente alto pero carece completamente de significancia estadística (p=1.000), indicando que la señal es un artefacto de la calibración.

#### Nivel 0 — Sin Señal Operativa (8 Casos)

Conciencia (-0.117), Contaminación (-0.004), Paradigmas (-0.006), Océanos (-0.044), Acidificación (-0.000), Erosión Dialéctica (-1.000), Acuíferos (-0.021), IoT (-0.899).

Bajo irrealismo operativo, Nivel 0 no significa "el hiperobjeto no existe" — significa "el instrumento no detecta cierre operativo con la sonda actual". La diferencia es crucial: un termómetro que no detecta campo magnético no refuta el magnetismo.

#### Controles de Falsación (3/3 Correctos)
- 06 Falsación Exogeneidad: ruido sin estructura → rechazado (EDI=0.055, cat=falsification).
- 07 Falsación No-Estacionariedad: Random Walk → rechazado (EDI=-0.882, cat=falsification).
- 08 Falsación Observabilidad: estados ocultos → rechazado (EDI=-1.000).

### Métricas Globales de Robustez

| Métrica | Valor | Descripción |
|---------|-------|-------------|
| **overall_pass=True** | 5/29 | Casos con 13 criterios simultáneos |
| **Significancia** (p<0.05 + EDI>0.01) | 14/29 | Casos con señal estadística |
| **Reproducibilidad** | 100% | seed=42, 999 permutaciones |

## Análisis de Selectividad

### Distribución del paisaje (26 casos genuinos)

De los 26 casos genuinos (excluyendo 3 falsaciones):
- **5 overall_pass=True** (19.2%): cierre operativo verificado
- **6 Nivel 3** (23.1%): componentes funcionales
- **3 Nivel 2** (11.5%): señal sugestiva
- **4 Nivel 1** (15.4%): tendencia
- **8 Nivel 0** (30.8%): sin señal

La selectividad (19.2% pasan overall) es una distribución altamente exigente que demuestra que el instrumento no está sesgado hacia la confirmación. Con el umbral EDI ≥ 0.30, solo los casos con señal macro realmente fuerte alcanzan Nivel 4. Los 3 controles de falsación siguen siendo correctamente rechazados.

### Diversidad de Dominios
Los 29 casos cubren dominios físicos (clima, energía, océanos, acidificación), biológicos (deforestación, fósforo, riesgo biológico, epidemiología), económicos (finanzas), tecnológicos (Starlink, IoT, Kessler), culturales (paradigmas, erosión dialéctica, conciencia), sociales (urbanización, fuga de cerebros, movilidad, justicia, postverdad), hídricos (acuíferos, salinización), materiales (microplásticos, contaminación) y de gobernanza (políticas estratégicas, Wikipedia).

### El Patrón de la Inercia Material

```mermaid
quadrantChart
    title Matriz de Emergencia: EDI vs Significancia
    x-axis "No Significativo (p > 0.05)" --> "Significativo (p < 0.05)"
    y-axis "Baja Eficacia (EDI < 0.30)" --> "Alta Eficacia (EDI > 0.30)"
    quadrant-1 "Cierre Operativo Fuerte"
    quadrant-2 "EDI Alto Sin Confirmar"
    quadrant-3 "Sin Señal"
    quadrant-4 "Señal Débil Confirmada"
    "Microplásticos": [0.85, 0.9]
    "Energía": [0.85, 0.72]
    "Deforestación": [0.85, 0.65]
    "Urbanización": [0.85, 0.45]
    "Fósforo": [0.85, 0.43]
    "Kessler": [0.85, 0.4]
    "Riesgo Bio": [0.75, 0.38]
    "Políticas": [0.8, 0.38]
    "Postverdad": [0.85, 0.35]
    "Starlink": [0.15, 0.78]
    "Clima": [0.15, 0.1]
```

Los casos con overall_pass=True cubren dominios diversos: desde energía (0.650) hasta microplásticos oceánicos (0.806). Los seis casos de Nivel 3 (weak) — incluyendo Kessler (0.299), Riesgo Biológico (0.294) y Políticas (0.289) — están marginalmente por debajo del umbral 0.30, indicando candidatos prioritarios para refinamiento.

### Diagnóstico: ¿Por Qué Algunos Casos se Clasifican en Nivel 0-1?

1. **Modelos ODE inadecuados:** La sonda no captura la dinámica macro del dominio. Problema del instrumento, no del fenómeno.
2. **No-estacionariedad:** Cambios estructurales entre entrenamiento y validación.
3. **Coupling destructivo:** Sesgo del ODE destruye información útil en el ABM.
4. **Señal-ruido insuficiente:** La señal macro existe pero el ruido domina.

---

## Diálogo Dialéctico y Falsación del Instrumento

El rigor del instrumento no reside en la clasificación universal, sino en su capacidad para producir un gradiente coherente y falsable.

### 1. El Caso Clima (EDI=0.011 vs Umbral 0.30)
**Crítica:** El caso paradigmático (Clima) queda en Nivel 1.
**Respuesta:** Bajo irrealismo operativo, esto es informativo, no problemático. El instrumento clasifica el clima regional bajo ODE Budyko-Sellers como un sistema sin cierre operativo fuerte en la resolución actual. Esto refina la taxonomía sin invalidar el instrumento. La honestidad de no forzar el resultado demuestra rigor.

### 2. Información Efectiva (EI) y sus Limitaciones
**Crítica:** El EI produce valores negativos en sistemas socio-técnicos.
**Respuesta:** La EI negativa indica que los residuos del modelo completo son más entrópicos que los del reducido. El EDI permanece como métrica principal porque mide eficacia predictiva sin supuestos sobre entropía residual.

### 3. Resolución 20×20 (400 agentes)
**Crítica:** 400 agentes son insuficientes para simular hiperobjetos planetarios.
**Respuesta:** El motor HybridModel es un instrumento de prueba de concepto. Pruebas de escalamiento (100 a 1600 agentes) muestran que EDI y CR se estabilizan rápidamente, sugiriendo invariancia a la escala por encima del umbral de masa crítica.

### 4. Circularidad en la Calibración
**Crítica:** Calibración y nudging son "ventriloquismo".
**Respuesta:** Circularidad eliminada: calibración en ventana de entrenamiento, evaluación en ventana de prueba con `assimilation_strength=0.0`. Verificado en 9 ubicaciones del código (`hybrid_validator.py`).

---

## Conclusiones

### Resultado principal: Paisaje de Emergencia Operativa completamente mapeado

El resultado no es "5/29 pasan" — es un **mapa completo** de 29 fenómenos posicionados en un gradiente de cierre operativo de 6 niveles:

| Nivel | Interpretación | Casos | Significado operativo |
|:-----:|:---|:---:|:---|
| 4 | Cierre operativo fuerte | 5 | Constructo macro indispensable |
| 3 | Componente funcional | 6 | Constricción significativa sub-umbral |
| 2 | Señal sugestiva | 3 | Candidato, resolución insuficiente |
| 1 | Tendencia | 4 | Sin significancia estadística |
| 0 | Sin señal | 8 | Instrumento no detecta cierre |
| — | Falsificación correcta | 3 | Controles negativos funcionan |

### Valor epistemológico bajo irrealismo operativo

1. **El instrumento es falsable:** El protocolo de validación con zero-nudging y permutation test descarta EDI inflados. El instrumento no es un rubber-stamp.
2. **Los controles de falsación funcionan:** 3/3 correctamente rechazados.
3. **La selectividad es discriminante:** 19.2% de casos genuinos alcanzan overall_pass (umbral EDI ≥ 0.30), con una distribución coherente a lo largo del gradiente.
4. **El gradiente es coherente:** Los fenómenos con inercia material, cascadas cuadráticas y ciclos biogeoquímicos se clasifican más alto, consistente con la teoría.
5. **Sin compromiso ontológico:** Nunca afirmamos "X es un hiperobjeto". Afirmamos "X exhibe cierre operativo de grado G según este instrumento".

### H1 — Hipótesis Central

**Un fenómeno exhibe cierre operativo de grado G cuando la eliminación de su constructo macro degrada la predicción micro en una proporción EDI ≥ G/100, verificable mediante el protocolo C1-C5 con zero-nudging.**

La tesis demuestra que ciertos fenómenos **funcionan como si tuvieran estructura macro autónoma**, y proporciona un instrumento calibrado para medir ese "como si" con precisión y honestidad.

---

# 04 Casos de Estudio: El Emergentómetro en Acción

Un instrumento de medición se valida por su capacidad de discriminar. Un termómetro que siempre marca 37°C es inútil. El Emergentómetro se aplicó a **29 fenómenos de dominios radicalmente distintos** — desde la física de debris orbital (Kessler) hasta la dinámica de postverdad en redes sociales — y produjo un gradiente amplio: desde EDI=-1.000 (sin señal, Erosión Dialéctica) hasta EDI=0.806 (señal muy fuerte, Microplásticos). Esta diversidad de resultados es la mejor evidencia de que el instrumento no está diseñado para "confirmar" hiperobjetos, sino para medirlos sin sesgos.

## Paisaje de Emergencia Operativa
El motor de simulación ha sido ejecutado sobre un universo de **29 casos**, tras la remoción de 3 casos por inviabilidad de datos reales. El protocolo C1-C5 + 8 criterios adicionales actúan como instrumento de **clasificación operativa**, permitiendo mapear el fenómeno en un gradiente de cierre.

Los resultados cuantitativos detallados (EDI, p-valores, CR) y la clasificación técnica definitiva se consolidan exclusivamente en la **Sección 03 Validación y Praxis**. Esta sección provee el contexto cualitativo y la justificación de las fuentes de datos para los casos más relevantes del paisaje.

---

## 1. Casos de Cierre Operativo Fuerte (Nivel 4 — overall_pass=True)

Representan los fenómenos donde el constructo macro es operativamente indispensable para la predicción micro. Cinco casos alcanzan este nivel con EDI ≥ 0.30 y las 13 condiciones simultáneas satisfechas.

*   **Microplásticos Oceánicos (ID 24):** Datos de OWID (Plastic Production). EDI=0.806 — el EDI más alto del corpus entre los overall_pass=True. El modelo Jambeck de acumulación persistente genera una constricción fuerte. BC=bias_only.
*   **Energía (ID 04):** Datos OPSD (producción energética). Modelo Lotka-Volterra de competencia energética con adopción tecnológica tipo TIMES. EDI=0.650. La constricción macro es fuertemente indispensable. BC=bias_only.
*   **Deforestación Global (ID 16):** Datos del World Bank (Área forestal). EDI=0.580. La ODE de frontera agrícola (von Thünen) captura la inercia del desplazamiento físico de la frontera forestal. BC=full.
*   **Urbanización (ID 18):** Datos World Bank (Población urbana). Logística con atracción económica y Preferential Attachment. EDI=0.337. Los patrones de urbanización exhiben cierre operativo. BC=full.
*   **Fósforo (ID 22):** Datos World Bank (Uso de fertilizantes). Ciclo biogeoquímico Carpenter. EDI=0.322. El ciclo del fósforo exhibe constricción macro robusta. BC=full.

---

## 2. Componentes Funcionales (Nivel 3 — weak)

Fenómenos con señal estadísticamente significativa y EDI entre 0.10-0.30 pero que no alcanzan overall_pass=True.

*   **Kessler (ID 20):** Datos CelesTrak (Desechos orbitales). Cascada cuadrática Kessler-Liou. EDI=0.299, p=0.000. La dinámica de debris orbital presenta constricción macro fuerte, marginalmente sub-umbral (0.30).
*   **Riesgo Biológico (ID 27):** Datos World Bank (Mortalidad). Cascada zoonótica Woolhouse. EDI=0.294, p=0.003. La dinámica One Health exhibe señal significativa sub-umbral.
*   **Políticas Estratégicas (ID 13):** Datos World Bank (Gasto militar). Inercia Institucional basada en North (1990). EDI=0.289, p=0.000. Las instituciones exhiben constricción macro significativa sub-umbral.
*   **Postverdad (ID 14):** Modelo SIS de Campo Medio para cascadas de desinformación. EDI=0.252, p=0.000. Señal significativa pero sub-umbral para cierre pleno.
*   **Epidemiología (ID 05):** Datos OWID (COVID-19). SEIR Kermack-McKendrick. EDI=0.129, p=0.000. Señal significativa pero sub-umbral para cierre operativo pleno.
*   **Movilidad (ID 11):** Datos World Bank (Tráfico aéreo). MFD con dinámica Greenshields. EDI=0.128, p=0.002. Constricción detectable pero insuficiente para overall_pass.

---

## 3. Señales Sugestivas (Nivel 2)

Fenómenos donde el instrumento detecta una señal estadísticamente significativa pero de magnitud insuficiente o con criterios técnicos no satisfechos.

*   **Finanzas (ID 09):** Datos de Yahoo Finance (SPY). EDI=0.081. La reflexividad inherente a los mercados (Soros, 1987) dificulta la separación macro/micro. Señal significativa (p=0.000) pero falla C4. CR=2.616 (único caso con CR > 2.0).
*   **Wikipedia (ID 15):** Datos Wikimedia. Lotka-Volterra aplicado a la dinámica calidad-controversia. EDI=0.080, p=0.000. Señal significativa pero EDI por debajo del umbral de componente funcional.
*   **Salinización (ID 21):** Datos World Bank (Tierras irrigadas). EDI=0.058. Señal detectable (p=0.004) pero magnitud insuficiente.

---

## 4. Otros Fenómenos del Paisaje (Niveles 0-1)

Incluye el caso paradigmático de **Clima Regional (ID 01)** (datos Meteostat/NOAA, EDI=0.011). Bajo el modelo Budyko-Sellers y la resolución actual, el instrumento no detecta un cierre operativo fuerte. Bajo irrealismo operativo, esto no refuta el fenómeno, sino que diagnostica la insuficiencia de la sonda particular para detectarlo en esta escala regional.

Caso notable en Nivel 1 con EDI nominalmente alto pero sin significancia estadística: **Starlink (EDI=0.690, p=1.000)** — carece de significancia, indicando señal artefactual.

8 casos se sitúan en Nivel 0, incluyendo Conciencia (EDI=-0.117), indicando que el modelo híbrido no detecta constricción macro o que el acoplamiento es incluso destructivo (anti-emergencia).

---

## 5. Controles de Falsación (3/3 Correctos)
Sistemas diseñados para probar la selectividad del protocolo: **Exogeneidad (06)**, **No-estacionariedad (07)** y **Observabilidad (08)**. Los tres controles son correctamente rechazados (falsification), confirmando que el instrumento no es un "rubber-stamp" y requiere estructura genuina para validar un caso.

---

## 6. Casos Removidos (Archivo)
Descartados por falta de fuentes de datos reales verificables: **Estética Global**, **Moderación Adversarial** y **RTB Publicidad**. Archivados en `Artifacts/casos_removidos/`.

---

## Conclusión: El Paisaje como Resultado Principal
La distribución actual (5 overall_pass, 6 weak, 3 suggestive, 4 trend, 8 null, 3 falsification) constituye un paisaje rico y discriminante. Los 3 controles de falsación correctamente rechazados garantizan que las clasificaciones positivas representan cierre operativo genuino. El mapa completo constituye el resultado principal de la tesis: un mapeo honesto y riguroso de la eficacia causal en el paisaje de los fenómenos masivamente distribuidos.

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

## 05_Bibliografia
- Ver carpeta `05_Bibliografia/` para referencias nucleares y fuentes de datos.

---

# Indice: EjerciciosCriticos

- Ejercicio Gladiadores Partida 1:
  - `EjerciciosCriticos/Ejercicio_Critico_Gladiadores_Partida1.md`
- Trazas, Posibles y Dudas:
  - `EjerciciosCriticos/Trazas_Mejoras_Possibles_Dudas.md`

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

# 05 Bibliografía Nuclear

## Bibliografía Nuclear (37 fuentes)
1. Morton, T. (2013). *Hyperobjects: Philosophy and Ecology after the End of the World*. University of Minnesota Press.
2. Harman, G. (2018). *Object-Oriented Ontology: A New Theory of Everything*. Pelican Books.
3. Latour, B. (2017). *Facing Gaia: Eight Lectures on the New Climatic Regime*. Polity Press.
4. Bennett, J. (2010). *Vibrant Matter: A Political Ecology of Things*. Duke University Press.
5. Bunge, M. (1979). *Treatise on Basic Philosophy, Volume 4: Ontology II: A World of Systems*. Reidel.
6. Bueno, G. (1978). *Ensayos materialistas*. Taurus.
7. Popper, K. (1959). *The Logic of Scientific Discovery*. Hutchinson.
8. Lakatos, I. (1978). *The Methodology of Scientific Research Programmes*. Cambridge University Press.
9. Luhmann, N. (1995). *Social Systems*. Stanford University Press.
10. Haken, H. (1983). *Synergetics: An Introduction*. Springer-Verlag.
11. Shannon, C. E. (1948). "A Mathematical Theory of Communication". *Bell System Technical Journal*.
12. Holland, J. H. (1995). *Hidden Order: How Adaptation Builds Complexity*. Addison-Wesley.
13. Schelling, T. C. (1978). *Micromotives and Macrobehavior*. W. W. Norton & Company.
14. Strogatz, S. H. (2014). *Nonlinear Dynamics and Chaos*. Westview Press.
15. Soros, G. (1987). *The Alchemy of Finance*. Simon & Schuster.
16. Taleb, N. N. (2012). *Antifragile: Things That Gain from Disorder*. Random House.
17. Evensen, G. (2009). *Data Assimilation: The Ensemble Kalman Filter*. Springer.
18. Ladyman, J. & Ross, D. (2007). *Every Thing Must Go: Metaphysics Naturalized*. Oxford University Press.
19. Woodward, J. (2003). *Making Things Happen: A Theory of Causal Explanation*. Oxford University Press.
20. Dennett, D. (1991). "Real Patterns". *The Journal of Philosophy*.
21. Batterman, R. (2002). *The Devil in the Details: Asymptotic Reasoning in Explanation, Reduction, and Emergence*. Oxford University Press.
22. Humphreys, P. (2016). *Emergence: A Philosophical Account*. Oxford University Press.
23. Chalmers, D. (2006). "Strong and Weak Emergence". En *The Re-Emergence of Emergence*. Oxford University Press.
24. Bedau, M. (1997). "Weak Emergence". *Philosophical Perspectives*.
25. Kim, J. (1999). "Making Sense of Emergence". *Philosophical Studies*.
26. O'Connor, T. & Wong, H. Y. (2005). "The Metaphysics of Emergence". *Noûs*.
27. Hoel, E. P. (2017). "When the Map Is Better Than the Territory". *Entropy*.
28. Budyko, M. I. (1969). "The effect of solar radiation variations on the climate of the Earth". *Tellus*.
29. Sellers, W. D. (1969). "A global climatic model based on the energy balance of the earth-atmosphere system". *Journal of Applied Meteorology*.
30. von Thünen, J. H. (1826). *Der Isolirte Staat in Beziehung auf Landwirthschaft und Nationalökonomie*.
31. Jambeck, J. R., et al. (2015). "Plastic waste inputs from land into the ocean". *Science*.
32. Docquier, F. & Rapoport, H. (2012). "Globalization, Brain Drain, and Development". *Journal of Economic Literature*.
33. van Fraassen, B. C. (1980). *The Scientific Image*. Oxford University Press.
34. Psillos, S. (1999). *Scientific Realism: How Science Tracks Truth*. Routledge.
35. Kant, I. (1781). *Kritik der reinen Vernunft*.
36. Kermack, W. O. & McKendrick, A. G. (1927). "A Contribution to the Mathematical Theory of Epidemics". *Proceedings of the Royal Society A*.
37. North, D. C. (1990). *Institutions, Institutional Change and Economic Performance*. Cambridge University Press.

## Fuentes de Datos (Repositorios Principales)
- **World Bank Open Data:** Indicadores de desarrollo, deforestación, movilidad y urbanización.
- **Our World in Data (OWID):** Producción de plásticos, energía y emisiones.
- **Meteostat / NOAA:** Series temporales climáticas.
- **Yahoo Finance:** Series temporales de mercados de capitales (SPY).
- **CelesTrak:** Datos de catálogo de satélites (TLE) para el caso Kessler.
- **Wikimedia Statistics:** Datos de actividad de Wikipedia y proyectos hermanos.