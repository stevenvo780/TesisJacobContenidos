# Reporte de Validación — Acidificación Oceánica (CO2SYS + Revelle Factor)

- generated_at: 2026-02-09T14:19:59.744230Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1407
- bootstrap_mean: -0.1404
- CI 95%: [-0.1511, -0.1308]
- weighted_value (LoE factor 0.20): -0.0281
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9974
- external: 0.4294
- CR: 2.3229
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.6123
- rmse_abm_no_ode: 1.4135
- rmse_ode: 8.3145
- rmse_reduced: 2.0224
- threshold: 1.0107

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1323
- damping: 0.0000
- ode_alpha: 0.0170
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3061

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0020
- bootstrap_mean: -0.0030
- CI 95%: [-0.0111, 0.0005]
- weighted_value (LoE factor 0.20): -0.0004
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9994
- external: 0.8640
- CR: 1.1566
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3497
- rmse_abm_no_ode: 3.3431
- rmse_ode: 9.2096
- rmse_reduced: 3.2742
- threshold: 2.3256

### Calibración
- forcing_scale: 0.8576
- macro_coupling: 0.2220
- damping: 0.0000
- ode_alpha: 0.1492
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9496

