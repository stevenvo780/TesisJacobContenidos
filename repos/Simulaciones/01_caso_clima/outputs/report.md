# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-09T03:04:48.065604Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.6424
- rmse_abm_no_ode: 3.6424
- rmse_ode: 6.0653
- rmse_reduced: 6.7513
- threshold: 2.5747

### Calibración
- forcing_scale: 0.3778
- macro_coupling: 0.8280
- damping: 0.5550
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1493

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9975
- external: 0.9980
- CR: 0.9995
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.1922
- rmse_abm_no_ode: 1.1922
- rmse_ode: 1.7271
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6911
- damping: 0.9500
- ode_alpha: 0.0060
- ode_beta: 0.1000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6353

