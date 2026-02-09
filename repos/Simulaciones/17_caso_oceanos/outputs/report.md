# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-09T18:26:38.383100Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1403
- bootstrap_mean: 0.1391
- CI 95%: [0.1197, 0.1559]
- weighted_value (LoE factor 0.20): 0.0281
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9615
- external: 0.1167
- CR: 8.2419
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.7575
- rmse_abm_no_ode: 5.5337
- rmse_ode: 1.4691
- rmse_reduced: 5.1439
- threshold: 0.9858

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 2.2767
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0532
- bootstrap_mean: 0.0697
- CI 95%: [0.0359, 0.1251]
- weighted_value (LoE factor 0.20): 0.0106
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9178
- external: -0.6878
- CR: 1.3344
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5834
- rmse_abm_no_ode: 3.7846
- rmse_ode: 2.7954
- rmse_reduced: 3.8040
- threshold: 2.7353

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 2.5036
- ode_rolling: None

