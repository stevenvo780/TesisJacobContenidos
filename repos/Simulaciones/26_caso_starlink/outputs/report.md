# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T18:53:57.429964Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5065
- bootstrap_mean: 0.5070
- CI 95%: [0.4949, 0.5204]
- weighted_value (LoE factor 0.80): 0.4052
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9956
- CR: 1.0043
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6299
- rmse_abm_no_ode: 1.2765
- rmse_ode: 0.8421
- rmse_reduced: 0.8072
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9603
- macro_coupling: 0.4810
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2810
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: -521.2714
- bootstrap_mean: -520.3016
- CI 95%: [-587.7953, -456.5154]
- weighted_value (LoE factor 0.80): -417.0171
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9865
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0661
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.6290
- rmse_reduced: 0.0001
- threshold: 0.1000

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1071
- ode_coupling_strength: 0.0857
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0002
- ode_rolling: None

