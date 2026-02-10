"""
abm.py — 18_caso_urbanizacion (Top-Tier)

Model: Preferential Attachment Urban Growth / Simon-Yule Process

Reference:
- Simon (1955): "Biometrika" (Rich-Get-Richer dynamics)
- Barabasi & Albert (1999): "Emergence of Scaling in Random Networks"
- Gabaix (1999): "Zipf's Law for Cities" (QJE)
- Bettencourt & West (2010): "A unified theory of urban living" (Nature)

Agents: Cities (nodes in a system)
State: Population (size)
Dynamics:
  - New people arrive each step
  - They migrate to cities with probability proportional to size (preferential attachment)
  - New cities form with small probability
  - Urban amenities attract migration (macro coupling)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Preferential Attachment Urban Growth ABM.
    
    Cities grow by attracting migrants proportional to current size.
    New cities occasionally emerge.
    
    Returns:
    - u: Urbanization rate (fraction of agents in cities vs rural)
    - grid: City population distribution (histogram-like)
    """
    rng = np.random.default_rng(seed)
    
    # Initial Cities
    n_initial_cities = params.get("n_initial_cities", 10)
    city_pop = rng.integers(100, 1000, size=n_initial_cities).astype(float)
    total_pop = city_pop.sum()
    rural_pop = total_pop * 0.5  # Start 50% rural
    
    # Forcing: Economic Driver (GDP growth -> migration pull)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps) * 0.02
        
    # Parameters
    # new_city_prob=0.02: ~2% de probabilidad anual de nueva ciudad
    #   (Rozenfeld et al. 2008, PNAS: tasa observada de aparición de clusters urbanos)
    new_city_prob = params.get("abm_new_city_prob", 0.02)
    # migration_rate=0.05: ~5% de población rural migra/año
    #   (UN WUP 2018: tasa media global de urbanización ~1-5%/año)
    migration_rate = params.get("abm_migration_rate", 0.05)
    # beta=1.15: exponente superlineal de Bettencourt (2007, PNAS)
    #   innovación, patentes, GDP escalan como N^1.15 (superlinear scaling)
    beta = params.get("abm_beta", 1.15)
    
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_u = []  # Urbanization rate
    series_grid = []
    store_grid = params.get("_store_grid", True)
    
    for t in range(steps):
        f_t = forcing[t] if t < len(forcing) else 0.02
        
        # Migración rural → urbana
        # Factor (1 + 5*f_t): elasticidad migración-crecimiento económico
        #   5.0: cada 1% de crecimiento GDP → 5% más migración
        #   (Henderson 2003, JEG: elasticidad ingreso-urbanización ≈ 3-7)
        migrants = migration_rate * rural_pop * (1 + 5 * f_t)
        migrants = max(0, migrants)
        rural_pop -= migrants
        rural_pop = max(100, rural_pop)  # Mínimo rural (evita extinción)
        
        # Distribute migrants via preferential attachment
        if len(city_pop) > 0:
            probs = city_pop / city_pop.sum()
            # Add small noise to avoid complete determinism
            probs = probs + 0.01
            probs = probs / probs.sum()
            
            # Each migrant chooses a city
            n_migrants = int(migrants)
            for _ in range(min(n_migrants, 1000)):  # Cap for efficiency
                city_idx = rng.choice(len(city_pop), p=probs)
                city_pop[city_idx] += migrants / n_migrants if n_migrants > 0 else 0
                
        # New city formation
        if rng.random() < new_city_prob:
            new_size = rng.integers(50, 200)
            city_pop = np.append(city_pop, new_size)
            rural_pop -= new_size
            rural_pop = max(100, rural_pop)
            
        # Macro Coupling: ODE urbanization target nudges migration balance
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target_rate = macro_series[t]
            current_rate = city_pop.sum() / (city_pop.sum() + rural_pop)
            delta = target_rate - current_rate
            # Shift population between urban and rural
            shift = coupling * abs(delta) * (city_pop.sum() + rural_pop) * 0.01
            if delta > 0:
                rural_pop -= shift
                city_pop *= (1 + shift / city_pop.sum()) if city_pop.sum() > 0 else 1.0
            else:
                rural_pop += shift
                city_pop *= max(0.9, 1 - shift / city_pop.sum()) if city_pop.sum() > 0 else 1.0
            rural_pop = max(100, rural_pop)
                
        # Calculate urbanization rate
        total = city_pop.sum() + rural_pop
        urban_rate = city_pop.sum() / total if total > 0 else 0
        series_u.append(urban_rate)
        
        # Grid: City size distribution (binned)
        grid_size = 20
        grid_rep = np.zeros((grid_size, grid_size))
        # Histogram of city sizes (log-scale bins)
        if len(city_pop) > 0:
            log_sizes = np.log10(city_pop + 1)
            hist, _ = np.histogram(log_sizes, bins=grid_size, range=(0, 6))
            grid_rep[0, :] = hist / hist.max() if hist.max() > 0 else 0
        if store_grid:
            series_grid.append(grid_rep.copy())
        
    return {"u": series_u, "forcing": forcing, "grid": series_grid}
