# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T01:52:58.994096Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -7.4672
- bootstrap_mean: -7.4686
- CI 95%: [-7.5677, -7.3790]
- weighted_value (LoE factor 0.80): -5.9738
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9352
- CR: 1.0692
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 10.3997
- rmse_abm_no_ode: 1.2282
- rmse_ode: 26.4893
- rmse_reduced: 0.9579
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9461
- macro_coupling: 0.5201
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2173

## Fase real
- **overall_pass**: False

### EDI
- valor: -194.8058
- bootstrap_mean: -195.1227
- CI 95%: [-228.4708, -163.4568]
- weighted_value (LoE factor 0.80): -155.8446
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8724
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0248
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.2354
- rmse_reduced: 0.0001
- threshold: 0.1000

### Calibración
- forcing_scale: 0.1239
- macro_coupling: 0.1073
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0002

