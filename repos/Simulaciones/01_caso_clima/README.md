# Caso 01 — Clima Regional (CONUS)

## Resumen

Modelado del **clima regional** como hiperobjeto mediante un modelo híbrido ABM+ODE basado en el **Balance Energético de Budyko-Sellers** linealizado. El observable es la temperatura media mensual de la región CONUS (Continental US) con drivers exógenos reales: CO₂ (Mauna Loa), TSI (irradiancia solar), OHC (contenido calórico oceánico) y AOD (profundidad óptica de aerosoles).

**Dominio**: Ciencias climáticas  
**Nivel de Evidencia (LoE)**: 5 (máximo) — IPCC AR6, CMIP6 ensemble, datos instrumentales de alta calidad  

---

## Estructura de Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador: configura, ejecuta validación híbrida C1–C5, escribe outputs |
| `ode.py` | Capa macro: Balance Energético linealizado (Budyko-Sellers) |
| `abm.py` | Capa micro legacy (NO USADA — se usa `common/abm_numpy.py`) |
| `metrics.py` | Métricas legacy (NO USADAS — se usa `common/hybrid_validator.py`) |
| `data.py` | Obtención de datos: Meteostat (temperatura), NOAA (CO₂), TSI, OHC, AOD |

> **Nota**: `validate.py` importa `make_abm_adapter` de `common/abm_numpy.py` (ABM vectorizado genérico) y el ODE local de `ode.py`. El `abm.py` local es código de referencia con el modelo CESM-inspired completo pero no se ejecuta en el pipeline de validación.

---

## Modelo Matemático

### ODE — Balance Energético Linealizado

Ecuación diferencial ordinaria que modela la evolución de anomalías de temperatura:

