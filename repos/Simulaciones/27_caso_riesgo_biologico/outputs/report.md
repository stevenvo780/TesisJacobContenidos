# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-09T16:04:20.954509Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4090
- bootstrap_mean: 0.4169
- CI 95%: [0.3406, 0.4910]
- weighted_value (LoE factor 0.80): 0.3272
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9966
- external: 0.9834
- CR: 1.0135
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0052
- rmse_abm_no_ode: 1.7008
- rmse_ode: 0.7150
- rmse_reduced: 2.4982
- threshold: 0.7584

### Calibración
- forcing_scale: 0.3518
- macro_coupling: 0.8851
- damping: 0.5266
- ode_alpha: 0.3062
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7417

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4138
- bootstrap_mean: 0.3797
- CI 95%: [0.1188, 0.5266]
- weighted_value (LoE factor 0.80): 0.3310
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9972
- CR: 1.0027
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4750
- rmse_abm_no_ode: 0.8103
- rmse_ode: 1.1552
- rmse_reduced: 2.1157
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2904
- damping: 0.6059
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1920

