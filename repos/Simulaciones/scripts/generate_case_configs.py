#!/usr/bin/env python3
"""
generate_case_configs.py — Genera case_config.json amplificados y validate.py slim
para todos los 28 casos que aún no usan case_runner.

Ejecutar desde repos/Simulaciones/:
  python3 scripts/generate_case_configs.py
"""
import json
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ═══════════════════════════════════════════════════════════════════════
# Definición de TODOS los 28 casos (extraídos de cada validate.py)
# ═══════════════════════════════════════════════════════════════════════

CASES = {
    "01_caso_clima": {
        "case_name": "Clima Regional (CONUS)",
        "ode_model": "mean_reversion",
        "ode_key": "tbar",
        "series_key": "tbar",
        "log_transform": False,
        "loe": 5,
        "data": {"csv": "data/conus_monthly.csv", "date_col": "date",
                 "value_col": "tavg",
                 "driver_cols": ["co2", "tsi", "ohc"]},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2010-01-01",
                  "real_start": "1990-01-01", "real_end": "2024-12-31",
                  "real_split": "2011-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.05,
            "forcing": {"type": "linear_cycle", "base": 0.0, "slope": 0.005,
                        "cycle_amp": 0.3, "cycle_period": 12, "noise_std": 0.03},
            "true_params": {"ode_alpha": 0.04, "ode_beta": 0.015, "ode_noise": 0.03}
        },
        "thresholds": {"corr_threshold": 0.7, "persistence_window": 12},
        "topology": {"enabled": True, "type": "small_world",
                     "params": {"k": 4, "p": 0.1}, "feedback_strength": 0.05},
        "extra_ode_params": {"seasonal_period": 12, "ode_alpha": 0.006, "ode_beta": 0.1},
        # Custom: data.py needs load_real_data (desestacionalización), make_synthetic
        "_needs_data_py": True,
    },
    "02_caso_conciencia": {
        "case_name": "Conciencia Colectiva",
        "ode_model": "logistic_forced",
        "ode_key": "c",
        "series_key": "c",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["suicide_rate", "tertiary_enrollment"]},
        "dates": {"synthetic_start": "2004-01-01", "synthetic_end": "2023-12-01",
                  "synthetic_split": "2015-01-01",
                  "real_start": "2004-01-01", "real_end": "2023-12-01",
                  "real_split": "2015-01-01"},
        "synthetic": {
            "freq": "YS", "measurement_noise": 0.03,
            "forcing": {"type": "logistic", "base": 0.0, "amplitude": 3.0,
                        "rate": 0.15, "cycle_amp": 0.1, "cycle_period": 10,
                        "noise_std": 0.02},
            "true_params": {"ode_alpha": 0.10, "ode_beta": 0.04, "ode_noise": 0.02,
                            "forcing_scale": 1.0}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 6},
        "extra_ode_params": {"ode_alpha": 0.08, "ode_beta": 0.03, "ode_noise": 0.03},
        "_needs_data_py": True,
    },
    "03_caso_contaminacion": {
        "case_name": "Contaminación PM2.5",
        "ode_model": "mean_reversion",
        "ode_key": "p",
        "series_key": "p",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "pm25",
                 "driver_cols": ["gdp_growth", "pop_growth"]},
        "dates": {"synthetic_start": "1980-01-01", "synthetic_end": "2019-01-01",
                  "synthetic_split": "2000-01-01",
                  "real_start": "1990-01-01", "real_end": "2022-01-01",
                  "real_split": "2010-01-01"},
        "synthetic": {
            "freq": "YS", "measurement_noise": 0.01,
            "forcing": {"type": "linear_cycle", "base": 0.0, "slope": 0.05,
                        "cycle_amp": 0.3, "cycle_period": 20, "noise_std": 0.05},
            "true_params": {"ode_alpha": 0.40, "ode_beta": 0.50, "ode_noise": 0.01}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.10, "ode_beta": 0.05},
        "_needs_data_py": True,
    },
    "04_caso_energia": {
        "case_name": "Energía (Consumo Per Cápita)",
        "ode_model": "mean_reversion",
        "ode_key": "e",
        "series_key": "e",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["urban_pct", "industry_pct"]},
        "dates": {"synthetic_start": "1980-01-01", "synthetic_end": "2019-01-01",
                  "synthetic_split": "2000-01-01",
                  "real_start": "1990-01-01", "real_end": "2023-01-01",
                  "real_split": "2010-01-01"},
        "synthetic": {
            "freq": "YS", "measurement_noise": 0.01,
            "forcing": {"type": "linear_cycle", "base": 0.0, "slope": 0.05,
                        "cycle_amp": 0.2, "cycle_period": 20, "noise_std": 0.03},
            "true_params": {"ode_alpha": 0.40, "ode_beta": 0.80, "ode_noise": 0.01,
                            "forcing_scale": 1.0}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.15, "ode_beta": 0.08},
        "_needs_data_py": True,
    },
    "05_caso_epidemiologia": {
        "case_name": "Epidemiología (COVID-19 Global)",
        "ode_model": "mean_reversion",
        "ode_key": "incidence",
        "series_key": "incidence",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["log_deaths", "vaccinated"]},
        "dates": {"synthetic_start": "2010-01-03", "synthetic_end": "2020-12-27",
                  "synthetic_split": "2017-01-01",
                  "real_start": "2020-03-01", "real_end": "2023-12-31",
                  "real_split": "2022-01-01"},
        "synthetic": {
            "freq": "W", "measurement_noise": 0.01,
            "forcing": {"type": "linear_cycle", "base": 0.0, "slope": 0.01,
                        "cycle_amp": 0.5, "cycle_period": 52, "noise_std": 0.05},
            "true_params": {"ode_alpha": 0.35, "ode_beta": 0.50, "ode_noise": 0.01,
                            "forcing_scale": 1.0}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 8},
        "extra_ode_params": {"ode_alpha": 0.30, "ode_beta": 0.15},
        "_needs_data_py": True,
    },
    "06_caso_falsacion_exogeneidad": {
        "case_name": "Falsación: Exogeneidad",
        "ode_model": "random_walk",
        "ode_key": "incidence",
        "series_key": "incidence",
        "log_transform": False,
        "loe": 1,
        "is_falsification": True,
        "data": {"csv": "data/memetic.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["unrelated_driver"]},
        "dates": {"synthetic_start": "2020-01-01", "synthetic_end": "2024-01-01",
                  "synthetic_split": "2022-01-01",
                  "real_start": "2020-01-01", "real_end": "2024-01-01",
                  "real_split": "2022-01-01"},
        "thresholds": {"corr_threshold": 0.7, "persistence_window": 6},
        "extra_ode_params": {},
        "_needs_data_py": True,
        "_falsification": True,
    },
    "07_caso_falsacion_no_estacionariedad": {
        "case_name": "Falsación: No-Estacionariedad",
        "ode_model": "random_walk",
        "ode_key": "incidence",
        "series_key": "incidence",
        "log_transform": False,
        "loe": 1,
        "is_falsification": True,
        "data": {"csv": "data/crypto.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["spurious_trend"]},
        "dates": {"synthetic_start": "2020-01-01", "synthetic_end": "2024-01-01",
                  "synthetic_split": "2022-01-01",
                  "real_start": "2020-01-01", "real_end": "2024-01-01",
                  "real_split": "2022-01-01"},
        "thresholds": {"corr_threshold": 0.7, "persistence_window": 6},
        "extra_ode_params": {},
        "_needs_data_py": True,
        "_falsification": True,
    },
    "08_caso_falsacion_observabilidad": {
        "case_name": "Falsación: Observabilidad Escasa",
        "ode_model": "constant",
        "ode_key": "incidence",
        "series_key": "incidence",
        "log_transform": False,
        "loe": 1,
        "is_falsification": True,
        "data": {"csv": "data/sparse_happiness.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["insufficient_driver"]},
        "dates": {"synthetic_start": "2005-01-01", "synthetic_end": "2023-01-01",
                  "synthetic_split": "2015-01-01",
                  "real_start": "2005-01-01", "real_end": "2023-01-01",
                  "real_split": "2015-01-01"},
        "thresholds": {"corr_threshold": 0.7, "persistence_window": 3},
        "extra_ode_params": {},
        "_needs_data_py": True,
        "_falsification": True,
    },
    "09_caso_finanzas": {
        "case_name": "Finanzas (SPY)",
        "ode_model": "mean_reversion",
        "ode_key": "x",
        "series_key": "x",
        "log_transform": False,
        "loe": 5,
        "data": {"csv": "data/spy_monthly.csv", "date_col": "date",
                 "value_col": "price",
                 "driver_cols": ["vix", "fedfunds", "inflation", "credit_spread", "volume"]},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2010-01-01",
                  "real_start": "1990-01-01", "real_end": "2024-12-31",
                  "real_split": "2011-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.08,
            "forcing": {"type": "linear_cycle", "base": 4.0, "slope": 0.005,
                        "cycle_amp": 0.3, "cycle_period": 48, "noise_std": 0.05},
            "true_params": {"ode_alpha": 0.15, "ode_beta": 0.50, "ode_noise": 0.05,
                            "forcing_scale": 1.0}
        },
        "thresholds": {"corr_threshold": 0.7, "persistence_window": 12},
        "topology": {"enabled": True, "type": "small_world",
                     "params": {"k": 4, "p": 0.1}, "feedback_strength": 0.05},
        "extra_ode_params": {},
        "_needs_data_py": True,
    },
    "10_caso_justicia": {
        "case_name": "Justicia Algorítmica",
        "ode_model": "mean_reversion",
        "ode_key": "j",
        "series_key": "j",
        "log_transform": False,
        "loe": 5,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["gdp_pc", "unemployment"]},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1996-01-01", "real_end": "2023-01-01",
                  "real_split": "2012-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.03,
            "forcing": {"type": "linear_cycle", "base": -0.1, "slope": 0.003,
                        "cycle_amp": 0.15, "cycle_period": 48, "noise_std": 0.02},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 0.50, "ode_noise": 0.02,
                            "forcing_scale": 1.0}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "topology": {"enabled": True, "type": "small_world",
                     "params": {"k": 4, "p": 0.1}, "feedback_strength": 0.05},
        "extra_ode_params": {},
        "_needs_data_py": True,
    },
    "12_caso_paradigmas": {
        "case_name": "Paradigmas Científicos (R&D)",
        "ode_model": "mean_reversion",
        "ode_key": "j",
        "series_key": "j",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["journal_articles", "patent_residents"]},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1996-01-01", "real_end": "2022-01-01",
                  "real_split": "2012-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.04,
            "forcing": {"type": "linear_cycle", "base": 2.0, "slope": 0.003,
                        "cycle_amp": 0.15, "cycle_period": 144, "noise_std": 0.02},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 0.50, "ode_noise": 0.02}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.05, "ode_beta": 0.50},
    },
    "13_caso_politicas_estrategicas": {
        "case_name": "Políticas Estratégicas (Bass Diffusion + Inertia)",
        "ode_model": "institutional_inertia",
        "ode_key": "s",
        "series_key": "s",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "1990-01-01", "synthetic_end": "2020-01-01",
                  "synthetic_split": "2010-01-01",
                  "real_start": "1980-01-01", "real_end": "2022-01-01",
                  "real_split": "2010-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.03,
            "forcing": {"type": "linear_cycle", "base": 0.5, "slope": 0.005,
                        "cycle_amp": 0.2, "cycle_period": 48, "noise_std": 0.03},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 0.3, "ode_gamma": 0.1,
                            "ode_noise": 0.02}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 24},
        "extra_ode_params": {
            "ode_alpha": 0.05, "ode_beta": 0.3, "ode_gamma": 0.1,
            "macro_coupling": 0.15
        },
    },
    "14_caso_postverdad": {
        "case_name": "Postverdad (SIS Infodemic)",
        "ode_model": "sis_contagion",
        "ode_key": "pv",
        "series_key": "pv",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["mobile_subs", "literacy"]},
        "dates": {"synthetic_start": "2015-01-01", "synthetic_end": "2023-01-01",
                  "synthetic_split": "2020-01-01",
                  "real_start": "2005-01-01", "real_end": "2023-01-01",
                  "real_split": "2016-01-01"},
        "synthetic": {
            "freq": "W", "measurement_noise": 0.02,
            "forcing": {"type": "linear_cycle", "base": 0.0, "slope": 0.005,
                        "cycle_amp": 0.2, "cycle_period": 52, "noise_std": 0.03},
            "true_params": {"ode_beta": 0.3, "ode_gamma": 0.15, "ode_noise": 0.02}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 12},
        "extra_ode_params": {"ode_beta": 0.3, "ode_gamma": 0.15},
    },
    "15_caso_wikipedia": {
        "case_name": "Wikipedia (Conocimiento Colectivo)",
        "ode_model": "mean_reversion",
        "ode_key": "w",
        "series_key": "w",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/wiki_climate.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2005-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2014-01-01",
                  "real_start": "2015-07-01", "real_end": "2024-12-01",
                  "real_split": "2021-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.04,
            "forcing": {"type": "linear_cycle", "base": 13.0, "slope": 0.002,
                        "cycle_amp": 0.3, "cycle_period": 12, "noise_std": 0.05},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 0.50, "ode_noise": 0.04}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 6},
        "extra_ode_params": {"ode_alpha": 0.05, "ode_beta": 0.50},
    },
    "16_caso_deforestacion": {
        "case_name": "Deforestación Global (von Thünen Frontier)",
        "ode_model": "accumulation_decay",
        "ode_key": "d",
        "series_key": "d",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/wb_deforestation.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "1990-01-01", "synthetic_end": "2022-01-01",
                  "synthetic_split": "2010-01-01",
                  "real_start": "1990-01-01", "real_end": "2022-01-01",
                  "real_split": "2010-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.12,
            "forcing": {"type": "exponential", "base": 0.025, "rate": 0.005,
                        "noise_std": 0.04},
            "true_params": {"ode_alpha": 0.06, "ode_beta": 0.008, "ode_noise": 0.04,
                            "ode_inflow": 0.06, "ode_decay": 0.008}
        },
        "thresholds": {"corr_threshold": 0.65, "persistence_window": 5},
        "extra_ode_params": {"ode_inflow": 0.06, "ode_decay": 0.008,
                             "forcing_scale": 0.10, "macro_coupling": 0.25},
        "_needs_data_py": True,
    },
    "17_caso_oceanos": {
        "case_name": "Océanos (OHC proxy)",
        "ode_model": "mean_reversion",
        "ode_key": "e",
        "series_key": "e",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1990-01-01", "real_end": "2023-01-01",
                  "real_split": "2010-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.3,
            "forcing": {"type": "linear_cycle", "base": 60.0, "slope": 0.03,
                        "cycle_amp": 1.5, "cycle_period": 48, "noise_std": 0.3},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 0.50, "ode_noise": 0.2}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.05, "ode_beta": 0.50},
    },
    "18_caso_urbanizacion": {
        "case_name": "Urbanización Global",
        "ode_model": "mean_reversion",
        "ode_key": "u",
        "series_key": "u",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/wb_urbanization.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1960-01-01", "real_end": "2022-01-01",
                  "real_split": "2000-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.15,
            "forcing": {"type": "logistic", "base": 34.0, "amplitude": 23.0,
                        "rate": 0.02, "noise_std": 0.2},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 0.50, "ode_noise": 0.15}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.05, "ode_beta": 0.50},
    },
    "19_caso_acidificacion_oceanica": {
        "case_name": "Acidificación Oceánica",
        "ode_model": "mean_reversion",
        "ode_key": "ac",
        "series_key": "ac",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1990-01-01", "real_end": "2020-01-01",
                  "real_split": "2010-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.2,
            "forcing": {"type": "linear_cycle", "base": 85.0, "slope": -0.03,
                        "cycle_amp": 2.5, "cycle_period": 24, "noise_std": 0.5},
            "true_params": {"ode_alpha": 0.10, "ode_beta": 0.50, "ode_noise": 0.2}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.10, "ode_beta": 0.50},
    },
    "20_caso_kessler": {
        "case_name": "Kessler (Debris Orbital)",
        "ode_model": "mean_reversion",
        "ode_key": "k",
        "series_key": "k",
        "log_transform": True,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1980-01-01", "real_end": "2024-01-01",
                  "real_split": "2010-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.20,
            "forcing": {"type": "linear_cycle", "base": 4.0, "slope": 0.025,
                        "cycle_amp": 0.4, "cycle_period": 120, "noise_std": 0.25},
            "true_params": {"ode_alpha": 0.15, "ode_beta": 0.50, "ode_noise": 0.20}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.15, "ode_beta": 0.50},
    },
    "21_caso_salinizacion": {
        "case_name": "Salinización de Suelos (Richards Bilineal)",
        "ode_model": "bilinear",
        "ode_key": "sl",
        "series_key": "sl",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/wb_arable_land.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1961-01-01", "real_end": "2022-01-01",
                  "real_split": "2005-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.08,
            "forcing": {"type": "logistic", "base": 0.3, "amplitude": 1.8,
                        "rate": 0.012, "cycle_amp": 0.2, "cycle_period": 48,
                        "noise_std": 0.12},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 1.0, "ode_gamma": 0.02,
                            "ode_noise": 0.08}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.05, "ode_beta": 1.0, "ode_gamma": 0.02},
        "_needs_data_py": True,
    },
    "22_caso_fosforo": {
        "case_name": "Ciclo del Fósforo (Carpenter Biogeoquímico)",
        "ode_model": "bilinear",
        "ode_key": "ph",
        "series_key": "ph",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/wb_fertilizer_consumption.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1966-01-01", "real_end": "2022-01-01",
                  "real_split": "2005-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.10,
            "forcing": {"type": "logistic", "base": 0.5, "amplitude": 2.0,
                        "rate": 0.015, "cycle_amp": 0.3, "cycle_period": 48,
                        "noise_std": 0.15},
            "true_params": {"ode_alpha": 0.07, "ode_beta": 1.0, "ode_gamma": 0.015,
                            "ode_noise": 0.10}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.07, "ode_beta": 0.50, "ode_gamma": 0.015},
        "_needs_data_py": True,
    },
    "23_caso_erosion_dialectica": {
        "case_name": "Erosión Dialéctica (Abrams-Strogatz Prestige)",
        "ode_model": "prestige_competition",
        "ode_key": "ed",
        "series_key": "ed",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "2005-01-01", "real_end": "2023-12-01",
                  "real_split": "2016-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.08,
            "forcing": {"type": "logistic", "base": 0.3, "amplitude": 1.8,
                        "rate": 0.012, "cycle_amp": 0.2, "cycle_period": 48,
                        "noise_std": 0.12},
            "true_params": {"ode_alpha": 0.03, "ode_beta": 1.0,
                            "ode_prestige": 0.008, "ode_noise": 0.08}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.03, "ode_beta": 1.0,
                             "ode_prestige": 0.008, "ode_amplification": 0.3},
        "_needs_data_py": True,
    },
    "24_caso_microplasticos": {
        "case_name": "Microplásticos Oceánicos (Jambeck Accumulation-Decay)",
        "ode_model": "accumulation_decay",
        "ode_key": "mp",
        "series_key": "mp",
        "log_transform": True,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1980-01-01", "real_end": "2020-12-01",
                  "real_split": "2005-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.08,
            "forcing": {"type": "logistic", "base": 0.2, "amplitude": 2.5,
                        "rate": 0.010, "cycle_amp": 0.15, "cycle_period": 48,
                        "noise_std": 0.10},
            "true_params": {"ode_alpha": 0.09, "ode_beta": 0.005, "ode_noise": 0.08}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.09, "ode_beta": 0.005},
        "_needs_data_py": True,
    },
    "25_caso_acuiferos": {
        "case_name": "Depleción de Acuíferos (Darcy-Theis)",
        "ode_model": "aquifer_darcy",
        "ode_key": "aq",
        "series_key": "aq",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["precip", "extraction_usgs", "withdrawal"]},
        "dates": {"synthetic_start": "1980-01-01", "synthetic_end": "2020-12-01",
                  "synthetic_split": "2002-01-01",
                  "real_start": "1980-01-01", "real_end": "2020-12-01",
                  "real_split": "2002-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.04,
            "forcing": {"type": "exponential", "base": 0.008, "rate": 0.003,
                        "noise_std": 0.02},
            "true_params": {"ode_alpha": 0.08, "ode_beta": 0.03,
                            "ode_extraction": 0.01, "ode_noise": 0.02}
        },
        "thresholds": {"corr_threshold": 0.60, "persistence_window": 12},
        "extra_ode_params": {"ode_extraction": 0.01, "forcing_scale": 0.12,
                             "macro_coupling": 0.28},
        "_needs_data_py": True,
    },
    "26_caso_starlink": {
        "case_name": "Constelaciones Satelitales Starlink (Saturation Growth)",
        "ode_model": "saturation_growth",
        "ode_key": "st",
        "series_key": "st",
        "log_transform": True,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "2019-01-01", "real_end": "2024-06-01",
                  "real_split": "2022-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.08,
            "forcing": {"type": "logistic", "base": 0.1, "amplitude": 2.5,
                        "rate": 0.025, "cycle_amp": 0.2, "cycle_period": 12,
                        "noise_std": 0.12},
            "true_params": {"ode_alpha": 0.18, "ode_beta": 1.0,
                            "ode_saturation": 0.002, "ode_noise": 0.08}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.18, "ode_beta": 1.0,
                             "ode_saturation": 0.002},
        "_needs_data_py": True,
    },
    "27_caso_riesgo_biologico": {
        "case_name": "Riesgo Biológico Global (Woolhouse Bilineal)",
        "ode_model": "bilinear",
        "ode_key": "b",
        "series_key": "b",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "2000-01-01", "real_end": "2024-01-01",
                  "real_split": "2016-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.08,
            "forcing": {"type": "logistic", "base": 0.3, "amplitude": 1.5,
                        "rate": 0.015, "cycle_amp": 0.2, "cycle_period": 48,
                        "noise_std": 0.12},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 1.0, "ode_gamma": 0.02,
                            "ode_noise": 0.08}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.05, "ode_beta": 1.0, "ode_gamma": 0.02},
        "_needs_data_py": True,
    },
    "28_caso_fuga_cerebros": {
        "case_name": "Fuga de Cerebros Global (Docquier-Rapoport)",
        "ode_model": "brain_drain",
        "ode_key": "fc",
        "series_key": "fc",
        "log_transform": False,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value",
                 "driver_cols": ["researchers", "enrollment", "remittances",
                                 "gdp_pc", "net_migration"]},
        "dates": {"synthetic_start": "1980-01-01", "synthetic_end": "2022-01-01",
                  "synthetic_split": "2005-01-01",
                  "real_start": "1980-01-01", "real_end": "2022-01-01",
                  "real_split": "2005-01-01"},
        "synthetic": {
            "freq": "YS", "measurement_noise": 0.03,
            "forcing": {"type": "exponential", "base": 0.01, "rate": 0.02,
                        "noise_std": 0.02},
            "true_params": {"ode_alpha": 0.06, "ode_beta": 0.02,
                            "ode_gamma_forcing": 0.08, "ode_delta_drain": 0.015,
                            "ode_drain_threshold": 1.5, "ode_noise": 0.008}
        },
        "thresholds": {"corr_threshold": 0.6, "persistence_window": 10},
        "extra_ode_params": {
            "ode_alpha": 0.06, "ode_beta": 0.02,
            "ode_gamma_forcing": 0.08, "ode_delta_drain": 0.015,
            "ode_drain_threshold": 1.5
        },
        "_needs_data_py": True,
    },
    "29_caso_iot": {
        "case_name": "Ecosistema IoT Global (Bass-Metcalfe Bilineal)",
        "ode_model": "bilinear",
        "ode_key": "io",
        "series_key": "io",
        "log_transform": True,
        "loe": 3,
        "data": {"csv": "data/dataset.csv", "date_col": "date",
                 "value_col": "value", "driver_cols": []},
        "dates": {"synthetic_start": "2000-01-01", "synthetic_end": "2019-12-01",
                  "synthetic_split": "2012-01-01",
                  "real_start": "1985-01-01", "real_end": "2022-01-01",
                  "real_split": "2008-01-01"},
        "synthetic": {
            "freq": "MS", "measurement_noise": 0.08,
            "forcing": {"type": "logistic", "base": 0.1, "amplitude": 2.5,
                        "rate": 0.012, "cycle_amp": 0.15, "cycle_period": 48,
                        "noise_std": 0.10},
            "true_params": {"ode_alpha": 0.05, "ode_beta": 1.0, "ode_gamma": 0.08,
                            "ode_noise": 0.08}
        },
        "thresholds": {"corr_threshold": 0.5, "persistence_window": 5},
        "extra_ode_params": {"ode_alpha": 0.05, "ode_beta": 1.0, "ode_gamma": 0.08},
        "_needs_data_py": True,
    },
}


