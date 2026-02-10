# Reporte de Validación — Falsación: No-Estacionariedad

- generated_at: 2026-02-10T14:21:39.941847

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -4.7130
- CI 95%: [-5.4817, -4.0556]
- weighted_value (LoE factor 0.20): -0.2000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.991

### Symploké y CR
- internal: 0.9990
- external: 0.9939
- CR: 1.0051
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.1259
- rmse_abm_no_ode: 0.5486
- rmse_ode: 5.3452
- rmse_reduced: 3.6765
- threshold: 1.0297

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

