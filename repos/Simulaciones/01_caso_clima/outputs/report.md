# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-09T18:53:45.844616Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0505
- bootstrap_mean: -0.0507
- CI 95%: [-0.0570, -0.0451]
- weighted_value (LoE factor 1.00): -0.0505
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9939
- CR: 1.0060
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 6.1568
- rmse_abm_no_ode: 5.8610
- rmse_ode: 8.2694
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.6481
- macro_coupling: 0.4561
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2539
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0096
- bootstrap_mean: 0.0096
- CI 95%: [0.0085, 0.0108]
- weighted_value (LoE factor 1.00): 0.0096
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0003
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1807
- rmse_abm_no_ode: 1.1922
- rmse_ode: 1.6955
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6353
- ode_rolling: None

