"""
data_universal.py — Cargador universal de datos reales con fallback.
"""

from __future__ import annotations

import os
import sys
import pandas as pd

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
SIM_ROOT = os.path.dirname(BASE_PATH)
if SIM_ROOT not in sys.path:
    sys.path.insert(0, SIM_ROOT)

import worldbank_universal_fetcher as wb
import enhanced_data_fetchers as enh


WORLD_BANK_MAP = {
    "10_caso_justicia": [
        ("RL.EST", "rule_of_law"),
        ("CC.EST", "corruption_control"),
        ("SI.POV.GINI", "gini"),
    ],
    "11_caso_movilidad": [
        ("IS.VEH.NVEH.P3", "vehicles_per_1000"),
        ("EP.PMP.SGAS.CD", "gas_price"),
        ("NY.GDP.PCAP.KD", "gdp_per_capita"),
    ],
    "13_caso_politicas_estrategicas": ("MS.MIL.XPND.GD.ZS", "military_spend_gdp"),
    "17_caso_oceanos": ("EN.ATM.CO2E.KT", "co2_emissions"),
    "19_caso_acidificacion_oceanica": ("EN.ATM.CO2E.PC", "co2_per_capita"),
    "23_caso_erosion_dialectica": ("SE.ADT.LITR.ZS", "literacy"),
    "24_caso_microplasticos": ("EN.ATM.GHGT.KT.CE", "ghg_emissions"),
    "25_caso_acuiferos": ("SH.H2O.BASW.ZS", "water_access"),
    "27_caso_riesgo_biologico": ("SH.DYN.MORT", "mortality"),
    "28_caso_fuga_cerebros": ("GB.XPD.RSDV.GD.ZS", "rd_expenditure"),
    "29_caso_iot": ("IT.CEL.SETS.P2", "mobile_subs"),
}

GOOGLE_TRENDS_MAP = {
    "02_caso_conciencia": {"keywords": ["global news", "breaking news"]},
    "14_caso_postverdad": {"keywords": ["fake news", "misinformation"]},
}

OPENALEX_MAP = {
    "12_caso_paradigmas": {"concept_id": "C41008148"},
}


def _filter_date_range(df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    if "date" not in df.columns:
        return df
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    return df[(df["date"] >= start_date) & (df["date"] <= end_date)]


def fetch_case_data(case_id: str, start_date: str, end_date: str, cache_path: str | None = None):
    # Cache primero
    if cache_path and os.path.exists(cache_path):
        df = pd.read_csv(cache_path, parse_dates=["date"])
        return df, {"source": "cache", "case": case_id}

    # World Bank
    if case_id in WORLD_BANK_MAP:
        cfg = WORLD_BANK_MAP[case_id]
        if isinstance(cfg, tuple):
            indicator, col = cfg
            df, err = wb.fetch_worldbank_indicator(indicator)
            if df is not None:
                df = df.rename(columns={"value": col})
                df["value"] = df[col]
                df = _filter_date_range(df, start_date, end_date)
                if cache_path:
                    os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                    df.to_csv(cache_path, index=False)
                return df, {"source": "worldbank", "indicator": indicator}
            return None, {"source": "worldbank", "error": err}

        frames = []
        indicators = []
        for indicator, col in cfg:
            df, err = wb.fetch_worldbank_indicator(indicator)
            if df is None:
                continue
            df = df.rename(columns={"value": col})
            frames.append(df[["date", col]])
            indicators.append(indicator)
        if not frames:
            return None, {"source": "worldbank", "error": "no_indicators"}
        merged = frames[0]
        for frame in frames[1:]:
            merged = merged.merge(frame, on="date", how="outer")
        first_col = frames[0].columns[1]
        merged["value"] = merged[first_col]
        merged = _filter_date_range(merged, start_date, end_date)
        if cache_path:
            os.makedirs(os.path.dirname(cache_path), exist_ok=True)
            merged.to_csv(cache_path, index=False)
        return merged, {"source": "worldbank", "indicators": indicators}

    # Google Trends
    if case_id in GOOGLE_TRENDS_MAP:
        cfg = GOOGLE_TRENDS_MAP[case_id]
        df, meta = enh.fetch_google_trends_proxy(
            keywords=cfg.get("keywords"),
            start_year=int(start_date[:4]),
            end_year=int(end_date[:4]),
            cache_path=cache_path,
        )
        df = df.rename(columns={"interest": "value"}) if "interest" in df.columns else df
        df = _filter_date_range(df, start_date, end_date)
        return df, meta

    # OpenAlex
    if case_id in OPENALEX_MAP:
        cfg = OPENALEX_MAP[case_id]
        df, meta = enh.fetch_openalex_citations(
            concept_id=cfg.get("concept_id"),
            start_year=int(start_date[:4]),
            end_year=int(end_date[:4]),
            cache_path=cache_path,
        )
        if "cited_by_count" in df.columns:
            df = df.rename(columns={"cited_by_count": "value"})
        elif "works_count" in df.columns:
            df = df.rename(columns={"works_count": "value"})
        df = _filter_date_range(df, start_date, end_date)
        return df, meta

    return None, {"source": "none", "case": case_id}
