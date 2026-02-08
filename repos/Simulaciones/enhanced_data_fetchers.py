"""
enhanced_data_fetchers.py — Mejora de Fuentes de Datos para Casos Críticos
Implementa APIs adicionales para casos con datos sintéticos

Casos mejorados:
- Conciencia (02): Google Trends
- Paradigmas (14): OpenAlex citations
- Starlink (29): CelesTrak satellite count
"""

import os
import sys
import json
import io
import zipfile
import re
import hashlib
from urllib.parse import quote
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SHARED_CACHE_DIR = os.environ.get(
    "SIM_SHARED_CACHE",
    os.path.join(BASE_PATH, "data_cache", "shared"),
)


def _shared_path(name: str) -> str:
    os.makedirs(SHARED_CACHE_DIR, exist_ok=True)
    return os.path.join(SHARED_CACHE_DIR, name)


def _url_cache_name(prefix: str, url: str, ext: str) -> str:
    digest = hashlib.md5(url.encode("utf-8")).hexdigest()
    return f"{prefix}_{digest}.{ext}"


# ==============================================================================
# 1. GOOGLE TRENDS (Conciencia / Atención Colectiva)
# ==============================================================================

def fetch_google_trends_proxy(keywords=["global news", "breaking news"], 
                               start_year=2010, end_year=2024, cache_path=None):
    """
    Fetch Google Trends data usando pytrends.
    Proxy para "conciencia colectiva" = atención mediática global.
    
    Returned: DataFrame con date, interest_over_time
    """
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "Google Trends", "cached": True}
    
    try:
        from pytrends.request import TrendReq
        
        pytrends = TrendReq(hl='en-US', tz=360)
        timeframe = f'{start_year}-01-01 {end_year}-12-31'
        
        pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='', gprop='')
        df = pytrends.interest_over_time()
        
        if df.empty:
            raise RuntimeError("No Google Trends data available")
        
        # Promediar keywords
        df = df.drop('isPartial', axis=1, errors='ignore')
        df['interest'] = df.mean(axis=1)
        df = df.reset_index().rename(columns={'date': 'date'})
        df = df[['date', 'interest']]
        
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        
        return df, {"source": "Google Trends", "cached": False, "keywords": keywords}
    
    except ImportError:
        print("⚠️ pytrends not installed. Run: pip install pytrends")
        # Fallback: generar datos sintéticos calibrados
        return _generate_synthetic_trends(start_year, end_year), {"source": "synthetic_fallback"}


def _generate_synthetic_trends(start_year, end_year):
    """Fallback: genera tendencias sintéticas realistas."""
    dates = pd.date_range(start=f'{start_year}-01-01', end=f'{end_year}-12-31', freq='MS')
    n = len(dates)
    
    # Tendencia + estacionalidad + ruido
    trend = np.linspace(40, 70, n)
    seasonal = 15 * np.sin(np.linspace(0, 4*np.pi, n))
    noise = np.random.normal(0, 5, n)
    interest = np.clip(trend + seasonal + noise, 0, 100)
    
    return pd.DataFrame({'date': dates, 'interest': interest})


# ==============================================================================
# 2. OPENALEX (Paradigmas / Citaciones Científicas)
# ==============================================================================

