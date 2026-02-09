# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-09T17:51:52.432624Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0000, 0.0000]
- weighted_value (LoE factor 0.20): -0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1215
- external: 0.1105
- CR: 1.0991
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8190
- rmse_abm_no_ode: 0.8190
- rmse_ode: 0.8242
- rmse_reduced: 0.8190
- threshold: 0.7999

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0000, 0.0000]
- weighted_value (LoE factor 0.20): -0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1035
- external: 0.0372
- CR: 2.7804
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
- rmse_ode: 3.2929
- rmse_reduced: 3.2945
- threshold: 3.2834

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.8000
- ode_beta: 0.2000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

