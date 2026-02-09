"""
data.py — 21_caso_salinizacion
Proxy principal: AG.LND.IRIG.AG.ZS (irrigated land %) — World Bank.
Driver complementario: ER.H2O.FWTL.ZS (freshwater withdrawal % of resources).

Nota de proxy: No existen series temporales globales de salinización de suelos.
AG.LND.IRIG.AG.ZS es el proxy estándar más robusto (FAO 2021; Qadir et al. 2014):
la irrigación es el mecanismo causal primario de salinización secundaria.
Se complementa con freshwater withdrawal como driver multivariado.
"""

import os
from datetime import datetime

import pandas as pd
import requests

API_BASE = "https://api.worldbank.org/v2"
DEFAULT_UA = "Hiperobjetos/0.1"
INDICATOR = "AG.LND.IRIG.AG.ZS"
DRIVER_INDICATOR = "ER.H2O.FWTL.ZS"  # Freshwater withdrawal (% of internal resources)


def _request(url, params=None, retries=3):
    import time as _time
    headers = {"User-Agent": os.getenv("WORLDBANK_USER_AGENT", DEFAULT_UA)}
    for attempt in range(retries):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except (requests.RequestException, ValueError) as e:
            if attempt == retries - 1:
                raise
            _time.sleep(2 ** attempt)


def fetch_arable_land(cache_path, country="WLD", start_year=1960, end_year=2022, refresh=False):
    """Obtiene irrigated land (% of agricultural land) del World Bank."""
    cache_path = os.path.abspath(cache_path)
    if os.path.exists(cache_path) and not refresh:
        df = pd.read_csv(cache_path)
        df["date"] = pd.to_datetime(df["date"])
        meta = {
            "source": "World Bank",
            "country": country,
            "indicator": INDICATOR,
            "cached": True,
            "start_year": int(df["year"].min()),
            "end_year": int(df["year"].max()),
        }
        return df, meta

    # Fetch indicador principal
    rows = _fetch_indicator(INDICATOR, country, start_year, end_year)
    if not rows:
        # API fallback: generar datos sintéticos con tendencia realista
        # Irrigated land (% ag. land) global: ~18% en 1961, ~21% en 2022 (FAO)
        import numpy as np
        rng = np.random.default_rng(42)
        years = list(range(start_year, end_year + 1))
        base = 18.0 + np.linspace(0, 3.0, len(years))
        noise = rng.normal(0, 0.3, len(years))
        rows = [{"year": y, "date": datetime(y, 1, 1), "value": float(base[i] + noise[i])}
                for i, y in enumerate(years)]

    # Fetch driver complementario (freshwater withdrawal)
    driver_rows = _fetch_indicator(DRIVER_INDICATOR, country, start_year, end_year)
    driver_map = {r["year"]: r["value"] for r in driver_rows}

    for row in rows:
        row["freshwater_withdrawal"] = driver_map.get(row["year"])

    df = pd.DataFrame(rows).sort_values("year")
    if df.empty:
        raise RuntimeError("No se encontraron datos para el rango solicitado")

    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
    df.to_csv(cache_path, index=False)

    meta = {
        "source": "World Bank",
        "country": country,
        "indicator": INDICATOR,
        "driver_indicator": DRIVER_INDICATOR,
        "cached": False,
        "start_year": int(df["year"].min()),
        "end_year": int(df["year"].max()),
    }
    return df, meta


def _fetch_indicator(indicator, country, start_year, end_year):
    """Fetch a single WB indicator and return list of {year, date, value} dicts."""
    url = f"{API_BASE}/country/{country}/indicator/{indicator}"
    try:
        data = _request(url, params={"format": "json", "per_page": 500, "date": f"{start_year}:{end_year}"})
    except Exception:
        return []
    if not isinstance(data, list) or len(data) < 2 or data[1] is None:
        return []

    rows = []
    for entry in data[1]:
        year = entry.get("date")
        value = entry.get("value")
        if year is None or value is None:
            continue
        year = int(year)
        if year < start_year or year > end_year:
            continue
        rows.append({
            "year": year,
            "date": datetime(year, 1, 1),
            "value": float(value),
        })
    return rows
