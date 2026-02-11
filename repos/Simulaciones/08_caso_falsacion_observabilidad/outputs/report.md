# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-11T00:09:01.049176

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1431
- bootstrap_mean: 0.1432
- CI 95%: [0.1370, 0.1503]
- weighted_value (LoE factor 0.20): 0.0286
- válido (0.30-0.90): False
- detrended_edi: 0.1431
- trend_ratio: 1.000
- trend_r2: 0.513

### Symploké y CR
- internal: 0.9979
- external: 0.9928
- CR: 1.0052
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1866
- rmse_abm_no_ode: 0.7047
- rmse_ode: 3.7924
- rmse_reduced: 2.5518
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
- ode_rolling: None

### Interpretación
**Control de falsación.** El rechazo del EDI es el resultado esperado y valida la sensibilidad del protocolo.

