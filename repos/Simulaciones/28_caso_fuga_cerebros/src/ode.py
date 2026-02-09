"""
ode.py — 28_caso_fuga_cerebros (Top-Tier)

Modelo ODE: Dinámica de Capital Humano con Brain Drain

Ecuaciones (Docquier & Rapoport 2012, simplificado):
  dH/dt = α*(E - βH) + γ*F - δ*D(H) + noise

Donde:
  H(t)  = stock de capital humano (proxy: R&D % PIB)
  E     = formación (matrícula terciaria, inversión educativa)
  F     = forcing exógeno (PIB, remesas, inversión extranjera)
  D(H)  = función de drenaje: emigración aumenta con H (brain drain paradox)
  α     = tasa de acumulación
  β     = depreciación natural del capital humano
  γ     = sensibilidad a forcing exógeno
  δ     = intensidad del brain drain

El "brain drain paradox": países con más capital humano
pierden más por migración (incentivo prospect).
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))


def simulate_ode(params, steps, seed=42):
    rng = np.random.default_rng(seed)

    alpha = float(params.get("ode_alpha", 0.06))
    beta = float(params.get("ode_beta", 0.02))
    gamma = float(params.get("ode_gamma_forcing", 0.08))
    delta = float(params.get("ode_delta_drain", 0.015))
    drain_threshold = float(params.get("ode_drain_threshold", 1.5))
    noise_std = float(params.get("ode_noise", 0.01))

    forcing = params.get("forcing_series") or [0.0] * steps
    assim_series = params.get("assimilation_series")
    assim_strength = float(params.get("assimilation_strength", 0.0))

    H = float(params.get("p0", 1.5))
    series = []

    for t in range(steps):
        f = forcing[t] if t < len(forcing) else 0.0
        # Acumulación natural
        accum = alpha * (f - beta * H)
        # Brain drain: aumenta cuadráticamente cuando H > threshold
        drain = delta * max(0, H - drain_threshold) ** 1.5
        # Forcing exógeno
        ext = gamma * f
        dH = accum + ext - drain + rng.normal(0, noise_std)
        H += dH
        H = np.clip(H, 0.1, 8.0)

        if assim_series is not None and t < len(assim_series):
            target = assim_series[t]
            if target is not None:
                H = H + assim_strength * (float(target) - H)
        if not np.isfinite(H):
            H = 1.5
        series.append(float(H))

    return {"fc": series, "forcing": forcing}
