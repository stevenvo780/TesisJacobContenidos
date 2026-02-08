# Reporte de Validación — Falsación: Exogeneidad

- generated_at: 2026-02-07T14:17:54.483388Z

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
- valor: -0.4009
- bootstrap_mean: -0.4026
- CI 95%: [-0.4909, -0.3199]
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9991
- external: 0.0202
- CR: 49.4923
- CR válido (>2.0): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6965
- rmse_ode: 0.8036
- rmse_reduced: 0.4972
- threshold: 0.4904

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.9671
- damping: 0.6425
- ode_alpha: 0.0337
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3778

