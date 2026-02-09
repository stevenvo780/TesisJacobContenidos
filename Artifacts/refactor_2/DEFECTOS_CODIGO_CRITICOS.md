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

## 5. ABM Y ODE NO ESTAN ACOPLADOS — ⚠️ PARCIALMENTE RESUELTO

> **Estado:** Se implementó acoplamiento **ODE→ABM** (top-down): la serie ODE se pasa como `macro_target_series` al ABM, que la usa como atractor en el término `mc * (macro_target - grid)`. También existe feedback **micro→macro** opcional que modifica el forcing antes de correr la ODE. Sin embargo:
> - 🚩 El acoplamiento es **unidireccional por defecto** (ODE corre primero, luego alimenta ABM)
> - 🚩 No hay iteración simultánea paso-a-paso
> - 🚩 La ODE no "ve" el estado del ABM durante la simulación

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`, lineas 696-698

```python
# ANTES (independientes):
abm = simulate_abm_fn(eval_params, steps, seed=2)   # Independiente
ode = simulate_ode_fn(eval_params, steps, seed=3)   # Independiente
```

```python
# AHORA (ODE→ABM):
ode = simulate_ode_fn(eval_params, steps, seed=3)
eval_params_ode["macro_target_series"] = ode[ode_key]
abm = simulate_abm_fn(eval_params_ode, steps, seed=2)
```

🚩 **Falta:** Acoplamiento bidireccional simultáneo paso-a-paso.

**Propuesta de acoplamiento real:**
```python
# En cada paso temporal:
ode_state = ode_solver.step(t, forcing[t])
macro_target = ode_state  # La ODE provee el target macro
# En el ABM:
delta = ... + mc * (macro_target - grid) + ...  # Acoplar a la ODE, no al mean(grid)
```

---

## 6. FASES SINTETICAS COMPARTIDAS — ❌ NO RESUELTO 🚩

> **Estado:** 🚩 25/29 casos siguen usando los mismos parámetros sintéticos (`ode_alpha=0.08, ode_beta=0.03`). La fase sintética genera datos idénticos para estos 25 casos. Cada caso debería tener parámetros de ODE sintética calibrados a su dominio.
>
> **Acción requerida:** Calibrar parámetros sintéticos por dominio para que cada caso tenga un ground truth diferenciado.

5+ grupos de casos comparten parametros sinteticos identicos:
- Grupo 1 (obs_mean=6.759): Clima, Energia, Finanzas, Wikipedia
- Grupo 2 (obs_mean=1.940): Oceanos, Acidificacion, Microplasticos, Acuiferos, IoT
- Grupo 3 (obs_mean=6.139): Justicia, Erosion Dialectica
- Grupo 4 (obs_mean=25.971): Politicas, Fuga Cerebros
- Grupo 5 (obs_mean=9.471): Movilidad, Riesgo Biologico

Todos generan datos sinteticos con la misma ODE `dX = alpha*(F-beta*X)`. La fase sintetica no discrimina dominios.
