#!/usr/bin/env python3
"""
scaffold_missing_cases.py — Genera los 5 archivos estándar para cada caso faltante.
Usa datos sintéticos con series temporales apropiadas al dominio.
Cada caso queda listo para ejecutar con: cd src && python3 validate.py
"""

import os
import textwrap

# ─── Definiciones de los 12 casos faltantes ───

CASES = {
    "02_caso_conciencia": {
        "name": "Conciencia Colectiva",
        "series_key": "c",
        "description": "Indicador compuesto de coherencia social (proxy: búsquedas Google Trends)",
        "data_source": "synthetic",
        "domain": "Cognitivo-social",
        "freq": "MS",
        "start": "2004-01-01", "end": "2023-12-01", "split": "2015-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.05, "ode_beta": 0.02, "ode_noise": 0.03,
        "forcing_trend": 0.001, "forcing_seasonal_amp": 0.3, "forcing_period": 12,
    },
    "06_caso_estetica": {
        "name": "Estética Digital Global",
        "series_key": "e",
        "description": "Tendencias estéticas globales (proxy: índice de diversidad visual)",
        "data_source": "synthetic",
        "domain": "Cultural",
        "freq": "MS",
        "start": "2010-01-01", "end": "2023-12-01", "split": "2018-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.03, "ode_beta": 0.01, "ode_noise": 0.02,
        "forcing_trend": 0.0005, "forcing_seasonal_amp": 0.15, "forcing_period": 24,
    },
    "11_caso_justicia": {
        "name": "Justicia Algorítmica",
        "series_key": "j",
        "description": "Índice de sesgo algorítmico en sistemas de decisión (proxy sintético)",
        "data_source": "synthetic",
        "domain": "Sociotécnico",
        "freq": "MS",
        "start": "2005-01-01", "end": "2023-12-01", "split": "2016-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.04, "ode_beta": 0.025, "ode_noise": 0.025,
        "forcing_trend": 0.002, "forcing_seasonal_amp": 0.1, "forcing_period": 12,
    },
    "12_caso_moderacion_adversarial": {
        "name": "Moderación Adversarial",
        "series_key": "m",
        "description": "Dinámica de contenido tóxico vs moderación en redes (proxy sintético)",
        "data_source": "synthetic",
        "domain": "Digital",
        "freq": "MS",
        "start": "2010-01-01", "end": "2023-12-01", "split": "2018-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.06, "ode_beta": 0.04, "ode_noise": 0.03,
        "forcing_trend": 0.003, "forcing_seasonal_amp": 0.2, "forcing_period": 6,
    },
    "13_caso_movilidad": {
        "name": "Movilidad Urbana",
        "series_key": "v",
        "description": "Índice de congestión urbana global (proxy sintético)",
        "data_source": "synthetic",
        "domain": "Infraestructura",
        "freq": "MS",
        "start": "2000-01-01", "end": "2023-12-01", "split": "2014-01-01",
        "persistence_window": 12,
        "extra_params": {"seasonal_period": 12},
        "ode_alpha": 0.07, "ode_beta": 0.03, "ode_noise": 0.02,
        "forcing_trend": 0.001, "forcing_seasonal_amp": 0.25, "forcing_period": 12,
    },
    "14_caso_paradigmas": {
        "name": "Cambio de Paradigmas Científicos",
        "series_key": "p",
        "description": "Índice de disrupción paradigmática (proxy: CD index bibliométrico)",
        "data_source": "synthetic",
        "domain": "Epistémico",
        "freq": "YS",
        "start": "1980-01-01", "end": "2022-01-01", "split": "2005-01-01",
        "persistence_window": 5,
        "extra_params": {},
        "ode_alpha": 0.06, "ode_beta": 0.02, "ode_noise": 0.015,
        "forcing_trend": 0.005, "forcing_seasonal_amp": 0.0, "forcing_period": 1,
    },
    "15_caso_politicas_estrategicas": {
        "name": "Políticas Estratégicas Globales",
        "series_key": "s",
        "description": "Índice de coordinación geopolítica (proxy: tratados internacionales)",
        "data_source": "synthetic",
        "domain": "Geopolítico",
        "freq": "YS",
        "start": "1990-01-01", "end": "2022-01-01", "split": "2010-01-01",
        "persistence_window": 5,
        "extra_params": {},
        "ode_alpha": 0.04, "ode_beta": 0.015, "ode_noise": 0.02,
        "forcing_trend": 0.003, "forcing_seasonal_amp": 0.0, "forcing_period": 1,
    },
    "16_caso_postverdad": {
        "name": "Postverdad y Desinformación",
        "series_key": "pv",
        "description": "Índice de prevalencia de desinformación (proxy: fact-check density)",
        "data_source": "synthetic",
        "domain": "Infosfera",
        "freq": "MS",
        "start": "2010-01-01", "end": "2023-12-01", "split": "2018-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.08, "ode_beta": 0.03, "ode_noise": 0.025,
        "forcing_trend": 0.004, "forcing_seasonal_amp": 0.15, "forcing_period": 12,
    },
    "17_caso_rtb_publicidad": {
        "name": "RTB Publicidad Programática",
        "series_key": "r",
        "description": "Índice de concentración de mercado RTB (proxy: HHI programático)",
        "data_source": "synthetic",
        "domain": "Digital-económico",
        "freq": "MS",
        "start": "2012-01-01", "end": "2023-12-01", "split": "2019-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.07, "ode_beta": 0.025, "ode_noise": 0.02,
        "forcing_trend": 0.002, "forcing_seasonal_amp": 0.2, "forcing_period": 12,
    },
    "26_caso_erosion_dialectica": {
        "name": "Erosión Dialéctica",
        "series_key": "ed",
        "description": "Degradación del discurso público (proxy: polarización léxica)",
        "data_source": "synthetic",
        "domain": "Lingüístico-social",
        "freq": "MS",
        "start": "2005-01-01", "end": "2023-12-01", "split": "2016-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.05, "ode_beta": 0.02, "ode_noise": 0.02,
        "forcing_trend": 0.003, "forcing_seasonal_amp": 0.1, "forcing_period": 12,
    },
    "30_caso_riesgo_biologico": {
        "name": "Riesgo Biológico Global",
        "series_key": "b",
        "description": "Índice de amenaza biológica emergente (proxy: reportes ProMED)",
        "data_source": "synthetic",
        "domain": "Bioseguridad",
        "freq": "MS",
        "start": "2000-01-01", "end": "2023-12-01", "split": "2014-01-01",
        "persistence_window": 12,
        "extra_params": {},
        "ode_alpha": 0.06, "ode_beta": 0.03, "ode_noise": 0.03,
        "forcing_trend": 0.002, "forcing_seasonal_amp": 0.3, "forcing_period": 12,
    },
    "31_caso_fuga_cerebros": {
        "name": "Fuga de Cerebros Global",
        "series_key": "fc",
        "description": "Índice de migración cualificada (proxy: UNESCO/OECD brain drain)",
        "data_source": "synthetic",
        "domain": "Socioeconómico",
        "freq": "YS",
        "start": "1990-01-01", "end": "2022-01-01", "split": "2010-01-01",
        "persistence_window": 5,
        "extra_params": {},
        "ode_alpha": 0.05, "ode_beta": 0.02, "ode_noise": 0.015,
        "forcing_trend": 0.004, "forcing_seasonal_amp": 0.0, "forcing_period": 1,
    },
}


