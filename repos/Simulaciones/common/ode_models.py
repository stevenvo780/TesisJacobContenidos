"""
ode_models.py — ODEs domain-specific (CPU) con selección por modelo.
"""

from __future__ import annotations

import math
import random


def _apply_assimilation(value, t, params):
    series = params.get("assimilation_series")
    strength = params.get("assimilation_strength", 0.0)
    if series is None or t >= len(series):
        return value
    target = series[t]
    if target is None:
        return value
    return value + strength * (target - value)


def simulate_ode_model(params: dict, steps: int, seed: int = 3):
    random.seed(seed)
    model = params.get("ode_model", "mean_reversion")
    forcing = params.get("forcing_series") or [0.0] * steps
    noise = float(params.get("ode_noise", 0.01))
    ode_key = params.get("ode_key") or params.get("series_key") or "p"

    # Common params
    alpha = float(params.get("ode_alpha", 0.05))
    beta = float(params.get("ode_beta", 0.02))

    # Fix C13: Coupling bidireccional ABM→ODE
    # abm_feedback_series: serie temporal del ABM mean field
    # abm_feedback_gamma: fuerza del feedback micro→macro
    abm_fb = params.get("abm_feedback_series")
    abm_gamma = float(params.get("abm_feedback_gamma", 0.0))

    if model == "seir":
        beta_seir = float(params.get("beta", 0.3))
        sigma = float(params.get("sigma", 0.2))
        gamma = float(params.get("gamma", 0.1))

        s = float(params.get("s0", 0.999))
        e = float(params.get("e0", 0.001))
        i = float(params.get("i0", 0.0))
        r = float(params.get("r0", 0.0))

        series = []
        for t in range(steps):
            f = forcing[t]
            beta_t = max(0.0, beta_seir + f)
            new_e = beta_t * s * i
            new_i = sigma * e
            new_r = gamma * i

            s = max(0.0, s - new_e)
            e = max(0.0, e + new_e - new_i)
            i = max(0.0, i + new_i - new_r)
            r = max(0.0, r + new_r)

            inc = new_i + random.uniform(-noise, noise)
            inc = _apply_assimilation(inc, t, params)
            series.append(inc)

        return {ode_key: series, "forcing": forcing}

    if model == "radiative_balance":
        # Simplificado: T += alpha * (F - beta*T^4) + ruido
        t_state = float(params.get("t0", 0.0))
        series = []
        for t in range(steps):
            f = forcing[t]
            t_clamped = max(-5.0, min(5.0, t_state))
            dx = alpha * (f - beta * (t_clamped ** 4))
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - t_state)
            t_state = t_state + dx + random.uniform(-noise, noise)
            if not math.isfinite(t_state):
                t_state = 0.0
            t_state = _apply_assimilation(t_state, t, params)
            series.append(t_state)
        return {ode_key: series, "forcing": forcing}

    if model == "heston":
        # Simplificación determinista de Heston (volatilidad estocástica)
        mu = float(params.get("ode_mu", alpha))
        kappa = float(params.get("ode_kappa", beta))
        theta = float(params.get("ode_theta", 0.1))
        xi = float(params.get("ode_xi", 0.1))

        p = float(params.get("p0", 0.0))
        v = float(params.get("v0", 0.1))
        series = []
        for t in range(steps):
            f = forcing[t]
            v = max(1e-6, v + kappa * (theta - v) + xi * math.sqrt(v) * random.uniform(-noise, noise))
            p = p + mu * p + math.sqrt(v) * random.uniform(-noise, noise) + f * 0.1
            p = _apply_assimilation(p, t, params)
            series.append(p)
        return {ode_key: series, "forcing": forcing}

    if model == "accumulation_decay":
        # dX = inflow*F - decay*X
        x = float(params.get("p0", 0.0))
        inflow = float(params.get("ode_inflow", alpha))
        decay = float(params.get("ode_decay", beta))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = inflow * f - decay * x
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "logistic_forced":
        # dX = r*X*(1-X/K) + gamma*F - delta*X
        x = float(params.get("p0", 0.1))
        r = float(params.get("ode_r", alpha))
        delta = float(params.get("ode_delta", beta))
        k = float(params.get("ode_k", 1.0))
        gamma = float(params.get("ode_gamma", 0.1))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = r * x * (1.0 - x / max(1e-6, k)) + gamma * f - delta * x
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "ocean_thermal":
        # Relajación térmica con inercia
        x = float(params.get("p0", 0.0))
        c = float(params.get("ode_c", 5.0))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = (alpha * (f - x)) / max(1e-6, c)
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "acidification":
        # pH disminuye con forcing (CO2), con recuperación lenta
        x = float(params.get("p0", 0.0))
        gamma = float(params.get("ode_gamma", 0.1))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = alpha * (0.0 - x) - gamma * f
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "aquifer_balance":
        # Balance hídrico simple
        x = float(params.get("p0", 0.0))
        recharge = float(params.get("ode_recharge", alpha))
        extraction = float(params.get("ode_extraction", beta))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = recharge * f - extraction * x
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "bilinear":
        # dX = α*(F - β*X) + γ*F*X
        # Retroalimentación no-lineal: estado amplifica forzamiento.
        # Dominios: fósforo (eutrofización), salinización (evaporación),
        #   riesgo biológico (bio-amplificación), IoT (efecto red).
        x = float(params.get("p0", 0.0))
        gamma = float(params.get("ode_gamma", 0.02))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = alpha * (f - beta * x) + gamma * f * x
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = max(-10.0, min(x, 10.0))
            if not math.isfinite(x):
                x = 0.0
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "prestige_competition":
        # dX = α*(F - β*X) + prestige*max(F,0)*(1 + c*|X|)
        # Competición asimétrica: prestigio amplifica forzamiento positivo.
        # Dominio: erosión lingüística (Abrams-Strogatz 2003).
        x = float(params.get("p0", 0.0))
        prestige = float(params.get("ode_prestige", 0.008))
        amplif = float(params.get("ode_amplification", 0.3))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = alpha * (f - beta * x) + prestige * max(0.0, f) * (1.0 + amplif * abs(x))
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = max(-10.0, min(x, 10.0))
            if not math.isfinite(x):
                x = 0.0
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "saturation_growth":
        # dX = α*(F - β*X) - saturation*X*|X|
        # Crecimiento con freno cuadrático (saturación orbital).
        # Dominio: mega-constelaciones (Kessler), capacidad de carga.
        x = float(params.get("p0", 0.0))
        saturation = float(params.get("ode_saturation", 0.002))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = alpha * (f - beta * x) - saturation * x * abs(x)
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = max(-10.0, min(x, 10.0))
            if not math.isfinite(x):
                x = 0.0
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "institutional_inertia":
        # dE = α*(E_target - E) + β*F - γ*E²
        # Dinámica institucional con rendimientos decrecientes.
        # Dominio: efectividad de políticas públicas (North 1990,
        # Acemoglu et al. 2001, Rodrik 2007).
        # E_target = target_base + target_slope * F(t)
        x = float(params.get("p0", 0.1))
        gamma = float(params.get("ode_gamma", 0.1))
        target_base = float(params.get("ode_target_base", 0.3))
        target_slope = float(params.get("ode_target_slope", 0.5))
        dt = float(params.get("ode_dt", 1.0))
        x_min = float(params.get("ode_clip_min", 0.0))
        x_max = float(params.get("ode_clip_max", 2.0))
        series = []
        for t in range(steps):
            f = forcing[t]
            e_target = target_base + target_slope * f
            dx = alpha * (e_target - x) + beta * f - gamma * x ** 2
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx * dt + random.uniform(-noise, noise)
            x = max(x_min, min(x, x_max))
            if not math.isfinite(x):
                x = 0.0
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "sis_contagion":
        # dI = β*I*(1-I) - γ*I + δ*F
        # Contagio SIS (Susceptible-Infected-Susceptible) con forcing.
        # Dominio: desinformación (Vosoughi et al. 2018),
        # memes culturales, difusión de innovación.
        x = float(params.get("p0", 0.05))
        gamma = float(params.get("ode_gamma", 0.15))
        delta = float(params.get("ode_delta", 0.2))
        dt = float(params.get("ode_dt", 0.5))
        x_min = float(params.get("ode_clip_min", 0.01))
        x_max = float(params.get("ode_clip_max", 0.99))
        series = []
        for t in range(steps):
            f = forcing[t]
            dx = beta * x * (1.0 - x) - gamma * x + delta * f
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx * dt + random.uniform(-noise, noise)
            x = max(x_min, min(x, x_max))
            if not math.isfinite(x):
                x = 0.05
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "aquifer_darcy":
        # dH = α*(F - β*H) - extraction*H/(|H|+1)
        # Balance hídrico Darcy-Theis con extracción antrópica.
        # La extracción tiene saturación logística: a mayor H,
        # más se extrae, pero con límite físico.
        # Ref: Theis (1935), De Marsily (2004), Konikow & Kendy (2005).
        x = float(params.get("p0", 0.0))
        extraction = float(params.get("ode_extraction", 0.01))
        series = []
        for t in range(steps):
            f = forcing[t]
            core = alpha * (f - beta * x)
            pump = extraction * x / (abs(x) + 1.0)
            dx = core - pump
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = max(-10.0, min(x, 10.0))
            if not math.isfinite(x):
                x = 0.0
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "brain_drain":
        # dH = α*(F - β*H) + γ*F - δ*max(0, H-threshold)^1.5
        # Capital humano con fuga de cerebros.
        # El drain se activa sobre un umbral (brain drain paradox:
        # más capital → más emigración). Docquier & Rapoport (2012).
        x = float(params.get("p0", 1.5))
        gamma = float(params.get("ode_gamma_forcing", 0.08))
        delta = float(params.get("ode_delta_drain", 0.015))
        drain_thr = float(params.get("ode_drain_threshold", 1.5))
        x_min = float(params.get("ode_clip_min", 0.1))
        x_max = float(params.get("ode_clip_max", 8.0))
        series = []
        for t in range(steps):
            f = forcing[t]
            accum = alpha * (f - beta * x)
            drain = delta * max(0.0, x - drain_thr) ** 1.5
            ext = gamma * f
            dx = accum + ext - drain
            if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
                dx += abm_gamma * (abm_fb[t] - x)
            x = x + dx + random.uniform(-noise, noise)
            x = max(x_min, min(x, x_max))
            if not math.isfinite(x):
                x = 1.5
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "random_walk":
        x = float(params.get("p0", 0.0))
        drift = float(params.get("ode_drift", 0.0))
        series = []
        for t in range(steps):
            x = x + drift + random.uniform(-noise, noise)
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    if model == "constant":
        x = float(params.get("p0", 0.0))
        series = []
        for t in range(steps):
            x = x + random.uniform(-noise, noise)
            x = _apply_assimilation(x, t, params)
            series.append(x)
        return {ode_key: series, "forcing": forcing}

    # Default: mean reversion (legacy) + bidirectional feedback
    x = float(params.get("p0", 0.0))
    series = []
    for t in range(steps):
        f = forcing[t]
        # ODE base: dX = α*(F - β*X)
        dx = alpha * (f - beta * x)
        # Fix C13: Feedback bidireccional ABM→ODE
        # Si hay serie ABM disponible, nudging hacia el campo medio micro
        if abm_fb is not None and t < len(abm_fb) and abm_gamma > 1e-8:
            dx += abm_gamma * (abm_fb[t] - x)
        x = x + dx + random.uniform(-noise, noise)
        x = _apply_assimilation(x, t, params)
        series.append(x)
    return {ode_key: series, "forcing": forcing}
