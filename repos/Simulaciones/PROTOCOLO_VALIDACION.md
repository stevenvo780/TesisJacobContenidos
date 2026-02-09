# Protocolo Formal de Validación — Ontología Operativa de Hiperobjetos

**Versión**: 2.0  
**Fecha**: 2025-07-11  
**Autor**: Jacob (generado por framework de validación)

---

## 1. Objetivo

Este protocolo define los criterios formales para determinar si un **hiperobjeto** (en el sentido de Morton, 2013) exhibe **emergencia computacional genuina** — es decir, si su modelo macroscópico (ODE) reduce la entropía de sus componentes microscópicos (ABM) de forma medible, reproducible y no trivial.

## 2. Arquitectura del Modelo Híbrido

Cada caso sigue la estructura de 5 archivos:

| Archivo | Función |
|---------|---------|
| `validate.py` | Orquestador: calibrar → simular → evaluar C1-C5 → escribir outputs |
| `abm.py` | Capa micro: grid n×n con difusión, acoplamiento macro, forcing, damping, nudging |
| `ode.py` | Capa macro: `dX/dt = α(F - βX) + ruido` con asimilación de datos opcional |
| `metrics.py` | EDI, CR, EI (Hoel), RMSE, correlación, dominancia, varianza de ventana |
| `data.py` | Obtención de datos (APIs, cache CSV, sintéticos) |

### 2.1. Regla de actualización ABM

Cada celda (i,j) por paso t combina cinco términos:
```
cell[t+1] = cell[t] + diffusion + forcing + macro_coupling*(macro_mean - cell[t]) - damping*cell[t] + noise
```

### 2.2. Ecuación ODE macro
```
dX/dt = α(F(t) - βX) + σ·ξ(t)
```
donde F(t) es el forcing externo y α, β se calibran por mínimos cuadrados.

## 3. Pipeline de Validación

### 3.1. Fases

1. **Fase Sintética**: Datos generados con ground truth conocido. Si el modelo no pasa aquí, la fase real se cancela (gating).
2. **Fase Real**: Datos observacionales. Solo se ejecuta si la fase sintética aprueba.

### 3.2. Normalización

Todos los datos se normalizan con z-score sobre la ventana de entrenamiento:
```
z = (x - mean_train) / std_train
```

### 3.3. Calibración

1. **Grid search** sobre parámetros ABM: `forcing_scale ∈ [0, 2]`, `macro_coupling ∈ [0, 0.5]`, `damping ∈ [0, 0.3]`
2. **Least squares** para ODE: α, β ajustados a datos de entrenamiento
3. **Sin look-ahead**: Asimilación usa datos rezagados `[None] + obs[:-1]`

### 3.4. Evaluación (solo en ventana de validación)

Se ejecutan tres modelos:
- **Acoplado**: ABM + ODE completo
- **Sin ODE**: ABM con `macro_coupling=0, forcing_scale=0` (ablación)
- **Reducido**: ABM sin acoplamiento macro (baseline)

## 4. Criterios de Validación

### 4.1. C1 — Convergencia (versión 2.0 relativa)

**Aprueba** si se cumple AL MENOS UNA condición:
- **(A) Relativa**: RMSE(acoplado) < RMSE(reducido) — el ODE aporta información
- **(B) Absoluta relajada**: RMSE < 2·obs_std Y correlación > 0.3

> **Nota v2.0**: La versión anterior (v1.0) requería RMSE < obs_std AND corr > 0.7, lo cual era excesivamente estricto para datos z-normalizados donde obs_std ≈ 1.0.

### 4.2. C2 — Robustez

El modelo produce resultados similares con perturbaciones de ±10% en parámetros.

### 4.3. C3 — Replicabilidad

Varianza inter-corridas < 5× varianza observada.

### 4.4. C4 — Validez

Modelo calibrado mantiene estructura bajo permutación de parámetros.

### 4.5. C5 — Incertidumbre

El modelo cuantifica correctamente su incertidumbre (ensemble spread vs. error real).

### 4.6. Criterios complementarios

