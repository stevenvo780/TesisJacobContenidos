# Reporte de Validación — Erosión Dialéctica

- generated_at: 2026-02-07T10:42:59.375646Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7275
- bootstrap_mean: 0.7276
- CI 95%: [0.7213, 0.7345]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0003
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4225
- rmse_ode: 1.7845
- rmse_reduced: 5.2198
- threshold: 1.7090

### Calibración
- forcing_scale: 0.3786
- macro_coupling: 0.5903
- damping: 0.5484
- ode_alpha: 0.0192
- ode_beta: 0.8210
- assimilation_strength: 0.0000
- calibration_rmse: 0.1475

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9231
- bootstrap_mean: 0.9232
- CI 95%: [0.9171, 0.9300]
- válido (0.30-0.90): False

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
- rmse_abm: 0.2596
- rmse_ode: 1.2640
- rmse_reduced: 3.3746
- threshold: 0.8592

### Calibración
- forcing_scale: 0.6338
- macro_coupling: 0.1884
- damping: 0.9500
- ode_alpha: 0.2911
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1283

