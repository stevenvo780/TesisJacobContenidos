# Reporte de Validación — Políticas Estratégicas (WGI Regulatory Quality)

- generated_at: 2026-02-06T21:58:44.629253Z

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
- valor: 0.2895
- bootstrap_mean: 0.2782
- CI 95%: [-0.0478, 0.4879]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9266
- CR: 1.0791
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0186
- rmse_ode: 1.9331
- rmse_reduced: 2.8412
- threshold: 0.9802

### Calibración
- forcing_scale: 0.1651
- macro_coupling: 0.0732
- damping: 0.1745
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8977

