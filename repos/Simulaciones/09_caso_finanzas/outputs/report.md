# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-08T21:30:50.854219Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.1509
- external: -0.0008
- CR: 179.7120
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 11589.9231
- rmse_abm_no_ode: 11589.9231
- rmse_ode: 11570.1013
- rmse_reduced: 11593.9671
- threshold: 10261.8656

### Calibración
- forcing_scale: 0.7472
- macro_coupling: 0.7907
- damping: 0.9235
- ode_alpha: 0.0014
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4576

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0249
- rmse_abm_no_ode: 1.0249
- rmse_ode: 20.4404
- rmse_reduced: 3.2170
- threshold: 1.1814

### Calibración
- forcing_scale: 0.7069
- macro_coupling: 0.5851
- damping: 0.9500
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4008

