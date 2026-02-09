# Caso 07 — Falsación por No-Estacionariedad

## Propósito

**Control negativo**: demuestra que el framework **no confunde regresión
espuria con emergencia causal** (Granger & Newbold 1974).

Dos tendencias lineales independientes producen correlación de Pearson
ρ > 0.99, pero NO existe relación causal.  El protocolo EDI debe
rechazar la hipótesis de emergencia.

**Resultado esperado**: EDI ≪ 0.30 → falsificación exitosa.

---

## Arquitectura (5 archivos)

| Archivo      | Rol                                              |
|-------------|---------------------------------------------------|
| `validate.py`| Orquestador: carga datos → `evaluate_phase` → EDI |
| `ode.py`     | Delega a `ode_models.py` modelo `random_walk`      |
| `abm.py`     | Delega a `abm_core.py` con `series_key="incidence"`|
| `data.py`    | Genera par de tendencias lineales independientes    |
| `metrics.py` | Métricas locales (RMSE, correlación, cohesión)     |

---

## Modelo de Datos — Regresión Espuria

### Diseño (Granger & Newbold 1974)

$$y(t) = t + \varepsilon_1, \quad \varepsilon_1 \sim \mathcal{N}(0, \sigma)$$
$$x(t) = t + \varepsilon_2, \quad \varepsilon_2 \sim \mathcal{N}(0, \sigma)$$

donde $\varepsilon_1$ y $\varepsilon_2$ son independientes.

### Correlación espuria

$$\rho(y, x) = \frac{\text{Var}(t)}{\text{Var}(t) + \sigma^2} \xrightarrow{n \to \infty} 1$$

Con $t \in [0, 1460]$ y $\sigma = 50$: $\text{Var}(t) \approx 178\,000$,
$\rho \approx 0.998$.

### Parámetros

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\sigma$  | 50    | SNR ≈ 29 al final del rango → ρ > 0.99 |
| freq      | diaria → semanal | Submuestreo W para runtime |
| seed      | 42    | Reproducibilidad |

---

## ODE — Random Walk (ode_models.py)

$$X_{t+1} = X_t + \delta + \varepsilon_t$$

Modelo sin estructura causal (control más débil posible).

---

## Configuración de Validación

```python
config = CaseConfig(
    case_name="Falsación: No-Estacionariedad",
    value_col="value",
    series_key="incidence",
    grid_size=20,
    driver_cols=["spurious_trend"],  # ← tendencia independiente
    ode_calibration=False,           # hipótesis nula
    abm_calibration=False,
    real_start="2020-01-01",
    real_end="2024-01-01",
    real_split="2022-01-01",
)
```

---

## Resultado

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| ρ(value, driver) | 0.998 | Correlación espuria altísima |
| EDI | −7.837 | Muy negativo → sin emergencia |
| Falsificación | ✅ **Exitosa** | EDI ≪ 0.30 pese a ρ ≈ 1.0 |

El framework distingue correctamente entre **correlación espuria** (por
tendencia compartida) y **causalidad descendente** (EDI).

---

## Correcciones Aplicadas (Auditoría)

| Problema | Corrección |
|----------|------------|
| `data.py`: `np.random` sin semilla → no reproducible | Añadido `np.random.default_rng(seed=42)` |
| `data.py`: código muerto Wikipedia API (~40 líneas) | Eliminado |
| `data.py`: `import requests, time, datetime` innecesarios | Eliminados |
| `data.py`: sin documentación del diseño experimental | Docstring con ref. Granger & Newbold |
| `validate.py`: función `make_synthetic` muerta | Eliminada |
| `validate.py`: `import numpy as np` no usado | Eliminado |
| `validate.py`: `rename(columns={"attention": "value"})` — columna inexistente | Eliminado |
| `validate.py`: comentarios residuales | Eliminados |

---

## Referencias

- Granger, C. W. J. & Newbold, P. (1974). Spurious regressions in econometrics. *Journal of Econometrics*, 2(2), 111–120.
- Phillips, P. C. B. (1986). Understanding spurious regressions in econometrics. *Journal of Econometrics*, 33(3), 311–340.