def merge_existing_config(case_dir, new_cfg):
    """Merge execution/abm/calibration from existing case_config.json."""
    existing_path = os.path.join(case_dir, "case_config.json")
    if not os.path.exists(existing_path):
        return
    with open(existing_path, "r") as f:
        old = json.load(f)
    # Preserve execution, abm, calibration if they exist in old
    for section in ("execution", "abm", "calibration"):
        if section in old and section not in new_cfg:
            new_cfg[section] = old[section]


def build_config_json(case_id, spec):
    """Build the amplified case_config.json dict."""
    cfg = {
        "case_name": spec["case_name"],
        "ode_model": spec["ode_model"],
        "ode_key": spec["ode_key"],
        "series_key": spec["series_key"],
        "log_transform": spec.get("log_transform", False),
        "loe": spec.get("loe", 3),
    }
    if spec.get("is_falsification"):
        cfg["is_falsification"] = True
        cfg["ode_calibration"] = False
        cfg["abm_calibration"] = False

    cfg["data"] = spec["data"]
    cfg["dates"] = spec["dates"]

    if "synthetic" in spec:
        cfg["synthetic"] = spec["synthetic"]

    cfg["thresholds"] = spec.get("thresholds", {"corr_threshold": 0.5, "persistence_window": 5})

    if "topology" in spec:
        cfg["topology"] = spec["topology"]

    # Merge existing execution/abm/calibration
    case_dir = os.path.join(BASE, case_id)
    existing_path = os.path.join(case_dir, "case_config.json")
    if os.path.exists(existing_path):
        with open(existing_path, "r") as f:
            old = json.load(f)
        for section in ("execution", "abm", "calibration"):
            if section in old:
                cfg[section] = old[section]

    # Defaults if not from existing
    if "execution" not in cfg:
        cfg["execution"] = {
            "grid_size": 25, "n_perm": 9999, "n_boot": 5000,
            "n_refine": 200000, "n_runs": 30
        }
    if "abm" not in cfg:
        cfg["abm"] = {
            "diffusion": 0.2, "noise": 0.002,
            "heterogeneity_strength": 0.25, "init_range": 0.5
        }
    if "calibration" not in cfg:
        cfg["calibration"] = {
            "param_grid": {
                "forcing_scale": [0.001, 0.005, 0.01, 0.05, 0.1, 0.2, 0.5, 0.99],
                "macro_coupling": [0.10, 0.15, 0.25, 0.35, 0.45, 0.55],
                "damping": [0.0, 0.1, 0.2, 0.4, 0.6, 0.8]
            }
        }

    cfg["extra_ode_params"] = spec.get("extra_ode_params", {})

    return cfg