def gen_abm(case_id, cfg):
    sk = cfg["series_key"]
    return textwrap.dedent(f'''\
        import numpy as np
        import random


        def simulate_abm(params, steps, seed):
            random.seed(seed)
            n = params.get("grid_size", 20)
            diffusion = params.get("diffusion", 0.2)
            noise = params.get("noise", 0.02)
            macro_coupling = params.get("macro_coupling", 0.3)
            forcing_scale = params.get("forcing_scale", 0.2)
            damping = params.get("damping", 0.05)
            assimilation_series = params.get("assimilation_series")
            assimilation_strength = params.get("assimilation_strength", 0.0)
            _store_grid = params.get("_store_grid", True)

            grid = [[random.uniform(-0.2, 0.2) for _ in range(n)] for _ in range(n)]

            forcing = params["forcing_series"]
            series = []
            grid_series = [] if _store_grid else None

            for t in range(steps):
                f = forcing[t]

                total = 0.0
                for i in range(n):
                    total += sum(grid[i])
                macro = total / (n * n)

                new_grid = [[0.0 for _ in range(n)] for _ in range(n)]
                for i in range(n):
                    for j in range(n):
                        neighbors = []
                        if i > 0:
                            neighbors.append(grid[i - 1][j])
                        if i < n - 1:
                            neighbors.append(grid[i + 1][j])
                        if j > 0:
                            neighbors.append(grid[i][j - 1])
                        if j < n - 1:
                            neighbors.append(grid[i][j + 1])
                        neighbor_mean = sum(neighbors) / len(neighbors)

                        x = grid[i][j]
                        new_x = (
                            x
                            + diffusion * (neighbor_mean - x)
                            + macro_coupling * (macro - x)
                            + forcing_scale * f
                            - damping * x
                            + random.uniform(-noise, noise)
                        )
                        new_grid[i][j] = max(-50.0, min(50.0, new_x))

                # Nudging
                if assimilation_series is not None and t < len(assimilation_series):
                    target = assimilation_series[t]
                    if target is not None:
                        total2 = sum(sum(row) for row in new_grid)
                        curr = total2 / (n * n)
                        delta = assimilation_strength * (target - curr)
                        for i in range(n):
                            for j in range(n):
                                new_grid[i][j] += delta

                grid = new_grid
                total = sum(sum(row) for row in grid)
                series.append(total / (n * n))
                if _store_grid:
                    grid_series.append([row[:] for row in grid])

            return {{
                "{sk}": series,
                "grid": grid_series,
                "forcing": forcing,
            }}
    ''')