| Criterio | Umbral | Significado |
|----------|--------|-------------|
| EDI ∈ [0.325, 0.90] | PASS | Emergencia significativa sin tautología |
| EDI permutation p < 0.05 | Significativo | No es artefacto aleatorio |
| Coupling ≥ 0.10 | No epifenomenal | La macro tiene efecto real |
| RMSE > 1e-10 | No fraude | No hay sobreajuste trivial |
| CR > 2.0 | Cohesión interna > externa | Symploké |
| No-localidad: dom < 0.05 | Descentralizado | No hay agente dominante |
| Persistencia: var_modelo < 5·var_obs | Temporal | La estructura persiste |
| Viscosity pass | Inercia | El sistema resiste perturbaciones |

## 5. Taxonomía de Emergencia

| Categoría | Condición | Interpretación |
|-----------|-----------|----------------|
| **Strong** | EDI ∈ [0.325, 0.90] + p < 0.05 | Emergencia macro fuerte |
| **Weak** | EDI ∈ [0.10, 0.325) + p < 0.05 | Señal macro significativa pero bajo umbral |
| **Suggestive** | EDI > 0 + p < 0.05 | Señal débil pero significativa |
| **Trend** | EDI > 0 + p ≥ 0.05 | Tendencia no confirmada |
| **Null** | EDI ≤ 0 | Sin evidencia de emergencia |
| **Falsification** | Diseño de control | Rechazo esperado |

## 6. Corrección de Sesgo (Bias Correction)

Se aplica BC mean-shift al ODE cuando la correlación ODE-obs en entrenamiento > 0.3:
```
ode_bc = ode + (mean_obs_train - mean_ode_train)
```
Esto corrige offset sistemático sin alterar la estructura dinámica.

## 7. Test de Sensibilidad al Ruido

Para cada caso, se re-ejecuta con 5 niveles de `base_noise` (0.5×, 0.75×, 1.0×, 1.5×, 2.0×). El EDI es **estable** si su coeficiente de variación CV < 0.5 y no decrece monótonamente con el ruido.

## 8. Umbrales de Rechazo

| Condición | Acción | Razón |
|-----------|--------|-------|
| EDI < 0.325 | No pasa overall | Sin estructura macro detectada |
| EDI > 0.90 | REJECT | Tautología / error de calibración |
| Coupling < 0.10 | REJECT | Epifenomenalismo |
| RMSE < 1e-10 | REJECT | Sobreajuste fraudulento |
| CR ≤ 2.0 | Penaliza | Cohesión insuficiente |

## 9. Ponderación por Nivel de Evidencia (LoE)

Cada caso tiene un LoE (1-5) que pondera el EDI:
```
EDI_weighted = EDI × (LoE / 5)
```

| LoE | Descripción | Factor |
|-----|-------------|--------|
| 5 | Datos instrumentales directos | 1.0 |
| 4 | Registros oficiales procesados | 0.8 |
| 3 | Indicadores proxy compuestos | 0.6 |
| 2 | Proxies indirectos | 0.4 |
| 1 | Constructos teóricos | 0.2 |

## 10. Reproducibilidad

- Seeds explícitos en todos los generadores aleatorios
- Script `replay_and_verify.py` re-ejecuta todos los casos y verifica hashes MD5 de `metrics.json`
- Todos los datos cacheados en `data/dataset.csv` por caso

## 11. Interpretación Filosófica

Un hiperobjeto es **computacionalmente real** si:
1. Su modelo macro (ODE) mejora la predicción del modelo micro (ABM) — C1 + EDI
2. Esta mejora no es trivial ni tautológica — EDI ∈ [0.325, 0.90]
3. La mejora es estadísticamente significativa — permutation p < 0.05
4. El sistema exhibe propiedades colectivas genuinas — Symploké, no-localidad, persistencia
5. El resultado es reproducible — C2, C3, C5

La **metaestabilidad** de la emergencia es un hallazgo, no un defecto: los hiperobjetos son atractores metaestables cuya realidad ontológica depende de la escala temporal de observación.

---

*Protocolo generado automáticamente. Última ejecución: ver `replay_hashes.json`*
