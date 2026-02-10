# Protocolo Formal de Validación — Irrealismo Operativo de Hiperobjetos

**Versión**: 3.0  
**Fecha**: 2025-07-11  
**Autor**: Jacob (generado por framework de validación)

---

## 1. Objetivo

Este protocolo define los criterios formales para clasificar el **grado de cierre operativo** de un fenómeno candidato a hiperobjeto (en el sentido de Morton, 2013). El marco teórico es el **irrealismo operativo**: no se asume compromiso ontológico sobre la existencia sustancial de los hiperobjetos; se mide únicamente si su modelo macroscópico (ODE) constriñe operativamente la dinámica de sus componentes microscópicos (ABM), expresado como un gradiente de niveles (0–4).

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
| EDI ∈ [0.325, 0.90] | Nivel ≥ 4 | Cierre operativo fuerte |
| EDI permutation p < 0.05 | Significativo | No es artefacto aleatorio |
| Coupling ≥ 0.10 | No epifenomenal | La macro tiene efecto medible |
| RMSE > 1e-10 | No fraude | No hay sobreajuste trivial |
| CR > 2.0 | Indicador (informativo) | Symploké — cohesión interna > externa |
| No-localidad: dom < 0.05 | Descentralizado | No hay agente dominante |
| Persistencia: var_modelo < 5·var_obs | Temporal | La estructura persiste |
| Viscosity pass | Inercia | El sistema resiste perturbaciones |

## 5. Taxonomía de Cierre Operativo

| Categoría | Nivel | Condición | Interpretación |
|-----------|:-----:|-----------|----------------|
| **Strong** | 4 | EDI ∈ [0.325, 0.90] + p < 0.05 | Cierre operativo fuerte: constricción macro→micro robusta |
| **Weak** | 3 | EDI ∈ [0.10, 0.325) + p < 0.05 | Cierre parcial: señal macro significativa pero bajo umbral |
| **Suggestive** | 2 | EDI > 0 + p < 0.05 | Cierre sugestivo: señal débil pero significativa |
| **Trend** | 1 | EDI > 0 + p ≥ 0.05 | Tendencia no confirmada estadísticamente |
| **Null** | 0 | EDI ≤ 0 | Sin evidencia de cierre operativo |
| **Falsification** | — | Diseño de control | Rechazo esperado por diseño |

> **Nivel 5** (hiperobjeto fuerte) se reserva teóricamente para fenómenos que además de Nivel 4 exhiban CR > 2.0 y persistencia extendida verificada longitudinalmente. Ningún caso actual alcanza este nivel.

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
| EDI < 0.325 | No alcanza Nivel 4 | Sin cierre operativo fuerte |
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

## 11. Interpretación bajo Irrealismo Operativo

Un fenómeno exhibe **cierre operativo de grado G** si:
1. Su modelo macro (ODE) constriñe la dinámica del modelo micro (ABM) — C1 + EDI
2. Esta constricción no es trivial ni tautológica — EDI ∈ [0.325, 0.90]
3. La constricción es estadísticamente significativa — permutation p < 0.05
4. El sistema exhibe propiedades colectivas medibles — Symploké, no-localidad, persistencia
5. El resultado es reproducible — C2, C3, C5

El grado G se expresa en la escala de niveles 0–4. No se predica existencia sustancial del hiperobjeto: el EDI mide grado de constricción operativa macro→micro, no realidad ontológica. La **metaestabilidad** de la emergencia es un hallazgo, no un defecto: los hiperobjetos son atractores metaestables cuyo grado de cierre operativo depende de la escala temporal de observación.

---

*Protocolo generado automáticamente. Última ejecución: ver `replay_hashes.json`*