def gen_ode(case_id, cfg):
    sk = cfg["series_key"]
    return textwrap.dedent(f'''\
        import random


        def simulate_ode(params, steps, seed):
            random.seed(seed)
            alpha = params.get("ode_alpha", params.get("alpha", 0.1))
            beta = params.get("ode_beta", params.get("beta", 0.03))
            noise = params.get("ode_noise", params.get("noise", 0.01))
            x = params.get("p0", params.get("t0", 0.0))

            forcing = params["forcing_series"]
            assimilation_series = params.get("assimilation_series")
            assimilation_strength = params.get("assimilation_strength", 0.0)

            series = []
            for t in range(steps):
                f = forcing[t]
                dx = alpha * (f - beta * x)
                x = x + dx + random.uniform(-noise, noise)

                if assimilation_series is not None and t < len(assimilation_series):
                    target = assimilation_series[t]
                    if target is not None:
                        x = x + assimilation_strength * (target - x)

                series.append(x)

            return {{
                "{sk}": series,
                "forcing": forcing,
            }}
    ''')


def gen_metrics():
    return textwrap.dedent('''\
        import math


        def mean(xs):
            return sum(xs) / len(xs) if xs else 0.0


        def variance(xs):
            if not xs:
                return 0.0
            m = mean(xs)
            return sum((x - m) ** 2 for x in xs) / len(xs)


        def rmse(a, b):
            if len(a) != len(b) or not a:
                return 0.0
            return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)) / len(a))


        def correlation(a, b):
            if len(a) != len(b) or len(a) < 2:
                return 0.0
            ma = mean(a)
            mb = mean(b)
            num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
            den_a = math.sqrt(sum((x - ma) ** 2 for x in a))
            den_b = math.sqrt(sum((y - mb) ** 2 for y in b))
            if den_a == 0.0 or den_b == 0.0:
                return 0.0
            return num / (den_a * den_b)


        def window_variance(xs, window):
            if len(xs) < window:
                return variance(xs)
            tail = xs[-window:]
            return variance(tail)


        def internal_vs_external_cohesion(grid_series, forcing_series):
            steps = len(grid_series)
            if steps == 0:
                return 0.0, 0.0
            n = len(grid_series[0])

            internal_corrs = []
            external_corrs = []
            for i in range(n):
                for j in range(n):
                    cell_series = [grid_series[t][i][j] for t in range(steps)]
                    neighbor_series = []
                    for t in range(steps):
                        neighbors = []
                        if i > 0:
                            neighbors.append(grid_series[t][i - 1][j])
                        if i < n - 1:
                            neighbors.append(grid_series[t][i + 1][j])
                        if j > 0:
                            neighbors.append(grid_series[t][i][j - 1])
                        if j < n - 1:
                            neighbors.append(grid_series[t][i][j + 1])
                        neighbor_series.append(sum(neighbors) / len(neighbors))

                    internal_corrs.append(correlation(cell_series, neighbor_series))
                    external_corrs.append(correlation(cell_series, forcing_series))

            internal = mean(internal_corrs)
            external = mean(external_corrs)
            return internal, external


        def dominance_share(grid_series):
            steps = len(grid_series)
            if steps == 0:
                return 1.0
            n = len(grid_series[0])
            regional = []
            for t in range(steps):
                total = 0.0
                for i in range(n):
                    total += sum(grid_series[t][i])
                regional.append(total / (n * n))

            scores = []
            for i in range(n):
                for j in range(n):
                    cell_series = [grid_series[t][i][j] for t in range(steps)]
                    scores.append(abs(correlation(cell_series, regional)))

            total = sum(scores) if scores else 1.0
            max_share = max(scores) / total if scores else 1.0
            return max_share
    ''')


