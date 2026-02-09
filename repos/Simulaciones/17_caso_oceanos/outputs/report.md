# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-09T17:03:57.911316Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0068
- bootstrap_mean: -0.0083
- CI 95%: [-0.0354, 0.0150]
- weighted_value (LoE factor 0.20): -0.0014
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9651
- external: 0.3465
- CR: 2.7854
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 5.5710
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

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0666
- bootstrap_mean: 0.0873
- CI 95%: [0.0451, 0.1566]
- weighted_value (LoE factor 0.20): 0.0133
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9363
- external: -0.7195
- CR: 1.3013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5326
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

