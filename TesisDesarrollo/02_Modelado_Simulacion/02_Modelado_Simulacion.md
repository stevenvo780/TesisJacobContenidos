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

## Arquitectura y Ejecución de los 32 Casos
La arquitectura actual del proyecto integra **32 motores de simulación completamente funcionales** y ejecutables. Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas.

Esta infraestructura permite una reproducibilidad total del EDI y CR reportados, eliminando la dependencia de métricas pre-generadas. El sistema utiliza datos reales de fuentes como World Bank, Wikimedia, Meteostat y yfinance para los casos de alta fidelidad, y generadores estocásticos controlados para los casos de falsación. Los 11 casos nuevos (22-32) amplían la cobertura a dominios como acidificación oceánica, uso de fósforo, acuíferos, conectividad digital (IoT/Starlink), capital intelectual, erosión discursiva, microplásticos, basura espacial y riesgo biológico.

### Protocolo de Simulacion
- **Fase sintetica:** calibracion interna y verificacion logica.
- **Fase real:** validacion con datos historicos.
- **Zero-Nudging:** En la versión final, la evaluación se realiza sin nudging (`assimilation_strength=0.0`) para medir la emergencia pura del acoplamiento macro.

## Criterios Tecnicos de Validación
- **EDI > 0.30:** condición necesaria de H1 — indica eficacia causal macro (emergencia fuerte).
- **CR > 2.0:** indicador complementario de frontera sistémica (no condición de H1).
- **C1-C5:** Protocolo de rigor aplicado a la convergencia, robustez, replicación, validez y gestión de incertidumbre.
- **overall_pass:** 11 condiciones simultáneas (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento ≥ 0.1, no-fraude RMSE).

## Resultados Consolidados (Matriz de Validación Técnica)

La siguiente tabla resume los resultados obtenidos tras la ejecución del pipeline completo en los 32 motores. Los valores representan el desempeño del modelo en modo **Zero-Nudging** (`assimilation_strength = 0.0`). Ejecución: Torre 32-core AMD 9950X3D, 16 workers paralelos, commit `323c254`. Optimizaciones: clamping numérico [-50,50], gating C2-C4, calibración ultra (grid 6400 combos, top 10 refinamiento × 5000 iteraciones, early stop 300), symploké con tolerancia numérica 1e-3. Datos reales del World Bank, Meteostat y yfinance.

### Bloque I — Casos Originales (01–21)

| Caso | EDI | EI | CR | corr | overall_pass | Estado |
| :--- | ---: | ---: | ---: | ---: | :---: | :--- |
| 01_caso_clima | 0.425 | 0.542 | 1.002 | 0.822 | ✅ | **Validado** |
| 02_caso_conciencia | -0.323 | -0.386 | 0.999 | -0.669 | ❌ | Rechazado |
| 03_caso_contaminacion | 0.124 | 0.243 | 1.365 | 0.711 | ❌ | Parcial (emergence✗) |
| 04_caso_energia | 0.351 | 0.327 | 1.116 | 0.789 | ✅ | **Validado** |
| 05_caso_epidemiologia | 0.172 | 0.200 | 0.830 | 0.743 | ❌ | Rechazado |
| 06_caso_estetica | 0.032 | -0.003 | — | 0.079 | ❌ | Rechazado |
| 07_caso_falsacion_exogeneidad | -0.959 | -0.441 | — | -0.183 | ❌ | **Control ❌** |
| 08_caso_falsacion_no_estacionariedad | 0.083 | 0.310 | — | 0.842 | ❌ | **Control ❌** |
| 09_caso_falsacion_observabilidad | 0.000 | 0.000 | — | — | ❌ | **Control ❌** |
| 10_caso_finanzas | 0.880 | 1.218 | 1.248 | 0.996 | ✅ | **Validado** |
| 11_caso_justicia | -0.237 | 0.037 | 0.999 | 0.408 | ❌ | Rechazado |
| 12_caso_moderacion_adversarial | 0.004 | -0.019 | — | 0.143 | ❌ | Rechazado |
| 13_caso_movilidad | 0.070 | -0.497 | 1.149 | 0.500 | ❌ | Rechazado |
| 14_caso_paradigmas | 0.657 | 0.882 | 1.001 | 0.953 | ✅ | **Validado** |
| 15_caso_politicas_estrategicas | 0.294 | -0.103 | 1.012 | 0.008 | ❌ | Parcial (EDI≈0.30, corr↓) |
| 16_caso_postverdad | 0.310 | -0.117 | 1.000 | -0.051 | ❌ | Parcial (EDI>0.30, corr↓) |
| 17_caso_rtb_publicidad | 0.426 | 0.464 | 1.030 | 0.755 | ✅ | **Validado** |
| 18_caso_wikipedia | 0.017 | 0.070 | 1.151 | 0.309 | ❌ | Rechazado |
| 19_caso_deforestacion | 0.846 | 0.850 | 1.000 | 0.919 | ✅ | **Validado** |
| 20_caso_oceanos | 0.737 | -0.433 | 1.005 | 0.361 | ❌ | Parcial (EDI alto, corr↓) |
| 21_caso_urbanizacion | 0.840 | 1.411 | 1.000 | 0.999 | ✅ | **Validado** |