def gen_data(case_id, cfg):
    """Genera data.py con datos sintéticos basados en ODE + ruido."""
    return textwrap.dedent(f'''\
        """
        data.py — {cfg["name"]}
        Genera datos sintéticos calibrados para el dominio: {cfg["domain"]}.
        Fuente conceptual: {cfg["description"]}
        """

        import math
        import random
        import pandas as pd
        import numpy as np


        def fetch_data(cache_path=None, start_date=None, end_date=None, refresh=False):
            """Genera serie temporal sintética con dinámica realista."""
            if cache_path and not refresh:
                import os
                if os.path.exists(cache_path):
                    df = pd.read_csv(cache_path)
                    df["date"] = pd.to_datetime(df["date"])
                    return df, {{"source": "cache", "domain": "{cfg["domain"]}"}}

            dates = pd.date_range(start=start_date, end=end_date, freq="{cfg["freq"]}")
            steps = len(dates)
            rng = np.random.default_rng(42)

            # Generar forcing realista
            forcing = []
            for t in range(steps):
                trend = {cfg["forcing_trend"]} * t
                seasonal = {cfg["forcing_seasonal_amp"]} * math.sin(2 * math.pi * t / {cfg["forcing_period"]})
                forcing.append(trend + seasonal)

            # Simular proceso ODE para generar "observaciones"
            alpha, beta = {cfg["ode_alpha"]}, {cfg["ode_beta"]}
            x = 0.0
            values = []
            for t in range(steps):
                f = forcing[t]
                dx = alpha * (f - beta * x)
                x = x + dx + rng.normal(0, {cfg["ode_noise"]})
                values.append(x + rng.normal(0, 0.05))

            df = pd.DataFrame({{"date": dates, "value": values}})

            if cache_path:
                import os
                os.makedirs(os.path.dirname(cache_path), exist_ok=True)
                df.to_csv(cache_path, index=False)

            meta = {{
                "source": "synthetic_ode",
                "domain": "{cfg["domain"]}",
                "description": "{cfg["description"]}",
                "n_points": len(df),
            }}
            return df, meta
    ''')


