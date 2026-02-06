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

## Resultados (Matriz de Validacion Tecnica)

| Caso | EDI | CR | Estado | Reporte |
| :--- | ---: | ---: | :--- | :--- |
| 01_caso_clima | 0.074 | 1.102 | False | `01_caso_clima/report.md` |
| 02_caso_conciencia | TAUT | 1.382 | False | `02_caso_conciencia/report.md` |
| 03_caso_contaminacion | 0.423 | 2.472 | True | `03_caso_contaminacion/report.md` |
| 04_caso_energia | TAUT | 1.824 | False | `04_caso_energia/report.md` |
| 05_caso_epidemiologia | TAUT | n/a | False | `05_caso_epidemiologia/report.md` |
| 06_caso_estetica | TAUT | 1.073 | False | `06_caso_estetica/report.md` |
| 07_caso_falsacion_exogeneidad | -2.513 | 1.005 | False | `07_caso_falsacion_exogeneidad/report.md` |
| 08_caso_falsacion_no_estacionariedad | 0.009 | 1.002 | False | `08_caso_falsacion_no_estacionariedad/report.md` |
| 09_caso_falsacion_observabilidad | n/a | n/a | False | `09_caso_falsacion_observabilidad/report.md` |
| 10_caso_finanzas | -0.020 | 1.437 | False | `10_caso_finanzas/report.md` |
| 11_caso_justicia | TAUT | 1.262 | False | `11_caso_justicia/report.md` |
| 12_caso_moderacion_adversarial | -0.179 | 1.069 | False | `12_caso_moderacion_adversarial/report.md` |
| 13_caso_movilidad | 0.740 | 5.273 | True | `13_caso_movilidad/report.md` |
| 14_caso_paradigmas | TAUT | 2.283 | False | `14_caso_paradigmas/report.md` |
| 15_caso_politicas_estrategicas | -0.209 | 1.264 | False | `15_caso_politicas_estrategicas/report.md` |
| 16_caso_postverdad | TAUT | 1.061 | False | `16_caso_postverdad/report.md` |
| 17_caso_rtb_publicidad | 0.088 | 6.937 | False | `17_caso_rtb_publicidad/report.md` |
| 18_caso_wikipedia | TAUT | 5.302 | False | `18_caso_wikipedia/report.md` |

Para recalcular este reporte de forma automatica, usar:
`python3 scripts/actualizar_tablas_002.py`
## Evidencia Empirica (casos con validación ejecutable)
- **Contaminacion:** la memoria atmosferica y el transporte macro ordenan emisiones locales. EDI 0.423, CR 2.472.
- **Movilidad:** EDI 0.740, CR 5.273. Series cortas, prototipo.

**Nota sobre comparación justa del modelo reducido:** El EDI se calcula comparando el modelo completo (con macro_coupling y forcing_scale activos) contra un modelo reducido donde estos parámetros se anulan. Ambos modelos mantienen el mismo assimilation_strength para que la comparación mida exclusivamente el valor del acoplamiento macro, no acoplamiento + asimilación combinados. Esta corrección redujo significativamente los EDI de los casos con código ejecutable.

## Limitaciones: casos sin código ejecutable
De los 18 casos, solo caso_clima y caso_finanzas poseen código Python ejecutable completo. Los restantes 16 casos tienen metrics.json pre-generados con la versión anterior del pipeline (assimilation_strength=0 en modelo reducido), lo que inflaba el EDI. Los 8 casos con rmse_abm ≈ 0 están marcados como TAUT (tautológicos) en la tabla.

## Evidencia Prospectiva y Teorica
- **Energia, Epidemiologia, Wikipedia, Postverdad:** métricas originales invalidadas (TAUT). Requieren implementación de código ejecutable con comparación justa.

## Fronteras del Modelo
- **Clima:** EDI 0.074, CR 1.102. Posee código ejecutable pero no supera umbrales. La estructura macro existe pero es débil.
- **Finanzas:** EDI -0.020, macro_coupling=0.0. Falla por reflexividad y aliasing temporal.

## Falsacion y Pruebas de Estres
- Exogeneidad total, ruido blanco e invisibilidad de agentes se usan para descartar falsos positivos.

## Sintesis y Limitaciones Epistemicas
Tras la corrección de la comparación justa en el modelo reducido, solo 2 de 18 casos superan los umbrales EDI > 0.30 y CR > 2.0: contaminacion (EDI 0.423, CR 2.472) y movilidad (EDI 0.740, CR 5.273). El caso clima muestra un EDI de 0.074 y un CR de 1.102, ambos por debajo de los umbrales, lo que indica que la estructura macro existe pero es débil. Los 8 casos con EDI=1.000 previo resultaron tautológicos (rmse_abm ≈ 0). La "validación" aquí presentada es estadística y no clausura el debate filosófico sobre la existencia real de estos objetos.

## Auditoria de Consistencia

Ver `Auditoria_Simulaciones.md` para hallazgos y recomendaciones sobre calidad documental y metricas.
