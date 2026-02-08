# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-08T21:29:06.336374Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0001
- bootstrap_mean: 0.0001
- CI 95%: [-0.0001, 0.0003]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.0193
- external: 0.0507
- CR: 0.3802
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: False
- c5_uncertainty: False

### Errores
- rmse_abm: 0.9347
- rmse_abm_no_ode: 0.9348
- rmse_ode: 0.9348
- rmse_reduced: 0.9348
- threshold: 0.9348

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.8876
- damping: 0.6032
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9999

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0939
- bootstrap_mean: 0.0988
- CI 95%: [0.0376, 0.1901]
- weighted_value (LoE factor 0.20): 0.0188
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9745
- external: 0.9878
- CR: 0.9866
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.6306
- rmse_abm_no_ode: 5.1104
- rmse_ode: 4.5218
- rmse_reduced: 4.5220
- threshold: 4.3680

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6375
- damping: 0.9312
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4389

