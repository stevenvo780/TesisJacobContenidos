# Reporte de Validación — Contaminación PM2.5

- generated_at: 2026-02-08T22:01:06.593509Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0001
- bootstrap_mean: -0.0001
- CI 95%: [-0.0002, -0.0001]
- weighted_value (LoE factor 0.20): -0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9905
- CR: 1.0093
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.1160
- rmse_abm_no_ode: 3.1156
- rmse_ode: 3.3262
- rmse_reduced: 4.1646
- threshold: 1.6454

### Calibración
- forcing_scale: 0.2227
- macro_coupling: 0.1000
- damping: 0.5037
- ode_alpha: 0.3440
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8068

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0001
- bootstrap_mean: 0.0001
- CI 95%: [0.0000, 0.0002]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9992
- external: 0.9992
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 9.4692
- rmse_abm_no_ode: 9.4704
- rmse_ode: 8.6372
- rmse_reduced: 8.5805
- threshold: 8.1069

### Calibración
- forcing_scale: 0.7599
- macro_coupling: 0.1057
- damping: 0.8321
- ode_alpha: 0.0716
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5186