### Bloque II — Casos Nuevos (22–32)

| Caso | EDI | EI | CR | corr | overall_pass | Estado |
| :--- | ---: | ---: | ---: | ---: | :---: | :--- |
| 22_caso_acidificacion_oceanica | 0.737 | -0.433 | 1.005 | 0.361 | ❌ | Parcial (C1✗, corr baja) |
| 23_caso_kessler | 0.704 | 0.287 | 1.002 | 0.499 | ❌ | Parcial (C1✗, corr media) |
| 24_caso_salinizacion | 0.164 | -0.103 | — | -0.275 | ❌ | Rechazado (corr negativa) |
| 25_caso_fosforo | 0.901 | 0.711 | 1.000 | 0.881 | ✅ | **Validado** |
| 26_caso_erosion_dialectica | 0.739 | 0.244 | 1.000 | 0.992 | ❌ | Parcial (C1✗, persist✗) |
| 27_caso_microplasticos | 0.432 | 0.792 | 4.359 | 0.917 | ❌ | Parcial (sym✗) |
| 28_caso_acuiferos | 0.866 | 0.815 | 1.000 | 1.000 | ✅ | **Validado** |
| 29_caso_starlink | 0.928 | 1.984 | 1.000 | 0.994 | ✅ | **Validado** |
| 30_caso_riesgo_biologico | 0.917 | 1.010 | 0.989 | 0.988 | ❌ | Parcial (sym✗, persist✗) |
| 31_caso_fuga_cerebros | 0.433 | 0.631 | 0.999 | 0.970 | ✅ | **Validado** |
| 32_caso_iot | 0.477 | 0.916 | 1.000 | 0.995 | ❌ | Parcial (C1✗) |

### Matriz de Protocolo Completa (32 casos × 11 criterios)

Cada celda indica el resultado del criterio en la **Fase Real** (`assimilation_strength = 0.0`). Un caso es **Validado** solo si las 11 condiciones son ✓ simultáneamente.

