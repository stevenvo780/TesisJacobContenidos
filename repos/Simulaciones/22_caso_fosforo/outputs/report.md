# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T14:45:52.011133Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3365
- bootstrap_mean: 0.3383
- CI 95%: [0.3144, 0.3683]
- weighted_value (LoE factor 0.60): 0.2019
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9954
- CR: 1.0045
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9498
- rmse_abm_no_ode: 1.4315
- rmse_ode: 0.4156
- rmse_reduced: 3.6084
- threshold: 0.9662

### Calibración
- forcing_scale: 0.9496
- macro_coupling: 0.3491
- damping: 0.9500
- ode_alpha: 0.1734
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2364

## Fase real
- **overall_pass**: False

### EDI
- valor: -4.8583
- bootstrap_mean: -4.9172
- CI 95%: [-5.9020, -4.2212]
- weighted_value (LoE factor 0.60): -2.9150
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9843
- external: 0.9692
- CR: 1.0156
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9165
- rmse_abm_no_ode: 0.3271
- rmse_ode: 4.3705
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

