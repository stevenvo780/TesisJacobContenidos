# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-09T14:20:01.328980Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0001
- bootstrap_mean: -0.0001
- CI 95%: [-0.0001, -0.0000]
- weighted_value (LoE factor 1.00): -0.0001
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.9870
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 11559.1092
- rmse_abm_no_ode: 11558.3879
- rmse_ode: 11561.2871
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
- valor: 0.0506
- bootstrap_mean: 0.0507
- CI 95%: [0.0440, 0.0568]
- weighted_value (LoE factor 1.00): 0.0506
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.9815
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 36.0127
- rmse_abm_no_ode: 37.9317
- rmse_ode: 29.7012
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

