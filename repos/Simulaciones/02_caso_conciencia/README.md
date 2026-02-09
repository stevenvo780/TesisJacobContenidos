# Caso 02 — Conciencia Colectiva

## Descripción

Modela la **conciencia colectiva** como un fenómeno emergente usando el
marco de la **Global Workspace Theory** (GWT, Baars 1988). La hipótesis
es que la atención social a temas de interés público (medida vía Google
Trends) exhibe dinámicas de ignición análogas a la conciencia neuronal.

**Dominio:** Cognitivo-social  
**Variable observable:** Volumen de búsquedas (Google Trends)  
**Driver:** Tasa de suicidio (World Bank) — proxy de malestar social  
**Resultado típico:** EDI_syn ≈ 0.11, EDI_real ≈ -0.06 (no validado)

---

## Modelo ODE — Atención-Decaimiento

### Ecuación

$$\frac{dA}{dt} = \alpha \cdot F(t) \cdot (1 - A) - \beta \cdot A$$

donde:
- $A \in [0, 1]$: nivel de atención colectiva normalizado
- $F(t) \geq 0$: forzamiento externo (volatilidad mediática)
- $\alpha$: tasa de sensibilidad (velocidad de respuesta)
- $\beta$: tasa de decaimiento (fatiga atencional)

### Punto de equilibrio

$$A^* = \frac{\alpha \cdot F}{\alpha \cdot F + \beta}$$

Con $F = 0.5$ (baseline): $A^* = \frac{0.5 \times 0.5}{0.5 \times 0.5 + 0.8} \approx 0.24$

### Forzamiento

$$F(t) = \max\left(0,\; 0.5 + f_s \cdot z_t\right)$$

donde $z_t$ es el Z-score del driver y $f_s$ es el forcing_scale calibrado.
El baseline 0.5 garantiza estimulación basal incluso sin noticias.

### Parámetros ODE

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| $\alpha$ | 0.5 mes⁻¹ | $\tau_{rise} = 1/\alpha = 2$ meses. Wu & Huberman (2007, PNAS 104:17599): picos de atención web en 1-3 meses |
| $\beta$ | 0.8 mes⁻¹ | $\tau_{decay} = 1/\beta \approx 1.25$ meses. Candia et al. (2019, Nat. Hum. Behav. 3:1006): half-life de atención ~1 mes |
| $\sigma_{noise}$ | 0.05 | ~5% del rango [0,1]. Gaussiano (CLT: suma de perturbaciones independientes) |
| $A_0$ | 0.1 | Atención basal ~10% de capacidad |
| $F_0$ | 0.5 | Punto medio del rango de forcing [0,1] |

### Ruido

Gaussiano $\mathcal{N}(0, \sigma)$ con $\sigma = 0.05$, justificado por el
Teorema Central del Límite (múltiples perturbaciones estocásticas independientes:
cambios de agenda mediática, eventos menores, variabilidad individual).

---

## Modelo ABM — Global Workspace Theory

### Arquitectura

16 módulos cognitivos en grid 4×4, cada uno representando una función
cognitiva (Visual, Auditory, Language, Memory, etc.). Los módulos compiten
por acceso al **espacio de trabajo global** (workspace) mediante un mecanismo
de **winner-take-all**.

### Ecuación de actualización

Para cada módulo $i$ en paso $t$:

$$a_i(t+1) = (1 - \delta) \cdot \left[a_i(t) + S_i(t)\right] - \lambda \cdot (a_i - \bar{a}) + B_i(t)$$

donde:
- $\delta$ = `decay_rate`: tasa de decaimiento (fatiga)
- $S_i(t)$ = `stimulus_response`: respuesta al estímulo externo
- $\lambda$ = `lateral_inhibition`: competencia lateral
- $\bar{a}$ = `mean(activations)`: activación media
- $B_i(t)$: boost de broadcast (solo si el módulo $i$ gana la ignición)

### Dinámica de ignición

Si $\max(a) > \theta_{ignition}$:
1. El módulo ganador recibe `broadcast_boost` (+30%)
2. Los demás son suprimidos (×0.7 = −30%)

Si $\max(a) \leq \theta_{ignition}$:
- Procesamiento inconsciente, workspace decae (×0.5)

### Variable de salida

$$C(t) = \max\left(W_{activation},\; \text{mean}(a_i)\right)$$

Combina ignición explícita con integración de fondo.

### Parámetros ABM

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| `n_modules` | 16 | Grid 4×4. Baars (1988) no fija número; 16 cubre las principales funciones cognitivas |
| `ignition_threshold` | 0.6 | 60% de activación máxima. Dehaene et al. (2006, Nature 440:752): umbral perceptual de ignición cortical ~60% |
| `decay_rate` | 0.2 | $\tau = 1/\delta = 5$ meses. Memoria de trabajo social decae en escala de meses |
| `lateral_inhibition` | 0.1 | Rango estándar en redes neuronales: 0.05–0.2 (Grossberg 1988) |
| `broadcast_boost` | 0.3 | +30% al ganador, simétrico con supresión -30% |
| Supresión perdedores | ×0.7 | -30%, complementario al boost |
| Factor macro coupling | 0.5 | Escala moderada de acoplamiento ODE→ABM. Clamp ∈ [0.8, 1.2] para estabilidad |

