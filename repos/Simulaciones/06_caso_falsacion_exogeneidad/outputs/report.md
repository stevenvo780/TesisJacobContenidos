# Reporte de Validación — Falsación: Exogeneidad

- generated_at: 2026-02-10T23:41:12.167691

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0052
- bootstrap_mean: 0.0052
- CI 95%: [0.0021, 0.0086]
- weighted_value (LoE factor 0.20): 0.0010
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9983
- external: 0.9927
- CR: 1.0056
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1646
- rmse_abm_no_ode: 2.2942
- rmse_ode: 3.8442
- rmse_reduced: 2.1760
- threshold: 0.1595

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

