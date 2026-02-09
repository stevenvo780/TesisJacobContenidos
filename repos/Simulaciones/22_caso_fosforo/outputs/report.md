# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T17:51:55.564947Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3567
- bootstrap_mean: 0.3596
- CI 95%: [0.3297, 0.3985]
- weighted_value (LoE factor 0.60): 0.2140
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9949
- CR: 1.0050
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8594
- rmse_abm_no_ode: 1.3359
- rmse_ode: 0.5559
- rmse_reduced: 3.5591
- threshold: 0.8987

### Calibración
- forcing_scale: 0.9465
- macro_coupling: 0.2935
- ode_coupling_strength: 0.2348
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1286
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2112

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.0691
- bootstrap_mean: -3.1013
- CI 95%: [-3.8195, -2.4885]
- weighted_value (LoE factor 0.60): -1.8415
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9985
- external: 0.9159
- CR: 1.0902
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3378
- rmse_abm_no_ode: 0.3288
- rmse_ode: 3.9051
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9385
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2782

