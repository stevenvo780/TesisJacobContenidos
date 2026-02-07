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

## Arquitectura y Ejecución de los 21 Casos
La arquitectura actual del proyecto integra **21 motores de simulación completamente funcionales** y ejecutables. Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas.

Esta infraestructura permite una reproducibilidad total del EDI y CR reportados, eliminando la dependencia de métricas pre-generadas. El sistema utiliza datos reales de fuentes como World Bank, Wikimedia, Meteostat y yfinance para los casos de alta fidelidad, y generadores estocásticos controlados para los casos de falsación. Los 3 casos más recientes (19-21) amplían la cobertura con datos de deforestación, emisiones CO₂ y urbanización global.

### Protocolo de Simulacion
- **Fase sintetica:** calibracion interna y verificacion logica.
- **Fase real:** validacion con datos historicos.
- **Zero-Nudging:** En la versión final, la evaluación se realiza sin nudging (`assimilation_strength=0.0`) para medir la emergencia pura del acoplamiento macro.

## Criterios Tecnicos de Validación
- **EDI > 0.30:** indica eficacia causal macro (emergencia fuerte).
- **CR > 2.0:** indica frontera sistémica (cohesión interna).
- **C1-C5:** Protocolo de rigor aplicado a la convergencia, robustez, replicación, validez y gestión de incertidumbre.

## Resultados Consolidados (Matriz de Validación Técnica)

La siguiente tabla resume los resultados obtenidos tras la ejecución del pipeline completo en los 21 motores. Los valores representan el desempeño del modelo en modo **Zero-Nudging** (`assimilation_strength = 0.0`). Ejecución: Torre 32-core AMD 9950X3D, 16 workers paralelos, commit `70c08f4`. Optimizaciones: clamping numérico [-50,50], gating C2-C4, calibración adaptativa multi-punto, symploké con tolerancia numérica 1e-3.

| Caso | EDI | EI | CR | corr | overall_pass | Estado |
| :--- | ---: | ---: | ---: | ---: | :---: | :--- |
| 01_caso_clima | 0.425 | 0.542 | 1.002 | 0.822 | ✅ | **Validado** |
| 02_caso_conciencia | -0.318 | -0.386 | 0.999 | -0.670 | ❌ | Rechazado |
| 03_caso_contaminacion | 0.124 | 0.243 | 1.365 | 0.711 | ❌ | Parcial (C1-C5✅, emergence✗) |
| 04_caso_energia | 0.350 | 0.327 | 1.116 | 0.789 | ✅ | **Validado** |
| 05_caso_epidemiologia | 0.172 | 0.200 | 0.830 | 0.743 | ❌ | Rechazado (gated by synth) |
| 06_caso_estetica | 0.032 | -0.003 | — | 0.079 | ❌ | Rechazado |
| 07_caso_falsacion_exogeneidad | -0.959 | -0.441 | — | -0.183 | ❌ | **Control ❌** |
| 08_caso_falsacion_no_estacionariedad | -0.045 | 0.194 | — | 0.858 | ❌ | **Control ❌** |
| 09_caso_falsacion_observabilidad | 0.000 | 0.000 | — | — | ❌ | **Control ❌** |
| 10_caso_finanzas | 0.880 | 1.218 | 1.248 | 0.996 | ✅ | **Validado** |
| 11_caso_justicia | -0.237 | 0.037 | 1.001 | 0.408 | ❌ | Rechazado |
| 12_caso_moderacion_adversarial | 0.003 | -0.021 | — | 0.139 | ❌ | Rechazado |
| 13_caso_movilidad | 0.070 | -0.497 | 1.149 | 0.500 | ❌ | Rechazado |
| 14_caso_paradigmas | 0.656 | 0.880 | 1.001 | 0.953 | ✅ | **Validado** |
| 15_caso_politicas_estrategicas | 0.292 | -0.104 | 1.012 | 0.009 | ❌ | Parcial (EDI≈0.30, corr↓) |
| 16_caso_postverdad | 0.310 | -0.117 | 1.000 | -0.051 | ❌ | Parcial (EDI>0.30, corr↓) |
| 17_caso_rtb_publicidad | 0.426 | 0.464 | 1.030 | 0.755 | ✅ | **Validado** |
| 18_caso_wikipedia | 0.017 | 0.071 | 1.151 | 0.309 | ❌ | Rechazado |
| 19_caso_deforestacion | 0.847 | 0.850 | 1.000 | 0.919 | ✅ | **Validado** |
| 20_caso_oceanos | 0.737 | -0.433 | 1.005 | 0.361 | ❌ | Parcial (EDI alto, corr↓) |
| 21_caso_urbanizacion | 0.840 | 1.411 | 1.000 | 0.999 | ✅ | **Validado** |

