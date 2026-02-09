# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T01:39:49.014273Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.7377
- bootstrap_mean: -0.7672
- CI 95%: [-1.1793, -0.4489]
- weighted_value (LoE factor 0.60): -0.4426
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.2861
- CR: 3.4949
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8035
- rmse_abm_no_ode: 1.0379
- rmse_ode: nan
- rmse_reduced: 1.8035
- threshold: 0.2679

### Calibración
- forcing_scale: 0.9217
- macro_coupling: 0.6503
- damping: 0.9500
- ode_alpha: 0.0496
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1435

## Fase real
- **overall_pass**: False

### EDI
- valor: -153.3398
- bootstrap_mean: -138.4750
- CI 95%: [-192.8494, -66.5513]
- weighted_value (LoE factor 0.60): -92.0039
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7468
- external: -0.5117
- CR: 1.4595
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 26.9494
- rmse_abm_no_ode: 0.1746
- rmse_ode: 39.2311
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

