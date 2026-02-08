# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-08T20:46:32.743910Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.7955
- bootstrap_mean: -0.7998
- CI 95%: [-1.1354, -0.5620]
- weighted_value (LoE factor 0.20): -0.1591
- válido (0.30-0.90): False

### Symploké y CR
- internal: -1.0000
- external: 0.0001
- CR: 16981.3851
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.9085
- rmse_abm_no_ode: 1.0630
- rmse_ode: 1.2308
- rmse_reduced: 1.5980
- threshold: 0.2755

### Calibración
- forcing_scale: 0.9824
- macro_coupling: 0.7164
- damping: 0.9500
- ode_alpha: 0.0559
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2503

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3745
- bootstrap_mean: -0.3761
- CI 95%: [-0.4072, -0.3479]
- weighted_value (LoE factor 0.20): -0.0749
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: -0.0871
- CR: 11.4828
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8776
- rmse_abm_no_ode: 1.3660
- rmse_ode: nan
- rmse_reduced: 1.8776
- threshold: 1.0186

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.9285
- damping: 0.4161
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6519

