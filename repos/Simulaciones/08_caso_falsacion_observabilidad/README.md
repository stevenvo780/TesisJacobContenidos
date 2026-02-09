# Caso 08 — Falsación por Observabilidad Escasa

## Propósito

**Control negativo**: demuestra que el framework rechaza un **driver
insuficiente** (proxy que solo captura la tendencia) cuando el target
contiene dinámica de alta frecuencia generada por una causa oculta.

| Componente | Fórmula | Información |
|------------|---------|-------------|
| Causa oculta Z | 0.05·t + 2·sin(0.5·t) | Tendencia + oscilación |
| Target Y | Z + ε_Y | Realidad completa |
| Driver X | 0.05·t + ε_X | Solo tendencia (proxy pobre) |

ρ(X, Y) ≈ 0.91 (por tendencia compartida), pero X carece de la
oscilación sin(0.5·t) que domina la varianza de Y.

**Resultado esperado**: EDI ≪ 0.30 → falsificación exitosa.

---

## Arquitectura (5 archivos)

| Archivo      | Rol                                              |
|-------------|---------------------------------------------------|
| `validate.py`| Orquestador: carga datos → `evaluate_phase` → EDI |
| `ode.py`     | Delega a `ode_models.py` modelo `constant`          |
| `abm.py`     | Delega a `abm_core.py` con `series_key="incidence"`|
| `data.py`    | Genera datos sintéticos de confounder               |
| `metrics.py` | Métricas locales (RMSE, correlación, cohesión)     |

---

## Modelo de Datos — Confounder Sintético

### Causa oculta (no observable)

$$Z(t) = 0.05\,t + 2\sin(0.5\,t)$$

- Tendencia: 0.05 unidades/mes (acumulación lenta)
- Oscilación: período $T = 2\pi/0.5 \approx 12.6$ meses

### Target

$$Y(t) = Z(t) + \varepsilon_Y, \quad \varepsilon_Y \sim \mathcal{N}(0, 0.2)$$

### Driver insuficiente

$$X(t) = 0.05\,t + \varepsilon_X, \quad \varepsilon_X \sim \mathcal{N}(0, 0.1)$$

### Parámetros

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| trend_slope | 0.05 u/mes | Tendencia lineal moderada |
| osc_ampl | 2.0 | Amplitud > σ_Y → señal detectable |
| osc_freq | 0.5 rad/mes | T ≈ 12.6 meses (sub-anual) |
| σ_Y | 0.2 | Ruido target (< amplitud oscilación) |
| σ_X | 0.1 | Ruido driver (< σ_Y) |
| freq datos | mensual (MS) | Resolución suficiente para capturar oscilación |

---

## ODE — Constant (ode_models.py)

$$X_{t+1} = X_t + \varepsilon_t, \quad \varepsilon_t \sim U(-\eta, \eta)$$

Modelo sin estructura: sólo ruido alrededor del valor inicial.
Control más débil posible para falsificación.

---

## Configuración de Validación

```python
config = CaseConfig(
    case_name="Falsación: Observabilidad Escasa",
    value_col="value",
    series_key="incidence",
    grid_size=20,
    persistence_window=3,
    driver_cols=["insufficient_driver"],  # ← proxy insuficiente
    ode_calibration=False,
    abm_calibration=False,
    real_start="2005-01-01",
    real_end="2023-01-01",
    real_split="2015-01-01",
)
```

---

## Resultado

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| ρ(X, Y) | 0.906 | Correlación alta (tendencia compartida) |
| EDI | −3.772 | Muy negativo → driver insuficiente rechazado |
| Falsificación | ✅ **Exitosa** | EDI ≪ 0.30 pese a ρ ≈ 0.91 |

El framework distingue correctamente entre un **proxy correlacionado**
(que solo captura la tendencia) y un **driver causal** (que debería
explicar la dinámica completa incluyendo la oscilación).

---

## Correcciones Aplicadas (Auditoría)

| Problema | Corrección |
|----------|------------|
| `data.py`: `np.random` sin semilla → no reproducible | Añadido `np.random.default_rng(seed=42)` |
| `data.py`: código muerto OWID API (`_request`, `DATA_URL`, `DEFAULT_UA`) | Eliminado |
| `data.py`: `import random, requests, datetime` innecesarios | Eliminados |
| `data.py`: `import numpy as np` dentro de función | Movido a nivel de módulo |
| `data.py`: params muertos (`entity`, `fallback_entity`, `drop_rate`, `refresh`) | Eliminados de firma |
| `data.py`: sin documentación del diseño experimental | Docstring completo |
| `validate.py`: función `make_synthetic` muerta | Eliminada |
| `validate.py`: `import numpy as np` no usado | Eliminado |
| `validate.py`: comentarios residuales | Eliminados |

---

## Referencias

- Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2ª ed.). Cambridge. — Confounders y causalidad.
- Spirtes, P., Glymour, C. & Scheines, R. (2000). *Causation, Prediction, and Search*. MIT Press.
