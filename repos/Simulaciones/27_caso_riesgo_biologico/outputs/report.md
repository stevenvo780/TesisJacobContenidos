# Reporte de Validación — Riesgo Biológico Global

- generated_at: 2026-02-08T20:43:24.876023Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4370
- bootstrap_mean: 0.4362
- CI 95%: [0.3851, 0.4821]
- weighted_value (LoE factor 0.20): 0.0874
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9997
- external: 0.9994
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3972
- rmse_abm_no_ode: 0.7055
- rmse_ode: 1.2300
- rmse_reduced: 1.5734
- threshold: 0.2563

### Calibración
- forcing_scale: 0.6300
- macro_coupling: 0.7804
- damping: 0.6092
- ode_alpha: 0.0517
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2637

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.7691
- bootstrap_mean: -0.8887
- CI 95%: [-2.4886, 0.0391]
- weighted_value (LoE factor 0.20): -0.1538
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9579
- external: 0.9567
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7581
- rmse_abm_no_ode: 0.4285
- rmse_ode: 2.1957
- rmse_reduced: 2.0985
- threshold: 0.2617

### Calibración
- forcing_scale: 0.9559
- macro_coupling: 0.7322
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1135

