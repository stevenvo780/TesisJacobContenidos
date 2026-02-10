# 02 Modelado y Simulación

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

## Rol Instrumental de la ODE: Sonda Operativa

La ODE no es la representación del hiperobjeto. Es una **sonda operativa**: un instrumento que genera una señal macro candidata para probar si la dinámica micro responde a constricciones de ese nivel. Bajo irrealismo operativo, lo que se mide no es "existencia" sino **grado de cierre operativo**. Si la eliminación de la constricción macro (ablación: forcing_scale=0, macro_coupling=0) degrada la predicción micro (EDI > 0.30), el constructo macro es operativamente indispensable.

La ODE es un modelo auxiliar cuya función es:
1. Generar la señal macro que alimenta al ABM (como condición de contorno).
2. Permitir la comparación ABM_completo vs ABM_reducido (el EDI no mide calidad de la ODE).
3. Servir de benchmark para evaluar la coherencia macro-micro (correlación ODE-ABM).

Esta distinción resuelve la objeción "Phantom ODE": una ODE con correlación baja puede coexistir con un EDI positivo porque lo que el EDI mide es la diferencia entre ABM con y sin constricción macro, no la calidad de la ODE como predictor independiente.

## Implementación de los 29 Casos
La arquitectura actual integra **29 motores de simulación completamente funcionales**. Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas. Se utilizan datos reales de fuentes como World Bank, Meteostat, Yahoo Finance, OWID, Wikimedia y CelesTrak.

### Protocolo de Simulación
- **Fase sintética:** calibración interna y verificación lógica.
- **Fase real:** clasificación con datos históricos.
- **Zero-Nudging:** En la versión final, la evaluación se realiza sin nudging (`assimilation_strength=0.0`) para medir el cierre operativo puro del acoplamiento macro.

## Criterios Técnicos de Clasificación
- **EDI ≥ 0.30:** Nivel 4 (cierre operativo fuerte).
- **Permutation test (p<0.05):** significancia estadística (999 permutaciones).
- **Bias Correction:** transformación afín condicional del target ODE para eliminar sesgo.
- **CR > 2.0:** indicador complementario de frontera sistémica.
- **overall_pass:** 11 condiciones simultáneas (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento, no-fraude).

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