import os
import pandas as pd
import requests

OWID_URL = "https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv"


def fetch_owid_world_weekly(start_date, end_date, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df

    resp = requests.get(OWID_URL, timeout=60)
    resp.raise_for_status()

    tmp_dir = os.path.dirname(cache_path or "./")
    if tmp_dir:
        os.makedirs(tmp_dir, exist_ok=True)
    tmp_path = os.path.join(tmp_dir or ".", "owid_covid.csv")
    with open(tmp_path, "wb") as f:
        f.write(resp.content)

    df = pd.read_csv(tmp_path, parse_dates=["date"])
    df = df[df["location"] == "World"]
    cols = ["date", "new_cases_smoothed", "new_deaths_smoothed", "people_vaccinated", "stringency_index"]
    cols = [c for c in cols if c in df.columns]
    df = df[cols].dropna(subset=["date", "new_cases_smoothed"])
    df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]

    if df.empty:
        raise RuntimeError("No OWID data for selected period")

    df["week"] = df["date"].dt.to_period("W").dt.start_time
    weekly = df.groupby("week", as_index=False).mean(numeric_only=True)
    weekly = weekly.rename(columns={"week": "date", "new_cases_smoothed": "cases",
                                    "new_deaths_smoothed": "deaths",
                                    "people_vaccinated": "vaccinated",
                                    "stringency_index": "stringency"})

    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        weekly.to_csv(cache_path, index=False)

    return weekly
