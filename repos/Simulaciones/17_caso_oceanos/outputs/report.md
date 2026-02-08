# Reporte de Validación — Temperatura Oceánica Global

- generated_at: 2026-02-08T20:41:24.526056Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3955
- bootstrap_mean: 0.3958
- CI 95%: [0.3895, 0.4020]
- weighted_value (LoE factor 0.20): 0.0791
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9982
- CR: 1.0018
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6071
- rmse_abm_no_ode: 1.0044
- rmse_ode: 0.1695
- rmse_reduced: 3.8166
- threshold: 1.0540

### Calibración
- forcing_scale: 0.6424
- macro_coupling: 0.4694
- damping: 0.6308
- ode_alpha: 0.1405
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1169

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.0749
- bootstrap_mean: -2.0749
- CI 95%: [-2.0751, -2.0746]
- weighted_value (LoE factor 0.20): -0.4150
- válido (0.30-0.90): False

### Symploké y CR
- internal: -1.0000
- external: -0.0000
- CR: 42194341.3494
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 47786.7907
- rmse_abm_no_ode: 15540.8073
- rmse_ode: 1.4014
- rmse_reduced: 2.0497
- threshold: 1.0498

### Calibración
- forcing_scale: 0.6385
- macro_coupling: 0.8272
- damping: 0.8281
- ode_alpha: 0.1307
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9647

