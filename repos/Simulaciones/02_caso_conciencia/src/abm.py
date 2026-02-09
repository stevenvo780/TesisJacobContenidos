"""
abm.py — 02_caso_conciencia

Modelo: Global Workspace Theory ABM (Baars/Dehaene)

La Teoría del Espacio Global de Trabajo (GWT) es el modelo neurocientífico
líder para la conciencia. Implementamos una versión basada en agentes donde
"módulos" cognitivos compiten por acceso a un espacio de broadcast global.

Ecuación de actualización por módulo i:
    a_i(t+1) = (1 - δ) · [a_i(t) + S_i(t)] - λ · (a_i - ā) + B_i(t)

donde:
    δ = decay_rate          : tasa de decaimiento (fatiga)
    S_i(t)                  : respuesta al estímulo externo
    λ = lateral_inhibition  : competencia lateral
    ā = mean(a)             : activación media
    B_i(t) = broadcast_boost si i = argmax(a) y max(a) > θ_ignition

Dinámica de ignición (Dehaene & Changeux 2011):
    - Si max(a) > θ_ignition: el módulo ganador obtiene boost,
      los demás son suprimidos (winner-take-all).
    - Si max(a) ≤ θ_ignition: procesamiento inconsciente (sin broadcast).

Conciencia = max(workspace_activation, mean(activations))

Referencias:
    - Baars (1988), "A Cognitive Theory of Consciousness"
    - Dehaene & Changeux (2011), Neuron 70(2):200-227
    - Tononi (2004), BMC Neurosci 5:42 (IIT, relacionado)
"""

import numpy as np

def simulate_abm(params, steps, seed=42):
    """
    Global Workspace Theory ABM.
    
    Módulos cognitivos compiten por acceso a la conciencia.
    El ganador hace broadcast global, creando experiencia integrada.
    
    Returns:
        dict con claves: c (nivel de conciencia), forcing, grid
    """
    rng = np.random.default_rng(seed)
    
    # ── Módulos cognitivos ──────────────────────────────────────────────
    # 16 módulos en grid 4×4. Baars (1988) no especifica un número fijo;
    # 16 módulos representan las principales funciones cognitivas que
    # compiten por acceso al workspace global.
    n_modules = params.get("n_modules", 16)
    grid_size = params.get("grid_size", 4)  # 4×4 = 16 módulos
    
    # Tipos de módulo (referencia funcional, no usado en cálculos)
    module_names = [
        "Visual", "Auditory", "Tactile", "Motor",
        "Language", "Memory", "Planning", "Emotion",
        "Attention", "Spatial", "Object", "Face",
        "Executive", "Social", "Self", "Meta"
    ]
    
    # Activaciones iniciales ∈ [0.1, 0.3]: procesamiento subliminal basal
    activations = rng.uniform(0.1, 0.3, size=n_modules)
    
    # Global Workspace (broadcast compartido)
    workspace_content = -1   # Índice del módulo ganador
    workspace_activation = 0.0
    
    # ── Parámetros del modelo ───────────────────────────────────────────
    # θ_ignition = 0.6: umbral de ignición para broadcast global.
    #   Dehaene et al. (2006, Nature 440:752) muestran que el umbral
    #   perceptual de ignición cortical está ~60% de la señal máxima.
    ignition_threshold = params.get("abm_threshold", 0.6)

    # δ = 0.2: tasa de decaimiento por paso (20% por mes).
    #   τ_decay = 1/δ = 5 meses. Para procesos cognitivos colectivos,
    #   la memoria de trabajo social decae en escala de meses.
    decay_rate = params.get("abm_decay", 0.2)

    # λ = 0.1: inhibición lateral (competencia entre módulos).
    #   Rango estándar en modelos de redes neuronales: 0.05-0.2
    #   (Grossberg 1988, "Nonlinear Neural Networks").
    lateral_inhibition = params.get("abm_inhibition", 0.1)

    # broadcast_boost = 0.3: refuerzo al módulo ganador.
    #   Simétrico con la supresión de perdedores (×0.7 = -30%).
    #   Winner-take-all con asimetría moderada.
    broadcast_boost = params.get("abm_broadcast", 0.3)
    
    # ── Forzamiento externo ───────────────────────────────────────────────
    # forcing_series viene Z-scored del validator (media≈0, std≈1).
    # Se modula alrededor de baseline 0.5 (punto medio de [0,1]).
    forcing = params.get("forcing_series")
    forcing_scale = params.get("forcing_scale", 0.05)
    if forcing is None:
        forcing = np.ones(steps) * 0.5
        forcing_scale = 1.0  # Valores directos en modo standalone
        
    # ── Acoplamiento macro (ODE → ABM) ─────────────────────────────────
    macro_series = params.get("macro_target_series")
    coupling = params.get("macro_coupling", 0.0)
    
    series_c = []
    series_grid = []
    
    for t in range(steps):
        # ── Estímulo externo ────────────────────────────────────────────
        f_t = forcing[t] if t < len(forcing) else 0.0
        if forcing_scale < 1.0:
            # Z-scored: modular alrededor de baseline 0.5
            stimulus = max(0.01, 0.5 + forcing_scale * f_t)
        else:
            # Valores directos (modo standalone)
            stimulus = f_t
        
        # 1. Activación bottom-up (estímulo + ruido)
        # Cada módulo responde diferencialmente al estímulo
        stimulus_response = rng.uniform(0, max(0.01, stimulus), size=n_modules)
        activations += stimulus_response
        
        # 2. Decaimiento (fatiga atencional)
        activations *= (1 - decay_rate)
        
        # 3. Competencia (inhibición lateral)
        mean_activation = np.mean(activations)
        activations -= lateral_inhibition * (activations - mean_activation)
        
        # 4. Ignición (winner-take-all para workspace global)
        max_idx = np.argmax(activations)
        max_activation = activations[max_idx]
        
        if max_activation > ignition_threshold:
            # ¡Ignición! Broadcast global (Dehaene & Changeux 2011)
            workspace_content = max_idx
            workspace_activation = max_activation
            
            # Boost al módulo ganador
            activations[max_idx] += broadcast_boost
            
            # Supresión de competidores: ×0.7 = -30%
            # Simétrico con broadcast_boost=0.3 (+30%)
            for i in range(n_modules):
                if i != max_idx:
                    activations[i] *= 0.7
        else:
            # Sin ignición (procesamiento inconsciente)
            workspace_activation *= 0.5  # Decaimiento del workspace
            
        # Clamping a [0, 1]
        activations = np.clip(activations, 0, 1)
        
        # ── Acoplamiento macro (ODE → ABM) ─────────────────────────────
        # Escala = 1 + coupling·0.5·(target - workspace_activation)
        # El factor 0.5 modera el acoplamiento para evitar sobreajuste.
        if macro_series is not None and t < len(macro_series) and coupling > 0:
            target = macro_series[t]
            scale = 1 + coupling * 0.5 * (target - workspace_activation)
            activations *= np.clip(scale, 0.8, 1.2)
            
        # Nivel de conciencia = max(workspace, mean(activations))
        # Combina ignición con integración de fondo (Dehaene 2014)
        consciousness = max(workspace_activation, np.mean(activations))
        
        series_c.append(consciousness)
        
        # Grid representation (sqrt(n_modules) x sqrt(n_modules))
        actual_grid_size = int(np.sqrt(n_modules))
        grid = activations[:actual_grid_size**2].reshape((actual_grid_size, actual_grid_size))
        series_grid.append(grid.copy())
        
    return {"c": series_c, "forcing": forcing, "grid": series_grid}
