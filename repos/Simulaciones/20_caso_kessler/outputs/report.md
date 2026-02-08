# Reporte de Validación — Síndrome de Kessler

- generated_at: 2026-02-08T20:43:02.767567Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -2.8572
- bootstrap_mean: -2.8601
- CI 95%: [-2.9832, -2.7419]
- weighted_value (LoE factor 0.20): -0.5714
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5566
- rmse_abm_no_ode: 0.4036
- rmse_ode: 2.6138
- rmse_reduced: 2.6310
- threshold: 0.4421

### Calibración
- forcing_scale: 0.5809
- macro_coupling: 0.6326
- damping: 0.5709
- ode_alpha: 0.0051
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0555

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.5320
- bootstrap_mean: -3.5382
- CI 95%: [-3.7629, -3.3165]
- weighted_value (LoE factor 0.20): -0.7064
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9987
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2199
- rmse_abm_no_ode: 0.2692
- rmse_ode: 3.1723
- rmse_reduced: 2.4621
- threshold: 0.4024

### Calibración
- forcing_scale: 0.9566
- macro_coupling: 0.4728
- damping: 0.9449
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0032

