# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T18:26:44.568587Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0491
- bootstrap_mean: 0.0491
- CI 95%: [0.0479, 0.0505]
- weighted_value (LoE factor 0.60): 0.0294
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9992
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9434
- rmse_abm_no_ode: 4.1468
- rmse_ode: 1.7962
- rmse_reduced: 6.8364
- threshold: 2.5948

### Calibración
- forcing_scale: 0.6455
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.6226
- ode_alpha: 0.0310
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1941
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: -5.9305
- bootstrap_mean: -6.2642
- CI 95%: [-9.7124, -4.4055]
- weighted_value (LoE factor 0.60): -3.5583
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9966
- external: 0.9976
- CR: 0.9990
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1590
- rmse_abm_no_ode: 0.1672
- rmse_ode: 3.6513
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9342
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1547
- ode_rolling: None

