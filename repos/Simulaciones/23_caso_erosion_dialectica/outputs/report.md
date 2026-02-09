# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T03:47:59.613142Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3197
- bootstrap_mean: 0.3197
- CI 95%: [0.3159, 0.3236]
- weighted_value (LoE factor 0.60): 0.1918
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9783
- CR: 1.0222
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8548
- rmse_abm_no_ode: 4.1963
- rmse_ode: 2.0268
- rmse_reduced: 6.8895
- threshold: 2.6262

### Calibración
- forcing_scale: 0.3919
- macro_coupling: 0.5879
- damping: 0.3686
- ode_alpha: 0.0340
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2060

## Fase real
- **overall_pass**: False

### EDI
- valor: -8.8879
- bootstrap_mean: -9.5310
- CI 95%: [-14.6909, -6.6137]
- weighted_value (LoE factor 0.60): -5.3328
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.6293
- external: 0.2974
- CR: 2.1163
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7265
- rmse_abm_no_ode: 0.1746
- rmse_ode: 3.5740
- rmse_reduced: 2.4425
- threshold: 0.3672

### Calibración
- forcing_scale: 0.9331
- macro_coupling: 0.9859
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1537

