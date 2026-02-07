# Reporte de Validación — Justicia (Rule of Law WGI)

- generated_at: 2026-02-06T21:57:54.157525Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2250
- bootstrap_mean: 0.2281
- CI 95%: [0.1860, 0.2729]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9996
- external: 0.9430
- CR: 1.0600
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5911
- rmse_ode: 0.8161
- rmse_reduced: 2.0531
- threshold: 0.6722

### Calibración
- forcing_scale: 0.0456
- macro_coupling: 0.8770
- damping: 0.1685
- ode_alpha: 0.4001
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9870

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3547
- bootstrap_mean: -0.3537
- CI 95%: [-0.4647, -0.2435]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.8190
- CR: 1.2209
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8479
- rmse_ode: 2.8987
- rmse_reduced: 2.1023
- threshold: 1.1597

### Calibración
- forcing_scale: 0.1343
- macro_coupling: 0.8555
- damping: 0.1657
- ode_alpha: 0.1626
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9548