def fetch_openalex_citations(concept_id="C41008148", start_year=2000, end_year=2023, cache_path=None):
    """
    Fetch citation data from OpenAlex for a specific concept.
    Default: C41008148 = "Computer science"
    
    Returns: DataFrame con year, works_count, cited_by_count
    """
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path)
        return df, {"source": "OpenAlex", "cached": True}
    
    url = f"https://api.openalex.org/concepts/{concept_id}"
    
    try:
        resp = requests.get(url, headers={"User-Agent": "Hiperobjetos/0.1"}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        
        counts_by_year = data.get("counts_by_year", [])
        
        # If no data, generate synthetic fallback
        if not counts_by_year:
            return _generate_synthetic_citations(start_year, end_year), {"source": "synthetic_fallback", "reason": "no_counts_by_year"}
        
        rows = []
        for entry in counts_by_year:
            year = entry.get("year")
            if year and start_year <= year <= end_year:
                rows.append({
                    "year": year,
                    "date": datetime(year, 1, 1),
                    "works_count": entry.get("works_count", 0),
                    "cited_by_count": entry.get("cited_by_count", 0)
                })
        
        if not rows:
            return _generate_synthetic_citations(start_year, end_year), {"source": "synthetic_fallback", "reason": "no_rows_in_range"}
            
        df = pd.DataFrame(rows).sort_values("year")
        
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        
        meta = {
            "source": "OpenAlex",
            "concept_id": concept_id,
            "concept_name": data.get("display_name", "Unknown"),
            "cached": False
        }
        return df, meta
    
    except requests.RequestException as e:
        print(f"⚠️ OpenAlex fetch failed: {e}")
        return _generate_synthetic_citations(start_year, end_year), {"source": "synthetic_fallback"}


def _generate_synthetic_citations(start_year, end_year):
    """Fallback: genera curvas de citación sintéticas (logistic growth)."""
    years = list(range(start_year, end_year + 1))
    n = len(years)
    
    # Logistic growth curve (paradigm shift)
    t = np.linspace(0, 10, n)
    works = 10000 * (1 / (1 + np.exp(-0.5 * (t - 5)))) + 5000
    citations = works * (3 + np.random.uniform(0, 1, n))
    
    return pd.DataFrame({
        'year': years,
        'date': [datetime(y, 1, 1) for y in years],
        'works_count': works.astype(int),
        'cited_by_count': citations.astype(int)
    })


# ==============================================================================
# 3. CELESTRAK (Starlink / Satélites)
# ==============================================================================

def fetch_celestrak_starlink_count(cache_path=None):
    """
    Fetch current Starlink satellite count from CelesTrak TLE.
    Historical data requires snapshots over time.
    
    Returns: Current count and metadata
    """
    if cache_path and os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            data = json.load(f)
        return data, {"source": "CelesTrak", "cached": True}
    
    url = "https://celestrak.org/NORAD/elements/gp.php?GROUP=starlink&FORMAT=json"
    
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        satellites = resp.json()
        
        active_count = len(satellites)
        
        result = {
            "date": datetime.now().isoformat(),
            "active_satellites": active_count,
            "sample_names": [s.get("OBJECT_NAME", "")[:20] for s in satellites[:5]]
        }
        
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            with open(cache_path, 'w') as f:
                json.dump(result, f, indent=2)
        
        return result, {"source": "CelesTrak", "cached": False}
    
    except requests.RequestException as e:
        print(f"⚠️ CelesTrak fetch failed: {e}")
        return {"date": datetime.now().isoformat(), "active_satellites": 5000, "note": "fallback estimate"}, {"source": "fallback"}


# ==============================================================================
# 4. FRED (Economic Data Backup)
# ==============================================================================

def fetch_fred_series(series_id="FEDFUNDS", start_date="2000-01-01", end_date=None, cache_path=None):
    """
    Fetch economic time series from FRED (Federal Reserve Economic Data).
    
    Popular series:
    - FEDFUNDS: Federal Funds Rate
    - CPIAUCSL: Consumer Price Index
    - UNRATE: Unemployment Rate
    - GDP: Gross Domestic Product
    """
    if cache_path is None:
        cache_path = _shared_path(f"fred_{series_id}.csv")
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "FRED", "cached": True}
    
    if end_date is None:
        end_date = datetime.now().strftime("%Y-%m-%d")
    
    # FRED API (requires API key, but CSV format is public)
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}&cosd={start_date}&coed={end_date}"
    
    try:
        df = pd.read_csv(url, parse_dates=["DATE"])
        df = df.rename(columns={"DATE": "date", series_id: "value"})
        df = df.dropna()
        
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            df.to_csv(cache_path, index=False)
        
        return df, {"source": "FRED", "series_id": series_id, "cached": False}
    
    except Exception as e:
        print(f"⚠️ FRED fetch failed: {e}")
        return pd.DataFrame(), {"source": "failed", "error": str(e)}


