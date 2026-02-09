# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T16:18:48.219251Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5640
- bootstrap_mean: 0.5645
- CI 95%: [0.5522, 0.5791]
- weighted_value (LoE factor 0.80): 0.4512
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9997
- external: 0.9941
- CR: 1.0056
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5584
- rmse_abm_no_ode: 1.2808
- rmse_ode: 0.9059
- rmse_reduced: 0.8072
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9625
- macro_coupling: 0.5500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2809

## Fase real
- **overall_pass**: False

### EDI
- valor: -546.5870
- bootstrap_mean: -545.5701
- CI 95%: [-616.3355, -478.6828]
- weighted_value (LoE factor 0.80): -437.2696
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9876
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
- rmse_abm: 0.0693
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.6585
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

