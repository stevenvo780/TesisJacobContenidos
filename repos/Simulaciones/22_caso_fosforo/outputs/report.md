# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T02:02:21.642046Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5320
- bootstrap_mean: 0.5320
- CI 95%: [0.4617, 0.6010]
- weighted_value (LoE factor 0.60): 0.3192
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9866
- CR: 1.0134
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3669
- rmse_abm_no_ode: 0.7838
- rmse_ode: 1.0949
- rmse_reduced: 2.7961
- threshold: 0.7146

### Calibración
- forcing_scale: 0.9351
- macro_coupling: 0.3008
- damping: 0.9500
- ode_alpha: 0.3090
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2793

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.4308
- bootstrap_mean: -0.4355
- CI 95%: [-1.2084, 0.1239]
- weighted_value (LoE factor 0.60): -0.2585
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9952
- external: 0.9601
- CR: 1.0365
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4681
- rmse_abm_no_ode: 0.3271
- rmse_ode: 1.2915
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9398
- macro_coupling: 0.6239
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2782

