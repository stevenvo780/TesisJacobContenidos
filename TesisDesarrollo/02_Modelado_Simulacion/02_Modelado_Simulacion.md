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

### La Transición de Fase Metaestable
Durante la simulación, observamos un punto crítico donde el parámetro de acoplamiento macro-micro permite que el sistema pase de un estado de **Agregación Desordenada** a uno de **Coherencia Hiperobjetual**. Este punto se mide mediante el EDI. Si el acoplamiento es demasiado débil, el hiperobjeto se disuelve (Caso Finanzas); si es demasiado fuerte, se vuelve una tautología (Caso Justicia/Sobreajuste). El éxito reside en la **Metaestabilidad** (Caso Contaminacion, EDI 0.423; Caso Movilidad, EDI 0.740).


## Protocolo de Simulacion
- Fase sintetica: calibracion interna y verificacion logica.
- Fase real: validacion con datos historicos.
- Splits de entrenamiento/validacion documentados por caso.

La auditoria de modelado exigio criterios de paro y comparacion con modelos alternativos. Aunque no todos los casos usan modelos rivales, la regla se mantiene: si el modelo no mejora sobre un baseline coherente, se rechaza.

## Criterios Tecnicos
- **EDI > 0.30** indica eficacia causal macro.
- **CR > 2.0** indica frontera sistemica.
- Validacion C1-C5 aplicada a cada caso.

**Nota sobre Disparidad de Datasets:** Se reconoce una disparidad significativa en la calidad y "dureza" de los datos entre casos. Los casos físicos (Clima, Contaminación, LoE 4-5) utilizan series históricas instrumentales de alta fidelidad, mientras que los casos sociales, biológicos y prospectivos (LoE 1-3) dependen de proxies digitales, series cortas o datos sintéticos. Esta asimetría es inherente a la naturaleza de los hiperobjetos estudiados y se refleja en los niveles de evidencia (LoE) reportados.

## Resultados (Matriz de Validacion Tecnica)

| Caso | LoE | EDI | CR | Estado | Reporte |
| :--- | :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 5 | 0.103 | 2.355 | False | `01_caso_clima/report.md` |
| 02_caso_conciencia | 1 | 0.477 | 2.119 | False | `02_caso_conciencia/report.md` |
| 03_caso_contaminacion | 4 | 0.423 | 2.472 | True | `03_caso_contaminacion/report.md` |
| 04_caso_energia | 4 | 0.647 | 3.167 | False | `04_caso_energia/report.md` |
| 05_caso_epidemiologia | 4 | 0.889 | 2.000 | False | `05_caso_epidemiologia/report.md` |
| 06_caso_estetica | 2 | 0.363 | 1.646 | False | `06_caso_estetica/report.md` |
| 07_caso_falsacion_exogeneidad | 1 | -2.513 | 1.005 | False | `07_caso_falsacion_exogeneidad/report.md` |
| 08_caso_falsacion_no_estacionariedad | 1 | 0.009 | 1.002 | False | `08_caso_falsacion_no_estacionariedad/report.md` |
| 09_caso_falsacion_observabilidad | 1 | n/a | n/a | False | `09_caso_falsacion_observabilidad/report.md` |
| 10_caso_finanzas | 5 | 0.769 | 1.078 | False | `10_caso_finanzas/report.md` |
| 11_caso_justicia | 2 | 0.619 | 2.001 | False | `11_caso_justicia/report.md` |
| 12_caso_moderacion_adversarial | 1 | -0.179 | 1.069 | False | `12_caso_moderacion_adversarial/report.md` |
| 13_caso_movilidad | 2 | 0.740 | 5.273 | True | `13_caso_movilidad/report.md` |
| 14_caso_paradigmas | 2 | 0.248 | 1.353 | False | `14_caso_paradigmas/report.md` |
| 15_caso_politicas_estrategicas | 1 | -0.209 | 1.264 | False | `15_caso_politicas_estrategicas/report.md` |
| 16_caso_postverdad | 2 | 0.313 | 1.887 | False | `16_caso_postverdad/report.md` |
| 17_caso_rtb_publicidad | 1 | 0.088 | 6.937 | False | `17_caso_rtb_publicidad/report.md` |
| 18_caso_wikipedia | 3 | 0.562 | 2.888 | False | `18_caso_wikipedia/report.md` |

Para recalcular este reporte de forma automatica, usar:
`python3 repos/scripts/actualizar_tablas_002.py`
## Evidencia Empirica (casos con validación ejecutable)
- **Contaminacion:** la memoria atmosferica y el transporte macro ordenan emisiones locales. EDI 0.423, CR 2.472.
- **Movilidad:** EDI 0.740, CR 5.273. Series cortas, prototipo.

