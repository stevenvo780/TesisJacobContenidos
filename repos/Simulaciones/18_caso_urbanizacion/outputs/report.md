# Reporte de Validación — Urbanización Global

- generated_at: 2026-02-08T20:50:21.464752Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.9922
- bootstrap_mean: -1.0106
- CI 95%: [-1.2395, -0.8301]
- weighted_value (LoE factor 0.20): -0.1984
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9996
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8632
- rmse_abm_no_ode: 0.4333
- rmse_ode: 2.4329
- rmse_reduced: 2.8496
- threshold: 0.4541

### Calibración
- forcing_scale: 0.9828
- macro_coupling: 0.2842
- damping: 0.9500
- ode_alpha: 0.2338
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2238

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0569
- bootstrap_mean: -0.0606
- CI 95%: [-0.3310, 0.1242]
- weighted_value (LoE factor 0.20): -0.0114
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9372
- CR: 1.0667
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2516
- rmse_abm_no_ode: 1.1842
- rmse_ode: 2.3176
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.9697
- macro_coupling: 0.4522
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0675

