"""
data.py — 10_caso_justicia
Descarga datos reales de Rule of Law (World Bank WGI) + drivers macro.

- Valor principal: RL.EST promediado de top-20 economías (1996-2023, anual)
- Driver 1: GDP per capita global (NY.GDP.PCAP.KD, WLD)
- Driver 2: Desempleo global (SL.UEM.TOTL.ZS, WLD)
"""

import os
import numpy as np
import pandas as pd
import requests


def _fetch_wb(indicator, country="WLD", start_year=1960, end_year=2023):
    """Descarga indicador del Banco Mundial."""
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
    params = {"format": "json", "per_page": 1000, "date": f"{start_year}:{end_year}"}
    resp = requests.get(url, params=params, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    if not isinstance(data, list) or len(data) < 2 or data[1] is None:
        return None
    rows = []
    for entry in data[1]:
        year = entry.get("date")
        value = entry.get("value")
        if year and value is not None:
            rows.append({"year": int(year), "value": float(value)})
    if not rows:
        return None
    return pd.DataFrame(rows).sort_values("year").reset_index(drop=True)


def _fetch_rl_global_avg(start_year=1996, end_year=2023):
    """Descarga RL.EST promediado de top-10 economías en una sola request."""
    countries = "USA;GBR;DEU;FRA;JPN;CAN;AUS;BRA;IND;CHN"
    url = f"https://api.worldbank.org/v2/country/{countries}/indicator/RL.EST"
    params = {"format": "json", "per_page": 5000, "date": f"{start_year}:{end_year}"}
    resp = requests.get(url, params=params, timeout=120)
    resp.raise_for_status()
    data = resp.json()

    if not isinstance(data, list) or len(data) < 2 or data[1] is None:
        return None

    rows = []
    for e in data[1]:
        if e.get("value") is not None:
            rows.append({"year": int(e["date"]), "value": float(e["value"])})

    if not rows:
        return None

    df = pd.DataFrame(rows)
    avg = df.groupby("year")["value"].mean().reset_index()
    return avg.sort_values("year").reset_index(drop=True)


def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
    """Descarga o carga datos de justicia + drivers."""
    start_date = start_date or "1996-01-01"
    end_date = end_date or "2023-12-31"

    if cache_path and not refresh and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": "10_caso_justicia"}

    start_year = int(start_date[:4])
    end_year = int(end_date[:4])

    # Valor principal: Rule of Law promediado
    rl = _fetch_rl_global_avg(start_year=max(1996, start_year), end_year=end_year)
    if rl is None or len(rl) < 5:
        return _synthetic_fallback(start_date, end_date)

    rl["date"] = pd.to_datetime(rl["year"].astype(str) + "-01-01")

    # Driver 1: GDP per capita global (normalizado como z-score)
    gdp = _fetch_wb("NY.GDP.PCAP.KD", country="WLD", start_year=start_year, end_year=end_year)
    if gdp is not None and len(gdp) > 0:
        gdp["date"] = pd.to_datetime(gdp["year"].astype(str) + "-01-01")
        gdp = gdp.rename(columns={"value": "gdp_pc"})
        rl = rl.merge(gdp[["date", "gdp_pc"]], on="date", how="left")
        # Normalizar GDP a z-score para compatibilidad con forcing
        mu, sigma = rl["gdp_pc"].mean(), rl["gdp_pc"].std()
        if sigma > 0:
            rl["gdp_pc"] = (rl["gdp_pc"] - mu) / sigma
    else:
        rl["gdp_pc"] = np.nan

    # Driver 2: Desempleo global
    unemp = _fetch_wb("SL.UEM.TOTL.ZS", country="WLD", start_year=start_year, end_year=end_year)
    if unemp is not None and len(unemp) > 0:
        unemp["date"] = pd.to_datetime(unemp["year"].astype(str) + "-01-01")
        unemp = unemp.rename(columns={"value": "unemployment"})
        rl = rl.merge(unemp[["date", "unemployment"]], on="date", how="left")
    else:
        rl["unemployment"] = np.nan

    df = rl[["date", "value", "gdp_pc", "unemployment"]].dropna(subset=["date", "value"])

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)

    return df, {"source": "worldbank_avg", "case": "10_caso_justicia",
                "n_countries": 20, "indicators": ["RL.EST", "NY.GDP.PCAP.KD", "SL.UEM.TOTL.ZS"]}


def _synthetic_fallback(start_date, end_date, seed=42):
    """Fallback sintético si WB falla."""
    rng = np.random.default_rng(seed)
    dates = pd.date_range(start=start_date, end=end_date, freq="YS")
    steps = len(dates)
    trend = np.linspace(-0.2, 0.1, steps)
    seasonal = 0.05 * np.sin(np.linspace(0, 4 * np.pi, steps))
    noise = rng.normal(0, 0.1, steps)
    values = trend + seasonal + noise
    return pd.DataFrame({"date": dates, "value": values}), {"source": "synthetic_fallback"}
