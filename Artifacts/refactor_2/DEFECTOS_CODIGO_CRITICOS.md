# Defectos de Codigo Criticos — Referencia Tecnica

> **Última actualización:** 2026-02-12 (commit 23214c0 — T1-T8 fixes). **overall_pass = 1/29** (Caso 16 Deforestación).
> Defectos D1-D8 ya resueltos. P4-P10 fixes previos. Nuevos fixes T1-T8: driver_cols expandido (19/29), synthetic params 29/29, salinización proxy mejorado, replay_hash.py, trend_bias test, docs circularidad/inercia, interpretación cautelosa.
>
> ⚠️ **Regresiones T1:** Caso 24 (Microplásticos) strong→trend (EDI 0.427→0.289, perdió sig). Caso 27 (Riesgo Bio) trend→null (EDI +0.105→-1.000). Causa: driver_cols adicionales empeoran OLS en series cortas.

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

## 5. ABM Y ODE NO ESTAN ACOPLADOS — ✅ RESUELTO (Fix C13-b, commit 3d0a9d1)

> **Estado:** Acoplamiento **bidireccional** implementado en `hybrid_validator.py`:
> - **ODE→ABM** (top-down): la serie ODE se pasa como `macro_target_series` al ABM, que la usa como atractor en el término `ode_cs * (macro_target - grid_mean)`.
> - **ABM→ODE** (bottom-up, Fix C13-b): nudging post-integración en `hybrid_validator.py`. Después de generar la serie ODE con `simulate_ode_fn`, se aplica `ode[t] += γ·(abm_mean[t] - ode[t])` con γ=0.05.
> - **2 iteraciones** de acoplamiento: ODE₁→ABM₁→nudge(ODE₁,ABM₁)→ABM₂ para convergencia.
> - **`ode_coupling_strength`** separado de `macro_coupling`: el auto-acoplamiento ABM usa `mc`, el nudging ODE→ABM usa `ode_cs = min(0.30, mc*0.8)`.
>
> **Fix C13-b (commit 3d0a9d1):** El nudging ABM→ODE se aplica como post-proceso sobre la serie ODE ya generada:
> ```python
> for t in range(1, len(ode)):
>     ode[t] += gamma * (abm_mean[t] - ode[t])  # gamma = 0.05
> ```
> Equivalente a integración Euler de primer orden para `dODE/dt += γ·(ABM_mean - ODE)`.
>
> Verificación: 29/29 casos tienen `ode_coupling_strength` y `calibration.abm_feedback_gamma=0.05` en `metrics.json`.

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

## 6. FASES SINTETICAS COMPARTIDAS — ✅ RESUELTO (T2, commit 23214c0)

> **Estado:** **29/29** casos tienen parámetros sintéticos domain-specific. T2 confirmó que todos los `validate.py` ya incluían `synth_meta` calibrado por dominio desde refactors anteriores.
>
> **Verificado:** `grep -l 'synth_meta\|synthetic_params' repos/Simulaciones/*/src/validate.py` = 29/29.

5+ grupos de casos comparten parametros sinteticos identicos:
- Grupo 1 (obs_mean=6.759): Clima, Energia, Finanzas, Wikipedia
- Grupo 2 (obs_mean=1.940): Oceanos, Acidificacion, Microplasticos, Acuiferos, IoT
- Grupo 3 (obs_mean=6.139): Justicia, Erosion Dialectica
- Grupo 4 (obs_mean=25.971): Politicas, Fuga Cerebros
- Grupo 5 (obs_mean=9.471): Movilidad, Riesgo Biologico

Todos generan datos sinteticos con la misma ODE `dX = alpha*(F-beta*X)`. La fase sintetica no discrimina dominios.

---

## 7. BIAS CORRECTION ODE→ABM — ✅ RESUELTO (commit 54234d6 + Fix #7-b/c en commit 3d0a9d1)

