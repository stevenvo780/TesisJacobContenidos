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
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import requests

BASE_PATH = os.path.dirname(os.path.abspath(__file__))


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
