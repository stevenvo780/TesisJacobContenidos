# Caso 03 — Contaminación PM2.5

## Descripción

Modela la **contaminación atmosférica por PM2.5** como hiperobjeto
emergente. La concentración de partículas finas a escala global es
resultado de miles de fuentes industriales y vehiculares individuales
que, en conjunto, generan un campo de concentración con estructura
espacial propia.

**Dominio:** Ambiental / Calidad del aire  
**Variable observable:** PM2.5 media global (μg/m³)  
**Datos:** World Bank (EN.ATM.PM25.MC.M3), resolución anual  
**Resultado típico:** EDI_syn ≈ 0.00, EDI_real ≈ 0.00 (no validado)

---

## Modelo ODE — Acumulación-Disipación

### Ecuación

$$\frac{dC}{dt} = \alpha \cdot f_s \cdot z_t - \beta \cdot C + \varepsilon(t)$$

donde:
- $C$: concentración media de PM2.5 (Z-scored)
- $z_t$: Z-score del forzamiento externo
- $f_s$: forcing_scale (calibrado por grid search)
- $\alpha$: tasa de acumulación por emisiones
- $\beta$: tasa de remoción (deposición + dispersión + regulación)
- $\varepsilon(t) \sim \mathcal{N}(0, \sigma)$: ruido estocástico

### Punto de equilibrio

$$C^* = \frac{\alpha \cdot f_s \cdot \bar{z}}{\beta}$$

### Justificación del modelo

La ecuación es la reducción temporal del Box Model de EPA (Seinfeld &
Pandis 2016, cap. 25) promediada sobre un año. Las partículas individuales
de PM2.5 tienen $\tau_{residencia} \sim 1$ semana, pero la señal de
concentración regional persiste 3-7 años por inercia del sistema emisor
(IPCC AR6, cap. 6).

### Parámetros ODE

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| $\alpha$ | 0.8 año⁻¹ | $\tau_{acum} = 1/\alpha = 1.25$ años. Sensibilidad a cambios en emisiones industriales |
| $\beta$ | 0.2 año⁻¹ | $\tau_{removal} = 1/\beta = 5$ años. Inercia del sistema emisor (IPCC AR6 cap. 6) |
| $\sigma_{noise}$ | 0.05 | ~5% variación estocástica. Gaussiano (CLT: variabilidad meteorológica + fuentes menores) |
| $C_0$ | 0.0 | Condición inicial (ajustada por validator a primer valor observado) |

---

## Modelo ABM — Pluma Gaussiana (AERMOD)

### Ecuación de dispersión

Para cada fuente puntual, la concentración en $(x, y)$ es:

$$C(x,y) = \frac{Q}{2\pi u \sigma_y \sigma_z} \exp\left(-\frac{y^2}{2\sigma_y^2}\right) \cdot 2 \exp\left(-\frac{H^2}{2\sigma_z^2}\right)$$

El factor 2 proviene de la reflexión del suelo (imagen especular).

### Coeficientes de dispersión (Pasquill-Gifford, clase D)

$$\sigma_y(x) = a_y \cdot x \cdot (1 + b_y |x|)^{-0.5}$$
$$\sigma_z(x) = a_z \cdot x \cdot (1 + b_z |x|)^{-0.5}$$

### Parámetros ABM

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| `grid_size` | 20 | Grid 20×20 (2000×2000 m a 100 m/celda) |
| `n_sources` | 3 | Fuentes puntuales dominantes en región urbana tipo |
| $a_y$ | 0.08 | Pasquill-Gifford clase D, Turner (1970) |
| $a_z$ | 0.06 | Pasquill-Gifford clase D, Turner (1970) |
| $b_y$ | 0.0001 | Corrección a distancia, Turner (1970) |
| $b_z$ | 0.0015 | Corrección a distancia, Turner (1970) |
| `wind_speed` | 5.0 m/s | Media global de viento superficial ~3-5 m/s (NCEP) |
| `wind_dir` | 270° | Viento del oeste (convención geográfica) |
| `deposition` | 0.01 | 1% por paso. Remoción neta (deposición + regulación) |
| Factor de conversión | $10^{-6}$ | g/m³ → μg/m³ (normalización de unidades) |

### Dinámica temporal

En cada paso $t$:
1. Decaimiento: `concentration *= (1 - deposition)`
2. Emisión: suma de plumas gaussianas de todas las fuentes
3. Viento: variación sinusoidal + ruido Gaussiano
4. Acoplamiento macro: `scale = 1 + coupling·0.1·(target - mean)/mean`

---

## Datos

### Variable principal
- **Fuente:** World Bank, indicador `EN.ATM.PM25.MC.M3`
- **Variable:** Exposición media de población a PM2.5 (μg/m³)
- **Rango:** 1990-2022 (anual)

### Drivers
- Sin drivers externos. Forzamiento inferido desde tendencia temporal.

### Split temporal
- Entrenamiento: 1980-1999 (sintético), 1990-2009 (real)
- Validación: 2000-2019 (sintético), 2010-2022 (real)

---

## Calibración

| Componente | Método |
|------------|--------|
| ODE (α, β) | **Fijos** desde literatura. `ode_calibration=False` |
| ABM (forcing_scale, macro_coupling, damping) | **Grid search** vía `hybrid_validator.calibrate_abm()` |

---

## Métricas espaciales (metrics.py)

| Métrica | Descripción |
|---------|-------------|
| Moran's I | Autocorrelación espacial. +1=clusters, 0=aleatorio, -1=disperso. Contiguity: Queen |
| Gini | Desigualdad espacial. $G = \frac{2\sum (i+1)x_i}{n\sum x_i} - \frac{n+1}{n}$ |

---

## Archivos del caso

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador: configura, ejecuta C1-C5, escribe outputs |
| `ode.py` | Macro: modelo acumulación-disipación anual |
| `abm.py` | Micro: pluma gaussiana AERMOD vectorizada |
| `data.py` | Carga PM2.5 del World Bank API |
| `metrics.py` | Moran's I, Gini, correlación, RMSE, dominancia |

---

## Auditoría (correcciones aplicadas)

1. **ODE reescrita**: El modelo original (Box Model EPA) operaba en escala horaria
   (ciclo diurno, k en 1/h) pero los datos son anuales. Los parámetros
   `ode_alpha` y `ode_beta` del config eran DEAD PARAMETERS (la ODE no los leía).
   Se reescribió como modelo lineal forzado anual $dC = \alpha \cdot F - \beta \cdot C$
   que es consistente con el framework y la escala temporal.
2. **Números mágicos eliminados**: Los factores `100` y `500` en la ODE original
   no tenían justificación física y fueron eliminados con la reescritura.
3. **Ruido**: Gaussiano con seed explícito (`np.random.RandomState`).
4. **Código diagnóstico eliminado**: Bloque de Moran's I y Gini en validate.py
   que ejecutaba ABM separadamente.
5. **Impresión de EDI**: Agregada para consistencia con otros casos.

---

## Referencias

- Cimorelli, A. J. et al. (2005). AERMOD: A Dispersion Model for Industrial Source Applications. *J. Appl. Meteor.*, 44, 682–693.
- IPCC AR6 WGI (2021). Chapter 6: Short-lived climate forcers.
- Pasquill, F. (1961). The estimation of the dispersion of windborne material. *Meteor. Mag.*, 90, 33–49.
- Seinfeld, J. H. & Pandis, S. N. (2016). *Atmospheric Chemistry and Physics*, 3rd ed. Wiley.
- Turner, D. B. (1970). *Workbook of Atmospheric Dispersion Estimates*. EPA AP-26.
