"""
abm.py — 29_caso_iot (Top-Tier)

ABM de Difusión Tecnológica en Red con Agentes Heterogéneos.

Modelo: Grid NxN donde cada celda representa una región/mercado.
Cada agente tiene:
  - adoption_level: nivel de adopción tecnológica [0, M]
  - income_factor: factor económico local (heterogéneo)
  - infra_factor: factor de infraestructura local (heterogéneo)
  - network_density: densidad de conexiones locales

Dinámica por step:
1. Difusión espacial: vecinos con alta adopción influencian (contagio tecnológico)
2. Bass local: innovación + imitación proporcional a adopción vecinal
3. Network effect: externalidades cuadráticas (Metcalfe)
4. Forcing macro: señal global de la ODE guía la tendencia
5. Heterogeneidad: regiones ricas adoptan más rápido (income_factor)
6. Saturación local con techo variable por región
7. Disruption events: shocks tecnológicos (e.g., lanzamiento 3G, 4G, 5G)

Referencia:
- Goldenberg et al. (2001) "Talk of the Network: A Complex Systems Look at Cellular"
- Delre et al. (2007) "Targeting and timing promotional activities"
"""

import os
import sys
import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "common"))
from abm_core import simulate_abm_core

SERIES_KEY = "io"


def simulate_abm(params, steps, seed=2):
    """
    ABM de difusión tecnológica. Usa abm_core con parametrización
    específica para capturar la dinámica de adopción IoT.

    Parámetros adicionales inyectados:
      - forcing_gradient_type: "random_hubs" (ciudades/hubs tecnológicos)
      - heterogeneity_strength: 0.25 (diferencias regionales marcadas)
      - macro_mode: "dynamic" con macro_gain para feedback Bass
    """
    p = dict(params)

    # Forzar heterogeneidad espacial tipo "hubs tecnológicos"
    if "forcing_gradient_type" not in p:
        p["forcing_gradient_type"] = "random_hubs"
    if "forcing_gradient_strength" not in p:
        p["forcing_gradient_strength"] = 0.7

    # Heterogeneidad paramétrica fuerte (países ricos vs pobres)
    if "heterogeneity_strength" not in p:
        p["heterogeneity_strength"] = 0.25

    return simulate_abm_core(p, steps, seed=seed, series_key=SERIES_KEY)
