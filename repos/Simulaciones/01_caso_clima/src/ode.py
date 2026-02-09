import math
import numpy as np

ODE_KEY = "tbar"

# ─── Constantes físicas del Balance Energético (Budyko-Sellers) ─────────
#
# C_eff: Capacidad calorífica efectiva atmósfera + capa de mezcla oceánica
#   Ref: Held & Soden (2006), J. Climate; IPCC AR5 WG1 Ch8 Box 8.1
#   Rango típico: 1e8–1e9 J/(m²·K); ~4e8 es estándar para escala mensual
C_EFF = 4.0e8  # [J / (m² · K)]

# Duración de un paso temporal (1 mes medio)
SECONDS_PER_MONTH = 30.44 * 24 * 3600  # ≈ 2.63e6 s

# Constante de Stefan-Boltzmann (CODATA 2018)
SIGMA = 5.67e-8  # [W / (m² · K⁴)]

# CO₂ pre-industrial (IPCC AR6 WG1 Table 2.2)
CO2_REF = 280.0  # [ppm]

# Sensibilidad radiativa al CO₂: ΔF = α·ln(CO₂/CO₂_ref)
#   Ref: Myhre et al. (1998), Geophys. Res. Lett.
ALPHA_CO2 = 5.35  # [W/m²]

def _apply_assimilation(value, t, params):
    series = params.get("assimilation_series")
    strength = params.get("assimilation_strength", 0.0)
    if series is None or t >= len(series):
        return value
    target = series[t]
    if target is None:
        return value
    return value + strength * (target - value)

def simulate_ode(params, steps, seed):
    """
    Modelo ODE de Balance Energético linealizado (Budyko-Sellers).
    
    Ecuación: dT'/dt = α·(F'(t) − β·T') + η(t)
    
    Donde:
      T' = anomalía de temperatura (espacio Z-scored)
      F' = forcing agregado (combinación lineal Z-scored de CO₂, TSI, OHC, AOD)
      α  = tasa de respuesta térmica ≈ Δt/C_eff
      β  = parámetro de retroalimentación ≈ λ·Δt/C_eff
      η  ~ N(0, σ²) = ruido de proceso (variabilidad interna)
    
    Refs:
      - Budyko (1969), Tellus
      - Sellers (1969), J. Appl. Meteorol.
      - North et al. (1981), Rev. Geophys.
    """
    rng = np.random.RandomState(seed)
    
    # Estado inicial (anomalía o temperatura absoluta según contexto)
    T = float(params.get("t0", 288.0))
    
    # Parámetros físicos
    # Albedo planetario medio: 0.29 ± 0.01 (Stephens et al. 2015, Nature Geosci.)
    albedo = float(params.get("ode_albedo", 0.3))
    # Emisividad efectiva: calibrada para T_eq ≈ 288 K
    #   De εσT⁴ = S(1−α)/4: ε = 1361·0.7/(4·5.67e-8·288⁴) ≈ 0.61
    epsilon = float(params.get("ode_emissivity", 0.61))
    # Amplitud de ruido estocástico (σ gaussiano)
    #   Justificación: CLT — fluctuaciones térmicas sub-grid son suma
    #   de muchos procesos independientes → distribución gaussiana
    noise_sigma = float(params.get("ode_noise", 0.1))
    
    # El forcing_series es construido por hybrid_validator como combinación
    # lineal Z-scored de los drivers exógenos (CO₂, TSI, OHC, AOD),
    # o como tendencia + lag si no hay drivers disponibles.
    
    # Balance energético linealizado: dT'/dt = α·(F'(t) − β·T')
    #
    # α ≈ Δt/C_eff ≈ 2.63e6 / 4e8 ≈ 6.6e-3 [adim en paso mensual]
    #   Controla la inercia térmica del sistema
    #   Escala temporal de respuesta: τ = 1/(α·β)
    #
    # β ≈ parámetro de retroalimentación climática (λ/C × Δt)
    #   λ_Planck ≈ 3.2 W/(m²·K) (IPCC AR6 Table 7.SM.5)
    #   λ_total ≈ 1.0–1.5 W/(m²·K) incluyendo feedbacks
    #   β = λ·Δt/C ≈ 1.2 × 2.63e6 / 4e8 ≈ 0.008
    #   Valores más altos (0.02–0.1) representan feedbacks adicionales
    #   o escalas temporales más rápidas en espacio Z-scored.
    alpha = float(params.get("ode_alpha", 0.05))
    beta = float(params.get("ode_beta", 0.02))
    
    series = []
    
    # Modelo en espacio de anomalías (Z-scored por hybrid_validator)
    x = float(params.get("p0", 0.0))
    forcing = params.get("forcing_series") or [0.0]*steps
    
    for t in range(steps):
        f = forcing[t] 
        
        # Balance energético linealizado de Budyko-Sellers:
        #   C·dT'/dt = F'(t) − λ·T'
        # En forma discreta adimensional: x' = x + α·(f − β·x) + η
        dx = alpha * (f - beta * x)
        x = x + dx + rng.normal(0.0, noise_sigma)
        
        x = _apply_assimilation(x, t, params)
        series.append(x)
        
    return {ODE_KEY: series, "forcing": forcing}
