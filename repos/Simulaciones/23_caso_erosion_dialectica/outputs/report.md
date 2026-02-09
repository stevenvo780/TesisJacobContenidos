# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T02:06:12.323400Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5044
- bootstrap_mean: 0.5014
- CI 95%: [0.3985, 0.5820]
- weighted_value (LoE factor 0.60): 0.3026
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9911
- CR: 1.0088
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2241
- rmse_abm_no_ode: 0.4522
- rmse_ode: 0.8629
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
- valor: -2.6195
- bootstrap_mean: -2.7940
- CI 95%: [-4.5848, -1.7606]
- weighted_value (LoE factor 0.60): -1.5717
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.3740
- external: 0.4369
- CR: 0.8559
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6320
- rmse_abm_no_ode: 0.1746
- rmse_ode: 0.8046
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

