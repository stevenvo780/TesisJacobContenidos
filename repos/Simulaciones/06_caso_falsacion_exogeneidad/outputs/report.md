# Reporte de Validación — Falsación: Exogeneidad

- generated_at: 2026-02-08T20:39:14.949425Z

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
- valor: 0.4692
- bootstrap_mean: 0.4702
- CI 95%: [0.4491, 0.4909]
- weighted_value (LoE factor 0.20): 0.0938
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9990
- CR: 1.0009
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.0547
- rmse_abm_no_ode: 1.9869
- rmse_ode: 0.9564
- rmse_reduced: 0.7016
- threshold: 0.5955

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6156
- damping: 0.8606
- ode_alpha: 0.0962
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5052

