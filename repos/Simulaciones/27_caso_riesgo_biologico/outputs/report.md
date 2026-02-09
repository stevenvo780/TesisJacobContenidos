# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T01:41:31.715455Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.7931
- bootstrap_mean: -0.8021
- CI 95%: [-1.0585, -0.5886]
- weighted_value (LoE factor 0.80): -0.6345
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.2802
- CR: 3.5695
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5562
- rmse_abm_no_ode: 0.8679
- rmse_ode: nan
- rmse_reduced: 1.5562
- threshold: 0.2518

### Calibración
- forcing_scale: 0.7158
- macro_coupling: 0.7819
- damping: 0.7006
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2331

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.9767
- bootstrap_mean: -1.1169
- CI 95%: [-2.6545, -0.3351]
- weighted_value (LoE factor 0.80): -0.7814
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.7623
- external: 0.2146
- CR: 3.5530
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8422
- rmse_abm_no_ode: 0.4261
- rmse_ode: 1.6405
- rmse_reduced: 2.0986
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9195
- macro_coupling: 0.9739
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.1210

