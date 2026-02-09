# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T14:19:57.642617Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0481
- bootstrap_mean: 0.0484
- CI 95%: [0.0440, 0.0528]
- weighted_value (LoE factor 0.20): 0.0096
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.5871
- external: 0.6931
- CR: 0.8470
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9007
- rmse_abm_no_ode: 0.9462
- rmse_ode: 0.5084
- rmse_reduced: 0.6097
- threshold: 0.4691

### Calibración
- forcing_scale: 0.2104
- macro_coupling: 0.1000
- damping: 0.1016
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.1410

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
- rmse_abm: 0.7633
- rmse_abm_no_ode: 0.7177
- rmse_ode: 1.7921
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

