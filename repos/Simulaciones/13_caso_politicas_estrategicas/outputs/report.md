# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-09T16:16:08.146084Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0029
- bootstrap_mean: -0.0029
- CI 95%: [-0.0040, -0.0020]
- weighted_value (LoE factor 0.20): -0.0006
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9270
- external: 0.8573
- CR: 1.0814
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4026
- rmse_abm_no_ode: 1.3985
- rmse_ode: 0.5130
- rmse_reduced: 1.4052
- threshold: 0.3900

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.3436
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7386

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0222
- bootstrap_mean: -0.0222
- CI 95%: [-0.0232, -0.0214]
- weighted_value (LoE factor 0.20): -0.0044
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4700
- external: -0.3209
- CR: 1.4645
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8343
- rmse_abm_no_ode: 1.7944
- rmse_ode: 0.9596
- rmse_reduced: 1.8131
- threshold: 0.1452

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3319

