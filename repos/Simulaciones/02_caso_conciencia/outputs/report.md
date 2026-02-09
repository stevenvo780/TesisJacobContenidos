# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T02:54:06.474993Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1552
- bootstrap_mean: 0.1502
- CI 95%: [0.0669, 0.2330]
- weighted_value (LoE factor 0.20): 0.0310
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8614
- external: 0.7040
- CR: 1.2236
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6108
- rmse_abm_no_ode: 0.7231
- rmse_ode: 0.9025
- rmse_reduced: 0.6794
- threshold: 0.2371

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
- internal: 0.9491
- external: 0.7841
- CR: 1.2104
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6046
- rmse_abm_no_ode: 1.6046
- rmse_ode: 1.4173
- rmse_reduced: 1.6046
- threshold: 0.9280

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

