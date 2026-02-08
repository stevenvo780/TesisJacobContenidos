# Reporte de Validación — Fuga de Cerebros Global

- generated_at: 2026-02-07T09:20:16.601260Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7599
- bootstrap_mean: 0.7602
- CI 95%: [0.7566, 0.7644]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0001
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1190
- rmse_ode: 2.3775
- rmse_reduced: 4.6608
- threshold: 1.4042

### Calibración
- forcing_scale: 0.3912
- macro_coupling: 0.6336
- damping: 0.5746
- ode_alpha: 0.0057
- ode_beta: 0.5331
- assimilation_strength: 0.0000
- calibration_rmse: 0.1408

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.8807
- bootstrap_mean: 0.8809
- CI 95%: [0.8771, 0.8852]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0001
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4267
- rmse_ode: 1.1143
- rmse_reduced: 3.5778
- threshold: 0.9456

### Calibración
- forcing_scale: 0.5220
- macro_coupling: 0.6542
- damping: 0.7791
- ode_alpha: 0.2452
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1372

