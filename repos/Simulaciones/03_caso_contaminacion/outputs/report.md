# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-09T02:32:01.647959Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1322
- external: 0.0908
- CR: 1.4564
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 5.3145
- rmse_abm_no_ode: 5.3145
- rmse_ode: 3.0349
- rmse_reduced: 5.3145
- threshold: 1.4325

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: 0.0000
- CI 95%: [-0.0000, 0.0000]
- weighted_value (LoE factor 0.20): -0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1000
- external: 0.0233
- CR: 4.2871
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 3.2945
- rmse_abm_no_ode: 3.2945
- rmse_ode: 3.2945
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