> **Estado:** Implementado en `hybrid_validator.py` con **4 modos** tras 3 mejoras incrementales:
> - **Fix #7-b: Umbral adaptativo** — Bajado de 0.5 a **0.3** para capturar ODE con correlación moderada pero útil. Resultado: `bias_only` subió de 7 a **11 casos** en fase real.
> - **Fix #7-b: Clipping de serie ODE** — `np.clip(ode, -5·range, +5·range)` protege contra explosión numérica (Starlink EDI=-521 acotado por clipping).
> - **Fix #7-c: Guarda de reversión** — Si BC empeora RMSE (ABM acoplado con BC peor que ABM sin ODE), se re-ejecuta sin BC. Si la versión sin BC es mejor, se revierte → `bc_mode = "reverted"`. Esto elimina casos donde BC destruía el resultado.
>
> **Resultados post Fix #7-b/c (fase real):**
> - `full`: 5 casos (05, 13, 16, 18, 22)
> - `bias_only`: 11 casos (01, 06-08, 10, 14, 17, 19, 23, 28, 29)
> - `none`: 10 casos (03-04, 09, 11-12, 15, 20, 24-26)
> - **`reverted`**: **3 casos** (02-Conciencia, 21-Salinización, 27-Riesgo Biológico)
>
> **Impacto de reversión:** Caso 27 pasó de null (EDI=-0.077) a **trend** (EDI=+0.105) tras revertir BC que empeoraba.

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`, líneas ~917-948

**Problema:** La ODE puede tener correlación alta con observaciones (corr > 0.8) pero operar en una escala completamente diferente (ej: ODE en miles, observaciones en unidades). Cuando esta serie se pasa como `macro_target_series` al ABM, el término de nudging `ode_cs * (macro_target - grid_mean)` genera fuerzas enormes que destruyen la predicción.

**Caso emblemático:** Deforestación (16) — ODE corr=0.878 con obs, pero RMSE_ode astronomía → EDI=-0.294. Con BC full: EDI=+0.629 (STRONG).

**Corrección implementada — 3 modos:**

```python
# 1. Calcular correlación y escala en periodo de entrenamiento
corr_train = np.corrcoef(ode_train, obs_train)[0, 1]
scale_factor = np.std(obs_train) / np.std(ode_train)

# 2. Decidir modo BC
if corr_train > 0.5 and 0.2 <= scale_factor <= 5.0:
    # FULL: transformada afín (media + std)
    ode_bc = (ode - mean_ode) * scale_factor + mean_obs
elif corr_train > 0.5:
    # BIAS_ONLY: solo corregir media (escala extrema → no tocar varianza)
    ode_bc = ode - mean_ode + mean_obs
else:
    # NONE: ODE no correlaciona — no aplicar BC
    ode_bc = ode
```

**Guardas de seguridad:**
- `scale_factor ∈ [0.2, 5.0]` — evita amplificación/compresión extrema de varianza
- `corr_train > 0.5` — BC solo cuando la ODE tiene señal útil
- Caso 28 protegido: scale_factor=5.4 → bias_only preservó EDI=+0.190

---

## 8. EVALUACIÓN BINARIA (PASS/FAIL) INADECUADA — ✅ RESUELTO (commit 54234d6)

> **Estado:** Implementada taxonomía de emergencia diferenciada con 6 categorías en `hybrid_validator.py`. Reemplaza la evaluación binaria `overall_pass` como único indicador.

**Archivo:** `repos/Simulaciones/common/hybrid_validator.py`, líneas ~1053-1079

**Problema:** Con `overall_pass = 0/29`, la evaluación binaria destruye toda la información. Casos con EDI=0.439 (microplásticos) y EDI=0.026 (finanzas, significativo) se clasifican igual que EDI=-545 (Starlink). La tesis pierde matiz explicativo.

**Corrección — Taxonomía de 6 categorías:**

| Categoría | Criterios | Resultado actual (real, commit 3d0a9d1) |
|-----------|-----------|-----------------|
| **strong** | EDI ∈ [0.325, 0.90] + sig + no falsación | 2 casos (16, 24) — Caso 16: **overall_pass=True** (commit c0bf312) |
| **weak** | EDI ∈ [0.10, 0.325) + sig | 1 caso (28) |
| **suggestive** | EDI > 0 + sig | 4 casos (09, 14, 17, 29) |
| **trend** | EDI > 0 + no sig | 6 casos (01, 11, 13, 18, 21, 27) |
| **null** | Todo lo demás | 13 casos |
| **falsification** | Controles de falsación | 3 casos (06, 07, 08) |

**Impacto en la tesis:** La narrativa pasa de "0/29 → H1 rechazada" a "**1/29 overall_pass + espectro de emergencia metaestable**: 2 strong + 1 weak + 4 suggestive + 6 trend".
