# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T01:51:18.147279Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4847
- bootstrap_mean: 0.4763
- CI 95%: [0.2365, 0.6986]
- weighted_value (LoE factor 0.60): 0.2908
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9997
- external: 0.9850
- CR: 1.0150
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2667
- rmse_abm_no_ode: 0.5176
- rmse_ode: 1.3261
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
- valor: -2.1628
- bootstrap_mean: -2.1429
- CI 95%: [-2.4600, -1.7253]
- weighted_value (LoE factor 0.60): -1.2977
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.7905
- external: 0.2026
- CR: 3.9015
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 2.7654
- rmse_abm_no_ode: 0.8744
- rmse_ode: 2.4122
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

