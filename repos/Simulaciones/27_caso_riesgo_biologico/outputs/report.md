# Reporte de Validación — Riesgo Biológico Global (Woolhouse Zoonotic)

- generated_at: 2026-02-09T03:01:35.555713Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.2982
- bootstrap_mean: -1.2970
- CI 95%: [-1.5139, -1.0578]
- weighted_value (LoE factor 0.80): -1.0386
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9922
- CR: 1.0079
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9138
- rmse_abm_no_ode: 0.3976
- rmse_ode: 4.2706
- rmse_reduced: 2.6869
- threshold: 0.1694

### Calibración
- forcing_scale: 0.4669
- macro_coupling: 0.1000
- damping: 0.4557
- ode_alpha: 0.0171
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1125

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.8857
- bootstrap_mean: -2.1841
- CI 95%: [-4.6323, -0.7053]
- weighted_value (LoE factor 0.80): -1.5085
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.8088
- external: 0.1762
- CR: 4.5909
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2295
- rmse_abm_no_ode: 0.4261
- rmse_ode: 2.4825
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

