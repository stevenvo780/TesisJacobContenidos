# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T04:16:14.432812Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1034
- bootstrap_mean: 0.1003
- CI 95%: [0.0319, 0.1685]
- weighted_value (LoE factor 0.20): 0.0207
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8809
- external: 0.7202
- CR: 1.2232
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6921
- rmse_abm_no_ode: 0.7719
- rmse_ode: 0.9827
- rmse_reduced: 0.7473
- threshold: 0.2588

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
- internal: 0.9622
- external: 0.8752
- CR: 1.0993
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8134
- rmse_abm_no_ode: 1.8134
- rmse_ode: 1.5198
- rmse_reduced: 1.8134
- threshold: 0.9943

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

