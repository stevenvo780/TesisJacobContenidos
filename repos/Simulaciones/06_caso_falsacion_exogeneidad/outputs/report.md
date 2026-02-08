# Reporte de Validación — Falsación: Exogeneidad

- generated_at: 2026-02-08T22:06:51.232767Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0194
- bootstrap_mean: -0.0207
- CI 95%: [-0.1901, 0.1341]
- weighted_value (LoE factor 0.20): -0.0039
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.1357
- external: 0.1112
- CR: 1.2203
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3113
- rmse_abm_no_ode: 1.2863
- rmse_ode: 1.4274
- rmse_reduced: 1.2869
- threshold: 1.2689

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 1.0000
- damping: 0.5663
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9992

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4627
- bootstrap_mean: 0.4638
- CI 95%: [0.4429, 0.4841]
- weighted_value (LoE factor 0.20): 0.0925
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9995
- external: 0.9988
- CR: 1.0007
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.0667
- rmse_abm_no_ode: 1.9855
- rmse_ode: 0.9564
- rmse_reduced: 0.7016
- threshold: 0.5955

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6003
- damping: 0.8897
- ode_alpha: 0.0962
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5053

