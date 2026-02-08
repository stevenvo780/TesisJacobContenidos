# Reporte de Validación — Acidificación Oceánica

- generated_at: 2026-02-08T20:52:46.766871Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -4.7228
- bootstrap_mean: -4.7287
- CI 95%: [-4.9211, -4.5848]
- weighted_value (LoE factor 0.20): -0.9446
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9988
- external: -0.2138
- CR: 4.6725
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4860
- rmse_abm_no_ode: 0.6091
- rmse_ode: 7.3711
- rmse_reduced: 3.3505
- threshold: 0.8715

### Calibración
- forcing_scale: 0.7429
- macro_coupling: 0.5470
- damping: 0.7324
- ode_alpha: 0.1001
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0637

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.4513
- bootstrap_mean: -0.4732
- CI 95%: [-0.7319, -0.2754]
- weighted_value (LoE factor 0.20): -0.0903
- válido (0.30-0.90): False

### Symploké y CR
- internal: -1.0000
- external: 0.0000
- CR: 2658223.2030
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 34.4842
- rmse_abm_no_ode: 23.7603
- rmse_ode: 2.7036
- rmse_reduced: 2.0497
- threshold: 1.0498

### Calibración
- forcing_scale: 0.6385
- macro_coupling: 0.8272
- damping: 0.8281
- ode_alpha: 0.1307
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9647

