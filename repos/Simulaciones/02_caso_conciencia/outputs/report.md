# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T03:39:45.100274Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1494
- bootstrap_mean: 0.1451
- CI 95%: [0.0683, 0.2229]
- weighted_value (LoE factor 0.20): 0.0299
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8641
- external: 0.7029
- CR: 1.2294
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6208
- rmse_abm_no_ode: 0.7298
- rmse_ode: 0.9589
- rmse_reduced: 0.6924
- threshold: 0.2580

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
- internal: 0.9612
- external: 0.8514
- CR: 1.1290
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8170
- rmse_abm_no_ode: 1.8170
- rmse_ode: 1.5410
- rmse_reduced: 1.8170
- threshold: 1.0128

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