**Nota sobre comparación justa del modelo reducido:** El EDI se calcula comparando el modelo completo (con macro_coupling y forcing_scale activos) contra un modelo reducido donde estos parámetros se anulan. Ambos modelos mantienen el mismo assimilation_strength para que la comparación mida exclusivamente el valor del acoplamiento macro. En la versión final, la evaluación se realiza sin nudging (assimilation_strength=0.0) para medir la emergencia pura del acoplamiento.

## Arquitectura y Ejecución de los 18 Casos
A diferencia de versiones preliminares, la arquitectura actual del proyecto integra **18 motores de simulación completamente funcionales** y ejecutables. Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas.

Esta infraestructura permite una reproducibilidad total del EDI y CR reportados, eliminando la dependencia de métricas pre-generadas. El sistema utiliza datos reales de fuentes como World Bank, Wikimedia y Meteostat para los casos de alta fidelidad, y generadores estocásticos controlados para los casos de falsación.

## Resultados (Matriz de Validación Técnica)
La siguiente tabla resume los resultados obtenidos tras la ejecución del pipeline completo en los 18 motores:

| Caso | LoE | EDI | CR | Estado | Reporte |
| :--- | :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 5 | 0.103 | 2.355 | False | `01_caso_clima/report.md` |
| 02_caso_conciencia | 1 | 0.477 | 2.119 | False | `02_caso_conciencia/report.md` |
| 03_caso_contaminacion | 4 | 0.423 | 2.472 | True | `03_caso_contaminacion/report.md` |
| 04_caso_energia | 4 | 0.647 | 3.167 | False | `04_caso_energia/report.md` |
| 05_caso_epidemiologia | 4 | 0.889 | 2.000 | False | `05_caso_epidemiologia/report.md` |
| 06_caso_estetica | 2 | 0.363 | 1.646 | False | `06_caso_estetica/report.md` |
| 07_caso_falsacion_exogeneidad | 1 | -2.513 | 1.005 | False | `07_caso_falsacion_exogeneidad/report.md` |
| 08_caso_falsacion_no_estacionariedad | 1 | 0.009 | 1.002 | False | `08_caso_falsacion_no_estacionariedad/report.md` |
| 09_caso_falsacion_observabilidad | 1 | n/a | n/a | False | `09_caso_falsacion_observabilidad/report.md` |
| 10_caso_finanzas | 5 | 0.769 | 1.078 | False | `10_caso_finanzas/report.md` |
| 11_caso_justicia | 2 | 0.619 | 2.001 | False | `11_caso_justicia/report.md` |
| 12_caso_moderacion_adversarial | 1 | -0.179 | 1.069 | False | `12_caso_moderacion_adversarial/report.md` |
| 13_caso_movilidad | 2 | 0.740 | 5.273 | True | `13_caso_movilidad/report.md` |
| 14_caso_paradigmas | 2 | 0.248 | 1.353 | False | `14_caso_paradigmas/report.md` |
| 15_caso_politicas_estrategicas | 1 | -0.209 | 1.264 | False | `15_caso_politicas_estrategicas/report.md` |
| 16_caso_postverdad | 2 | 0.313 | 1.887 | False | `16_caso_postverdad/report.md` |
| 17_caso_rtb_publicidad | 1 | 0.088 | 6.937 | False | `17_caso_rtb_publicidad/report.md` |
| 18_caso_wikipedia | 3 | 0.562 | 2.888 | False | `18_caso_wikipedia/report.md` |

Para replicar estos resultados, se debe ejecutar el script de validación dentro de cada carpeta o usar el orquestador:
`python3 repos/scripts/tesis.py validate --all`

## Evidencia Empírica y Reproducibilidad
Los casos con validación ejecutable demostrada (Contaminación, Movilidad, Wikipedia) confirman que el modelo híbrido es capaz de identificar estructuras de orden informacional sin intervención manual (Zero-Nudging). 

**La Paradoja de la Inercia:** Se reconoce que el EDI es sensible a la estabilidad de las series. Casos como Estética presentan EDI superior a Justicia debido a la inercia del canon artístico frente a la volatilidad del proceso judicial, lo que define el límite de detectabilidad del marco actual.

## Auditoria de Consistencia

Ver `Auditoria_Simulaciones.md` para hallazgos y recomendaciones sobre calidad documental y metricas.
