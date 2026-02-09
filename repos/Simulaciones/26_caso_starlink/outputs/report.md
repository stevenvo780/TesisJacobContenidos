# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T01:46:16.143075Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -4.4055
- bootstrap_mean: -4.4091
- CI 95%: [-4.6246, -4.2314]
- weighted_value (LoE factor 0.80): -3.5244
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9544
- CR: 1.0478
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.0899
- rmse_abm_no_ode: 1.6816
- rmse_ode: 28.3789
- rmse_reduced: 4.2297
- threshold: 1.1779

### Calibración
- forcing_scale: 0.2938
- macro_coupling: 0.1590
- damping: 0.2823
- ode_alpha: 0.0067
- ode_beta: 0.4901
- assimilation_strength: 0.0000
- calibration_rmse: 0.1368

## Fase real
- **overall_pass**: False

### EDI
- valor: -107.5397
- bootstrap_mean: -107.7654
- CI 95%: [-128.3601, -90.6683]
- weighted_value (LoE factor 0.80): -86.0318
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9429
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
- rmse_abm: 0.0137
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.1304
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

