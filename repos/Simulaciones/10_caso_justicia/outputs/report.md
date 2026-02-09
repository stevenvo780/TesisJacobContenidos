# Reporte de Validación — Justicia Algorítmica

- generated_at: 2026-02-09T14:45:51.818918Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0248
- bootstrap_mean: -0.0251
- CI 95%: [-0.0398, -0.0140]
- weighted_value (LoE factor 0.20): -0.0050
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9984
- external: 0.9360
- CR: 1.0666
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5956
- rmse_abm_no_ode: 0.5812
- rmse_ode: 1.1943
- rmse_reduced: 0.5812
- threshold: 0.2495

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0559
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8509

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9666
- external: 0.9073
- CR: 1.0654
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8889
- rmse_abm_no_ode: 1.8889
- rmse_ode: 1.5598
- rmse_reduced: 1.8889
- threshold: 0.3262

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.1330
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8940

