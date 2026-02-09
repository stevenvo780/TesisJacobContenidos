import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from ode_models import simulate_ode_model

ODE_MODEL = "logistic_forced"
ODE_KEY = "c"


def simulate_ode(params, steps, seed):
    """
    Modelo de Atención-Decaimiento (Attention-Decay).

    Ecuación:
        dA/dt = α · F(t) · (1 − A) − β · A

    donde:
        A ∈ [0,1]  : nivel de atención colectiva normalizado
        F(t) ≥ 0   : forzamiento externo (volatilidad mediática Z-scored + baseline)
        α           : tasa de sensibilidad (velocidad de respuesta)
        β           : tasa de decaimiento (fatiga atencional)

    Justificación del modelo:
        La ecuación es una ODE logística forzada con saturación. El término
        α·F·(1−A) captura la respuesta sigmoidal a estímulos (Kahneman 1973,
        "Attention and Effort"), mientras que β·A modela el decaimiento
        exponencial de la atención colectiva (Candia et al. 2019,
        Nature Human Behaviour 3:1006).

    Punto de equilibrio:
        A* = α·F / (α·F + β)
        Con F=0.5 (baseline): A* = 0.5·0.5 / (0.5·0.5 + 0.8) ≈ 0.24

    Referencias:
        - Kahneman (1973), "Attention and Effort"
        - Wu & Huberman (2007), PNAS 104(45):17599 — atención colectiva en web
        - Candia et al. (2019), Nat. Hum. Behav. 3:1006 — decaimiento biexponencial
    """
    rng = np.random.RandomState(seed)

    # ── Parámetros ──────────────────────────────────────────────────────
    # α = 0.5 mes⁻¹ → τ_rise = 1/α = 2 meses.
    #   Wu & Huberman (2007) miden picos de atención web en 1-3 meses.
    alpha = float(params.get("ode_alpha", 0.5))

    # β = 0.8 mes⁻¹ → τ_decay = 1/β ≈ 1.25 meses.
    #   Candia et al. (2019) reportan half-life de atención colectiva ~1 mes.
    beta = float(params.get("ode_beta", 0.8))

    # σ_noise = 0.05 → fluctuaciones ≈ 5% del rango [0,1].
    #   Gaussiana por CLT: suma de múltiples perturbaciones estocásticas
    #   independientes (cambios de agenda, eventos menores).
    noise_sigma = float(params.get("ode_noise", 0.05))

    # ── Estado inicial ──────────────────────────────────────────────────
    # A₀ = 0.1 → atención basal baja (~10% de capacidad).
    A = float(params.get("c0", 0.1))

    # ── Forzamiento ─────────────────────────────────────────────────────
    # forcing_series viene Z-scored del validator (media≈0, std≈1).
    # Se modula alrededor de un baseline F₀ = 0.5 (punto medio de [0,1]).
    forcing = params.get("forcing_series") or [0.0] * steps
    forcing_scale = params.get("forcing_scale", 0.05)

    series = []

    for t in range(steps):
        f_t = forcing[t]
        # F(t) = max(0, 0.5 + fs·z_t), donde z_t es Z-score del driver.
        # Baseline 0.5 garantiza estimulación basal incluso sin noticias.
        F = max(0.0, 0.5 + forcing_scale * f_t)

        # dA = α·F·(1−A) − β·A
        dA = alpha * F * (1.0 - A) - beta * A
        A += dA

        # Ruido estocástico (Gaussiano, CLT)
        A += rng.normal(0.0, noise_sigma)

        # Clamping a [0, 1] (atención normalizada)
        A = max(0.0, min(1.0, A))

        series.append(A)

    return {ODE_KEY: series, "forcing": forcing}
