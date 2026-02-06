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
| 01_caso_clima | 5 | 0.103 | 2.355 | False | `01_caso_clima/report.md` |
| 02_caso_conciencia | 1 | 0.477 | 2.119 | False | `02_caso_conciencia/report.md` |
| 03_caso_contaminacion | 4 | 0.423 | 2.472 | **True** | `03_caso_contaminacion/report.md` |
| 04_caso_energia | 4 | 0.647 | 3.167 | False | `04_caso_energia/report.md` |
| 05_caso_epidemiologia | 4 | 0.889 | 2.000 | False | `05_caso_epidemiologia/report.md` |
| 06_caso_estetica | 2 | 0.363 | 1.646 | False | `06_caso_estetica/report.md` |
| 07_caso_falsacion_exogeneidad | 1 | -2.513 | 1.005 | False | `07_caso_falsacion_exogeneidad/report.md` |
| 08_caso_falsacion_no_estacionariedad | 1 | 0.009 | 1.002 | False | `08_caso_falsacion_no_estacionariedad/report.md` |
| 09_caso_falsacion_observabilidad | 1 | n/a | n/a | False | `09_caso_falsacion_observabilidad/report.md` |
| 10_caso_finanzas | 5 | 0.769 | 1.078 | False | `10_caso_finanzas/report.md` |
| 11_caso_justicia | 2 | 0.619 | 2.001 | False | `11_caso_justicia/report.md` |
| 12_caso_moderacion_adversarial | 1 | -0.179 | 1.069 | False | `12_caso_moderacion_adversarial/report.md` |
| 13_caso_movilidad | 2 | 0.740 | 5.273 | **True** | `13_caso_movilidad/report.md` |
| 14_caso_paradigmas | 2 | 0.248 | 1.353 | False | `14_caso_paradigmas/report.md` |
| 15_caso_politicas_estrategicas | 1 | -0.209 | 1.264 | False | `15_caso_politicas_estrategicas/report.md` |
| 16_caso_postverdad | 2 | 0.313 | 1.887 | False | `16_caso_postverdad/report.md` |
| 17_caso_rtb_publicidad | 1 | 0.088 | 6.937 | False | `17_caso_rtb_publicidad/report.md` |
| 18_caso_wikipedia | 3 | 0.562 | 2.888 | False | `18_caso_wikipedia/report.md` |

**Nota sobre la Matriz:** El campo "Estado" es **True** solo si el caso cumple simultáneamente con EDI > 0.30, CR > 2.0 y todos los criterios C1-C5. Para replicar estos resultados de forma automática:
`python3 repos/scripts/tesis.py validate --all`

## Análisis de Evidencia y Hallazgos
Los casos validados (Contaminación, Movilidad) demuestran que el modelo híbrido identifica estructuras de orden informacional autónomas. Sin embargo, la disparidad de resultados revela la **"Paradoja de la Inercia"**: el EDI es altamente sensible a la estabilidad de las series. 

Sistemas como la **Estética** presentan un EDI superior a la **Justicia** no por una mayor "importancia", sino por la inercia del canon artístico frente a la volatilidad procedimental del sistema legal. Esto marca el límite técnico del marco actual: detecta **estabilidad informacional macroscópica**, no necesariamente relevancia ontológica absoluta.

## Auditoria de Consistencia
Ver `Auditoria_Simulaciones.md` para hallazgos y recomendaciones detalladas sobre la calidad de los datos y el comportamiento de las métricas en casos de borde.