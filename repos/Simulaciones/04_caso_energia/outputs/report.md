# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-08T23:05:33.611105Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.6592
- bootstrap_mean: -1.6603
- CI 95%: [-1.7345, -1.5950]
- weighted_value (LoE factor 0.20): -0.3318
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4906
- external: 0.7862
- CR: 0.6240
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 17.4591
- rmse_abm_no_ode: 6.5655
- rmse_ode: 0.5629
- rmse_reduced: 3.5446
- threshold: 1.0076

### Calibración
- forcing_scale: 0.9115
- macro_coupling: 0.6636
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.1684

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0020
- bootstrap_mean: -0.0029
- CI 95%: [-0.0293, 0.0207]
- weighted_value (LoE factor 0.20): -0.0004
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9607
- external: 0.9491
- CR: 1.0122
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1892
- rmse_abm_no_ode: 1.1868
- rmse_ode: 1.1906
- rmse_reduced: 1.4485
- threshold: 1.2251

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6789
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.6894

