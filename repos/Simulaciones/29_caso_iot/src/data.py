"""
data.py — 29_caso_iot (Top-Tier)

Ecosistema IoT Global: Difusión tecnológica masiva como hiperobjeto.

Fuentes de datos reales (multi-indicador World Bank):
1. IT.CEL.SETS.P2 — Suscripciones móviles por 100 hab (variable objetivo)
2. IT.NET.USER.ZS — Individuos usando internet (%)
3. IT.NET.BBND.P2 — Suscripciones banda ancha fija por 100 hab
4. IT.NET.SECR.P6 — Servidores seguros por millón de personas
5. NY.GDP.PCAP.KD — PIB per cápita (driver económico)
6. NY.GDP.MKTP.KD.ZG — Crecimiento del PIB (%)

Modelo teórico de referencia:
- Bass (1969): "A New Product Growth Model for Consumer Durables"
- Metcalfe's Law: valor de red ∝ N²
- Rogers (2003): Diffusion of Innovations (S-curve)
- ITU "Measuring the Information Society" reports
"""

import os
import sys
import numpy as np
import pandas as pd

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from worldbank_universal_fetcher import fetch_worldbank_indicator


def _synthetic_fallback(start_date, end_date, seed=42):
    """Fallback sintético con dinámica Bass + network effects realistas."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)

    # Bass diffusion calibrado a telecomunicaciones globales (1990-2020)
    p_innov = 0.008     # Innovación (early adopters)
    q_imit = 0.38       # Imitación (efecto red/boca a boca)
    M = 125.0            # Saturación (subs/100 hab, > 100 por multi-SIM)

    N = 0.3
    values = []
    internet = []
    broadband = []
    gdp = []

    gdp_base = 5000.0
    inet_base = 0.5
    bb_base = 0.01

    for t in range(steps):
        # Bass: dN/dt = [p + q*(N/M)] * (M - N)
        adoption_rate = (p_innov + q_imit * N / M) * (M - N)
        # Network externality boost: Metcalfe correction
        metcalfe_boost = 0.001 * (N / M) ** 2 * (M - N)
        dN = adoption_rate + metcalfe_boost
        N += dN + rng.normal(0, 0.8)
        N = np.clip(N, 0.1, M * 1.05)
        values.append(N)

        # Drivers correlacionados pero no determinísticos
        gdp_base *= (1.0 + 0.025 + rng.normal(0, 0.01))
        gdp.append(gdp_base)
        inet_base = min(95.0, inet_base + 2.5 + rng.normal(0, 0.5))
        internet.append(inet_base)
        bb_base = min(40.0, bb_base + 0.8 + rng.normal(0, 0.2))
        broadband.append(bb_base)

    df = pd.DataFrame({
        "date": dates,
        "value": values,
        "internet_users": internet,
        "broadband": broadband,
        "gdp_pc": gdp,
    })
    meta = {
        "source": "synthetic_bass_metcalfe",
        "p_innov": p_innov,
        "q_imit": q_imit,
        "M": M,
    }
    return df, meta


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    """
    Obtiene datos multivariados de adopción tecnológica global.
    Variable principal: suscripciones móviles por 100 hab.
    Drivers: internet_users, broadband, secure_servers, gdp_pc, gdp_growth
    """
    start_date = start_date or "1980-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "29_caso_iot"}

    indicators = {
        "IT.CEL.SETS.P2": "mobile_subs",
        "IT.NET.USER.ZS": "internet_users",
        "IT.NET.BBND.P2": "broadband",
        "IT.NET.SECR.P6": "secure_servers",
        "NY.GDP.PCAP.KD": "gdp_pc",
        "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    }

    frames = {}
    errors = []
    for indicator, col_name in indicators.items():
        try:
            df_ind, err = fetch_worldbank_indicator(indicator, country="WLD")
            if df_ind is not None and not df_ind.empty:
                df_ind = df_ind.rename(columns={"value": col_name})
                df_ind["date"] = pd.to_datetime(df_ind["date"])
                frames[col_name] = df_ind[["date", col_name]].dropna()
            else:
                errors.append(f"{indicator}: {err}")
        except Exception as e:
            errors.append(f"{indicator}: {e}")

    if "mobile_subs" not in frames:
        print(f"[WARN] Sin indicador principal: {errors}")
        return _synthetic_fallback(start_date, end_date)

    df = frames["mobile_subs"].copy().rename(columns={"mobile_subs": "value"})
    for col_name, frame in frames.items():
        if col_name == "mobile_subs":
            continue
        df = df.merge(frame, on="date", how="outer")

    df = df.sort_values("date")
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    for col in ["internet_users", "broadband", "secure_servers", "gdp_pc", "gdp_growth"]:
        if col in df.columns:
            df[col] = df[col].interpolate(method="linear", limit_direction="both")

    df = df.dropna(subset=["value"])

    if len(df) < 10:
        return _synthetic_fallback(start_date, end_date)

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    meta = {
        "source": "WorldBank_multi",
        "indicators": list(indicators.keys()),
        "obs_count": len(df),
        "obs_mean": float(df["value"].mean()),
        "errors": errors if errors else None,
    }
    return df, meta
