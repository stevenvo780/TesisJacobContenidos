# Reporte de Validación — Falsación: No-Estacionariedad

- generated_at: 2026-02-09T15:23:39.551245

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -4.9011
- CI 95%: [-5.6393, -4.1781]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9947
- CR: 1.0043
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.1332
- rmse_abm_no_ode: 0.5325
- rmse_ode: 5.3456
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

