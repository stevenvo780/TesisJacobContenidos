# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T03:47:53.902719Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3586
- bootstrap_mean: 0.3616
- CI 95%: [0.3261, 0.4109]
- weighted_value (LoE factor 0.80): 0.2868
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9965
- CR: 1.0033
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9362
- rmse_abm_no_ode: 1.4595
- rmse_ode: 0.8092
- rmse_reduced: 3.5358
- threshold: 1.0544

### Calibración
- forcing_scale: 0.9465
- macro_coupling: 0.3435
- damping: 0.9500
- ode_alpha: 0.2822
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3112

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.8042
- bootstrap_mean: -3.9032
- CI 95%: [-5.1211, -2.9801]
- weighted_value (LoE factor 0.80): -3.0434
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.7858
- external: 0.2011
- CR: 3.9068
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.7339
- rmse_abm_no_ode: 0.7772
- rmse_ode: 7.1100
- rmse_reduced: 6.8775
- threshold: 2.1513

### Calibración
- forcing_scale: 0.9442
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2618

