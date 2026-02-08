# Reporte de Validación — Constelaciones Satelitales (Starlink)

- generated_at: 2026-02-08T20:54:57.911595Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -2.0965
- bootstrap_mean: -2.0979
- CI 95%: [-2.1915, -2.0217]
- weighted_value (LoE factor 0.20): -0.4193
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9998
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8699
- rmse_abm_no_ode: 0.6039
- rmse_ode: 3.0414
- rmse_reduced: 3.0752
- threshold: 0.6776

### Calibración
- forcing_scale: 0.6267
- macro_coupling: 0.6792
- damping: 0.6168
- ode_alpha: 0.0091
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0580

## Fase real
- **overall_pass**: False

### EDI
- valor: -2.7539
- bootstrap_mean: -2.7572
- CI 95%: [-2.9365, -2.6093]
- weighted_value (LoE factor 0.20): -0.5508
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9992
- CR: 1.0007
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5193
- rmse_abm_no_ode: 0.4047
- rmse_ode: 3.8112
- rmse_reduced: 2.8434
- threshold: 0.6042

### Calibración
- forcing_scale: 0.9566
- macro_coupling: 0.4728
- damping: 0.9449
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0057

