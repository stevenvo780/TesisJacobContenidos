"""
data.py — 05_caso_epidemiologia

Fuente: Our World in Data (OWID) COVID-19 Dataset.
Variable objetivo: log(new_cases_smoothed + 1) semanal, agregado mundial.
Drivers:
    - log_deaths: log(new_deaths_smoothed + 1), proxy de severidad/variante.
    - vaccinated: people_vaccinated_per_hundred, intervención externa.

Log-transform reduce la heterocedasticidad de 4 órdenes de magnitud
(1K→6M casos semanales) y captura cambios porcentuales consistentes
entre olas (Alpha, Delta, Omicron).

Referencia:
    Mathieu, E. et al. (2021). A global database of COVID-19
    vaccinations. Nature Human Behaviour, 5, 947-953.
"""

import os
import numpy as np
import pandas as pd
import requests

OWID_URL = (
    "https://raw.githubusercontent.com/owid/covid-19-data/"
    "master/public/data/owid-covid-data.csv"
)


def fetch_covid_data(start_date, end_date, cache_path=None):
    """
    Descarga datos OWID COVID-19 (World), agrega semanalmente y
    aplica log-transform a casos y muertes.

    Returns
    -------
    pd.DataFrame con columnas: date, value, log_deaths, vaccinated
    """
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        return df[mask].reset_index(drop=True)

    # Descarga streaming (>200 MB): solo World rows
    chunks = []
    for chunk in pd.read_csv(OWID_URL, chunksize=50000,
                             parse_dates=["date"], low_memory=False):
        world = chunk[chunk["location"] == "World"]
        if not world.empty:
            chunks.append(world)
    if not chunks:
        raise RuntimeError("No se encontraron datos OWID para 'World'")

    raw = pd.concat(chunks, ignore_index=True)
    cols = ["date", "new_cases_smoothed", "new_deaths_smoothed",
            "people_vaccinated_per_hundred"]
    raw = raw[cols].dropna(subset=["new_cases_smoothed"]).copy()
    raw["people_vaccinated_per_hundred"] = (
        raw["people_vaccinated_per_hundred"].fillna(0)
    )

    # Agregación semanal
    raw["week"] = raw["date"].dt.to_period("W").dt.start_time
    weekly = raw.groupby("week", as_index=False).mean(numeric_only=True)
    weekly = weekly.rename(columns={
        "week": "date",
        "new_cases_smoothed": "cases",
        "new_deaths_smoothed": "deaths",
        "people_vaccinated_per_hundred": "vaccinated",
    })

    # Log-transform (log1p para manejar 0s)
    weekly["value"] = np.log1p(weekly["cases"])
    weekly["log_deaths"] = np.log1p(weekly["deaths"])

    out = weekly[["date", "value", "log_deaths", "vaccinated"]].copy()

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        out.to_csv(cache_path, index=False)

    mask = (out["date"] >= start_date) & (out["date"] <= end_date)
    return out[mask].reset_index(drop=True)
