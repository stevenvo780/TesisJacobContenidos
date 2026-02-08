# Reporte de Validación — Ecosistema IoT Global

- generated_at: 2026-02-08T20:55:50.894812Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.9898
- bootstrap_mean: -0.9907
- CI 95%: [-1.0823, -0.9083]
- weighted_value (LoE factor 0.20): -0.1980
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9981
- CR: 1.0019
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0651
- rmse_abm_no_ode: 0.5353
- rmse_ode: 1.4342
- rmse_reduced: 1.8176
- threshold: 0.3400

### Calibración
- forcing_scale: 0.1629
- macro_coupling: 0.7320
- damping: 0.1678
- ode_alpha: 0.0586
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2572

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0024
- bootstrap_mean: -0.0025
- CI 95%: [-0.0048, -0.0005]
- weighted_value (LoE factor 0.20): -0.0005
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9963
- CR: 1.0037
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 36.1692
- rmse_abm_no_ode: 36.0825
- rmse_ode: 36.8750
- rmse_reduced: 39.5206
- threshold: 10.8708

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1088
- damping: 0.7446
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.4979

