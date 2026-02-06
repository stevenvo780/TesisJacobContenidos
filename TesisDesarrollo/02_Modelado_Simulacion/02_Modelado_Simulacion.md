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
Durante la simulación, observamos un punto crítico donde el parámetro de acoplamiento macro-micro permite que el sistema pase de un estado de **Agregación Desordenada** a uno de **Coherencia Hiperobjetual**. Este punto se mide mediante el EDI. Si el acoplamiento es demasiado débil, el hiperobjeto se disuelve (Caso Finanzas); si es demasiado fuerte, se vuelve una tautología (Caso Justicia/Sobreajuste). El éxito reside en la **Metaestabilidad** (Caso Clima).


## Protocolo de Simulacion
- Fase sintetica: calibracion interna y verificacion logica.
- Fase real: validacion con datos historicos.
- Splits de entrenamiento/validacion documentados por caso.

La auditoria de modelado exigio criterios de paro y comparacion con modelos alternativos. Aunque no todos los casos usan modelos rivales, la regla se mantiene: si el modelo no mejora sobre un baseline coherente, se rechaza.

## Criterios Tecnicos
- **EDI > 0.30** indica eficacia causal macro.
- **CR > 2.0** indica frontera sistemica.
- Validacion C1-C5 aplicada a cada caso.

## Resultados (Matriz de Validacion Tecnica)

| Caso | EDI | CR | Estado | Reporte |
| :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 0.458 | 1.057 | True | `01_caso_clima/report.md` |
| 02_caso_conciencia | 1.000 | 1.382 | True | `02_caso_conciencia/report.md` |
| 03_caso_contaminacion | 0.423 | 2.472 | True | `03_caso_contaminacion/report.md` |
| 04_caso_energia | 1.000 | 1.824 | True | `04_caso_energia/report.md` |
| 05_caso_epidemiologia | 1.000 | n/a | True | `05_caso_epidemiologia/report.md` |
| 06_caso_estetica | 1.000 | 1.073 | True | `06_caso_estetica/report.md` |
| 07_caso_falsacion_exogeneidad | -2.513 | 1.005 | False | `07_caso_falsacion_exogeneidad/report.md` |
| 08_caso_falsacion_no_estacionariedad | 0.009 | 1.002 | False | `08_caso_falsacion_no_estacionariedad/report.md` |
| 09_caso_falsacion_observabilidad | n/a | n/a | False | `09_caso_falsacion_observabilidad/report.md` |
| 10_caso_finanzas | 0.975 | 1.396 | True | `10_caso_finanzas/report.md` |
| 11_caso_justicia | 1.000 | 1.262 | True | `11_caso_justicia/report.md` |
| 12_caso_moderacion_adversarial | -0.179 | 1.069 | False | `12_caso_moderacion_adversarial/report.md` |
| 13_caso_movilidad | 0.740 | 5.273 | True | `13_caso_movilidad/report.md` |
| 14_caso_paradigmas | 1.000 | 2.283 | True | `14_caso_paradigmas/report.md` |
| 15_caso_politicas_estrategicas | -0.209 | 1.264 | False | `15_caso_politicas_estrategicas/report.md` |
| 16_caso_postverdad | 1.000 | 1.061 | True | `16_caso_postverdad/report.md` |
| 17_caso_rtb_publicidad | 0.088 | 6.937 | False | `17_caso_rtb_publicidad/report.md` |
| 18_caso_wikipedia | 1.000 | 5.302 | True | `18_caso_wikipedia/report.md` |

Para recalcular este reporte de forma automatica, usar:
`python3 scripts/actualizar_tablas_002.py`
## Evidencia Empirica (LoE 4-5)
- **Clima:** el parametro macro de balance energetico esclaviza fluctuaciones locales.
- **Energia:** la estabilidad de red impone restricciones macro sobre agentes de consumo.
- **Epidemiologia:** la tasa global de contagio organiza el micro.
- **Contaminacion:** la memoria atmosferica y el transporte macro ordenan emisiones locales.

## Evidencia Prospectiva y Teorica
- **Wikipedia y Postverdad:** dinamicas de informacion con alta reflexividad, validacion prospectiva.

## Fronteras del Modelo
- **Finanzas:** falla por reflexividad y aliasing temporal (alta frecuencia).
- **Movilidad:** prototipo, inestabilidad del atractor macro en series largas.

## Falsacion y Pruebas de Estres
- Exogeneidad total, ruido blanco e invisibilidad de agentes se usan para descartar falsos positivos.

## Sintesis y Limitaciones Epistemicas
El motor hibrido sugiere que sistemas con alta inercia estructural (Clima, Epidemiología) responden eficazmente a un modelado macroscópico. Sin embargo, en dominios de alta frecuencia o baja materialidad (Finanzas, Estética), los resultados deben interpretarse con cautela: un EDI alto podría reflejar inercia histórica más que causalidad ontológica fuerte. La "validación" aquí presentada es estadística y no clausura el debate filosófico sobre la existencia real de estos objetos.

## Auditoria de Consistencia

Ver `Auditoria_Simulaciones.md` para hallazgos y recomendaciones sobre calidad documental y metricas.
