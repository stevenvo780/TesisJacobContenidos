# Reporte de Validación — Falsación: No-Estacionariedad

- generated_at: 2026-02-08T20:37:03.416816Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0122
- bootstrap_mean: 0.0119
- CI 95%: [-0.0315, 0.0488]
- weighted_value (LoE factor 0.20): 0.0024
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6211
- external: -0.1416
- CR: 4.3871
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2712
- rmse_abm_no_ode: 1.2869
- rmse_ode: 1.4274
- rmse_reduced: 1.2869
- threshold: 1.2689

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.5304
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9993

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.6650
- bootstrap_mean: -2.6647
- CI 95%: [-2.7235, -2.6110]
- weighted_value (LoE factor 0.20): -0.5330
- válido (0.30-0.90): False

### Symploké y CR
- internal: -1.0000
- external: -0.0000
- CR: 943804.9561
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 180.7323
- rmse_abm_no_ode: 49.3128
- rmse_ode: 0.6478
- rmse_reduced: 0.8170
- threshold: 0.6482

### Calibración
- forcing_scale: 0.7870
- macro_coupling: 1.0000
- damping: 0.6968
- ode_alpha: 0.0797
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3956

