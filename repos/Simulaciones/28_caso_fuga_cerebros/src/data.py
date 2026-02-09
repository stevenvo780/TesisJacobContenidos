"""
data.py — 28_caso_fuga_cerebros (Top-Tier)

Hiperobjeto: Fuga de Cerebros Global (Brain Drain)

Fuentes de datos reales (World Bank + UNESCO):
1. GB.XPD.RSDV.GD.ZS — Gasto en I+D (% del PIB) — Variable objetivo
2. SP.POP.SCIE.RD.P6 — Investigadores en I+D por millón
3. SE.TER.ENRR — Matrícula terciaria bruta (%)
4. BX.TRF.PWKR.DT.GD.ZS — Remesas recibidas (% del PIB)
5. NY.GDP.PCAP.KD — PIB per cápita
6. SM.POP.NETM — Migración neta

Modelo teórico:
- Modelo gravitacional de Tinbergen (1962) para migración
- Docquier & Rapoport (2012): "Globalization, Brain Drain, and Development"
- Beine, Docquier & Rapoport (2001): "Brain drain and economic growth"
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from worldbank_universal_fetcher import fetch_worldbank_indicator


def _synthetic_fallback(start_date, end_date, seed=42):
    """Sintético con dinámica de brain drain realista."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)
    # Modelo: R&D sube lentamente, con drenaje por migración
    rd = 1.0
    values = []
    researchers = []
    enrollment = []
    for t in range(steps):
        # Tendencia creciente + shocks de fuga
        brain_drain = rng.exponential(0.02) if rng.random() < 0.15 else 0.0
        rd += 0.03 - brain_drain + rng.normal(0, 0.02)
        rd = np.clip(rd, 0.3, 5.0)
        values.append(rd)
        researchers.append(800 + 50 * t + rng.normal(0, 50))
        enrollment.append(20 + 1.5 * t + rng.normal(0, 2))
    df = pd.DataFrame({
        "date": dates, "value": values,
        "researchers": researchers, "enrollment": enrollment,
    })
    return df, {"source": "synthetic_brain_drain"}


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    start_date = start_date or "1980-01-01"
    end_date = end_date or "2023-12-31"
    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "28_caso_fuga_cerebros"}

    indicators = {
        "GB.XPD.RSDV.GD.ZS": "rd_gdp",
        "SP.POP.SCIE.RD.P6": "researchers",
        "SE.TER.ENRR": "enrollment",
        "BX.TRF.PWKR.DT.GD.ZS": "remittances",
        "NY.GDP.PCAP.KD": "gdp_pc",
        "SM.POP.NETM": "net_migration",
    }
    frames = {}
    errors = []
    for ind, col in indicators.items():
        try:
            df_i, err = fetch_worldbank_indicator(ind, country="WLD")
            if df_i is not None and not df_i.empty:
                df_i = df_i.rename(columns={"value": col})
                df_i["date"] = pd.to_datetime(df_i["date"])
                frames[col] = df_i[["date", col]].dropna()
            else:
                errors.append(f"{ind}: {err}")
        except Exception as e:
            errors.append(f"{ind}: {e}")

    if "rd_gdp" not in frames:
        return _synthetic_fallback(start_date, end_date)

    df = frames["rd_gdp"].rename(columns={"rd_gdp": "value"})
    for col, frame in frames.items():
        if col == "rd_gdp":
            continue
        df = df.merge(frame, on="date", how="outer")
    df = df.sort_values("date")
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    for col in ["researchers", "enrollment", "remittances", "gdp_pc", "net_migration"]:
        if col in df.columns:
            df[col] = df[col].interpolate(method="linear", limit_direction="both")
    df = df.dropna(subset=["value"])
    if len(df) < 10:
        return _synthetic_fallback(start_date, end_date)
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df, {"source": "WorldBank_multi", "obs_count": len(df),
                "obs_mean": float(df["value"].mean()), "errors": errors or None}
