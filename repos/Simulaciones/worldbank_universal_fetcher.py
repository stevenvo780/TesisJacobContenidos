"""
worldbank_universal_fetcher.py — Fetcher Universal de World Bank para Todos los Casos
Implementa descarga automática de indicadores del World Bank para todos los casos aplicables.
"""

import os
import sys
import json
from datetime import datetime
import pandas as pd
import requests

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

# Mapeo de casos a indicadores del World Bank
WORLDBANK_INDICATORS = {
    "03_caso_contaminacion": {
        "indicator": "EN.ATM.PM25.MC.M3",
        "description": "PM2.5 air pollution, population exposed",
        "column_name": "pm25"
    },
    "05_caso_epidemiologia": {
        "indicator": "SH.DYN.MORT",
        "description": "Mortality rate, under-5 (per 1,000 live births)",
        "column_name": "mortality"
    },
    "11_caso_justicia": {
        "indicator": "RL.EST",
        "description": "Rule of Law: Estimate (WGI)",
        "column_name": "rule_of_law"
    },
    "13_caso_movilidad": {
        "indicator": "IS.AIR.PSGR",
        "description": "Air transport, passengers carried",
        "column_name": "passengers"
    },
    "15_caso_politicas_estrategicas": {
        "indicator": "GC.TAX.TOTL.GD.ZS",
        "description": "Tax revenue (% of GDP)",
        "column_name": "tax_revenue"
    },
    "16_caso_postverdad": {
        "indicator": "IT.NET.USER.ZS",
        "description": "Individuals using the Internet (% of population)",
        "column_name": "internet_users"
    },
    "19_caso_deforestacion": {
        "indicator": "AG.LND.FRST.ZS",
        "description": "Forest area (% of land area)",
        "column_name": "forest_area"
    },
    "20_caso_oceanos": {
        "indicator": "EN.ATM.CO2E.KT",
        "description": "CO2 emissions (kt)",
        "column_name": "co2_emissions"
    },
    "21_caso_urbanizacion": {
        "indicator": "SP.URB.TOTL.IN.ZS",
        "description": "Urban population (% of total population)",
        "column_name": "urban_pop"
    },
    "22_caso_acidificacion_oceanica": {
        "indicator": "EN.ATM.CO2E.PC",
        "description": "CO2 emissions (metric tons per capita)",
        "column_name": "co2_per_capita"
    },
    "24_caso_salinizacion": {
        "indicator": "AG.LND.ARBL.ZS",
        "description": "Arable land (% of land area)",
        "column_name": "arable_land"
    },
    "25_caso_fosforo": {
        "indicator": "AG.CON.FERT.ZS",
        "description": "Fertilizer consumption (kg per hectare)",
        "column_name": "fertilizer"
    },
    "26_caso_erosion_dialectica": {
        "indicator": "SE.ADT.LITR.ZS",
        "description": "Literacy rate, adult total (% ages 15+)",
        "column_name": "literacy"
    },
    "27_caso_microplasticos": {
        "indicator": "EN.ATM.GHGT.KT.CE",
        "description": "Total greenhouse gas emissions (kt of CO2 equivalent)",
        "column_name": "ghg_emissions"
    },
    "28_caso_acuiferos": {
        "indicator": "SH.H2O.BASW.ZS",
        "description": "People using safely managed drinking water (% pop)",
        "column_name": "water_access"
    },
    "30_caso_riesgo_biologico": {
        "indicator": "SH.DYN.MORT",
        "description": "Mortality rate, under-5",
        "column_name": "mortality"
    },
    "31_caso_fuga_cerebros": {
        "indicator": "GB.XPD.RSDV.GD.ZS",
        "description": "Research and development expenditure (% of GDP)",
        "column_name": "rd_expenditure"
    },
    "32_caso_iot": {
        "indicator": "IT.CEL.SETS.P2",
        "description": "Mobile cellular subscriptions (per 100 people)",
        "column_name": "mobile_subs"
    },
}


def fetch_worldbank_indicator(indicator, country="WLD", start_year=1960, end_year=2023):
    """Fetch World Bank indicator data."""
    url = f"https://api.worldbank.org/v2/country/{country}/indicator/{indicator}"
    params = {"format": "json", "per_page": 500, "date": f"{start_year}:{end_year}"}
    
    try:
        resp = requests.get(url, params=params, headers={"User-Agent": "Hiperobjetos/0.1"}, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        
        if not isinstance(data, list) or len(data) < 2 or data[1] is None:
            return None, f"No data for {indicator}"
        
        rows = []
        for entry in data[1]:
            year = entry.get("date")
            value = entry.get("value")
            if year and value is not None:
                rows.append({
                    "year": int(year),
                    "date": datetime(int(year), 1, 1),
                    "value": float(value)
                })
        
        if not rows:
            return None, "No valid entries"
        
        df = pd.DataFrame(rows).sort_values("year")
        return df, None
    
    except Exception as e:
        return None, str(e)


def update_case_data(case_id, info, cache_dir):
    """Update data.py for a specific case with World Bank data."""
    indicator = info["indicator"]
    column_name = info["column_name"]
    
    print(f"  Fetching {indicator}...")
    df, error = fetch_worldbank_indicator(indicator)
    
    if df is None:
        print(f"  ❌ Failed: {error}")
        return None
    
    # Save cache
    cache_path = os.path.join(cache_dir, f"{case_id}_worldbank.csv")
    df.to_csv(cache_path, index=False)
    
    print(f"  ✅ {len(df)} datapoints ({df['year'].min()}-{df['year'].max()})")
    
    return {
        "case": case_id,
        "indicator": indicator,
        "description": info["description"],
        "datapoints": len(df),
        "year_range": f"{df['year'].min()}-{df['year'].max()}",
        "cache_path": cache_path
    }


def main():
    print("🌐 WORLD BANK UNIVERSAL FETCHER")
    print("=" * 60)
    
    cache_dir = os.path.join(BASE_PATH, "data_cache", "worldbank")
    os.makedirs(cache_dir, exist_ok=True)
    
    results = []
    success_count = 0
    fail_count = 0
    
    for case_id, info in WORLDBANK_INDICATORS.items():
        print(f"\n📊 {case_id}: {info['description']}")
        
        result = update_case_data(case_id, info, cache_dir)
        if result:
            results.append(result)
            success_count += 1
        else:
            fail_count += 1
    
    # Save summary
    summary_path = os.path.join(BASE_PATH, "outputs_gpu", "worldbank_fetch_summary.json")
    with open(summary_path, "w") as f:
        json.dump({
            "generated_at": datetime.now().isoformat(),
            "total_cases": len(WORLDBANK_INDICATORS),
            "success": success_count,
            "failed": fail_count,
            "results": results
        }, f, indent=2)
    
    print("\n" + "=" * 60)
    print(f"📊 RESUMEN:")
    print(f"   ✅ Éxito: {success_count}/{len(WORLDBANK_INDICATORS)}")
    print(f"   ❌ Fallidos: {fail_count}/{len(WORLDBANK_INDICATORS)}")
    print(f"   📁 Cache: {cache_dir}")
    print(f"   📋 Summary: {summary_path}")
    
    # Print table
    print("\n📋 DATOS DESCARGADOS:")
    print("| Caso | Indicador | Puntos | Rango |")
    print("|------|-----------|--------|-------|")
    for r in results:
        print(f"| {r['case'][:20]} | {r['indicator']} | {r['datapoints']} | {r['year_range']} |")


if __name__ == "__main__":
    main()