# Cases that are falsification (special validate.py structure)
FALSIFICATION_CASES = {"06_caso_falsacion_exogeneidad",
                       "07_caso_falsacion_no_estacionariedad",
                       "08_caso_falsacion_observabilidad"}

# Cases where data.py already has load_real_data + make_synthetic
DATA_PY_READY = {"12_caso_paradigmas", "13_caso_politicas_estrategicas",
                 "14_caso_postverdad", "15_caso_wikipedia",
                 "17_caso_oceanos", "18_caso_urbanizacion",
                 "19_caso_acidificacion_oceanica", "20_caso_kessler"}


def build_validate_py(case_id, spec):
    """Generate slim validate.py content."""
    name = spec["case_name"]
    model = spec["ode_model"]

    if case_id in FALSIFICATION_CASES:
        # Falsification cases use the same slim validate.py but case_runner
        # handles them differently via is_falsification flag
        pass  # Fall through to normal generation

    return f'''"""validate.py — {name}

Usa case_runner.py centralizado + case_config.json declarativo.
ODE: {model}.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from case_runner import run_case

if __name__ == "__main__":
    run_case(os.path.dirname(os.path.abspath(__file__)))
'''


def main():
    written = 0
    skipped_validate = 0
    for case_id, spec in sorted(CASES.items()):
        case_dir = os.path.join(BASE, case_id)
        if not os.path.isdir(case_dir):
            print(f"  SKIP: {case_id} no existe")
            continue

        # 1. Write case_config.json
        cfg = build_config_json(case_id, spec)
        cfg_path = os.path.join(case_dir, "case_config.json")
        with open(cfg_path, "w", encoding="utf-8") as f:
            json.dump(cfg, f, indent=2, ensure_ascii=False)
        print(f"  ✅ {case_id}/case_config.json")

        # 2. Write validate.py (skip falsification cases)
        val_content = build_validate_py(case_id, spec)

        val_path = os.path.join(case_dir, "src", "validate.py")
        with open(val_path, "w", encoding="utf-8") as f:
            f.write(val_content)
        print(f"  ✅ {case_id}/src/validate.py (slim)")
        written += 1

    print(f"\n{'='*60}")
    print(f"Escritos: {written} validate.py slim + {written} case_config.json")
    print(f"\nPendiente: mover load_real_data/make_synthetic de validate.py a data.py")
    print(f"para los casos que las definen inline (Grupo B).")


if __name__ == "__main__":
    main()
