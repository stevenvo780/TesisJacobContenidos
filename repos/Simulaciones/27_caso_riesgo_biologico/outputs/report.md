# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T02:22:13.086646Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1972
- bootstrap_mean: 0.1977
- CI 95%: [0.1719, 0.2310]
- weighted_value (LoE factor 0.80): 0.1577
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9997
- external: 0.9860
- CR: 1.0140
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.8173
- rmse_abm_no_ode: 1.0180
- rmse_ode: 0.8019
- rmse_reduced: 1.2918
- threshold: 0.1522

### Calibración
- forcing_scale: 0.8353
- macro_coupling: 0.6283
- damping: 0.8107
- ode_alpha: 0.0107
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2475

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.6297
- bootstrap_mean: -4.0780
- CI 95%: [-7.4826, -1.7697]
- weighted_value (LoE factor 0.80): -2.9037
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8602
- external: 0.1227
- CR: 7.0108
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9726
- rmse_abm_no_ode: 0.4261
- rmse_ode: 3.9146
- rmse_reduced: 2.0986
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.9739
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1210