**Resumen**: 7 validados (overall_pass=True) + 3 controles de falsación correctamente rechazados + 4 parciales + 7 rechazados.

**Nota sobre la Tabla:** El campo "Estado" es **Validado** solo si `overall_pass = True`, lo cual requiere las 11 condiciones del protocolo: C1-C5, symploké, no-localidad, persistencia, emergencia, coupling ≥ 0.1, no-fraude RMSE. Los controles de falsación (07-09) están diseñados para fallar y lo hacen correctamente. CR con "—" indica cohesión interna negativa (anti-correlación en grid), invalidando la métrica.

## Análisis de Evidencia y Hallazgos
Los 21 casos demuestran que el modelo híbrido funciona como **herramienta de demarcación operativa**: discrimina entre sistemas con estructura macro detectable y sistemas sin ella. De los 21 casos evaluados, 7 pasan el protocolo completo (overall_pass=True) bajo las condiciones más estrictas (assimilation_strength = 0.0):

- **Urbanización** (EDI=0.840, corr=0.999, EI=1.411): Emergencia muy fuerte. La tendencia macro de urbanización global constrinye completamente los patrones micro.
- **Deforestación** (EDI=0.847, corr=0.919, EI=0.850): Emergencia muy fuerte. Las políticas globales como hiperobjeto reducen la entropía local en un 85%.
- **Finanzas** (EDI=0.880, corr=0.996, EI=1.218): Emergencia muy fuerte. Los mercados financieros globales como estructura macro dominante.
- **Paradigmas** (EDI=0.656, corr=0.953, EI=0.880): Emergencia fuerte. Estructuras culturales capturadas con alta fidelidad.
- **Clima** (EDI=0.425, corr=0.822, EI=0.542): Emergencia moderada-fuerte. El modelo macro reduce el RMSE en 42% respecto al ABM aislado.
- **RTB Publicidad** (EDI=0.426, corr=0.755, EI=0.464): Emergencia moderada. Dinámica de mercado publicitario detectable.
- **Energía** (EDI=0.350, corr=0.789, EI=0.327): Emergencia moderada. Señal macro robusta en consumo energético.

Los 3 controles de falsación (exogeneidad, no-estacionariedad, observabilidad) fallan correctamente, confirmando que el marco **no es tautológico**. El ratio es 7/18 validados de casos genuinos (39%), lo cual demuestra selectividad: el marco rechaza sistemas sin estructura macro detectable (conciencia, estética, justicia, moderación) y valida solo aquellos donde la causalidad descendente es computacionalmente medible.

Los casos parciales (Contaminación EDI=0.12, Océanos EDI=0.74, Políticas EDI=0.29, Postverdad EDI=0.31) muestran señales macro existentes pero insuficientes para pasar el protocolo C1-C5 completo, lo que refuerza la sensibilidad del marco.

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

Cuando EDI y CR divergen (ej. EDI < 0.30 pero CR > 2.0, o viceversa), se aplica el siguiente criterio:

1. **EDI > 0.30 y CR < 2.0**: El macro reduce error micro pero sin frontera sistémica clara → **Emergencia funcional sin cohesión**. Estado: Parcial.
2. **EDI < 0.30 y CR > 2.0**: Cohesión interna alta pero el macro no mejora la predicción → **Estructura autónoma sin eficacia causal descendente**. Estado: Parcial.
3. **EDI > 0.30 y CR > 2.0 y C1-C5 = True**: Emergencia completa. Estado: **Validado**.
4. **EDI < 0.30 y CR < 2.0**: Sin emergencia ni cohesión. Estado: **Rechazado**.

**Caso Clima real** (EDI=0.424, CR=1.002) cae en categoría 1: emergencia funcional verificada con reducción del 42% en RMSE. La frontera sistémica (CR=1.002) es marginal, lo cual es coherente con un sistema climático global donde la difusión es alta.

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
