# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T04:22:48.560223Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1549
- bootstrap_mean: 0.1504
- CI 95%: [0.0695, 0.2393]
- weighted_value (LoE factor 0.20): 0.0310
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8610
- external: 0.7026
- CR: 1.2255
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5633
- rmse_abm_no_ode: 0.6666
- rmse_ode: 0.8854
- rmse_reduced: 0.6252
- threshold: 0.2598

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
- internal: 0.9567
- external: 0.8358
- CR: 1.1446
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8573
- rmse_abm_no_ode: 1.8573
- rmse_ode: 1.6074
- rmse_reduced: 1.8573
- threshold: 1.0637

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

