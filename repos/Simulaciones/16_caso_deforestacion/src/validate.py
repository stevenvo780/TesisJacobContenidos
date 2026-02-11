"""validate.py — Deforestación Global (von Thünen Frontier)

Usa case_runner.py centralizado + case_config.json declarativo.
ODE: accumulation_decay.
"""

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))

from case_runner import run_case

if __name__ == "__main__":
    run_case(os.path.dirname(os.path.abspath(__file__)))