# ==============================================================================
# 5. WMO (Sea Level, SST, OHC) + BADC-CSV Parser
# ==============================================================================

def _parse_badc_csv(text: str) -> pd.DataFrame:
    lines = text.splitlines()
    data_idx = None
    for i, line in enumerate(lines):
        if line.strip().lower() == "data":
            data_idx = i
            break
    if data_idx is None or data_idx + 1 >= len(lines):
        raise ValueError("BADC-CSV data section not found")
    data_text = "\n".join(lines[data_idx + 1 :])
    return pd.read_csv(io.StringIO(data_text))


def _badc_zip_to_df(url: str, inner_name: str, cache_path: str | None = None) -> pd.DataFrame:
    if cache_path and os.path.exists(cache_path):
        return pd.read_csv(cache_path, parse_dates=["date"])
    shared_zip = _shared_path(_url_cache_name("wmo", url, "zip"))
    if not os.path.exists(shared_zip):
        resp = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        with open(shared_zip, "wb") as f:
            f.write(resp.content)
    zf = zipfile.ZipFile(shared_zip)
    with zf.open(inner_name) as f:
        text = f.read().decode("utf-8")
    df = _parse_badc_csv(text)
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df


def _annual_to_monthly(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date").set_index("date")
    monthly = df[[value_col]].resample("MS").interpolate("linear")
    return monthly.reset_index()


def fetch_wmo_sea_level(start_date=None, end_date=None, cache_path=None):
    url = (
        "https://climateindicators-wmo-dashboard.org/"
        "climate_dashboard/sites/default/files/formatted_data/Sea_level_data_files.zip"
    )
    df = _badc_zip_to_df(url, "sealevel_AVISO.csv", cache_path=cache_path)
    df = df.rename(columns={"data": "sea_level"})
    df["date"] = pd.to_datetime(
        dict(year=df["year"], month=df["month"], day=df.get("day", 1)),
        errors="coerce",
    )
    df = df[["date", "sea_level"]].dropna()
    df = df.groupby(pd.Grouper(key="date", freq="MS"), as_index=False).mean()
    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return df, {"source": "WMO", "dataset": "sea_level"}


def fetch_wmo_ohc(start_date=None, end_date=None, cache_path=None):
    url = (
        "https://climateindicators-wmo-dashboard.org/"
        "climate_dashboard/sites/default/files/formatted_data/Ocean_heat_content_data_files.zip"
    )
    df = _badc_zip_to_df(url, "ohc_GCOS.csv", cache_path=cache_path)
    df = df.rename(columns={"data": "ohc"})
    df["year"] = pd.to_numeric(df.get("year"), errors="coerce")
    df = df.dropna(subset=["year"])
    df["date"] = pd.to_datetime(df["year"].astype(int), format="%Y", errors="coerce")
    df = df[["date", "ohc"]].dropna()
    df = _annual_to_monthly(df, "ohc")
    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return df, {"source": "WMO", "dataset": "ocean_heat_content"}


def fetch_wmo_sst(start_date=None, end_date=None, cache_path=None, variant="ERSST"):
    url = (
        "https://climateindicators-wmo-dashboard.org/"
        "climate_dashboard/sites/default/files/formatted_data/Sea-surface_temperature_data_files.zip"
    )
    inner = "sst_ERSST.csv" if variant.upper() == "ERSST" else "sst_HadSST4.csv"
    df = _badc_zip_to_df(url, inner, cache_path=cache_path)
    df = df.rename(columns={"data": "sst"})
    df["year"] = pd.to_numeric(df.get("year"), errors="coerce")
    df = df.dropna(subset=["year"])
    df["date"] = pd.to_datetime(df["year"].astype(int), format="%Y", errors="coerce")
    df = df[["date", "sst"]].dropna()
    df = _annual_to_monthly(df, "sst")
    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    return df, {"source": "WMO", "dataset": f"sst_{variant.upper()}"}


# ==============================================================================
# 6. Solar Irradiance (SORCE/TSIS) + Stratospheric Aerosols (GISS)
# ==============================================================================

def _fetch_tsi_daily(url: str) -> pd.DataFrame:
    shared_txt = _shared_path(_url_cache_name("tsi", url, "txt"))
    if not os.path.exists(shared_txt):
        resp = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        with open(shared_txt, "w", encoding="utf-8") as f:
            f.write(resp.text)
    with open(shared_txt, "r", encoding="utf-8") as f:
        text = f.read()
    rows = []
    for line in text.splitlines():
        if not line.strip() or line.startswith(";") or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) < 5:
            continue
        yyyymmdd = parts[0].split(".")[0]
        try:
            dt = datetime.strptime(yyyymmdd, "%Y%m%d")
            tsi = float(parts[4])
        except Exception:
            continue
        rows.append({"date": dt, "tsi": tsi})
    return pd.DataFrame(rows)


