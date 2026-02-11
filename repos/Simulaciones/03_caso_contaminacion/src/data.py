"""
data.py — 03_caso_contaminacion

Fuente primaria: World Bank PM2.5 (EN.ATM.PM25.MC.M3) global, 1990-2020.
Drivers exógenos (World Bank):
  - coal_pct    (EG.ELC.COAL.ZS): % electricidad de carbón  → proxy emisiones directas
  - gdp_growth  (NY.GDP.MKTP.KD.ZG): crecimiento PIB %     → actividad económica
  - renewable_pct (EG.FEC.RNEW.ZS): % energía renovable    → mitigación

Correlaciones con PM2.5 (validación 2010-2020):
  coal_pct: r=+0.721, gdp_growth: r=+0.530, renewable_pct: r=-0.662
"""

import os

import pandas as pd
import requests


# Indicadores World Bank para drivers exógenos
WB_INDICATORS = {
    "EN.ATM.PM25.MC.M3": "pm25",
    "EG.ELC.COAL.ZS": "coal_pct",
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "EG.FEC.RNEW.ZS": "renewable_pct",
}


def _fetch_wb(indicator, start_year, end_year):
    """Descarga un indicador del World Bank para 'WLD' (mundo)."""
    url = (
        f"https://api.worldbank.org/v2/country/WLD/indicator/"
        f"{indicator}?format=json&per_page=2000&date={start_year}:{end_year}"
    )
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    payload = resp.json()
    if not isinstance(payload, list) or len(payload) < 2 or not payload[1]:
        return {}
    return {
        int(e["date"]): float(e["value"])
        for e in payload[1]
        if e.get("value") is not None
    }


def fetch_pm25_data(start_date, end_date, cache_path=None):
    """
    Carga dataset multi-variable: PM2.5 + 3 drivers exógenos.
    Usa cache local (dataset.csv) si existe.
    """
    start_year = int(start_date[:4])
    end_year = int(end_date[:4])

    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        mask = (df["date"].dt.year >= start_year) & (df["date"].dt.year <= end_year)
        return df.loc[mask].reset_index(drop=True)

    # Descargar todos los indicadores
    years = list(range(start_year, end_year + 1))
    data = {"date": [pd.Timestamp(f"{y}-01-01") for y in years]}

    for indicator, col in WB_INDICATORS.items():
        wb = _fetch_wb(indicator, start_year, end_year)
        data[col] = [wb.get(y) for y in years]

    df = pd.DataFrame(data)

    # Interpolar NaN (algunos años pueden faltar)
    for col in WB_INDICATORS.values():
        df[col] = pd.to_numeric(df[col], errors="coerce")
        df[col] = df[col].interpolate(method="linear").bfill().ffill()

    df = df.dropna(subset=["pm25"]).sort_values("date").reset_index(drop=True)

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df


# Alias de compatibilidad
def fetch_pm25_worldbank(start_date, end_date, cache_path=None):
    return fetch_pm25_data(start_date, end_date, cache_path=cache_path)
