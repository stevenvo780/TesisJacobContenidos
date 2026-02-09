# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T02:06:00.581082Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.0606
- bootstrap_mean: -1.1099
- CI 95%: [-1.6621, -0.6845]
- weighted_value (LoE factor 0.60): -0.6364
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9666
- CR: 1.0344
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0666
- rmse_abm_no_ode: 0.5176
- rmse_ode: 4.7795
- rmse_reduced: 2.6779
- threshold: 0.6478

### Calibración
- forcing_scale: 0.9465
- macro_coupling: 0.3435
- damping: 0.9500
- ode_alpha: 0.3138
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3079

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.5647
- bootstrap_mean: -2.5359
- CI 95%: [-2.7816, -2.1012]
- weighted_value (LoE factor 0.60): -1.5388
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.7107
- external: 0.2503
- CR: 2.8397
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 3.1168
- rmse_abm_no_ode: 0.8744
- rmse_ode: 4.5003
- rmse_reduced: 1.0780
- threshold: 0.1357

### Calibración
- forcing_scale: 0.9487
- macro_coupling: 0.7718
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2739

