# Reporte de Validación — Postverdad (SIS Infodemic)

- generated_at: 2026-02-09T01:18:34.553147Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0025
- bootstrap_mean: 0.0026
- CI 95%: [0.0018, 0.0034]
- weighted_value (LoE factor 0.20): 0.0005
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0836
- external: 0.0974
- CR: 0.8575
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0412
- rmse_abm_no_ode: 2.0464
- rmse_ode: 2.3958
- rmse_reduced: 2.0484
- threshold: 0.6609

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 1.2773

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0025
- bootstrap_mean: 0.0026
- CI 95%: [0.0018, 0.0034]
- weighted_value (LoE factor 0.20): 0.0005
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0836
- external: 0.0974
- CR: 0.8575
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0412
- rmse_abm_no_ode: 2.0464
- rmse_ode: 2.3958
- rmse_reduced: 2.0484
- threshold: 0.6609

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 1.2773

