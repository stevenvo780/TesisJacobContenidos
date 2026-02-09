# Reporte de Validación — Erosión Dialéctica (Abrams-Strogatz)

- generated_at: 2026-02-09T01:51:46.852082Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1386
- bootstrap_mean: 0.1381
- CI 95%: [0.1202, 0.1538]
- weighted_value (LoE factor 0.60): 0.0831
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9845
- external: 0.9846
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.1255
- rmse_abm_no_ode: 1.3066
- rmse_ode: 0.8930
- rmse_reduced: 1.1107
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9121
- macro_coupling: 0.6153
- damping: 0.9199
- ode_alpha: 0.0350
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1630

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.7689
- bootstrap_mean: -4.0017
- CI 95%: [-6.4388, -2.4282]
- weighted_value (LoE factor 0.60): -2.2613
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.4684
- external: 0.3562
- CR: 1.3149
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8327
- rmse_abm_no_ode: 0.1746
- rmse_ode: 0.7527
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

