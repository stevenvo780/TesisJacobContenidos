"""
abm.py — 02_caso_conciencia (Top-Tier)

Model: Global Workspace Theory ABM (Baars/Dehaene)

Global Workspace Theory is THE leading neuroscience model of consciousness.
We implement an agent-based version where mental "modules" compete for 
access to a global broadcast workspace.

Reference:
- Baars (1988): "A Cognitive Theory of Consciousness"
- Dehaene & Changeux (2011): "Experimental and Theoretical Approaches to Conscious Processing"
- Tononi (2004): Integrated Information Theory (related)

Agents: Cognitive Modules (Perception, Memory, Language, etc.)
State: 
  - Activation level (0-1)
  - Content (what information is being processed)
Dynamics:
  - Competition for global workspace access
  - Ignition (threshold crossing -> global broadcast)
  - Bottom-up activation from stimuli
  - Top-down modulation from attention
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Global Workspace Theory ABM.
    
    Cognitive modules compete for access to consciousness.
    Winner broadcasts globally, creating integrated experience.
    
    Returns:
    - c: Consciousness Level (Global Workspace activation)
    - grid: Module activation pattern
    """
    rng = np.random.default_rng(seed)
    
    # Modules (cognitive processors)
    n_modules = params.get("n_modules", 16)
    grid_size = params.get("grid_size", 4)  # 4x4 = 16 modules
    
    # Module types
    module_names = [
        "Visual", "Auditory", "Tactile", "Motor",
        "Language", "Memory", "Planning", "Emotion",
        "Attention", "Spatial", "Object", "Face",
        "Executive", "Social", "Self", "Meta"
    ]
    
    # Module activations (0-1)
    activations = rng.uniform(0.1, 0.3, size=n_modules)
    
    # Global Workspace (shared broadcast)
    workspace_content = -1  # Index of winning module
    workspace_activation = 0.0
    
    # Parameters
    ignition_threshold = params.get("abm_threshold", 0.6)  # Threshold for broadcast
    decay_rate = params.get("abm_decay", 0.2)  # Activation decay
    lateral_inhibition = params.get("abm_inhibition", 0.1)  # Competition
    broadcast_boost = params.get("abm_broadcast", 0.3)  # Winner boost
    
    # Forcing: External stimuli (news volatility, attention-grabbing events)
    forcing = params.get("forcing_series")
    if forcing is None:
        forcing = np.ones(steps) * 0.5
        
    # Macro Coupling (ODE consciousness level)
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_c = []
    series_grid = []
    
    for t in range(steps):
        # External stimulus strength
        stimulus = forcing[t] if t < len(forcing) else 0.5
        
        # 1. Bottom-up activation (stimulus + noise)
        # Different modules respond to different stimuli
        stimulus_response = rng.uniform(0, max(0.01, stimulus), size=n_modules)
        activations += stimulus_response  # Full stimulus, not attenuated
        
        # 2. Decay
        activations *= (1 - decay_rate)
        
        # 3. Competition (lateral inhibition)
        mean_activation = np.mean(activations)
        activations -= lateral_inhibition * (activations - mean_activation)
        
        # 4. Check for ignition (winner-take-all for workspace)
        max_idx = np.argmax(activations)
        max_activation = activations[max_idx]
        
        if max_activation > ignition_threshold:
            # Ignition! Global broadcast
            workspace_content = max_idx
            workspace_activation = max_activation
            
            # Boost winning module
            activations[max_idx] += broadcast_boost
            
            # Suppress others (global workspace exclusivity)
            for i in range(n_modules):
                if i != max_idx:
                    activations[i] *= 0.7
        else:
            # No ignition (unconscious processing)
            workspace_activation *= 0.5  # Decay
            
        # Clamp activations
        activations = np.clip(activations, 0, 1)
        
        # Macro coupling
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target = macro_series[t]
            scale = 1 + coupling * 0.5 * (target - workspace_activation)
            activations *= np.clip(scale, 0.8, 1.2)
            
        # Consciousness level = global workspace activation
        # Combines ignition events with background integration (Dehaene)
        consciousness = max(workspace_activation, np.mean(activations))
        
        series_c.append(consciousness)
        
        # Grid representation (sqrt(n_modules) x sqrt(n_modules))
        actual_grid_size = int(np.sqrt(n_modules))
        grid = activations[:actual_grid_size**2].reshape((actual_grid_size, actual_grid_size))
        series_grid.append(grid.copy())
        
    return {"c": series_c, "forcing": forcing, "grid": series_grid}