def fetch_tsi_monthly(start_date=None, end_date=None, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        return pd.read_csv(cache_path, parse_dates=["date"]), {"source": "cache"}
    sorce_url = "http://lasp.colorado.edu/data/sorce/tsi_data/daily/sorce_tsi_L3_c24h_latest.txt"
    tsis_url = "https://lasp.colorado.edu/data/tsis/tsi_data/tsis_tsi_L3_c24h_latest.txt"
    df = pd.concat(
        [_fetch_tsi_daily(sorce_url), _fetch_tsi_daily(tsis_url)],
        ignore_index=True,
    ).dropna()
    if df.empty:
        return pd.DataFrame(), {"source": "TSI", "error": "no_data"}
    df["date"] = pd.to_datetime(df["date"])
    df = df.groupby(pd.Grouper(key="date", freq="MS"), as_index=False)["tsi"].mean()
    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df, {"source": "SORCE+TSIS", "dataset": "tsi"}


def fetch_giss_aod_monthly(start_date=None, end_date=None, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        return pd.read_csv(cache_path, parse_dates=["date"]), {"source": "cache"}
    url = "https://data.giss.nasa.gov/modelforce/strataer/tau.line_2012.12.txt"
    shared_txt = _shared_path(_url_cache_name("giss_aod", url, "txt"))
    if not os.path.exists(shared_txt):
        resp = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        with open(shared_txt, "w", encoding="utf-8") as f:
            f.write(resp.text)
    with open(shared_txt, "r", encoding="utf-8") as f:
        text = f.read()
    rows = []
    for line in text.splitlines():
        if not line.strip():
            continue
        if re.match(r"^[A-Za-z\\-]", line.strip()):
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        try:
            yearmon = float(parts[0])
            year = int(yearmon)
            frac = yearmon - year
            month = int(round(frac * 12 + 0.5))
            month = min(max(month, 1), 12)
            dt = datetime(year, month, 1)
            aod = float(parts[1])
        except Exception:
            continue
        rows.append({"date": dt, "aod": aod})
    df = pd.DataFrame(rows)
    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df, {"source": "GISS", "dataset": "aod"}


# ==============================================================================
# 7. OWID Grapher (Plastics, etc.)
# ==============================================================================

def fetch_owid_grapher_series(slug_candidates, entity="World", cache_path=None):
    last_error = None
    for slug in slug_candidates:
        local_cache = cache_path
        if local_cache is None:
            local_cache = _shared_path(f"owid_{slug}.csv")
        if local_cache and os.path.exists(local_cache):
            return pd.read_csv(local_cache, parse_dates=["date"]), {"source": "cache"}
        url = f"https://ourworldindata.org/grapher/{slug}.csv"
        try:
            resp = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
            resp.raise_for_status()
            df = pd.read_csv(io.StringIO(resp.text))
        except Exception as e:
            last_error = str(e)
            continue
        if df.empty or "Year" not in df.columns:
            continue
        value_cols = [c for c in df.columns if c not in ("Entity", "Code", "Year")]
        if not value_cols:
            continue
        value_col = value_cols[0]
        if entity in df["Entity"].unique():
            df = df[df["Entity"] == entity]
        else:
            df = df[df["Entity"] == df["Entity"].iloc[0]]
        df = df[["Year", value_col]].rename(columns={"Year": "year", value_col: "value"})
        df["date"] = pd.to_datetime(df["year"].astype(int), format="%Y")
        df = df[["date", "value"]].dropna()
        if local_cache:
            os.makedirs(os.path.dirname(local_cache), exist_ok=True)
            df.to_csv(local_cache, index=False)
        return df, {"source": "OWID", "slug": slug, "entity": entity}
    return pd.DataFrame(), {"source": "OWID", "error": last_error or "no_slug_worked"}


# ==============================================================================
# 8. CelesTrak SATCAT Time Series
# ==============================================================================

def _satcat_timeseries(df, start_date, end_date):
    df = df.copy()
    df["launch_date"] = pd.to_datetime(df["LAUNCH_DATE"], errors="coerce")
    df["decay_date"] = pd.to_datetime(df["DECAY_DATE"], errors="coerce")
    df = df.dropna(subset=["launch_date"])
    idx = pd.date_range(start=start_date, end=end_date, freq="MS")
    launch_counts = df["launch_date"].dt.to_period("M").dt.to_timestamp().value_counts()
    decay_counts = df["decay_date"].dropna().dt.to_period("M").dt.to_timestamp().value_counts()
    launch_series = launch_counts.reindex(idx, fill_value=0).sort_index()
    decay_series = decay_counts.reindex(idx, fill_value=0).sort_index()
    active_series = (launch_series.cumsum() - decay_series.cumsum()).clip(lower=0)
    out = pd.DataFrame({
        "date": idx,
        "active": active_series.values,
        "launches": launch_series.values,
    })
    return out


def fetch_celestrak_satcat_timeseries(start_date, end_date, filter_fn=None, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        return pd.read_csv(cache_path, parse_dates=["date"]), {"source": "cache"}
    url = "https://celestrak.org/pub/satcat.csv"
    shared_csv = _shared_path(_url_cache_name("satcat", url, "csv"))
    if not os.path.exists(shared_csv):
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        with open(shared_csv, "w", encoding="utf-8") as f:
            f.write(resp.text)
    df = pd.read_csv(shared_csv)
    if filter_fn is not None:
        df = df[filter_fn(df)]
    ts = _satcat_timeseries(df, start_date, end_date)
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        ts.to_csv(cache_path, index=False)
    return ts, {"source": "CelesTrak", "dataset": "satcat"}


def fetch_celestrak_debris_timeseries(start_date, end_date, name_contains=None, owner=None, cache_path=None):
    def _filter(df):
        sel = df["OBJECT_TYPE"].fillna("") == "DEB"
        if name_contains:
            sel &= df["OBJECT_NAME"].fillna("").str.contains(name_contains, case=False)
        if owner:
            sel &= df["OWNER"].fillna("").str.contains(owner, case=False)
        return sel

    ts, meta = fetch_celestrak_satcat_timeseries(
        start_date,
        end_date,
        filter_fn=_filter,
        cache_path=cache_path,
    )
    ts = ts.rename(columns={"launches": "debris_new", "active": "debris_active"})
    meta.update({"type": "debris"})
    return ts, meta


# ==============================================================================
# 9. GRAVIS (GFZ) Chartdata
# ==============================================================================

def fetch_gravis_chartdata(model, field, bset, basin, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        return pd.read_csv(cache_path, parse_dates=["date"]), {"source": "cache"}
    url = f"https://gravis.gfz.de/chartdata/{model}/{field}/{bset}/{quote(basin)}"
    resp = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
    resp.raise_for_status()
    js = resp.json()
    # data: list of series; use first
    series = js.get("data", [])
    if not series:
        return pd.DataFrame(), {"source": "GRAVIS", "error": "no_data"}
    points = series[0]
    rows = []
    for p in points:
        try:
            year = int(p.get("y"))
            day = int(p.get("d"))
            dt = datetime(year, 1, 1) + timedelta(days=day - 1)
            val = float(p.get("v"))
        except Exception:
            continue
        rows.append({"date": dt, "value": val})
    df = pd.DataFrame(rows).sort_values("date")
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df, {"source": "GRAVIS", "model": model, "field": field, "basin": basin}


# ==============================================================================
# 10. PMEL CO2 Time Series (pCO2 + pH)
# ==============================================================================

def fetch_pmel_co2_timeseries(station="WHOTS", start_date=None, end_date=None, cache_path=None):
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache"}
    url = f"https://www.pmel.noaa.gov/co2/timeseries/{station}.txt"
    shared_txt = _shared_path(_url_cache_name("pmel", url, "txt"))
    if not os.path.exists(shared_txt):
        resp = requests.get(url, timeout=60, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        with open(shared_txt, "w", encoding="utf-8") as f:
            f.write(resp.text)
    df = pd.read_csv(shared_txt, comment="#", sep="\\t", engine="python")
    if "datetime_utc" not in df.columns:
        return pd.DataFrame(), {"source": "PMEL", "error": "no_datetime_utc"}
    df = df.rename(columns={
        "datetime_utc": "date",
        "pCO2_sw": "pco2_sw",
        "pH_sw": "ph_sw",
    })
    df["date"] = pd.to_datetime(df["date"])
    keep = ["date"]
    if "pco2_sw" in df.columns:
        keep.append("pco2_sw")
    if "ph_sw" in df.columns:
        keep.append("ph_sw")
    df = df[keep].dropna(subset=["date"])
    df = df.groupby(pd.Grouper(key="date", freq="MS"), as_index=False).mean()
    if start_date and end_date:
        df = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df, {"source": "PMEL", "station": station}


# ==============================================================================
# 11. USGS Groundwater Withdrawals (Tabla Water Science School)
# ==============================================================================

def fetch_usgs_groundwater_withdrawals(cache_path=None):
    if cache_path and os.path.exists(cache_path):
        return pd.read_csv(cache_path, parse_dates=["date"]), {"source": "cache"}
    url = "https://www.usgs.gov/special-topics/water-science-school/science/groundwater-use-united-states"
    tables = pd.read_html(url)
    if not tables:
        return pd.DataFrame(), {"source": "USGS", "error": "no_tables"}
    t = tables[0]
    # First row is header
    header = t.iloc[0].tolist()
    t = t[1:].copy()
    t.columns = header
    if "Year" not in t.columns:
        return pd.DataFrame(), {"source": "USGS", "error": "no_year_col"}
    t["Year"] = pd.to_numeric(t["Year"], errors="coerce")
    t = t.dropna(subset=["Year"])
    # Use Fresh groundwater withdrawals (billion gallons per day)
    fresh_col = None
    for c in t.columns:
        if str(c).strip().lower().startswith("fresh"):
            fresh_col = c
            break
    if fresh_col is None:
        return pd.DataFrame(), {"source": "USGS", "error": "no_fresh_col"}
    t[fresh_col] = pd.to_numeric(t[fresh_col], errors="coerce")
    t = t.dropna(subset=[fresh_col])
    df = pd.DataFrame({
        "date": pd.to_datetime(t["Year"].astype(int), format="%Y"),
        "extraction_usgs": t[fresh_col].astype(float),
    }).sort_values("date")
    if cache_path:
        os.makedirs(os.path.dirname(cache_path), exist_ok=True)
        df.to_csv(cache_path, index=False)
    return df, {"source": "USGS", "unit": "Bgal/d"}


# ==============================================================================
# MAIN: Test all enhanced fetchers
# ==============================================================================

def main():
    print("🔬 ENHANCED DATA FETCHERS TEST")
    print("=" * 60)
    
    output_dir = os.path.join(BASE_PATH, "data_cache")
    os.makedirs(output_dir, exist_ok=True)
    
    # 1. Google Trends (Conciencia)
    print("\n📊 Testing Google Trends...")
    try:
        df, meta = fetch_google_trends_proxy(
            keywords=["global news", "world news"],
            cache_path=os.path.join(output_dir, "google_trends_awareness.csv")
        )
        print(f"   ✅ {len(df)} datapoints, source: {meta.get('source')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # 2. OpenAlex (Paradigmas)
    print("\n📊 Testing OpenAlex...")
    try:
        df, meta = fetch_openalex_citations(
            concept_id="C41008148",  # Computer Science
            cache_path=os.path.join(output_dir, "openalex_cs_citations.csv")
        )
        print(f"   ✅ {len(df)} years, concept: {meta.get('concept_name', 'N/A')}")
        if not df.empty:
            print(f"   Latest: {df.iloc[-1]['year']} - {df.iloc[-1]['cited_by_count']:,} citations")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # 3. CelesTrak (Starlink)
    print("\n📊 Testing CelesTrak...")
    try:
        data, meta = fetch_celestrak_starlink_count(
            cache_path=os.path.join(output_dir, "celestrak_starlink.json")
        )
        print(f"   ✅ Active Starlink satellites: {data.get('active_satellites', 'N/A')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    # 4. FRED (Backup economic data)
    print("\n📊 Testing FRED...")
    try:
        df, meta = fetch_fred_series(
            series_id="CPIAUCSL",  # CPI
            cache_path=os.path.join(output_dir, "fred_cpi.csv")
        )
        print(f"   ✅ {len(df)} datapoints, source: {meta.get('source')}")
    except Exception as e:
        print(f"   ❌ Failed: {e}")
    
    print("\n" + "=" * 60)
    print("✅ Enhanced data fetchers ready!")
    print(f"   Cache directory: {output_dir}")


if __name__ == "__main__":
    main()


def fetch_celestrak_catalog_count(group="active", cache_path=None):
    """
    Fetch count of tracked objects from CelesTrak catalog group.
    group: 'active', 'starlink', 'all', etc.
    """
    if cache_path is None:
        cache_path = _shared_path(f"celestrak_{group}.json")
    if cache_path and os.path.exists(cache_path):
        with open(cache_path, 'r') as f:
            data = json.load(f)
        return data, {"source": "CelesTrak", "cached": True, "group": group}

    url = f"https://celestrak.org/NORAD/elements/gp.php?GROUP={group}&FORMAT=json"

    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        satellites = resp.json()
        count = len(satellites)
        result = {
            "date": datetime.now().isoformat(),
            "count": count,
            "group": group,
        }
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            with open(cache_path, 'w') as f:
                json.dump(result, f, indent=2)
        return result, {"source": "CelesTrak", "cached": False, "group": group}
    except requests.RequestException as e:
        print(f"⚠️ CelesTrak catalog fetch failed: {e}")
        if cache_path and os.path.exists(cache_path):
            with open(cache_path, 'r') as f:
                data = json.load(f)
            return data, {"source": "CelesTrak", "cached": True, "fallback": True, "group": group}
        return {"date": datetime.now().isoformat(), "count": 0, "group": group}, {"source": "CelesTrak", "error": str(e)}
