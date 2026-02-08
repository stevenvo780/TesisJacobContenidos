# Reporte de Validación — Cambio de Paradigmas Científicos

- generated_at: 2026-02-07T08:36:22.673335Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7613
- bootstrap_mean: 0.7614
- CI 95%: [0.7580, 0.7648]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0001
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1375
- rmse_ode: 2.2531
- rmse_reduced: 4.7653
- threshold: 1.4611

### Calibración
- forcing_scale: 0.3496
- macro_coupling: 0.8098
- damping: 0.5167
- ode_alpha: 0.0048
- ode_beta: 0.5708
- assimilation_strength: 0.0000
- calibration_rmse: 0.1376

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.8633
- bootstrap_mean: 0.8634
- CI 95%: [0.8598, 0.8671]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0001
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5229
- rmse_ode: 1.0964
- rmse_reduced: 3.8247
- threshold: 1.0348

### Calibración
- forcing_scale: 0.5234
- macro_coupling: 0.3933
- damping: 0.7810
- ode_alpha: 0.2509
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1484

