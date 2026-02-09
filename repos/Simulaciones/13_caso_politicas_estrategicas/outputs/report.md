# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-09T02:32:09.325463Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0036
- bootstrap_mean: -0.0036
- CI 95%: [-0.0049, -0.0026]
- weighted_value (LoE factor 0.20): -0.0007
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9500
- external: 0.8563
- CR: 1.1094
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3946
- rmse_abm_no_ode: 1.3896
- rmse_ode: 0.5130
- rmse_reduced: 1.3908
- threshold: 0.3900

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.3546
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7415

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0036
- bootstrap_mean: -0.0036
- CI 95%: [-0.0049, -0.0026]
- weighted_value (LoE factor 0.20): -0.0007
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9500
- external: 0.8563
- CR: 1.1094
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3946
- rmse_abm_no_ode: 1.3896
- rmse_ode: 0.5130
- rmse_reduced: 1.3908
- threshold: 0.3900

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.3546
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7415

