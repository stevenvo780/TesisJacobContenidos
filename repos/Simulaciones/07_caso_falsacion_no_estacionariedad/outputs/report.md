# Reporte de Validación — Falsación: No-Estacionariedad

- generated_at: 2026-02-12T03:57:45.275786Z

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.8819
- bootstrap_mean: -0.8811
- CI 95%: [-0.9131, -0.8459]
- weighted_value (LoE factor 0.20): -0.1764
- válido (0.30-0.90): False
- detrended_edi: -0.8819
- trend_ratio: 1.000
- trend_r2: 0.945

### Symploké y CR
- internal: 0.9998
- external: 0.9944
- CR: 1.0054
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.0591
- rmse_abm_no_ode: 1.6255
- rmse_ode: 5.1132
- rmse_reduced: 3.5658
- threshold: 1.0132

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

