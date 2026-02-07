# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-07T07:29:46.687240Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.6869
- bootstrap_mean: 0.6870
- CI 95%: [0.6809, 0.6936]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1139
- rmse_ode: 1.8845
- rmse_reduced: 6.7513
- threshold: 2.5747

### Calibración
- forcing_scale: 0.3214
- macro_coupling: 0.9249
- damping: 0.4669
- ode_alpha: 0.0241
- ode_beta: 0.8965
- assimilation_strength: 0.0000
- calibration_rmse: 0.1487

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.4341
- bootstrap_mean: 0.4316
- CI 95%: [0.3740, 0.4875]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9995
- CR: 1.0003
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5626
- rmse_ode: 1.5087
- rmse_reduced: 0.9942
- threshold: 0.9906

### Calibración
- forcing_scale: 1.5945
- macro_coupling: 0.4711
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5577

