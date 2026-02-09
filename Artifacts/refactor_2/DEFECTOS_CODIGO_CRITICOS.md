# Defectos de Codigo Criticos — Referencia Tecnica

## 1. DATA LEAKAGE EN FORCING — ✅ RESUELTO

> **Estado:** Corregido en `hybrid_validator.py`. El `lag_forcing` ahora usa persistencia (`last_known`) para el periodo de validación en lugar de `obs[:-1]`. La tendencia se ajusta solo con datos de entrenamiento.

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`
**Lineas:** 644-647

```python
# ACTUAL (PROBLEMATICO):
forcing_trend, trend_params = build_forcing_from_training(obs[:val_start], steps)
lag_forcing = [obs[0]] + obs[:-1]  # <-- obs del periodo de validacion se filtran aqui
forcing_series = [forcing_trend[i] + 0.5 * lag_forcing[i] for i in range(steps)]
```

**Problema:** `obs[:-1]` incluye observaciones del periodo de validacion (t >= val_start). El modelo "ve" el futuro.

**Correccion propuesta:**
```python
# CORREGIDO:
forcing_trend, trend_params = build_forcing_from_training(obs[:val_start], steps)
# Solo usar observaciones del entrenamiento para lag_forcing
lag_train = [obs[0]] + list(obs[:val_start-1])
# Para validacion: usar ultimo valor conocido (persistence)
lag_val = [obs[val_start-1]] * (steps - val_start)
lag_forcing = lag_train + lag_val
forcing_series = [forcing_trend[i] + 0.5 * lag_forcing[i] for i in range(steps)]
```

---

## 2. INCONSISTENCIA overall_pass vs EDI > 0.90 — ✅ RESUELTO (código)

> **Estado:** El código ahora incluye `edi_valid` (rango 0.30–0.90) dentro de la conjunción `overall_pass = all([..., edi_valid, cr_valid])`. Los `metrics.json` actuales ya reflejan `overall_pass = 0/29`, confirmando la corrección.

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`
**Problema original:** `overall_pass` no incorporaba la regla `edi.valid == false` cuando EDI > 0.90.

**Buscar donde se calcula overall_pass y agregar:**
```python
# overall_pass debe incluir:
overall_pass = (
    c1_convergence and c2_robustness and c3_replication
    and c4_validity and c5_uncertainty
    and coupling_check and rmse_fraud_check
    and edi_result["valid"]  # <-- AGREGAR ESTO
)
```

---

## 3. ODE GENERICA (28/29 IDENTICAS) — ✅ RESUELTO

> **Estado:** Ahora existen **11 modelos ODE distintos** en `common/ode_library.py`: Budyko-Sellers (clima), Heston (finanzas), SEIR (epidemiología), Swing Equation (energía), Ocean Thermal (océanos), Acidification (acidificación), Aquifer Balance (acuíferos), Accumulation-Decay, Logistic-Forced, Random Walk y Constant. Cada caso selecciona un `ode_model` específico.

**Archivos:** `repos/Simulaciones/caso_*/src/ode.py` (28 archivos)

**Antes todas usaban la misma ecuacion:**
```python
dX/dt = alpha * (F(t) - beta * X) + noise
```

**Solo caso_epidemiologia (05) tiene ODE especifica (SEIR).**

**ODEs domain-specific recomendadas:**

### Clima (balance radiativo):
```python
# Modelo de Budyko-Sellers simplificado
S = 1361  # W/m2 solar constant
alpha_albedo = 0.3  # albedo promedio
epsilon = 0.62  # emisividad
sigma = 5.67e-8  # Stefan-Boltzmann
C = 4.0e8  # capacidad termica efectiva J/(m2*K)

def dT_dt(T, F_co2, t):
    """F_co2 = forcing radiativo por CO2 (W/m2)"""
    return (S * (1 - alpha_albedo) / 4 - epsilon * sigma * T**4 + F_co2) / C
```

### Finanzas (volatilidad estocastica):
```python
# Modelo Heston simplificado
def dp_dt(p, v, mu, dt, dW1):
    return mu * p * dt + np.sqrt(v) * p * dW1

def dv_dt(v, kappa, theta, xi, dt, dW2):
    return kappa * (theta - v) * dt + xi * np.sqrt(v) * dW2
```

### Acuiferos (balance hidrico):
```python
# Ecuacion de balance de masa
def dh_dt(h, recharge, extraction, K, S):
    """h = nivel freatico, K = conductividad, S = storativity"""
    return (recharge - extraction - K * h) / S
```

