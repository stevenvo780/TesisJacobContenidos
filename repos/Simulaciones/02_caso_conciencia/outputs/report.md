# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-08T22:53:50.881300Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5024
- bootstrap_mean: 0.5023
- CI 95%: [0.4400, 0.5579]
- weighted_value (LoE factor 0.20): 0.1005
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9922
- external: 0.9622
- CR: 1.0312
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5092
- rmse_abm_no_ode: 1.0234
- rmse_ode: 0.9002
- rmse_reduced: 1.4462
- threshold: 0.2762

### Calibración
- forcing_scale: 0.9197
- macro_coupling: 0.5520
- damping: 0.9500
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2956

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0912
- bootstrap_mean: -0.0916
- CI 95%: [-0.1061, -0.0771]
- weighted_value (LoE factor 0.20): -0.0182
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9928
- external: 0.9471
- CR: 1.0483
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6567
- rmse_abm_no_ode: 1.5182
- rmse_ode: 1.7101
- rmse_reduced: 1.8076
- threshold: 0.9681

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.4200
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6141

