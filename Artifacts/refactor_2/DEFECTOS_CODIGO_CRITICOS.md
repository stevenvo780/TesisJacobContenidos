# Defectos de Codigo Criticos — Referencia Tecnica

## 1. DATA LEAKAGE EN FORCING

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

## 2. INCONSISTENCIA overall_pass vs EDI > 0.90

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`
**Problema:** `overall_pass` no incorpora la regla `edi.valid == false` cuando EDI > 0.90.

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

## 3. ODE GENERICA (28/29 IDENTICAS)

**Archivos:** `repos/Simulaciones/caso_*/src/ode.py` (28 archivos)

**Todas usan la misma ecuacion:**
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

## 4. ABM SIN HETEROGENEIDAD

**Archivos:** `repos/Simulaciones/caso_*/src/abm.py` (todos)

**Problema:** Todos los agentes son identicos. La ecuacion de actualizacion:
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

## 5. ABM Y ODE NO ESTAN ACOPLADOS

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`, lineas 696-698

```python
abm = simulate_abm_fn(eval_params, steps, seed=2)   # Independiente
ode = simulate_ode_fn(eval_params, steps, seed=3)    # Independiente
```

No hay ninguna linea donde la salida de la ODE alimente al ABM. El `macro_coupling` en el ABM acopla celdas a su propio promedio (`grid.mean()`), no a la ODE.

**Propuesta de acoplamiento real:**
```python
# En cada paso temporal:
ode_state = ode_solver.step(t, forcing[t])
macro_target = ode_state  # La ODE provee el target macro
# En el ABM:
delta = ... + mc * (macro_target - grid) + ...  # Acoplar a la ODE, no al mean(grid)
```

---

## 6. FASES SINTETICAS COMPARTIDAS

5+ grupos de casos comparten parametros sinteticos identicos:
- Grupo 1 (obs_mean=6.759): Clima, Energia, Finanzas, Wikipedia
- Grupo 2 (obs_mean=1.940): Oceanos, Acidificacion, Microplasticos, Acuiferos, IoT
- Grupo 3 (obs_mean=6.139): Justicia, Erosion Dialectica
- Grupo 4 (obs_mean=25.971): Politicas, Fuga Cerebros
- Grupo 5 (obs_mean=9.471): Movilidad, Riesgo Biologico

Todos generan datos sinteticos con la misma ODE `dX = alpha*(F-beta*X)`. La fase sintetica no discrimina dominios.
