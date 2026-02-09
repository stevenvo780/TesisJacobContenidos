# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T03:04:32.494700Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1359
- bootstrap_mean: 0.1313
- CI 95%: [0.0524, 0.2083]
- weighted_value (LoE factor 0.20): 0.0272
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8648
- external: 0.7067
- CR: 1.2237
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6958
- rmse_abm_no_ode: 0.8052
- rmse_ode: 0.9834
- rmse_reduced: 0.7557
- threshold: 0.2902

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9782
- external: 0.8438
- CR: 1.1593
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6657
- rmse_abm_no_ode: 1.6657
- rmse_ode: 1.6653
- rmse_reduced: 1.6657
- threshold: 0.9277

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0000

