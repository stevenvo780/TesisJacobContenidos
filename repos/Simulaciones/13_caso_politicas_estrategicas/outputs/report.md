# Reporte de Validación — Políticas Estratégicas Globales

- generated_at: 2026-02-08T20:49:44.022076Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6986
- bootstrap_mean: 0.6980
- CI 95%: [0.6680, 0.7286]
- weighted_value (LoE factor 0.20): 0.1397
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9967
- CR: 1.0031
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.1743
- rmse_abm_no_ode: 0.5782
- rmse_ode: 1.3907
- rmse_reduced: 1.7375
- threshold: 0.2904

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5409
- damping: 0.9500
- ode_alpha: 0.0545
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2630

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.4956
- bootstrap_mean: -2.4447
- CI 95%: [-3.3708, -1.5755]
- weighted_value (LoE factor 0.20): -0.4991
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9416
- external: 0.0016
- CR: 576.8935
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 10.7981
- rmse_abm_no_ode: 3.0890
- rmse_ode: 0.6550
- rmse_reduced: 1.0256
- threshold: 0.1639

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.9456
- ode_alpha: 0.1057
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2881

