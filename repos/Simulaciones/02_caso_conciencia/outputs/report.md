# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T14:45:48.576120Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1342
- bootstrap_mean: 0.1347
- CI 95%: [0.1239, 0.1457]
- weighted_value (LoE factor 0.20): 0.0268
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4487
- external: 0.5794
- CR: 0.7744
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9152
- rmse_abm_no_ode: 1.0571
- rmse_ode: 0.4890
- rmse_reduced: 0.7272
- threshold: 0.4812

### Calibración
- forcing_scale: 0.2413
- macro_coupling: 0.3983
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.1573

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
- rmse_ode: 1.7922
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

