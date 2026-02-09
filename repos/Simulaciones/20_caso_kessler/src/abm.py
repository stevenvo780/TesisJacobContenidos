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
    # NOTE: forcing_series comes Z-scored from the validator (mean≈0, std≈1).
    # We use it to MODULATE launch rate around baseline (~80), not as raw count.
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.ones(steps) * 80
        forcing_scale = 1.0  # Direct values if standalone
        
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
        f_t = forcing[t] if t < len(forcing) else 0.0
        if forcing_scale < 1.0:
            # Z-scored forcing: modulate around baseline 80 launches/step
            L_t = 80.0 * (1.0 + forcing_scale * f_t)
        else:
            # Direct physical values (standalone mode)
            L_t = f_t
        
        # Add new launches (vectorized distribution across shells)
        new_objects = max(0, int(L_t * 1.5))
        if new_objects > 0:
            target_shells = rng.choice([3, 4, 5, 6], p=[0.1, 0.3, 0.4, 0.2], size=new_objects)
            size_classes = rng.choice([0, 1, 2], p=[0.6, 0.3, 0.1], size=new_objects)
            np.add.at(population, (target_shells, size_classes), 1)
            
        # Collisions and fragmentation (vectorized per shell)
        for shell in range(n_shells):
            shell_total = population[shell].sum()
            
            # Collision probability ~ N^2 (random encounter)
            collision_prob = collision_coeff * shell_total ** 2
            # Cap collisions to prevent runaway cascade (physical: limited collision cross-section)
            n_collisions = min(rng.poisson(collision_prob), 50)
            
            if n_collisions == 0:
                continue
            
            # Determine how many collisions can actually happen (need 2 objects per collision)
            available_large = int(population[shell, 2])
            available_medium = int(population[shell, 1])
            
            # Count collisions by type
            ll_collisions = min(n_collisions, available_large // 2)
            remaining = n_collisions - ll_collisions
            lm_collisions = min(remaining, min(available_large - ll_collisions * 2, available_medium))
            remaining -= lm_collisions
            mm_collisions = min(remaining, (available_medium - lm_collisions) // 2)
            actual_collisions = ll_collisions + lm_collisions + mm_collisions
            
            if actual_collisions == 0:
                continue
            
            # Remove colliding objects
            population[shell, 2] -= 2 * ll_collisions + lm_collisions
            population[shell, 1] -= lm_collisions + 2 * mm_collisions
            
            # Generate fragments in batch (NASA Standard Breakup Model)
            new_small_arr = rng.integers(500, 1500, size=actual_collisions)
            new_medium_arr = rng.integers(50, 150, size=actual_collisions)
            new_large_arr = rng.integers(5, 20, size=actual_collisions)
            
            total_new_small = new_small_arr.sum()
            total_new_medium = new_medium_arr.sum()
            total_new_large = new_large_arr.sum()
            
            # Distribute fragments (80% same shell, 10% each adjacent)
            for sh in range(max(0, shell-1), min(n_shells, shell+2)):
                frac = 0.8 if sh == shell else 0.1
                population[sh, 0] += int(total_new_small * frac)
                population[sh, 1] += int(total_new_medium * frac)
                population[sh, 2] += int(total_new_large * frac)
                    
        # Atmospheric decay (vectorized)
        decay_arr = np.array(decay_rate[:n_shells] if len(decay_rate) >= n_shells 
                             else decay_rate + [0.001] * (n_shells - len(decay_rate)))
        removed = (population * decay_arr[:, None]).astype(int)
        population = np.maximum(0, population - removed)
                
        # Macro Coupling: ODE signal modulates debris generation/removal
        # macro_series is Z-scored: positive = more debris expected, negative = less
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target_z = macro_series[t]
            # Modulate population by small factor based on Z-scored target
            scale = 1 + coupling * 0.01 * target_z
            population = (population * np.clip(scale, 0.95, 1.05)).astype(int)
            population = np.maximum(0, population)
                
        # Total trackable debris (large + medium)
        total_debris = population[:, 1:].sum()
        series_k.append(total_debris)
        # Represent population as square grid for validator compatibility
        grid_size = int(np.ceil(np.sqrt(n_shells * n_size_classes)))
        grid_rep = np.zeros((grid_size, grid_size))
        flat_pop = population.flatten()
        grid_rep.flat[:len(flat_pop)] = flat_pop
        series_grid.append(grid_rep)
        
    return {"k": series_k, "forcing": forcing, "grid": series_grid}