---

## 4. ABM SIN HETEROGENEIDAD — ✅ RESUELTO

> **Estado:** El ABM ahora implementa 3 capas de heterogeneidad en `common/abm_core.py`:
> - **`forcing_gradient`** (radial/linear/random_hubs) — forcing espacialmente no uniforme
> - **`heterogeneity_strength=0.15`** — difusión, damping y ruido varían por celda
> - **Topología opcional** — small-world o scale-free
>
> Todos los casos pasan por `hybrid_validator.py` que inyecta estos parámetros por defecto.

**Archivos:** `repos/Simulaciones/caso_*/src/abm.py` (todos)

**Problema original:** Todos los agentes eran identicos. La ecuacion de actualizacion:
```python
delta = diff * (nb_mean - grid) + fs * f + mc * (macro - grid) - dmp * grid + noise
```
no tiene ningun termino que distinga un agente de otro excepto su posicion en la grilla (que se homogeniza por difusion).

**Existe solucion no integrada:** `common/abm_gpu_v3.py` implementa:
- `forcing_gradient`: forzamiento espacialmente heterogeneo
- `_neighbor_mean_sparse`: difusion por red compleja (no solo grilla regular)
- `adjacency_matrix`: topologia de red configurable

**Pero NINGUN validate.py lo usa.** Grep confirma 0 archivos de validacion importan `abm_gpu_v3`.

---

## 5. ABM Y ODE NO ESTAN ACOPLADOS — ✅ RESUELTO

> **Estado:** Acoplamiento **bidireccional** implementado en `hybrid_validator.py`:
> - **ODE→ABM** (top-down): la serie ODE se pasa como `macro_target_series` al ABM, que la usa como atractor en el término `ode_cs * (macro_target - grid_mean)`.
> - **ABM→ODE** (bottom-up): el campo medio del ABM se pasa como `abm_feedback_series` a la ODE con `abm_feedback_gamma=0.05`. La ODE recibe feedback `dx += gamma * (abm_mean[t] - x)`.
> - **2 iteraciones** de acoplamiento: ODE₁→ABM₁→ODE₂→ABM₂ para convergencia.
> - **`ode_coupling_strength`** separado de `macro_coupling`: el auto-acoplamiento ABM usa `mc`, el nudging ODE→ABM usa `ode_cs = min(0.30, mc*0.8)`.
>
> Verificación: 29/29 casos tienen `ode_coupling_strength` y `abm_feedback_gamma=0.05` en `metrics.json`.

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`

```python
# ACTUAL (bidireccional, 2 iteraciones):
# Iteración 1: ODE→ABM
ode1 = simulate_ode_fn(eval_params, steps, seed=3)
eval_params["macro_target_series"] = ode1[ode_key]
abm1 = simulate_abm_fn(eval_params, steps, seed=2)
# Iteración 2: ABM→ODE→ABM  
eval_params["abm_feedback_series"] = abm1["global_mean"]
eval_params["abm_feedback_gamma"] = 0.05
ode2 = simulate_ode_fn(eval_params, steps, seed=3)
eval_params["macro_target_series"] = ode2[ode_key]
abm_final = simulate_abm_fn(eval_params, steps, seed=2)
```

---

## 6. FASES SINTETICAS COMPARTIDAS — ⚠️ PARCIALMENTE RESUELTO

> **Estado:** 6/29 casos ya tienen parámetros sintéticos domain-specific (01 clima, 02 conciencia, 03 contaminación, 04 energía, 09 finanzas, 10 justicia). Los 23 restantes siguen usando `ode_alpha=0.08, ode_beta=0.03`.
>
> **Acción requerida:** Calibrar parámetros sintéticos por dominio para los 23 casos restantes.

5+ grupos de casos comparten parametros sinteticos identicos:
- Grupo 1 (obs_mean=6.759): Clima, Energia, Finanzas, Wikipedia
- Grupo 2 (obs_mean=1.940): Oceanos, Acidificacion, Microplasticos, Acuiferos, IoT
- Grupo 3 (obs_mean=6.139): Justicia, Erosion Dialectica
- Grupo 4 (obs_mean=25.971): Politicas, Fuga Cerebros
- Grupo 5 (obs_mean=9.471): Movilidad, Riesgo Biologico

Todos generan datos sinteticos con la misma ODE `dX = alpha*(F-beta*X)`. La fase sintetica no discrimina dominios.
