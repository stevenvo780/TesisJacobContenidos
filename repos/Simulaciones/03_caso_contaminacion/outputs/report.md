# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-08T23:00:25.857052Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3284
- bootstrap_mean: 0.3191
- CI 95%: [0.1634, 0.4657]
- weighted_value (LoE factor 0.20): 0.0657
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9992
- external: 0.9341
- CR: 1.0698
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9994
- rmse_abm_no_ode: 2.9773
- rmse_ode: 4.1996
- rmse_reduced: 3.9723
- threshold: 1.4119

### Calibración
- forcing_scale: 0.3380
- macro_coupling: 0.9821
- damping: 0.5096
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7974

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1225
- bootstrap_mean: 0.1218
- CI 95%: [-0.0621, 0.2400]
- weighted_value (LoE factor 0.20): 0.0245
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9967
- external: 0.9848
- CR: 1.0121
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3679
- rmse_abm_no_ode: 3.8380
- rmse_ode: 3.2931
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6782
- damping: 0.7618
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6665

