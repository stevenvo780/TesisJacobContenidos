# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T15:57:32.287731Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2927
- bootstrap_mean: 0.2928
- CI 95%: [0.2880, 0.2979]
- weighted_value (LoE factor 0.60): 0.1756
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9820
- CR: 1.0183
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9341
- rmse_abm_no_ode: 4.1484
- rmse_ode: 1.7962
- rmse_reduced: 6.8364
- threshold: 2.5948

### Calibración
- forcing_scale: 0.6500
- macro_coupling: 0.6511
- damping: 0.6241
- ode_alpha: 0.0310
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1943

## Fase real
- **overall_pass**: False

### EDI
- valor: -9.0837
- bootstrap_mean: -9.7582
- CI 95%: [-15.1846, -6.6466]
- weighted_value (LoE factor 0.60): -5.4502
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.6306
- external: 0.2956
- CR: 2.1331
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7607
- rmse_abm_no_ode: 0.1746
- rmse_ode: 3.6513
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

