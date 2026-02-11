"""
ode.py — 05_caso_epidemiologia

Modelo: Acumulación-Disipación de Incidencia Epidémica (escala semanal)

Ecuación:
    dI/dt = α · F(t) − β · I + ε(t)

donde:
    I       : log-incidencia (log(nuevos_casos + 1), Z-scored)
    F(t)    : forcing combinado (log_deaths + vaccinated, OLS-ponderado)
    α       : sensibilidad a drivers (mortalidad/variante + intervención)
    β       : tasa de decaimiento natural de olas epidémicas
    ε(t)    : shocks estocásticos (nuevas variantes, super-spreaders)

Justificación:
    La log-incidencia de COVID-19 sigue dinámicas de olas con
    acumulación rápida (exponencial → log-lineal) y decaimiento
    natural por depleción de susceptibles e inmunidad poblacional.
    El forcing captura:
    - Mortalidad (proxy de severidad de variante + presión selectiva)
    - Vacunación (intervención externa que modula susceptibilidad)
    β captura la tendencia natural de las olas a decaer (τ ~ 5-10 sem).

Punto de equilibrio:
    I* = α·F / β

Referencias:
    - Cori, A. et al. (2013). A New Framework for Estimating
      Time-Varying Reproduction Numbers. Am. J. Epidemiol., 178(9).
    - Mathieu, E. et al. (2021). COVID-19 vaccinations. Nat. Hum. Behav.
    - Kermack, W. O. & McKendrick, A. G. (1927). A Contribution to the
      Mathematical Theory of Epidemics. Proc. R. Soc. A, 115(772).
"""

import numpy as np


def simulate_ode(params, steps, seed=42):
    """
    Modelo de acumulación-disipación de log-incidencia epidémica.
    dI/dt = α·F(t) − β·I + ε(t)
    """
    rng = np.random.RandomState(seed)

    # α = 0.30: sensibilidad a forcing.
    #   Un incremento de 1σ en drivers eleva log-incidencia
    #   con τ_acum ~ 3 semanas.
    alpha = float(params.get("ode_alpha", 0.30))

    # β = 0.15: decaimiento natural de olas epidémicas.
    #   τ_decay = 1/β ≈ 7 semanas. Las olas COVID duran ~6-12 semanas
    #   (Alpha ~8 sem, Delta ~10 sem, Omicron ~6 sem).
    beta = float(params.get("ode_beta", 0.15))

    noise_sigma = float(params.get("ode_noise", 0.02))

    I = float(params.get("p0", 0.0))

    forcing = params.get("forcing_series") or [0.0] * steps
    forcing_scale = float(params.get("forcing_scale", 1.0))

    series_I = []

    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.0
        dI = alpha * (forcing_scale * f_t) - beta * I
        dI += rng.normal(0.0, noise_sigma)
        I += dI
        series_I.append(I)

    return {"incidence": series_I, "forcing": forcing}
