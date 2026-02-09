# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-09T17:52:11.945500Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0005
- bootstrap_mean: -0.0005
- CI 95%: [-0.0011, -0.0001]
- weighted_value (LoE factor 0.20): -0.0001
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9297
- external: 0.8593
- CR: 1.0820
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3993
- rmse_abm_no_ode: 1.3985
- rmse_ode: 0.5130
- rmse_reduced: 1.4052
- threshold: 0.3900

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.3436
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7386

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0111
- bootstrap_mean: 0.0111
- CI 95%: [0.0107, 0.0116]
- weighted_value (LoE factor 0.20): 0.0022
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4633
- external: -0.2849
- CR: 1.6262
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7745
- rmse_abm_no_ode: 1.7944
- rmse_ode: 0.9596
- rmse_reduced: 1.8131
- threshold: 0.1452

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3319

