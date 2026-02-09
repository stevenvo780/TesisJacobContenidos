# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T02:50:51.071649Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1737
- bootstrap_mean: 0.1756
- CI 95%: [0.1552, 0.2026]
- weighted_value (LoE factor 0.80): 0.1390
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9993
- external: 0.9988
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4028
- rmse_abm_no_ode: 2.9079
- rmse_ode: 1.6136
- rmse_reduced: 5.1575
- threshold: 1.7106

### Calibración
- forcing_scale: 0.9109
- macro_coupling: 0.5043
- damping: 0.9500
- ode_alpha: 0.3897
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4524

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0037
- bootstrap_mean: 0.0036
- CI 95%: [-0.0146, 0.0192]
- weighted_value (LoE factor 0.80): 0.0030
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9581
- CR: 1.0437
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.5305
- rmse_abm_no_ode: 34.6601
- rmse_ode: 34.9228
- rmse_reduced: 40.8515
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5962
- macro_coupling: 1.0000
- damping: 0.2894
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5975

