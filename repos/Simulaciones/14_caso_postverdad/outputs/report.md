# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-09T15:37:06.365762Z

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
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0214
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0027

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0031
- bootstrap_mean: 0.0030
- CI 95%: [0.0006, 0.0058]
- weighted_value (LoE factor 0.20): 0.0006
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8027
- external: 0.7605
- CR: 1.0555
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9566
- rmse_abm_no_ode: 2.9658
- rmse_ode: 2.9096
- rmse_reduced: 2.9720
- threshold: 1.1553

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.7794

