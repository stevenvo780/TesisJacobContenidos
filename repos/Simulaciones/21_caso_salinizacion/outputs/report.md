# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T18:53:38.131299Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3220
- bootstrap_mean: 0.3262
- CI 95%: [0.2681, 0.3952]
- weighted_value (LoE factor 0.60): 0.1932
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9985
- CR: 1.0013
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4887
- rmse_abm_no_ode: 0.7207
- rmse_ode: 1.0657
- rmse_reduced: 2.9446
- threshold: 0.6860

### Calibración
- forcing_scale: 0.9459
- macro_coupling: 0.3413
- ode_coupling_strength: 0.2731
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2983
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1538
- bootstrap_mean: 0.1539
- CI 95%: [0.0872, 0.2248]
- weighted_value (LoE factor 0.60): 0.0923
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9984
- external: 0.9536
- CR: 1.0469
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6513
- rmse_abm_no_ode: 0.7697
- rmse_ode: 3.7483
- rmse_reduced: 1.0780
- threshold: 0.1357

### Calibración
- forcing_scale: 0.9405
- macro_coupling: 0.4163
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2754
- ode_rolling: None

