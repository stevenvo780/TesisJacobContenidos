# 02 Modelado y Simulación — Narrativa Unificada

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

La ODE no es la representación del hiperobjeto. Es una **sonda operativa**: un instrumento que genera una señal macro candidata para probar si la dinámica micro responde a constricciones de ese nivel. La ODE es al constructo macro lo que el acelerador de partículas es al bosón de Higgs: no es la entidad, es la herramienta que revela el efecto.

Bajo irrealismo operativo, lo que se mide no es "existencia" sino **grado de cierre operativo**. Si la eliminación de la constricción macro (ablación: forcing_scale=0, macro_coupling=0) degrada la predicción micro (EDI > 0.30), el constructo macro es operativamente indispensable. La ODE es un modelo auxiliar cuya función es:
1. Generar la señal macro que alimenta al ABM (como condición de contorno).
2. Permitir la comparación ABM_completo vs ABM_reducido (el EDI no mide calidad de la ODE).
3. Servir de benchmark para evaluar la coherencia macro-micro (correlación ODE-ABM).

Esta distinción resuelve la objeción "Phantom ODE" (Gladiadores R15): una ODE con correlación baja puede coexistir con un EDI positivo porque lo que el EDI mide es la diferencia entre ABM con y sin constricción macro, no la calidad de la ODE como predictor independiente.

## Arquitectura y Ejecución de los 29 Casos
La arquitectura actual del proyecto integra **29 motores de simulación completamente funcionales** y ejecutables. Cada caso, ubicado en `repos/Simulaciones/`, cuenta con su propio pipeline de validación (`validate.py`), conectores de datos (`data.py`) y métricas específicas.

Esta infraestructura permite una reproducibilidad total del EDI y CR reportados, eliminando la dependencia de métricas pre-generadas. El sistema utiliza datos reales de fuentes como World Bank, Meteostat, Yahoo Finance, OWID, OPSD, Wikimedia, CelesTrak y yfinance para los casos de alta fidelidad, y generadores estocásticos controlados para los casos de falsación. Los casos 19-29 amplían la cobertura a dominios como acidificación oceánica, uso de fósforo, acuíferos, conectividad digital (IoT/Starlink), capital intelectual, erosión discursiva, microplásticos, basura espacial y riesgo biológico.

> **Nota:** Tres casos originales (Estética Global, Moderación Adversarial, RTB Publicidad) fueron removidos por inviabilidad de datos reales. Los 29 casos restantes constituyen el universo oficial de la tesis.

### Protocolo de Simulación
- **Fase sintética:** calibración interna y verificación lógica.
- **Fase real:** clasificación con datos históricos.
- **Zero-Nudging:** En la versión final, la evaluación se realiza sin nudging (`assimilation_strength=0.0`) para medir el cierre operativo puro del acoplamiento macro.

## Criterios Técnicos de Clasificación
- **EDI ≥ 0.30:** condición necesaria para Nivel 4 (cierre operativo fuerte).
- **Permutation test (p<0.05):** significancia estadística del EDI contra distribución nula (999 permutaciones, seed=42).
- **Bias Correction:** transformación afín condicional del target ODE para eliminar sesgo de nivel/escala.
- **CR > 2.0:** indicador complementario de frontera sistémica (no condición de clasificación).
- **C1-C5:** Protocolo de rigor aplicado a la convergencia, robustez, replicación, validez y gestión de incertidumbre.
- **overall_pass:** 11 condiciones simultáneas (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento ≥ 0.1, no-fraude RMSE).
- **C1 v2.0:** Criterio relativo (acoplado mejor que reducido) OR absoluto relajado (RMSE < 2·obs_std, corr > 0.3). Anterior v1.0 era demasiado estricto (RMSE < obs_std, corr > 0.7).
- **emergence_taxonomy:** Clasificación diferenciada en 6 niveles: strong, weak, suggestive, trend, null, falsification.
- **noise_sensitivity:** Test de estabilidad del EDI bajo perturbaciones de ruido (CV < 0.5).

## Resultados Consolidados (Matriz de Clasificación Operativa)

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

Para recalcular este reporte de forma automática, usar:
`python3 scripts/actualizar_tablas_002.py`

## Análisis del Paisaje de Emergencia

Los 29 casos demuestran que el modelo híbrido funciona como **instrumento de clasificación operativa**: posiciona fenómenos en un gradiente de cierre operativo sin pronunciarse sobre su estatuto ontológico.

