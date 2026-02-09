# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T02:42:45.242431Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1605
- bootstrap_mean: 0.1556
- CI 95%: [0.0708, 0.2466]
- weighted_value (LoE factor 0.20): 0.0321
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8614
- external: 0.7014
- CR: 1.2280
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5185
- rmse_abm_no_ode: 0.6177
- rmse_ode: 0.8471
- rmse_reduced: 0.5872
- threshold: 0.2674

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9782
- external: 0.7334
- CR: 1.3339
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8394
- rmse_abm_no_ode: 1.8394
- rmse_ode: 1.8263
- rmse_reduced: 1.8394
- threshold: 1.0547

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

