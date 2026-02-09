# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T02:13:30.304377Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4628
- bootstrap_mean: 0.4631
- CI 95%: [0.4394, 0.4874]
- weighted_value (LoE factor 0.60): 0.2777
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9997
- external: 0.9921
- CR: 1.0076
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2429
- rmse_abm_no_ode: 0.4522
- rmse_ode: 0.2756
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
- valor: -3.7456
- bootstrap_mean: -3.9360
- CI 95%: [-5.9567, -2.6795]
- weighted_value (LoE factor 0.60): -2.2474
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.4550
- external: 0.3607
- CR: 1.2614
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8286
- rmse_abm_no_ode: 0.1746
- rmse_ode: 0.4550
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