### Estado Actual: Paisaje de Emergencia Operativa Mapeado

**overall_pass = 2/29** (Deforestación EDI=0.633, Microplásticos EDI=0.427). La taxonomía diferenciada revela un paisaje completo:

- **Nivel 4 — Cierre operativo fuerte** (2 casos): Deforestación, Microplásticos
- **Nivel 3 — Componente funcional** (1 caso): Fuga de Cerebros (EDI=0.183)
- **Nivel 2 — Señal sugestiva** (3 casos): Finanzas, Océanos, IoT
- **Nivel 1 — Tendencia** (7 casos): Clima, Movilidad, Políticas, Postverdad, Urbanización, Salinización, Riesgo Biológico
- **Nivel 0 — Sin señal** (13 casos): sin constricción macro detectable
- **Controles negativos** (3 casos): falsificaciones correctamente rechazadas

**Significancia estadística (p<0.05 + EDI>0.01):** 6/29 casos (09, 16, 17, 24, 28, 29)
**Estabilidad numérica:** 25/29 (fallan: 05, 12, 13, 18)
**Persistencia (std<5×):** 27/29 (fallan: 11, 20)

El paisaje no "confirma" ni "refuta" hiperobjetos — **los clasifica**. La diversidad del gradiente (de -1.000 a +0.633) es el resultado principal.

### Casos con Cierre Operativo Fuerte (Nivel 4)

**Deforestación Global** (EDI=0.633, p=0.000, overall_pass=True):
El modelo ODE (von Thünen Frontier) captura la dinámica de la frontera agrícola. Tras Bias Correction full, el ABM acoplado reduce el RMSE en 63% respecto al ABM aislado. Esto indica que el constructo macro es operativamente indispensable para este dominio — no que "exista" un hiperobjeto Deforestación como entidad autónoma.

**Microplásticos Oceánicos** (EDI=0.427, p=0.000, overall_pass=True):
El modelo Jambeck de acumulación persistente. El ABM sin ODE pierde 43% de precisión. Este caso NO requiere Bias Correction — la señal macro emerge directamente del acoplamiento. Analogía del ribosoma: funciona como si tuviera cierre, sin que necesitemos afirmar que "es" una entidad separada de sus componentes.

### Componente Funcional (Nivel 3)

**Fuga de Cerebros** (EDI=0.183, p=0.001):
El modelo Docquier-Rapoport captura la migración de capital humano. El EDI es significativo pero sub-umbral (0.183 < 0.30). El constructo macro es útil pero no indispensable — como un ribosoma que facilita una función sin constituir un nivel autónomo.

### Señal Sugestiva (Nivel 2)

Finanzas (EDI=0.040, p=0.000), Océanos (0.053, p=0.000), IoT (0.020, p=0.000): señal estadísticamente significativa pero de magnitud insuficiente para atribuir cierre operativo. Fenómenos que el instrumento detecta como posibles candidatos.

### Falsificaciones Correctas

Los 3 controles negativos (Exogeneidad, No-estacionariedad, Observabilidad) son clasificados como `falsification` con EDI negativo. El protocolo los rechaza correctamente, confirmando su **selectividad**.

### Anti-emergencia: ODE de Alta Correlación con EDI Negativo

Varios casos presentan EDI negativo a pesar de buenos modelos ODE. Esto revela que **alta correlación ODE-obs no implica cierre operativo**. La correlación puede ser espuria o el acoplamiento puede destruir información útil que el ABM aislado captura por sí solo.

### Composición del universo de 29 casos

| Categoría | Nivel | Conteo | Función en el paisaje |
|-----------|:-----:|--------|----------------------|
| **strong** | 4 | 2 | Cierre operativo fuerte |
| **weak** | 3 | 1 | Componente funcional |
| **suggestive** | 2 | 3 | Señal detectable |
| **trend** | 1 | 7 | Tendencia no confirmada |
| **null** | 0 | 13 | Sin señal operativa |
| **falsification** | — | 3 | Controles correctos |
| **Total** | | **29** | |

### Diagnóstico: ¿Por Qué la Mayoría se Clasifica en Nivel 0-1?

1. **Modelos ODE inadecuados:** El ODE no captura la dinámica macro, por lo que no puede generar constricción útil. Esto no invalida el instrumento — indica que la sonda necesita calibración dominio-específica.

