# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-09T18:26:43.840748Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: -0.0133
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8853
- rmse_abm_no_ode: 2.8853
- rmse_ode: 1.9349
- rmse_reduced: 2.8853
- threshold: 0.6609

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0214
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0027
- ode_rolling: None

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0012
- bootstrap_mean: 0.0011
- CI 95%: [0.0000, 0.0020]
- weighted_value (LoE factor 0.20): 0.0002
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.7932
- external: 0.7522
- CR: 1.0544
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9622
- rmse_abm_no_ode: 2.9658
- rmse_ode: 2.9096
- rmse_reduced: 2.9720
- threshold: 1.1553

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.7794
- ode_rolling: None

