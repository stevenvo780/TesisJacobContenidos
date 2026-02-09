# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-09T12:51:48.913083

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.1439
- bootstrap_mean: -2.1538
- CI 95%: [-2.5255, -1.8154]
- weighted_value (LoE factor 0.20): -0.4288
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9977
- external: 0.9942
- CR: 1.0036
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.2073
- rmse_abm_no_ode: 0.7021
- rmse_ode: 3.8161
- rmse_reduced: 2.5512
- threshold: 0.9158

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- ode_coupling_strength: 0.1600
- abm_feedback_gamma: 0.0500
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

