# Caso 10 — Justicia Algorítmica

## Propósito

Evaluar si la «justicia algorítmica» (normas legales que permean la
sociedad) exhibe propiedades de hiperobjeto: viscosidad temporal,
no-localidad, y causalidad descendente sobre las opiniones individuales.

---

## Arquitectura (5 archivos)

| Archivo      | Rol                                              |
|-------------|---------------------------------------------------|
| `validate.py`| Orquestador: pipeline C1-C5 sintético→real       |
| `ode.py`     | Delega a `ode_models.py` modelo `logistic_forced`  |
| `abm.py`     | Deffuant Bounded Confidence (opinión espacial)     |
| `data.py`    | Datos reales vía `data_universal` + fallback      |
| `metrics.py` | Métricas estándar                                 |

---

## ODE — Logística Forzada (ode_models.py)

$$\frac{dX}{dt} = r\,X\!\left(1 - \frac{X}{K}\right) + \gamma\,F(t) - \delta\,X + \varepsilon$$

| Parámetro | Clave | Default | Justificación |
|-----------|-------|---------|---------------|
| $r$       | `ode_r` / `ode_alpha` | 0.05 | Tasa crecimiento logístico |
| $K$       | `ode_k` | 1.0 | Capacidad de carga (opinión normalizada [0,1]) |
| $\gamma$  | `ode_gamma` | 0.1 | Sensibilidad al forcing |
| $\delta$  | `ode_delta` / `ode_beta` | 0.02 | Tasa de decaimiento |

---

## ABM — Deffuant Bounded Confidence Espacial

Modelo de dinámica de opinión (Deffuant et al. 2000) en grilla:

### Regla de actualización (por vecino $j$)

$$\text{si } |o_i - o_j| < \varepsilon: \quad \Delta o_i = \mu \cdot (o_j - o_i)$$

Con 4 vecinos, la actualización total se normaliza por $\times 0.25 = 1/4$.

### Campo global (fuerza de la ley)

$$o_i \leftarrow o_i + \lambda \cdot (F_t - o_i) + \varepsilon_\sigma$$

### Parámetros

| Parámetro | Clave | Valor | Justificación |
|-----------|-------|-------|---------------|
| $\varepsilon$ | `abm_epsilon` | 0.2 | Límite de confianza (Deffuant et al. 2000: rango 0.1–0.5) |
| $\mu$ | `abm_mu` | 0.3 | Velocidad convergencia (clásico: 0.5 para pares) |
| $\lambda$ | `abm_law_strength` | 0.05 | Influencia legal sobre opinión |
| $\sigma$ | hardcoded | 0.01 | Ruido estocástico por paso |
| $\times 0.25$ | hardcoded | 1/4 | Normalización: 4 vecinos en grilla 2D |
| grid_size | config | 20 | 400 agentes |

---

## Datos

Fuente: Índice de Estado de Derecho (World Justice Project / World Bank),
cargado vía `data_universal.fetch_case_data`. Fallback sintético si falla.

Período: 1963-01-01 a 2023-01-01, split 2005-01-01.

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | −0.025 | Sin estructura macro |
| Real | 0.000 | Neutral → sin emergencia detectable |

---

## Correcciones Aplicadas (Auditoría)

| Problema | Corrección |
|----------|------------|
| `abm.py`: `import random` muerto (nunca usado, usa `np.random.default_rng`) | Eliminado |
| `abm.py`: sin documentación de parámetros | Docstring completo con refs Deffuant |
| `validate.py`: docstring genérico | Reescrito con contexto específico |

---

## Referencias

- Deffuant, G., Neau, D., Amblard, F. & Weisbuch, G. (2000). Mixing beliefs among interacting agents. *Advances in Complex Systems*, 3(01n04), 87–98.
- Hegselmann, R. & Krause, U. (2002). Opinion dynamics and bounded confidence models, analysis, and simulation. *Journal of Artificial Societies and Social Simulation*, 5(3).
