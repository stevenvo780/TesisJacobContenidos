# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T03:47:51.873133Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0951
- bootstrap_mean: 0.0923
- CI 95%: [0.0283, 0.1614]
- weighted_value (LoE factor 0.20): 0.0190
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8820
- external: 0.7173
- CR: 1.2296
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6763
- rmse_abm_no_ode: 0.7473
- rmse_ode: 0.9738
- rmse_reduced: 0.7243
- threshold: 0.2435

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
- internal: 0.9704
- external: 0.7116
- CR: 1.3636
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7265
- rmse_abm_no_ode: 1.7265
- rmse_ode: 1.6477
- rmse_reduced: 1.7265
- threshold: 0.9461

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

