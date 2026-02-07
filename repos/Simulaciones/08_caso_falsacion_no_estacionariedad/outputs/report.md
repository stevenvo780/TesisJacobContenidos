# Reporte de Validación — Falsación: No-Estacionariedad

- generated_at: 2026-02-07T14:21:48.393779Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7041
- bootstrap_mean: 0.7074
- CI 95%: [0.6355, 0.7754]
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
- rmse_abm: 0.8958
- rmse_ode: 0.8802
- rmse_reduced: 3.0272
- threshold: 1.1951

### Calibración
- forcing_scale: 0.5916
- macro_coupling: 0.1000
- damping: 0.9500
- ode_alpha: 0.3976
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6965

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0902
- bootstrap_mean: 0.0903
- CI 95%: [0.0280, 0.1567]
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9956
- external: 0.0313
- CR: 31.8461
- CR válido (>2.0): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6784
- rmse_ode: 0.8582
- rmse_reduced: 0.7456
- threshold: 0.6415

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.6289
- ode_alpha: 0.0315
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4461

