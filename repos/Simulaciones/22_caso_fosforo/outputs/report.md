# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T01:40:53.145463Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0394
- bootstrap_mean: 0.0364
- CI 95%: [-0.0378, 0.0855]
- weighted_value (LoE factor 0.60): 0.0236
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9997
- external: 0.9827
- CR: 1.0174
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4528
- rmse_abm_no_ode: 1.5124
- rmse_ode: 1.5330
- rmse_reduced: 3.6779
- threshold: 0.9054

### Calibración
- forcing_scale: 0.9404
- macro_coupling: 0.3765
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2426

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.6907
- bootstrap_mean: -0.6970
- CI 95%: [-1.1486, -0.3189]
- weighted_value (LoE factor 0.60): -0.4144
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9968
- external: 0.9691
- CR: 1.0286
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5531
- rmse_abm_no_ode: 0.3271
- rmse_ode: 1.1576
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9398
- macro_coupling: 0.6239
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2782

