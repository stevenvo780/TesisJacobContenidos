# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T02:02:29.136137Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4872
- bootstrap_mean: 0.4877
- CI 95%: [0.4642, 0.5122]
- weighted_value (LoE factor 0.60): 0.2923
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9997
- external: 0.9922
- CR: 1.0076
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2319
- rmse_abm_no_ode: 0.4522
- rmse_ode: 0.3084
- rmse_reduced: 2.2145
- threshold: 0.2328

### Calibración
- forcing_scale: 0.9240
- macro_coupling: 0.5225
- damping: 0.9500
- ode_alpha: 0.1628
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1118

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.2959
- bootstrap_mean: -3.4722
- CI 95%: [-5.6427, -2.1379]
- weighted_value (LoE factor 0.60): -1.9776
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.4585
- external: 0.3638
- CR: 1.2601
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7501
- rmse_abm_no_ode: 0.1746
- rmse_ode: 0.5540
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

