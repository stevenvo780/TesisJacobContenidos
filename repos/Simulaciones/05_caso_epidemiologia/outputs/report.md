# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-09T16:14:05.279853Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4457
- bootstrap_mean: 0.4401
- CI 95%: [0.3611, 0.5145]
- weighted_value (LoE factor 0.20): 0.0891
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.3949
- external: 0.2630
- CR: 1.5012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.3625
- rmse_abm_no_ode: 4.2623
- rmse_ode: 0.4775
- rmse_reduced: 15.2230
- threshold: 0.1000

### Calibración
- forcing_scale: 1.0000
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0068
- ode_beta: 0.8095
- assimilation_strength: 0.0000
- calibration_rmse: 20.1559

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: -0.0004
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.5221
- rmse_abm_no_ode: 4.5221
- rmse_ode: 4606.4346
- rmse_reduced: 13.8782
- threshold: 4.3680

### Calibración
- forcing_scale: 0.1000
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