| # | Caso | EDI | C1 | C2 | C3 | C4 | C5 | Sym | NL | Per | Emr | Cp | Result |
| :--- | :--- | ---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| 01 | Clima | 0.425 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 02 | Conciencia | -0.323 | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 03 | Contaminación | 0.124 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 04 | Energía | 0.351 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 05 | Epidemiología | 0.172 | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 06 | Estética | 0.032 | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 07 | Falsación Exogeneidad | -0.966 | ✗ | ✗ | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ | Control ❌ |
| 08 | Falsación No-Estacionariedad | -0.049 | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | Control ❌ |
| 09 | Falsación Observabilidad | 0.000 | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | Control ❌ |
| 10 | Finanzas | 0.880 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 11 | Justicia | -0.237 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 12 | Moderación Adversarial | 0.004 | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 13 | Movilidad | 0.070 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Rechazado |
| 14 | Paradigmas | 0.656 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 15 | Políticas Estratégicas | 0.294 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Rechazado |
| 16 | Postverdad | 0.310 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Rechazado |
| 17 | RTB Publicidad | 0.426 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 18 | Wikipedia | 0.017 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | Rechazado |
| 19 | Deforestación | 0.846 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 20 | Océanos | 0.737 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Rechazado |
| 21 | Urbanización | 0.840 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 22 | Acidificación Oceánica | 0.737 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Rechazado |
| 23 | Kessler | 0.704 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Rechazado |
| 24 | Salinización | 0.164 | ✗ | ✗ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | Rechazado |
| 25 | Fósforo | 0.901 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 26 | Erosión Dialéctica | 0.739 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | Rechazado |
| 27 | Microplásticos | 0.432 | ✓ | ✓ | ✓ | ✓ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ | Rechazado |
| 28 | Acuíferos | 0.866 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 29 | Starlink | 0.928 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 30 | Riesgo Biológico | 0.917 | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✗ | ✓ | ✓ | Rechazado |
| 31 | Fuga Cerebros | 0.433 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **Validado** |
| 32 | IoT | 0.477 | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | Rechazado |

**Nota sobre la Tabla:** C1-C5 = Criterios del protocolo de validación. Sym = Symploké, NL = No-localidad, Per = Persistencia, Emr = Emergencia, Cp = Coupling ≥ 0.1. `overall_pass` = todas las 11 condiciones ✓ simultáneamente. Los 3 controles de falsación (07-09) están diseñados para fallar y lo hacen correctamente.

### Análisis de Selectividad del Protocolo

De los 32 casos evaluados: **11 validados**, **18 rechazados genuinos**, **3 controles de falsación** correctamente rechazados.

**Distribución de modos de fallo** en los 18 rechazados genuinos:

| Criterio | Fallos | % | Rol |
| :--- | :---: | :---: | :--- |
| C1 (Convergencia) | 14/18 | 78% | Filtro más selectivo — exige RMSE < obs_std en escala Z |
| Emergence | 7/18 | 39% | Exige que el modelo acoplado supere al ABM aislado |
| Symploké | 7/18 | 39% | Cohesión interna ≥ externa (topología) |
| Persistencia | 3/18 | 17% | Estabilidad temporal de la señal macro |
| C5 (Incertidumbre) | 2/18 | 11% | Bootstrap del EDI debe mantenerse en [0.30, 0.90] |
| C2 (Robustez) | 1/18 | 6% | Estabilidad bajo perturbación de parámetros |

**Prueba de no-tautología — 8 casos con EDI > 0.30 rechazados:**

| Caso | EDI | Criterios que fallan | Interpretación |
| :--- | ---: | :--- | :--- |
| Riesgo Biológico | 0.917 | Sym, Per | Señal macro fuerte pero sin coherencia topológica ni temporal |
| Erosión Dialéctica | 0.739 | C1, Per | Tendencia global pero convergencia y persistencia insuficientes |
| Océanos | 0.737 | C1 | EDI alto pero ABM no converge — señal sin modelo micro adecuado |
| Acidificación Oceánica | 0.737 | C1 | Estructura macro pero calibración insuficiente |
| Kessler | 0.704 | C1 | Tráfico aéreo con shock COVID-19 destruye convergencia |
| IoT | 0.477 | C1 | Tendencia clara pero ABM no alcanza RMSE suficiente |
| Microplásticos | 0.432 | C5, Sym | Señal detectable pero coherencia topológica insuficiente |
| Postverdad | 0.310 | C1 | EDI marginal y C1 falla — señal macro débil |

