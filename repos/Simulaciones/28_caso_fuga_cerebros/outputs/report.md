# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-09T18:26:35.452594Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.7537
- bootstrap_mean: 0.7594
- CI 95%: [0.6913, 0.8428]
- weighted_value (LoE factor 0.60): 0.4522
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9683
- CR: 1.0327
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6858
- rmse_abm_no_ode: 2.7838
- rmse_ode: 0.7834
- rmse_reduced: 5.3990
- threshold: 1.7147

### Calibración
- forcing_scale: 0.9504
- macro_coupling: 0.3895
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2390
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1903
- bootstrap_mean: 0.1875
- CI 95%: [0.0359, 0.2971]
- weighted_value (LoE factor 0.60): 0.1142
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9995
- external: 0.9909
- CR: 1.0087
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.7399
- rmse_abm_no_ode: 4.6188
- rmse_ode: 3.4863
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6611
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4387
- ode_rolling: None

