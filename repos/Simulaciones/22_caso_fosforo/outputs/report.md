# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T02:06:04.960252Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3820
- bootstrap_mean: 0.3684
- CI 95%: [0.0933, 0.5772]
- weighted_value (LoE factor 0.60): 0.2292
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9716
- CR: 1.0291
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4844
- rmse_abm_no_ode: 0.7838
- rmse_ode: 3.7891
- rmse_reduced: 2.7961
- threshold: 0.7146

### Calibración
- forcing_scale: 0.9351
- macro_coupling: 0.3008
- damping: 0.9500
- ode_alpha: 0.3090
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2793

## Fase real
- **overall_pass**: False

### EDI
- valor: -5.0526
- bootstrap_mean: -5.1184
- CI 95%: [-7.0622, -3.7260]
- weighted_value (LoE factor 0.60): -3.0316
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9983
- external: 0.9323
- CR: 1.0707
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9800
- rmse_abm_no_ode: 0.3271
- rmse_ode: 5.0236
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9398
- macro_coupling: 0.6239
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2782

