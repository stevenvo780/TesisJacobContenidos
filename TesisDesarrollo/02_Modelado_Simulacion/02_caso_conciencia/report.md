# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T18:53:33.519955Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0183
- bootstrap_mean: 0.0181
- CI 95%: [0.0100, 0.0262]
- weighted_value (LoE factor 0.20): 0.0037
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.5380
- external: 0.6273
- CR: 0.8576
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1018
- rmse_abm_no_ode: 1.1223
- rmse_ode: 1.0791
- rmse_reduced: 1.1208
- threshold: 1.0629

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1368
- ode_coupling_strength: 0.1094
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3109
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0361
- bootstrap_mean: -0.0377
- CI 95%: [-0.0610, -0.0101]
- weighted_value (LoE factor 0.20): -0.0072
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7687
- external: 0.8211
- CR: 0.9362
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7437
- rmse_abm_no_ode: 0.7177
- rmse_ode: 1.7348
- rmse_reduced: 1.3440
- threshold: 0.6211

### Calibración
- forcing_scale: 0.4355
- macro_coupling: 0.0725
- ode_coupling_strength: 0.0580
- abm_feedback_gamma: 0.0500
- damping: 0.1736
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8698
- ode_rolling: None

