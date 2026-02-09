# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-09T04:22:55.767442Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1482
- bootstrap_mean: -0.1510
- CI 95%: [-0.2101, -0.1013]
- weighted_value (LoE factor 0.20): -0.0296
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9796
- external: 0.5341
- CR: 1.8341
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4137
- rmse_abm_no_ode: 2.9730
- rmse_ode: 1.3662
- rmse_reduced: 2.8308
- threshold: 0.9858

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0068
- ode_beta: 0.7284
- assimilation_strength: 0.0000
- calibration_rmse: 2.1270

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0664
- bootstrap_mean: -0.0688
- CI 95%: [-0.1239, -0.0199]
- weighted_value (LoE factor 0.20): -0.0133
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9790
- external: 0.5030
- CR: 1.9465
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9122
- rmse_abm_no_ode: 2.7310
- rmse_ode: 0.8567
- rmse_reduced: 2.6002
- threshold: 1.1913

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0082
- ode_beta: 0.9450
- assimilation_strength: 0.0000
- calibration_rmse: 2.1528

