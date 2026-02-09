# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-08T22:39:43.202396

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.7512
- bootstrap_mean: -3.7786
- CI 95%: [-4.3485, -3.2775]
- weighted_value (LoE factor 0.20): -0.7502
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9979
- external: 0.8407
- CR: 1.1870
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.2842
- rmse_abm_no_ode: 0.6912
- rmse_ode: 3.7406
- rmse_reduced: 2.5521
- threshold: 0.9209

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