$$
\frac{dT'}{dt} = \alpha \cdot (F'(t) - \beta \cdot T') + \eta(t)
$$

Donde:
- $T'(t)$: anomalía de temperatura (Z-scored por `hybrid_validator`)
- $F'(t)$: forcing agregado (combinación lineal Z-scored de drivers)
- $\alpha$: tasa de respuesta térmica
- $\beta$: parámetro de retroalimentación climática
- $\eta(t) \sim \mathcal{N}(0, \sigma^2)$: ruido de proceso (variabilidad interna)

**Discretización** (Euler explícito, paso mensual):

$$
T'_{t+1} = T'_t + \alpha \cdot (F'_t - \beta \cdot T'_t) + \eta_t
$$

#### Derivación de Parámetros

El modelo es la linealización del balance energético completo:

$$
C \cdot \frac{dT}{dt} = F(t) - \lambda \cdot T
$$

Donde $C$ es la capacidad calórica efectiva y $\lambda$ el parámetro de feedback.

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| $\alpha$ | 0.006 | $\Delta t / C_{\text{eff}} = 2.63 \times 10^6 \, \text{s} \;/\; 4 \times 10^8 \, \text{J/(m²·K)} \approx 6.6 \times 10^{-3}$ |
| $\beta$ | 0.1 | $\lambda \cdot \Delta t / C_{\text{eff}}$ con amplificación por feedbacks rápidos (vapor de agua, albedo-hielo) en espacio Z-scored |
| $\sigma$ | 0.02 | Ruido de proceso ODE (variabilidad interna no resuelta) |

**Escala temporal de equilibrio**: $\tau = 1/(\alpha \cdot \beta) = 1/(0.006 \times 0.1) \approx 1667$ meses $\approx 139$ años (consistente con equilibrio profundo océano-atmósfera).

**Constantes físicas utilizadas**:

| Constante | Valor | Referencia |
|-----------|-------|------------|
| $C_{\text{eff}}$ | $4 \times 10^8$ J/(m²·K) | Held & Soden (2006), IPCC AR5 WG1 Ch8 |
| $\sigma_{\text{SB}}$ | $5.67 \times 10^{-8}$ W/(m²·K⁴) | CODATA 2018 |
| $S_0$ (constante solar) | 1361 W/m² | IAU 2015 nominal |
| CO₂ pre-industrial | 280 ppm | IPCC AR6 WG1 Table 2.2 |
| $\Delta F_{2\times\text{CO}_2}$ | $5.35 \cdot \ln(2)$ W/m² | Myhre et al. (1998) |
| Albedo planetario | 0.3 | Stephens et al. (2015) |
| Emisividad efectiva $\epsilon$ | 0.61 | De $\epsilon \sigma T^4 = S(1-\alpha)/4$ a $T=288$ K |

**Referencias del modelo**:
- Budyko, M. I. (1969). "The effect of solar radiation variations on the climate of the Earth". *Tellus*, 21(5).
- Sellers, W. D. (1969). "A Global Climatic Model Based on the Energy Balance of the Earth-Atmosphere System". *J. Appl. Meteorol.*, 8(3).
- North, G. R., Cahalan, R. F., & Coakley, J. A. (1981). "Energy balance climate models". *Rev. Geophys.*, 19(1).

### ABM — Difusión Espacial Vectorizada

Se usa el motor genérico `common/abm_numpy.py` con la siguiente regla de actualización:

$$
G_{t+1} = G_t + d \cdot (\bar{N}_t - G_t) + f_s \cdot F_t + m_c \cdot (\bar{G}_t - G_t) - \delta \cdot G_t + \eta_t
$$

Donde:
- $G_t \in \mathbb{R}^{n \times n}$: grilla de temperatura ($n = 20$, 400 celdas)
- $\bar{N}_t$: promedio de vecinos 4-conectados (difusión)
- $d = 0.2$: coeficiente de difusión (calibrado por grid search)
- $f_s$: escala de forcing (calibrado)
- $F_t$: forcing exógeno en paso $t$
- $m_c$: acoplamiento macro (calibrado)
- $\bar{G}_t$: media global de la grilla (campo medio)
- $\delta$: amortiguamiento (calibrado)
- $\eta_t \sim U(-a, a)$: ruido uniforme acotado

**Acoplamiento descendente (ODE→ABM)**:

Cuando el ODE macro está acoplado, se aplica nudging:

$$
G_t \leftarrow G_t + m_c \cdot (T'_{\text{ODE},t} - \bar{G}_t)
$$

Esto implementa la "descendencia causal" del hiperobjeto: la estructura macro (ODE) constriñe la dinámica micro (ABM).

**Topología**: Red de mundo pequeño Watts-Strogatz (k=4, p=0.1) sobre la grilla, lo que permite conexiones de largo alcance con baja probabilidad de reconexión.

### Calibración

| Parámetro | Método | Rango |
|-----------|--------|-------|
| $f_s$ (forcing_scale) | Grid search + refinamiento | [0.001, 0.01, 0.05, 0.1, 0.5, 1.0] |
| $m_c$ (macro_coupling) | Grid search + refinamiento | [0.1, 0.3, 0.5, 0.7, 0.9] |
| $\delta$ (damping) | Grid search + refinamiento | [0.0, 0.2, 0.5, 0.8] |
| $\alpha, \beta$ (ODE) | Fijados por física | `ode_calibration=False` |

La función objetivo del grid search es RMSE penalizado por correlación:

$$
\text{score} = \text{RMSE} \times \max(0.5, \; 2 - r)
$$

donde $r$ es la correlación de Pearson entre predicción y observación en el periodo de entrenamiento.

---

## Datos

### Observable
- **Fuente**: Meteostat API — Temperatura media mensual (`tavg`)
- **Región**: CONUS (24°N–49.5°N, 125°W–66.5°W)
- **Método**: Promedio de las 10 estaciones con mayor cobertura (>85%)
- **Periodo**: 1990-01-01 a 2024-12-31
- **Split**: Entrenamiento 1990–2010, Validación 2011–2024

### Drivers Exógenos
| Driver | Fuente | Unidad | Rol Físico |
|--------|--------|--------|------------|
| CO₂ | NOAA Mauna Loa (`co2_mm_mlo.txt`) | ppm | Forzamiento radiativo de gases de efecto invernadero |
| TSI | SORCE/TSIS (vía fetcher) | W/m² | Variabilidad de irradiancia solar |
| OHC | WMO (vía fetcher) | J | Contenido calórico oceánico (inercia térmica) |
| AOD | GISS (vía fetcher) | adim | Profundidad óptica de aerosoles (efecto enfriamiento) |

El `hybrid_validator` construye el forcing como regresión multivariada Z-scored:

$$
F'_t = \mathbf{w}^T \cdot \mathbf{z}_t, \quad \mathbf{w} = (X_{\text{train}}^T X_{\text{train}} + \lambda I)^{-1} X_{\text{train}}^T \mathbf{y}_{\text{train}}
$$

con regularización ridge $\lambda = 10^{-3}$.

---

## Sintético (Ground Truth)

Datos generados por el ODE con parámetros conocidos:

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\alpha_{\text{true}}$ | 0.08 | Respuesta rápida ($\tau \approx 12$ meses) para test de recuperabilidad |
| $\beta_{\text{true}}$ | 0.03 | Feedback moderado |
| $\sigma_{\text{noise}}$ | 0.02 | Ruido de proceso |
| Forcing | $0.01 \cdot t$ | Lineal: 0→2.4 en 240 meses ($\approx 65\%$ de $\Delta F_{2\times\text{CO}_2}$) |
| Ruido medición | $\sigma = 0.05$ | Típico para estaciones meteorológicas |
| Periodo | 2000–2019 | 240 meses |
| Split | 2010 | 120 train / 120 val |

---

## Parámetros y Justificaciones

### Configuración del Validador

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `grid_size` | 20 | 400 celdas — balance computación/resolución espacial |
| `persistence_window` | 12 | 12 meses = 1 año climatológico |
| `corr_threshold` | 0.70 | Correlación fuerte esperada (drivers conocidos del clima) |
| `feedback_strength` | 0.05 | 5% de retroalimentación micro→macro (albedo-hielo → forcing) |
| `ode_calibration` | False | α, β fijados por derivación física (no calibrados) |
| `loe` | 5 | Máximo: IPCC AR6, CMIP6, datos instrumentales |
| Topología | Small-world (k=4, p=0.1) | Watts & Strogatz (1998); conexiones de largo alcance atmosféricas |

### Ruido

| Componente | Distribución | Amplitud | Justificación |
|------------|-------------|----------|---------------|
| ODE η(t) | $\mathcal{N}(0, 0.02^2)$ | σ = 0.02 | CLT: variabilidad interna agregada de muchos procesos sub-grid |
| ABM η(t) | $U(-a, a)$ | a = `base_noise` (calibrado) | Acotado para estabilidad numérica |
| Sintético (medición) | $\mathcal{N}(0, 0.05^2)$ | σ = 0.05 | Error típico de estación meteorológica |

---

## Ejecución

```bash
cd repos/Simulaciones/01_caso_clima/src
python3 validate.py
```

**Outputs**:
- `outputs/metrics.json`: Métricas completas (EDI, C1–C5, Symploké, etc.)
- `outputs/report.md`: Reporte narrativo

---

## Resultados Típicos

| Fase | EDI | C1 | C2 | C3 | C4 | C5 | Overall |
|------|-----|----|----|----|----|----|---------|
| Sintético | ~-0.60 | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ |
| Real | ~-0.30 | ❌ | ❌ | ✅ | ✅ | ❌ | ❌ |

**Interpretación**: El EDI negativo indica que el ABM sin ODE trackea mejor que el acoplado. Esto es consistente con la alta inercia climática (τ ≈ 139 años) — en una ventana de 14 años, la estructura macro del ODE no aporta información predictiva adicional significativa sobre la tendencia que el ABM puro ya captura mediante el forcing directo. El caso documenta correctamente los límites del framework cuando la escala temporal del hiperobjeto excede la ventana observacional.

---

## Auditoría de Números

### Valores Corregidos
1. **Ruido ODE**: Cambiado de `random.uniform(-a, a)` a `np.random.normal(0, σ)` — el Teorema Central del Límite justifica distribución gaussiana para fluctuaciones térmicas agregadas.
2. **`humidity_coupling = 0.01`**: Eliminado — parámetro muerto (nunca utilizado en el pipeline).
3. **Comentario "~5 years"**: Corregido a "~14 años" (1/α = 167 meses) y "~139 años" (τ = 1/(α·β) = 1667 meses).

### Valores Verificados (sin cambio necesario)
- Todas las constantes físicas coinciden con fuentes estándar (IPCC, CODATA, IAU).
- Los parámetros calibrados (fs, mc, damping) no son números mágicos — son resultado del grid search.
- α=0.006 y β=0.1 tienen derivación física documentada.
