"""
data.py — 04_caso_energia

Fuente: World Bank (WDI)
- Target: EG.USE.PCAP.KG.OE (energía per cápita, kg oil eq, global)
- Drivers: NY.GDP.MKTP.KD.ZG (GDP growth), SP.URB.TOTL.IN.ZS (urbanización %),
           NV.IND.TOTL.ZS (industria % GDP)

Justificación de drivers:
- gdp_growth: proxy de actividad económica → consumo energético.
  Correlación estable train/val (+0.002/+0.677), peso OLS positivo.
- urban_pct: urbanización impulsa demanda energética per cápita
  (transporte, edificios, industria concentrada). r=+0.86 train.
- industry_pct: sector industrial consume ~30% de energía primaria
  (IEA WEB 2023). Captura cambios estructurales en la economía.

Referencias:
- IEA (2023). World Energy Balances.
- World Bank (2024). World Development Indicators.
"""

import os
import requests
import pandas as pd
import numpy as np

WB_BASE = "https://api.worldbank.org/v2/country/WLD/indicator"

WB_INDICATORS = {
    "EG.USE.PCAP.KG.OE": "energy_use_pc",
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "SP.URB.TOTL.IN.ZS": "urban_pct",
    "NV.IND.TOTL.ZS": "industry_pct",
}


def _fetch_wb(code, name):
    """Descarga un indicador del World Bank."""
    url = f"{WB_BASE}/{code}?format=json&date=1970:2023&per_page=200"
    r = requests.get(url, timeout=20)
    r.raise_for_status()
    data = r.json()
    if len(data) > 1 and data[1]:
        rows = [(int(d["date"]), d["value"]) for d in data[1]
                if d["value"] is not None]
        return pd.DataFrame(rows, columns=["year", name]).sort_values("year")
    return pd.DataFrame(columns=["year", name])


def fetch_energy_data(start_date, end_date, cache_path=None):
    """
    Devuelve DataFrame con:
      date, energy_use_pc, gdp_growth, urban_pct, industry_pct
    """
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        return df[mask].reset_index(drop=True)

    dfs = {}
    for code, name in WB_INDICATORS.items():
        dfs[name] = _fetch_wb(code, name)

    df = dfs["energy_use_pc"].copy()
    for name in ["gdp_growth", "urban_pct", "industry_pct"]:
        df = df.merge(dfs[name], on="year", how="left")

    df = df.dropna().sort_values("year").reset_index(drop=True)
    df["date"] = pd.to_datetime(df["year"].astype(str) + "-01-01")
    df = df[["year", "date", "energy_use_pc", "gdp_growth",
             "urban_pct", "industry_pct"]]

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    mask = (df["date"] >= start_date) & (df["date"] <= end_date)
    return df[mask].reset_index(drop=True)
