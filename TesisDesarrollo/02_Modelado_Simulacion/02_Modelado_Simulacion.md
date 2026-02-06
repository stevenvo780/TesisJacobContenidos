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

## Arquitectura y Ejecución de los 18 Casos
A diferencia de versiones preliminares, la arquitectura actual del proyecto integra **18 motores de simulación completamente funcionales** y ejecutables. Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas.

Esta infraestructura permite una reproducibilidad total del EDI y CR reportados, eliminando la dependencia de métricas pre-generadas. El sistema utiliza datos reales de fuentes como World Bank, Wikimedia y Meteostat para los casos de alta fidelidad, y generadores estocásticos controlados para los casos de falsación.

### Protocolo de Simulacion
- **Fase sintetica:** calibracion interna y verificacion logica.
- **Fase real:** validacion con datos historicos.
- **Zero-Nudging:** En la versión final, la evaluación se realiza sin nudging (`assimilation_strength=0.0`) para medir la emergencia pura del acoplamiento macro.

## Criterios Tecnicos de Validación
- **EDI > 0.30:** indica eficacia causal macro (emergencia fuerte).
- **CR > 2.0:** indica frontera sistémica (cohesión interna).
- **C1-C5:** Protocolo de rigor aplicado a la convergencia, robustez, replicación, validez y gestión de incertidumbre.

## Resultados Consolidados (Matriz de Validación Técnica)

La siguiente tabla resume los resultados obtenidos tras la ejecución del pipeline completo en los 18 motores. Los valores representan el desempeño del modelo en modo **Zero-Nudging**.

| Caso | LoE | EDI | CR | Estado | Reporte |
| :--- | :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 5 | 0.002 | 4.817 | Parcial (CR) | `01_caso_clima/report.md` |
| 02_caso_conciencia | 1 | 0.477 | 2.119 | False | `02_caso_conciencia/report.md` |
| 03_caso_contaminacion | 4 | -0.076 | 2.003 | Falsado (C5) | `03_caso_contaminacion/report.md` |
| 04_caso_energia | 4 | 0.647 | 3.167 | False | `04_caso_energia/report.md` |
| 05_caso_epidemiologia | 4 | 0.889 | 2.000 | False | `05_caso_epidemiologia/report.md` |
| 06_caso_estetica | 2 | 0.363 | 1.646 | False | `06_caso_estetica/report.md` |
| 07_caso_falsacion_exogeneidad | 1 | -2.513 | 1.005 | False | `07_caso_falsacion_exogeneidad/report.md` |
| 08_caso_falsacion_no_estacionariedad | 1 | 0.009 | 1.002 | False | `08_caso_falsacion_no_estacionariedad/report.md` |
| 09_caso_falsacion_observabilidad | 1 | n/a | n/a | False | `09_caso_falsacion_observabilidad/report.md` |
| 10_caso_finanzas | 5 | 0.769 | 1.078 | False | `10_caso_finanzas/report.md` |
| 11_caso_justicia | 2 | 0.619 | 2.001 | False | `11_caso_justicia/report.md` |
| 12_caso_moderacion_adversarial | 1 | -0.179 | 1.069 | False | `12_caso_moderacion_adversarial/report.md` |
| 13_caso_movilidad | 2 | 0.385 | 1.151 | Parcial (EDI) | `13_caso_movilidad/report.md` |
| 14_caso_paradigmas | 2 | 0.248 | 1.353 | False | `14_caso_paradigmas/report.md` |
| 15_caso_politicas_estrategicas | 1 | -0.209 | 1.264 | False | `15_caso_politicas_estrategicas/report.md` |
| 16_caso_postverdad | 2 | 0.313 | 1.887 | False | `16_caso_postverdad/report.md` |
| 17_caso_rtb_publicidad | 1 | 0.088 | 6.937 | False | `17_caso_rtb_publicidad/report.md` |
| 18_caso_wikipedia | 3 | 0.562 | 2.888 | False | `18_caso_wikipedia/report.md` |

**Nota sobre la Matriz:** El campo "Estado" es **True** solo si el caso cumple simultáneamente con EDI > 0.30, CR > 2.0 y todos los criterios C1-C5. Para replicar estos resultados de forma automática:
`python3 repos/scripts/tesis.py validate --all`

## Análisis de Evidencia y Hallazgos
Los casos presentados demuestran que el modelo híbrido funciona como **herramienta de demarcación operativa**: discrimina entre sistemas con estructura macro detectable y sistemas sin ella. Sin embargo, ningún caso cumple simultáneamente EDI > 0.30, CR > 2.0 y C1-C5 = True bajo el código más estricto (assimilation_strength = 0.0 en todas las fases). Los resultados se clasifican como **Validación Parcial**:

- **Movilidad** (EDI=0.385, CR=1.15): emergencia funcional verificada pero sin frontera sistémica.
- **Clima** (EDI=0.002, CR=4.82): cohesión interna excepcional pero sin eficacia causal descendente medible.
- **Contaminación** (EDI=-0.076, CR=2.00): falsado bajo código estricto, reportado como corrección C5.

La disparidad de resultados revela la **"Paradoja de la Inercia"**: el EDI es altamente sensible a la estabilidad de las series.

Sistemas como la **Estética** presentan un EDI superior a la **Justicia** no por una mayor "importancia", sino por la inercia del canon artístico frente a la volatilidad procedimental del sistema legal. Esto marca el límite técnico del marco actual: detecta **estabilidad informacional macroscópica**, no necesariamente relevancia ontológica absoluta.

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

**Caso Clima real** (EDI=0.002, CR=4.82) cae en categoría 2: estructura autónoma verificada, eficacia causal pendiente de mejor calibración.

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