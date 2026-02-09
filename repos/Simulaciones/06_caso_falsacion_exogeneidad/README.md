# Caso 06 — Falsación por Exogeneidad

## Propósito

**Control negativo** del framework de validación.  Demuestra que el
protocolo de Dependencia Efectiva (EDI) **no hallucina causalidad
espuria** cuando el driver exógeno es completamente independiente de la
señal objetivo.

| Señal objetivo | Driver exógeno | Relación causal |
|----------------|----------------|-----------------|
| GBM (caótico)  | sin(2π t/365)  | **Ninguna**     |

**Resultado esperado**: EDI ≪ 0.30 → falsificación exitosa.

---

## Arquitectura (5 archivos)

| Archivo      | Rol                                              |
|-------------|---------------------------------------------------|
| `validate.py`| Orquestador: carga datos → `evaluate_phase` → EDI |
| `ode.py`     | Delega a `ode_models.py` modelo `random_walk`      |
| `abm.py`     | Delega a `abm_core.py` con `series_key="incidence"`|
| `data.py`    | Genera serie GBM + driver sinusoidal               |
| `metrics.py` | Métricas locales (RMSE, correlación, cohesión)     |

---

## Modelo de Datos — Movimiento Browniano Geométrico (GBM)

### Ecuación (Hull 2018)

$$S(t) = S_0 \cdot \exp\!\left(\sum_{i=1}^{t}\left[(\mu - \tfrac{\sigma^2}{2})\Delta t + \sigma\sqrt{\Delta t}\,Z_i\right]\right)$$

donde $Z_i \sim \mathcal{N}(0,1)$ i.i.d.

### Parámetros

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\mu$     | 0.0005 d⁻¹ | ≈ 18 % anualizado (Baur & Dimpfl 2021, BTC drift) |
| $\sigma$  | 0.04       | ≈ 76 % vol. anualizada (BTC histórico 2017-2023) |
| $S_0$     | 10 000     | Nivel inicial arbitrario (se normaliza Z-score) |
| $P_\text{jump}$ | 0.01 | 1 % de días con salto ×0.9 o ×1.1 (componente Lévy) |

### Driver espurio

$$d(t) = \sin\!\left(\frac{2\pi\,t}{365}\right)$$

Periodicidad anual pura sin relación causal con el GBM.  Si el framework
detectara EDI > 0.30, indicaría un fallo fundamental del protocolo.

---

## ODE — Random Walk (ode_models.py)

$$X_{t+1} = X_t + \delta + \varepsilon_t$$

donde $\delta$ = drift (por defecto 0) y $\varepsilon_t \sim U(-\eta, \eta)$.

Este modelo no tiene estructura causal — es el control más débil posible.

| Parámetro | Valor | Origen |
|-----------|-------|--------|
| `ode_drift` | 0.0 | Sin dirección preferente |
| `ode_noise` | 0.01 | Default de `ode_models.py` |

---

## ABM — Motor estándar (abm_core.py)

Grilla $n \times n$ con regla de actualización:

$$g_{ij}^{t+1} = g_{ij}^t + d \cdot (\bar{g}_{\text{vec}} - g_{ij}^t) + f_s \cdot F_t + m_c \cdot (\bar{X} - g_{ij}^t) - \delta \cdot g_{ij}^t + \varepsilon$$

| Parámetro | Valor por defecto | Rol |
|-----------|-------------------|-----|
| `grid_size` | 20 | 400 celdas |
| `diffusion` | 0.2 | Acoplamiento vecinos |
| `forcing_scale` | Calibrado | Sensibilidad al driver |
| `macro_coupling` | Calibrado | Acoplamiento ODE→ABM |
| `damping` | Calibrado | Disipación |

---

## Configuración de Validación

```python
config = CaseConfig(
    case_name="Falsación: Exogeneidad",
    value_col="value",
    series_key="incidence",
    grid_size=20,
    driver_cols=["unrelated_driver"],  # ← driver sin relación causal
    ode_calibration=False,             # No calibrar (hipótesis nula)
    abm_calibration=False,             # No calibrar (hipótesis nula)
    real_start="2020-01-01",
    real_end="2024-01-01",
    real_split="2022-01-01",
)
```

**Nota**: calibración deshabilitada intencionalmente.  Si el framework
encontrara EDI alto *sin* calibrar contra datos reales, sería un fallo
del protocolo.

---

## Resultado

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| EDI     | −0.615 | Muy negativo → sin estructura macro detectable |
| Falsificación | ✅ **Exitosa** | EDI ≪ 0.30 |

---

## Correcciones Aplicadas (Auditoría)

| Problema | Corrección |
|----------|------------|
| `data.py`: `np.random` sin semilla → no reproducible | Añadido `np.random.default_rng(seed=42)` |
| `data.py`: código muerto Wikipedia API (`_fetch_article_daily`, `DEFAULT_ARTICLES`, `API_BASE`) | Eliminado |
| `data.py`: `import requests, time, datetime` innecesarios | Eliminados |
| `data.py`: bloque `try/raise/except` artificial | Reescrito directo |
| `data.py`: parámetros GBM sin documentación | Documentados con refs (Hull 2018, Baur & Dimpfl 2021) |
| `validate.py`: función `make_synthetic` muerta (nunca llamada) | Eliminada |
| `validate.py`: `print(f"DEBUG: ...")` en producción | Eliminado |
| `validate.py`: `import numpy as np` no usado | Eliminado |
| `validate.py`: comentarios residuales (`# No longer needed`, `# load_real_data_wrapper`) | Eliminados |

---

## Referencias

- Hull, J. (2018). *Options, Futures, and Other Derivatives* (10ª ed.). Pearson. — GBM.
- Baur, D. G. & Dimpfl, T. (2021). *The volatility of Bitcoin and its role as a medium of exchange and a store of value*. Empirical Economics, 61, 2663–2683. — Parámetros BTC.
- Morton, T. (2013). *Hyperobjects*. University of Minnesota Press. — Viscosidad temporal, no-localidad.
