# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-09T17:00:06.613253

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.1340
- CI 95%: [-2.5032, -1.7969]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.513

### Symploké y CR
- internal: 0.9979
- external: 0.9933
- CR: 1.0046
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1935
- rmse_abm_no_ode: 0.7021
- rmse_ode: 3.7928
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
- ode_rolling: None

### Interpretación
Este es un caso de **falsación por diseño**. El rechazo del EDI es el resultado esperado y valida la sensibilidad del protocolo.

