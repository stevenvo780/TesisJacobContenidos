# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-08T21:17:49.183271

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.7062
- bootstrap_mean: -3.7280
- CI 95%: [-4.2561, -3.2589]
- weighted_value (LoE factor 0.20): -0.7412
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9980
- external: 0.8340
- CR: 1.1966
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3413
- rmse_abm_no_ode: 0.7100
- rmse_ode: 3.8104
- rmse_reduced: 2.5605
- threshold: 0.9246

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