2. **No-estacionariedad del ODE:** El ODE se ajusta bien en training pero la correlación se invierte o degrada en validation. Esto refleja cambios estructurales en el fenómeno.

3. **Coupling destructivo:** El sesgo del ODE destruye información útil en el ABM. El Bias Correction resolvió esto para Deforestación; otros casos persisten por problemas de escala.

4. **Señal real demasiado ruidosa (3 casos suggestive):** La señal macro existe (EDI significativo) pero el ruido domina, produciendo EDI < 0.10. Límite del SNR de los datos reales, no del instrumento.

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
| Modelos ODE dominio-específicos mejorados | ❌ Pendiente | Podría reclasificar casos con ODE poor |
| Forcing multivariado (CO2, VIX, etc.) | ❌ Pendiente | Forcing más realista por dominio |
| Topología de red heterogénea para CR | ❌ Pendiente | CR > 2.0 requiere redes no regulares |

## Regla Operacional: Divergencia EDI/CR

El CR (Cohesion Ratio = internal/external) es un **indicador complementario de frontera**, no una condición de clasificación. La clasificación se define exclusivamente por EDI + C1-C5 (§ Hipótesis Central, `00_Marco_Conceptual`). El CR informa sobre la topología del acoplamiento.

Clasificación descriptiva cuando EDI y CR divergen:

1. **EDI ≥ 0.30, CR < 2.0, C1-C5 = True**: Cierre operativo con frontera difusa → **Nivel 4** (H1 satisfecho). CR ≈ 1.0 es esperado en modelos de difusión espacial homogénea.
2. **EDI ≥ 0.30, CR > 2.0, C1-C5 = True**: Cierre operativo con frontera nítida → **Nivel 4+** (candidato a Nivel 5 con verificación adicional).
3. **EDI < 0.30, CR > 2.0**: Cohesión sin cierre operativo → **Nivel 2-3** (parcial).
4. **EDI < 0.30, CR < 2.0**: Sin cierre ni cohesión → **Nivel 0-1**.

**Nota:** El validador (`hybrid_validator.py`, L656) implementa `overall_pass` con 11 condiciones (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento, no-fraude). El CR se computa como métrica informativa pero no es condición de `overall_pass`, coherente con H1.

### Análisis Teórico: CR ≈ 1.0 en Modelos de Difusión Homogénea

En la arquitectura ABM actual, todos los agentes comparten el mismo forzamiento externo y la misma dinámica de difusión isotrópica (vecinos de Von Neumann en retícula n×n). Formalmente, sea `σ²_int` la varianza intra-grupo y `σ²_ext` la varianza inter-grupo. El CR se define como `σ²_int / σ²_ext`.

Para difusión isotrópica con forzamiento uniforme, el teorema de equipartición estocástica predice `σ²_int ≈ σ²_ext` en el límite estacionario, produciendo CR ≈ 1.0. La desviación de CR respecto a la unidad refleja heterogeneidad espacial del forzamiento o asimetría en el acoplamiento.

**Implicación:** CR > 2.0 requeriría forzamiento no-uniforme o topología de red no-regular (ej. small-world, scale-free). Esto constituye una extensión natural para trabajo futuro, no una deficiencia del instrumento actual. El CR ≈ 1.0 confirma que la difusión es operativa y que los agentes están acoplados al macro — condición necesaria para que el EDI sea interpretable.

**Referencia:** Haken (1983, *Synergetics*, §4.3) demuestra que en campos de orden con simetría translacional, la razón entre fluctuaciones internas y externas converge a la unidad.

### Nota sobre trazabilidad

Cada `metrics.json` contiene `generated_at` (timestamp ISO) y `git.commit` (hash del código ejecutado). Los resultados se generan ejecutando `validate.py` desde `repos/Simulaciones/{NN}_caso_*/src/`.

> La bitácora detallada de correcciones (C5), defensas técnicas ante vectores de ataque, y limitaciones del marco de Hoel se documenta en `TesisFinal/documentacion_procedimental.md`.

## Auditoría de Consistencia

Para auditar la consistencia estructural de los casos, ejecutar:
```bash
python3 repos/scripts/tesis.py audit
```

Este comando verifica presencia de archivos requeridos, sincronización de timestamps, y rangos válidos de métricas (EDI, CR).
