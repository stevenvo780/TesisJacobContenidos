# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T16:17:44.323738Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3864
- bootstrap_mean: 0.3890
- CI 95%: [0.3603, 0.4243]
- weighted_value (LoE factor 0.60): 0.2318
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9935
- CR: 1.0064
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8200
- rmse_abm_no_ode: 1.3363
- rmse_ode: 0.5559
- rmse_reduced: 3.5591
- threshold: 0.8987

### Calibración
- forcing_scale: 0.9465
- macro_coupling: 0.3435
- damping: 0.9500
- ode_alpha: 0.1286
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2112

## Fase real
- **overall_pass**: False

### EDI
- valor: -4.2685
- bootstrap_mean: -4.3192
- CI 95%: [-5.1568, -3.7007]
- weighted_value (LoE factor 0.60): -2.5611
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9874
- external: 0.9845
- CR: 1.0030
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7235
- rmse_abm_no_ode: 0.3271
- rmse_ode: 3.9051
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

