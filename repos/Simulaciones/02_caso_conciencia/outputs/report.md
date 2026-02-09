# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T04:43:33.042787Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1859
- bootstrap_mean: 0.1802
- CI 95%: [0.0812, 0.2805]
- weighted_value (LoE factor 0.20): 0.0372
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8631
- external: 0.7018
- CR: 1.2299
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4749
- rmse_abm_no_ode: 0.5834
- rmse_ode: 0.8187
- rmse_reduced: 0.5440
- threshold: 0.2408

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9610
- external: 0.6922
- CR: 1.3885
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.7920
- rmse_abm_no_ode: 1.7920
- rmse_ode: 1.6960
- rmse_reduced: 1.7920
- threshold: 0.9824

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

