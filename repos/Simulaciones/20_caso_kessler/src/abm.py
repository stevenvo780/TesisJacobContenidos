"""
abm.py — 20_caso_kessler (Top-Tier)

Model: N-Body Debris Field ABM (NASA LEGEND-inspired)

This ABM simulates individual debris objects in orbital shells.
Collisions generate new fragments following the NASA Standard Breakup Model.

Reference:
- Johnson et al. (2001): "NASA's New Breakup Model of EVOLVE 4.0" (Adv. Space Res.)
- Liou & Johnson (2006): "Instability of LEO Environment" (Science)
- ESA DELTA/IMAGO: Debris Environment Long-Term Analysis

Agents: Debris Objects (position, velocity, size)
State: Orbital shell (altitude band), size class
Dynamics:
  - Orbital decay (atmospheric drag)
  - Collision probability (Poisson process based on spatial density)
  - Fragmentation cascade (collision -> multiple new objects)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Orbital Debris Field ABM.
    
    Simplified shell model: LEO divided into altitude bands.
    Objects drift between shells due to drag.
    Collisions happen stochastically based on density.
    
    Returns:
    - k: Total debris count
    - grid: Population by shell (altitude) and size class
    """
    rng = np.random.default_rng(seed)
    
    # Orbital shells (altitude bands: 200-2000 km in 10 bands)
    n_shells = params.get("n_shells", 10)
    n_size_classes = 3  # Small (<1cm), Medium (1-10cm), Large (>10cm)
    
    # Initial population distribution (most debris at 800-1000 km)
    population = np.zeros((n_shells, n_size_classes))
    for shell in range(n_shells):
        # Peak density at shell 4-5 (800-1000 km)
        peak_factor = np.exp(-((shell - 4)**2) / 5)
        population[shell, 0] = int(50000 * peak_factor)  # Small
        population[shell, 1] = int(5000 * peak_factor)   # Medium
        population[shell, 2] = int(1000 * peak_factor)   # Large
        
    # Forcing: Launch rate
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps) * 80
        
    # Parameters
    collision_coeff = params.get("abm_collision_coeff", 1e-9)
    decay_rate = params.get("abm_decay_rate", [0.05, 0.03, 0.02, 0.015, 0.01, 
                                                0.008, 0.006, 0.004, 0.003, 0.002])  # Per shell
    
    # Macro Coupling
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_k = []  # Total debris count
    series_grid = []
    
    for t in range(steps):
        L_t = forcing[t] if t < len(forcing) else 80
        
        # Add new launches (distributed across shells)
        new_objects = int(L_t * 1.5)  # Typical payload + rocket body + fragments
        for _ in range(new_objects):
            target_shell = rng.choice([3, 4, 5, 6], p=[0.1, 0.3, 0.4, 0.2])  # Most to 700-1000km
            size_class = rng.choice([0, 1, 2], p=[0.6, 0.3, 0.1])  # Mostly small
            population[target_shell, size_class] += 1
            
        # Collisions and fragmentation
        for shell in range(n_shells):
            # Spatial density
            shell_total = population[shell].sum()
            
            # Collision probability ~ N^2 (random encounter)
            collision_prob = collision_coeff * shell_total ** 2
            n_collisions = rng.poisson(collision_prob)
            
            for _ in range(n_collisions):
                # Remove two colliding objects (preferentially large)
                if population[shell, 2] >= 2:
                    population[shell, 2] -= 2
                elif population[shell, 2] >= 1 and population[shell, 1] >= 1:
                    population[shell, 2] -= 1
                    population[shell, 1] -= 1
                elif population[shell, 1] >= 2:
                    population[shell, 1] -= 2
                else:
                    continue
                    
                # Generate fragments (NASA Standard Breakup Model)
                # Large->Large collision: ~1000 trackable fragments
                new_small = rng.integers(500, 1500)
                new_medium = rng.integers(50, 150)
                new_large = rng.integers(5, 20)
                
                # Distribute fragments (mostly same shell, some adjacent)
                for sh in range(max(0, shell-1), min(n_shells, shell+2)):
                    frac = 0.8 if sh == shell else 0.1
                    population[sh, 0] += int(new_small * frac)
                    population[sh, 1] += int(new_medium * frac)
                    population[sh, 2] += int(new_large * frac)
                    
        # Atmospheric decay
        for shell in range(n_shells):
            for size in range(n_size_classes):
                decay = decay_rate[shell] if shell < len(decay_rate) else 0.001
                removed = int(population[shell, size] * decay)
                population[shell, size] = max(0, population[shell, size] - removed)
                
        # Macro Coupling: Adjust to match macro debris count
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target = macro_series[t]
            current = population.sum()
            if current > 0:
                scale = 1 + coupling * 0.01 * (target - current) / current
                population = population * np.clip(scale, 0.9, 1.1)
                
        # Total trackable debris (large + medium)
        total_debris = population[:, 1:].sum()
        series_k.append(total_debris)
        series_grid.append(population.copy())
        
    return {"k": series_k, "forcing": forcing, "grid": series_grid}