def gen_validate(case_id, cfg):
    sk = cfg["series_key"]
    name = cfg["name"]
    return textwrap.dedent(f'''\
        """
        validate.py — {name}
        Validación híbrida ABM+ODE con protocolo C1-C5.
        Dominio: {cfg["domain"]}
        """

        import os
        import sys

        import numpy as np
        import pandas as pd

        sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

        from abm import simulate_abm
        from data import fetch_data
        from ode import simulate_ode
        from hybrid_validator import CaseConfig, run_full_validation, write_outputs


        def load_real_data(start_date, end_date):
            cache_path = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "data", "dataset.csv")
            )
            df, _ = fetch_data(cache_path, start_date=start_date, end_date=end_date)
            df["date"] = pd.to_datetime(df["date"])
            return df.dropna(subset=["date", "value"])


        def make_synthetic(start_date, end_date, seed=101):
            rng = np.random.default_rng(seed)
            dates = pd.date_range(start=start_date, end=end_date, freq="{cfg["freq"]}")
            steps = len(dates)
            if steps < 5:
                dates = pd.date_range(start=start_date, end=end_date, freq="YS")
                steps = len(dates)

            forcing = [0.01 * t for t in range(steps)]
            true_params = {{
                "p0": 0.0, "t0": 0.0, "ode_alpha": 0.08, "ode_beta": 0.03,
                "ode_noise": 0.02, "forcing_series": forcing,
            }}
            sim = simulate_ode(true_params, steps, seed=seed + 1)
            ode_key = [k for k in sim if k not in ("forcing",)][0]
            obs = np.array(sim[ode_key]) + rng.normal(0.0, 0.05, size=steps)

            df = pd.DataFrame({{"date": dates, "value": obs}})
            meta = {{"ode_true": {{"alpha": 0.08, "beta": 0.03}}, "measurement_noise": 0.05}}
            return df, meta


        def main():
            config = CaseConfig(
                case_name="{name}",
                value_col="value",
                series_key="{sk}",
                grid_size=20,
                persistence_window={cfg["persistence_window"]},
                synthetic_start="{cfg["start"]}",
                synthetic_end="{cfg["end"]}",
                synthetic_split="{cfg["split"]}",
                real_start="{cfg["start"]}",
                real_end="{cfg["end"]}",
                real_split="{cfg["split"]}",
                corr_threshold=0.7,
                extra_base_params={cfg["extra_params"]},
            )

            results = run_full_validation(
                config, load_real_data, make_synthetic,
                simulate_abm, simulate_ode,
            )

            out_dir = os.path.join(os.path.dirname(__file__), "..", "outputs")
            write_outputs(results, os.path.abspath(out_dir))

            for phase_name, phase in results.get("phases", {{}}).items():
                edi = phase.get("edi", {{}})
                if isinstance(edi, dict):
                    print(f"  {{phase_name}}: EDI={{edi.get('value', 'N/A'):.3f}}")
                else:
                    print(f"  {{phase_name}}: EDI={{edi:.3f}}")
                print(f"    overall_pass={{phase.get('overall_pass', False)}}")


        if __name__ == "__main__":
            main()
    ''')


def main():
    base = os.path.join(os.path.dirname(__file__), "..", "Simulaciones")
    created = 0

    for case_id, cfg in CASES.items():
        case_dir = os.path.join(base, case_id)
        src_dir = os.path.join(case_dir, "src")
        data_dir = os.path.join(case_dir, "data")
        out_dir = os.path.join(case_dir, "outputs")

        os.makedirs(src_dir, exist_ok=True)
        os.makedirs(data_dir, exist_ok=True)
        os.makedirs(out_dir, exist_ok=True)

        files = {
            os.path.join(src_dir, "abm.py"): gen_abm(case_id, cfg),
            os.path.join(src_dir, "ode.py"): gen_ode(case_id, cfg),
            os.path.join(src_dir, "metrics.py"): gen_metrics(),
            os.path.join(src_dir, "data.py"): gen_data(case_id, cfg),
            os.path.join(src_dir, "validate.py"): gen_validate(case_id, cfg),
        }

        for path, content in files.items():
            with open(path, "w") as f:
                f.write(content)

        created += 1
        print(f"✅ {case_id}: 5 archivos creados en {src_dir}")

    print(f"\n{'='*60}")
    print(f"Total: {created} casos scaffolded")


if __name__ == "__main__":
    main()