Este resultado es **central para la tesis**: un EDI alto no garantiza validación. El protocolo C1-C5 actúa como filtro multi-criterio que elimina falsos positivos. Si la metodología fuera un *rubber stamp*, estos 8 casos pasarían. No pasan.

## Análisis de Evidencia y Hallazgos

Los 32 casos demuestran que el modelo híbrido funciona como **herramienta de demarcación operativa**: discrimina entre sistemas con estructura macro detectable y sistemas sin ella.

**Emergencia Muy Fuerte (EDI > 0.80) — 6 casos validados:**
- **Starlink** (EDI=0.928): Conectividad digital global como hiperobjeto.
- **Fósforo** (EDI=0.901): Ciclo global de fósforo como hiperobjeto agrícola-ambiental.
- **Finanzas** (EDI=0.880): Mercados financieros globales como estructura macro dominante.
- **Acuíferos** (EDI=0.866): Acceso global a agua potable como hiperobjeto hídrico.
- **Deforestación** (EDI=0.846): Políticas globales reducen la entropía local en un 85%.
- **Urbanización** (EDI=0.840): Tendencia macro de urbanización constrinye los patrones micro.

**Emergencia Fuerte (0.30 < EDI < 0.80) — 5 casos validados:**
- **Paradigmas** (EDI=0.656): Estructuras culturales capturadas con alta fidelidad.
- **Fuga de Cerebros** (EDI=0.433): Inversión global en I+D como proxy de capital intelectual.
- **Clima** (EDI=0.425): El modelo macro reduce el RMSE en 42% respecto al ABM aislado.
- **RTB Publicidad** (EDI=0.426): Dinámica de mercado publicitario detectable.
- **Energía** (EDI=0.351): Señal macro robusta en consumo energético.

Los 3 controles de falsación (exogeneidad, no-estacionariedad, observabilidad) fallan correctamente, confirmando que el marco **no es tautológico**.

## C5 — Bitácora de Correcciones y Reporte de Fallos

### Corrección 2026-02-06: Bug EI=0.0 (Información Efectiva)

**Problema detectado:** Los archivos `metrics.json` de los 18 casos almacenaban `effective_information: 0.0` de forma sistemática. El valor nulo se debía a una versión anterior de la función `effective_information()` en `repos/Simulaciones/common/hybrid_validator.py` que no persistía correctamente el cálculo KDE.

**Corrección:** Re-ejecución de `validate.py` en los casos 01 (Clima), 03 (Contaminación) y 13 (Movilidad) con el código corregido. Resultados:

| Caso | Fase | EI anterior | EI corregido |
|------|------|:-----------:|:------------:|
| 01_Clima | synthetic | 0.0 | 0.871 |
| 01_Clima | real | 0.0 | 0.002 |
| 03_Contaminación | synthetic | N/A | 0.048 |
| 03_Contaminación | real | N/A | -0.022 |
| 13_Movilidad | synthetic | 0.0 | 0.633 |
| 13_Movilidad | real | N/A | -0.347 |

**Commit de referencia:** `4264f4a` (branch main).

**Nota:** EI es métrica complementaria, no criterio de existencia de H1. H1 se define por EDI > 0.30 y el protocolo C1-C5. La corrección de EI no altera los criterios de validación.

### Corrección 2026-02-06: Eliminación de assimilation_strength en calibración

**Problema detectado:** Versiones anteriores del calibrador usaban `assimilation_strength > 0` durante la fase de calibración (grid-search), permitiendo que el modelo accediera a observaciones futuras durante el ajuste.

**Corrección:** El código actual fuerza `assimilation_strength = 0.0` tanto en calibración como en evaluación. Esto hace el framework más estricto: los casos deben demostrar emergencia sin ningún tipo de nudging observacional.

