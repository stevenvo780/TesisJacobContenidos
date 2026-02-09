# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T15:04:19.690434Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1120
- bootstrap_mean: 0.1122
- CI 95%: [0.1003, 0.1248]
- weighted_value (LoE factor 0.20): 0.0224
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.5707
- external: 0.6715
- CR: 0.8498
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8346
- rmse_abm_no_ode: 0.9399
- rmse_ode: 0.7464
- rmse_reduced: 0.6156
- threshold: 0.5985

### Calibración
- forcing_scale: 0.3253
- macro_coupling: 0.2780
- damping: 0.0574
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.1340

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0634
- bootstrap_mean: -0.0662
- CI 95%: [-0.1056, -0.0193]
- weighted_value (LoE factor 0.20): -0.0127
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7455
- external: 0.8032
- CR: 0.9281
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7632
- rmse_abm_no_ode: 0.7177
- rmse_ode: 1.7923
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.4355
- macro_coupling: 0.1225
- damping: 0.1736
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8698

