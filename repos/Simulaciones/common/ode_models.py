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
            t_state = t_state + alpha * (f - beta * (t_state ** 4)) + random.uniform(-noise, noise)
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
            x = x + inflow * f - decay * x + random.uniform(-noise, noise)
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
            x = x + r * x * (1.0 - x / max(1e-6, k)) + gamma * f - delta * x + random.uniform(-noise, noise)
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
            x = x + (alpha * (f - x)) / max(1e-6, c) + random.uniform(-noise, noise)
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
            x = x + alpha * (0.0 - x) - gamma * f + random.uniform(-noise, noise)
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
            x = x + recharge * f - extraction * x + random.uniform(-noise, noise)
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

    # Default: mean reversion (legacy)
    x = float(params.get("p0", 0.0))
    series = []
    for t in range(steps):
        f = forcing[t]
        x = x + alpha * (f - beta * x) + random.uniform(-noise, noise)
        x = _apply_assimilation(x, t, params)
        series.append(x)
    return {ode_key: series, "forcing": forcing}