**Impacto:** Algunos casos que pasaban con la calibración anterior (ej. Contaminación real, EDI antiguo ≈ 0.42) ahora no pasan (EDI fresco = -0.076). Esto demuestra que el marco es **falsable** y **autocorrectivo**.

## Regla Operacional: Divergencia EDI/CR

El CR (Cohesion Ratio = internal/external) es un **indicador complementario de frontera**, no una condición necesaria de H1. H1 se define exclusivamente por EDI > 0.30 + C1-C5 (§ Hipótesis Central, línea 17 de `00_Marco_Conceptual`). El CR informa sobre la topología del acoplamiento.

Clasificación descriptiva cuando EDI y CR divergen:

1. **EDI > 0.30, CR < 2.0, C1-C5 = True**: Emergencia funcional con frontera difusa → **Validado** (H1 satisfecho). CR ≈ 1.0 es esperado en modelos de difusión espacial homogénea.
2. **EDI > 0.30, CR > 2.0, C1-C5 = True**: Emergencia completa con frontera nítida → **Validado**.
3. **EDI < 0.30, CR > 2.0**: Cohesión sin eficacia causal → **Parcial**.
4. **EDI < 0.30, CR < 2.0**: Sin emergencia ni cohesión → **Rechazado**.

**Nota:** El validador (`hybrid_validator.py`, L656) implementa `overall_pass` con 11 condiciones (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento, no-fraude). El CR se computa como métrica informativa pero no es condición de `overall_pass`, coherente con H1.

**Caso Clima real** (EDI=0.424, CR=1.002) satisface H1: emergencia funcional con reducción del 42% en RMSE.

## Limitaciones del Marco de Hoel: EI Negativo en Sistemas Socio-Técnicos

### El Problema

La Información Efectiva (EI) de Hoel, diseñada para cuantificar la ventaja causal del nivel macro sobre el micro, produce **valores negativos** en varios casos reales:

| Caso | EI real | Interpretación |
|------|:---:|---|
| Movilidad | -0.347 | El macro genera residuos más entrópicos que el modelo reducido |
| Contaminación | -0.022 | Efecto marginal negativo |
| Clima | 0.002 | Efecto nulo/marginal |

### Diagnóstico

La EI negativa indica que los residuos del modelo completo (ABM+ODE) son **más entrópicos** que los del modelo reducido (ABM solo). Esto ocurre cuando el modelo macro extrae la señal estructurada y deja residuos que son ruido puro — de mayor entropía que los residuos parcialmente estructurados del modelo sin macro.

Críticamente, esto **coexiste con EDI positivo** (ej. Movilidad: EI=-0.347 pero EDI=0.385). El modelo predice mejor (menor RMSE) pero sus errores son más aleatorios. Esta disociación entre eficacia predictiva (EDI) e información efectiva (EI) constituye una **limitación fundamental** del marco de Hoel aplicado a sistemas socio-técnicos ruidosos.

### Implicaciones para la Tesis

1. **EI no puede ser condición necesaria de H1** en su forma actual. La Condición de Emergencia Informacional (§ Marco Conceptual) queda restringida a sistemas con señal-ruido alto (ej. fase sintética, donde EI es consistentemente positivo).
2. **EDI permanece como métrica principal** de eficacia causal descendente, dado que mide reducción de error predictivo sin supuestos sobre la entropía de los residuos.
3. **Trabajo futuro:** Desarrollar una variante de EI que normalice por la entropía del baseline o que use información mutua condicional en lugar de diferencia de entropías.

Esta limitación se descubrió durante el proceso adversarial de validación (Gladiadores, Iteraciones 3-6) y se registra aquí como parte del protocolo C5 de reporte de fallos.

## Auditoria de Consistencia
Ver `Auditoria_Simulaciones.md` para hallazgos y recomendaciones detalladas sobre la calidad de los datos y el comportamiento de las métricas en casos de borde.
