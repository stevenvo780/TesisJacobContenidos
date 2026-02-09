# Reporte de Validación — Finanzas (SPY)

- generated_at: 2026-02-09T17:51:53.202542Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0000, -0.0000]
- weighted_value (LoE factor 1.00): -0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.9866
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 20481509.0743
- rmse_abm_no_ode: 20481508.8624
- rmse_ode: 20481508.8351
- rmse_reduced: 20481508.9052
- threshold: 19219447.7270

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0012
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 4.7318

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0257
- bootstrap_mean: 0.0257
- CI 95%: [0.0223, 0.0288]
- weighted_value (LoE factor 1.00): 0.0257
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.9844
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 36.9584
- rmse_abm_no_ode: 37.9317
- rmse_ode: 29.7012
- rmse_reduced: 37.5564
- threshold: 1.1814

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0017
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 10.2667

