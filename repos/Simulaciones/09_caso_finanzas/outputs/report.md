# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-09T02:31:23.672682Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: [[ True]]
- c5_uncertainty: [[ True]]

### Errores
- rmse_abm: 11558.3879
- rmse_abm_no_ode: 11558.3879
- rmse_ode: 11578.0384
- rmse_reduced: 11558.3001
- threshold: 10261.8656

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0014
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 6.7094

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: [[ True]]
- c5_uncertainty: [[ True]]

### Errores
- rmse_abm: 37.9317
- rmse_abm_no_ode: 37.9317
- rmse_ode: 30.5774
- rmse_reduced: 37.5564
- threshold: 1.1814

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 10.2667

