# Reporte de Validación — Falsación: No-Estacionariedad

- generated_at: 2026-02-09T13:26:32.206856

## Fase real
- **overall_pass**: False

### EDI
- valor: -4.9238
- bootstrap_mean: -4.9405
- CI 95%: [-5.6839, -4.2126]
- weighted_value (LoE factor 0.20): -0.9848
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9989
- external: 0.9956
- CR: 1.0033
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.1541
- rmse_abm_no_ode: 0.5325
- rmse_ode: 5.3794
- rmse_reduced: 3.6758
- threshold: 1.0297

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- ode_coupling_strength: 0.1600
- abm_feedback_gamma: 0.0500
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000
- ode_rolling: None

