# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-09T09:19:56.191604

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.8473
- bootstrap_mean: -3.8702
- CI 95%: [-4.4127, -3.3584]
- weighted_value (LoE factor 0.20): -0.7695
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9981
- external: 0.8138
- CR: 1.2265
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4078
- rmse_abm_no_ode: 0.7030
- rmse_ode: 3.8902
- rmse_reduced: 2.5252
- threshold: 0.9162

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

