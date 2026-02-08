# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-08T20:48:11.451298Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9996
- external: 0.9999
- CR: 0.9998
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 11591.8750
- rmse_abm_no_ode: 11591.8750
- rmse_ode: 11571.0462
- rmse_reduced: 11593.9671
- threshold: 10261.8656

### Calibración
- forcing_scale: 0.7749
- macro_coupling: 0.6446
- damping: 0.9500
- ode_alpha: 0.0014
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4581

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0957
- rmse_abm_no_ode: 1.0957
- rmse_ode: 19.5087
- rmse_reduced: 3.2170
- threshold: 1.1814

### Calibración
- forcing_scale: 0.7068
- macro_coupling: 0.1083
- damping: 0.9500
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4008

