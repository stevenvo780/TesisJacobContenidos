"""validate.py — Caso 11: Movilidad Urbana.

Usa case_runner.py centralizado + case_config.json declarativo.
ODE: mean_reversion (Daganzo 2007).
Datos: Vehículos registrados (World Bank) + GDP per capita + tráfico aéreo.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from case_runner import run_case

if __name__ == "__main__":
    run_case(os.path.dirname(os.path.abspath(__file__)))
