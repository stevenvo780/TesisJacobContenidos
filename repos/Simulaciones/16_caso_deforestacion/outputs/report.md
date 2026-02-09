# Reporte de Validación — Deforestación (SLEUTH + Stock Dynamics)

- generated_at: 2026-02-09T01:31:28.881995Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0001
- bootstrap_mean: 0.0001
- CI 95%: [0.0000, 0.0001]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0153
- external: 0.0263
- CR: 0.5823
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5351
- rmse_abm_no_ode: 3.5354
- rmse_ode: 3.1314
- rmse_reduced: 3.5421
- threshold: 2.4919

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0218

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0079
- bootstrap_mean: 0.0079
- CI 95%: [0.0060, 0.0098]
- weighted_value (LoE factor 0.20): 0.0016
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.2530
- external: 0.1262
- CR: 2.0050
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3636
- rmse_abm_no_ode: 1.3745
- rmse_ode: 0.9120
- rmse_reduced: 1.3640
- threshold: 0.2596

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0182
- ode_beta: 0.3702
- assimilation_strength: 0.0000
- calibration_rmse: 0.8844

