# Caso 09 — Finanzas (SPY / S&P 500)

## Propósito

Evaluar si el mercado financiero (S&P 500) exhibe emergencia tipo
hiperobjeto.  Resultado histórico: **RECHAZADO** — EDI ≈ 0.05 (por
debajo del umbral 0.30), consistente con reflexividad (Soros 1987),
aliasing temporal, y eficiencia de mercado (Fama 1970).

---

## Arquitectura (5 archivos)

| Archivo      | Rol                                              |
|-------------|---------------------------------------------------|
| `validate.py`| Orquestador: datos reales SPY → pipeline C1-C5   |
| `ode.py`     | Delega a `ode_models.py` modelo `heston`           |
| `abm.py`     | HAM Brock-Hommes espacial (fundamentalistas + chartistas) |
| `data.py`    | Descarga SPY + VIX + FedFunds + CPI + credit spread |
| `metrics.py` | Métricas estándar + kurtosis + vol. clustering    |

---

## ODE — Heston Simplificado (ode_models.py)

Modelo de volatilidad estocástica (Heston 1993):

$$dv = \kappa(\theta - v)\,dt + \xi\sqrt{v}\,dW_v$$
$$dp = \mu\,p\,dt + \sqrt{v}\,dW_p + 0.1\,F(t)$$

### Parámetros

| Parámetro | Clave | Default | Justificación |
|-----------|-------|---------|---------------|
| $\mu$ | `ode_mu` | 0.05 | Drift medio (= ode_alpha default) |
| $\kappa$ | `ode_kappa` | 0.02 | Velocidad reversión vol (= ode_beta) |
| $\theta$ | `ode_theta` | 0.1 | Nivel equilibrio volatilidad |
| $\xi$ | `ode_xi` | 0.1 | Vol-of-vol (Heston 1993) |
| $v_0$ | `v0` | 0.1 | Volatilidad inicial |

**Nota**: Los parámetros por defecto se calibran vía grid search
del framework `hybrid_validator.py` (ode_alpha → μ, ode_beta → κ).

---

## ABM — Heterogeneous Agent Model (Brock-Hommes espacial)

Modelo de agentes heterogéneos (Brock & Hommes 1998) en versión
espacial con switching tipo Ising:

### Tipos de agentes
- **Fundamentalistas**: $D_f = g_f \cdot (P^* - P_t)$ (reversión al valor fundamental)
- **Chartistas**: $D_c = g_c \cdot (P_t - P_{t-1})$ (seguimiento de tendencia)

### Exceso de demanda

$$\Delta P = \frac{n_f D_f + n_c D_c + \varepsilon}{\lambda}$$

### Switching (discrete choice)

$$n_c = \frac{1}{1 + e^{-\beta(\pi_c - \pi_f)}}$$

donde $\pi_c, \pi_f$ son rentabilidades acumuladas con decaimiento $\eta$.

### Parámetros

| Parámetro | Clave | Default | Justificación |
|-----------|-------|---------|---------------|
| $\beta$ | `abm_beta` | 3.0 | Intensidad de elección (Brock & Hommes 1998) |
| $g_f$ | `abm_g_fund` | 0.1 | Agresividad fundamentalista |
| $g_c$ | `abm_g_chart` | 0.5 | Agresividad chartista |
| $\sigma_\varepsilon$ | `abm_noise` | 0.05 | Ruido de mercado |
| $\eta$ | hardcoded | 0.1 | Decaimiento de memoria de beneficios |
| $\lambda$ | calculado | $0.1 \cdot N$ | Profundidad de mercado |
| Factor ×10 | hardcoded | 10.0 | Escalamiento forcing→precio (absorbido por grid search) |

**Nota sobre grid_size=1**: Con 1 agente, el modelo espacial se reduce
al modelo agregado clásico de Brock & Hommes (1998).

---

## Datos Reales

| Fuente | Serie | Variable |
|--------|-------|----------|
| Yahoo Finance | SPY | log(Close) → `value` |
| Yahoo Finance | ^VIX | `vix` |
| FRED | FEDFUNDS | `fedfunds` |
| FRED | CPIAUCSL | `inflation` (YoY) |
| FRED | BAA-AAA | `credit_spread` |
| Yahoo Finance | SPY Volume | `volume` |

Período: 1990-01-01 a 2024-12-31, split 2011-01-01.

---

## Configuración de Validación

```python
config = CaseConfig(
    case_name="Finanzas (SPY)",
    value_col="value",
    series_key="x",
    grid_size=1,
    driver_cols=["vix", "fedfunds", "inflation", "credit_spread", "volume"],
    use_topology=True,
    topology_type="small_world",
    topology_params={"k": 4, "p": 0.1},
    feedback_strength=0.05,
    loe=5,
)
```

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | −0.000 | Neutral |
| Real | 0.051 | Muy bajo → **RECHAZADO** |

El mercado financiero no exhibe emergencia tipo hiperobjeto bajo este
protocolo.  Consistente con:
- **Reflexividad** (Soros 1987): los agentes reaccionan al agregado,
  creando ciclos endógenos que impiden la causalidad descendente estable.
- **Eficiencia de mercado** (Fama 1970): la información se incorpora
  demasiado rápido para que la ODE macro capture estructura.
- **Aliasing temporal**: la frecuencia mensual pierde dinámica intradiaria.

---

## Correcciones Aplicadas (Auditoría)

| Problema | Corrección |
|----------|------------|
| `abm.py`: `import random` muerto (nunca usado) | Eliminado |
| `validate.py`: `sentiment_scale=0.05` en extra_base_params (ABM no lo lee) | Eliminado (parámetro muerto) |
| `validate.py`: bloque diagnóstico verbose (Stylized Facts) | Eliminado (funciones kurtosis/vol_clustering quedan en metrics.py) |
| `validate.py`: docstring genérico | Reescrito con contexto específico |

### Números documentados pero no modificados

| Número | Ubicación | Justificación |
|--------|-----------|---------------|
| `×10` (forcing→precio) | abm.py L64 | Escalamiento absorbido por grid search de forcing_scale |
| `clip(-100, 100)` | abm.py L172 | Límite anti-explosión; rango [-100,100] en log-precio ≈ $e^{-100}$ a $e^{100}$ |
| `clip(-20, 20)` | abm.py L98 | Estabilidad numérica logística |
| `eta=0.1` | abm.py L91 | Decaimiento memoria; τ = 1/η = 10 pasos |

---

## Referencias

- Brock, W. A. & Hommes, C. H. (1998). Heterogeneous beliefs and routes to chaos in a simple asset pricing model. *Journal of Economic Dynamics and Control*, 22(8-9), 1235–1274.
- Heston, S. L. (1993). A closed-form solution for options with stochastic volatility. *Review of Financial Studies*, 6(2), 327–343.
- Fama, E. F. (1970). Efficient capital markets: A review of theory and empirical work. *Journal of Finance*, 25(2), 383–417.
- Soros, G. (1987). *The Alchemy of Finance*. Simon & Schuster.
