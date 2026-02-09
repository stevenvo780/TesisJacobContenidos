# Reporte de Validación — Síndrome de Kessler (NASA LEGEND + ORDEM)

- generated_at: 2026-02-09T04:22:54.569276Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -16.7572
- bootstrap_mean: -16.6822
- CI 95%: [-18.3912, -14.5364]
- weighted_value (LoE factor 0.20): -3.3514
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8323
- external: 0.8127
- CR: 1.0241
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 11600777.0750
- rmse_abm_no_ode: 653299.1466
- rmse_ode: 7501170013604411.0000
- rmse_reduced: 700761.2854
- threshold: 8.9265

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.1132
- ode_beta: 0.7548
- assimilation_strength: 0.0000
- calibration_rmse: 163478.4258

## Fase real
- **overall_pass**: False

### EDI
- valor: -16.6351
- bootstrap_mean: -16.5605
- CI 95%: [-18.2412, -14.4389]
- weighted_value (LoE factor 0.20): -3.3270
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8324
- external: 0.8171
- CR: 1.0187
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 11626563.9536
- rmse_abm_no_ode: 659284.6462
- rmse_ode: 12877165873998730.0000
- rmse_reduced: 699352.7889
- threshold: 24.6834

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.2575
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 165252.9292