---

## Acoplamiento macro ↔ micro

| Dirección | Mecanismo |
|-----------|-----------|
| ODE → ABM | `macro_target_series`: la atención macro modula las activaciones de los módulos. `scale = 1 + coupling·0.5·(target − workspace)`, clamped ∈ [0.8, 1.2] |
| ABM → ODE | Indirecto vía EDI: se evalúa si el acoplamiento macro reduce el error del ABM |

---

## Datos

### Variable principal
- **Fuente:** Google Trends (via `data_universal.fetch_case_data`)
- **Proxy:** Volumen de búsqueda como indicador de atención colectiva
- **Rango:** 2004-01 a 2023-12 (mensual)

### Driver
- **suicide_rate**: Tasa de suicidio por 100k habitantes (World Bank)
  - Justificación: Durkheim (1897, *Le Suicide*) establece la tasa de suicidio
    como indicador sociológico clásico de cohesión/anomia social
  - Resolución: anual, interpolado a mensual

### Split temporal
- Entrenamiento: 2004-01 a 2014-12 (~132 meses)
- Validación: 2015-01 a 2023-12 (~108 meses)

---

## Calibración

| Componente | Método |
|------------|--------|
| ODE (α, β) | **Fijos** — derivados de literatura (ver tabla ODE). `ode_calibration=False` |
| ABM (forcing_scale, macro_coupling, damping) | **Grid search** — vía `hybrid_validator.calibrate_abm()` |

---

## Métricas avanzadas (metrics.py)

| Métrica | Descripción | Implementación |
|---------|-------------|----------------|
| Shannon Entropy | $H(X) = -\sum p(x) \log_2 p(x)$ | Discretización por regla de Sturges: $n_{bins} = \lceil 1 + \log_2 N \rceil$ |
| LZC Proxy | Razón de compresión zlib como proxy de complejidad de Kolmogorov | `len(zlib.compress(bin)) / len(bin)` |
| Φ Proxy | Información integrada (Tononi 2004) | `corr(whole_{t}, whole_{t+1}) − mean(corr(part_{i,t}, part_{i,t+1}))` |

---

## Archivos del caso

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador: configura, ejecuta validación C1-C5, escribe outputs |
| `ode.py` | Modelo macro: Atención-Decaimiento (logística forzada) |
| `abm.py` | Modelo micro: Global Workspace Theory (16 módulos, ignición) |
| `data.py` | Carga datos reales (Google Trends) vía `data_universal` |
| `metrics.py` | Shannon entropy, LZC proxy, Φ proxy, correlación, RMSE |

---

## Resultados típicos

```
synthetic: EDI = 0.112, overall_pass = False
real:      EDI = -0.063, overall_pass = False
```

El caso NO valida la hipótesis de hiperobjeto (EDI < 0.30). El driver
(tasa de suicidio) tiene resolución temporal demasiado baja (anual) para
capturar la dinámica mensual de la atención colectiva.

---

## Auditoría (correcciones aplicadas)

1. **ODE noise**: `random.uniform` → `rng.normal` (Gaussiano, CLT). Seed explícito para reproducibilidad.
2. **grid_size**: Corregido de 20 → 4 para consistencia con ABM local (16 módulos = 4×4).
3. **Código muerto eliminado**: Bloque de "Advanced Metrics" en validate.py que ejecutaba ABM separadamente con funciones rotas.
4. **metrics.py — dominance_share**: Agregado `return max_share` faltante.
5. **metrics.py — lempel_ziv_complexity**: Eliminada función incompleta (siempre retornaba 0). Se conserva `lzc_proxy` (compresión zlib) que es funcional.
6. **metrics.py — shannon_entropy**: Eliminado código muerto (`math.histogram` no existe). Binning fijo 10 → regla de Sturges $\lceil 1 + \log_2 N \rceil$.
7. **Documentación**: Todos los parámetros ahora tienen derivación y referencia bibliográfica.

---

## Referencias

- Baars, B. J. (1988). *A Cognitive Theory of Consciousness*. Cambridge University Press.
- Candia, C. et al. (2019). The universal decay of collective memory and attention. *Nature Human Behaviour*, 3, 1006–1012.
- Dehaene, S. & Changeux, J.-P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.
- Dehaene, S. et al. (2006). Conscious, preconscious, and subliminal processing. *Nature*, 440, 752.
- Durkheim, É. (1897). *Le Suicide*. Félix Alcan.
- Grossberg, S. (1988). Nonlinear neural networks: Principles, mechanisms, and architectures. *Neural Networks*, 1(1), 17–61.
- Kahneman, D. (1973). *Attention and Effort*. Prentice-Hall.
- Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.
- Wu, F. & Huberman, B. A. (2007). Novelty and collective attention. *PNAS*, 104(45), 17599–17601.
