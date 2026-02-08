# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-08T20:36:41.395272Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3756
- bootstrap_mean: 0.3762
- CI 95%: [0.2894, 0.4819]
- weighted_value (LoE factor 0.20): 0.0751
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.8556
- external: 0.8517
- CR: 1.0045
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2289
- rmse_abm_no_ode: 1.9682
- rmse_ode: 1.1583
- rmse_reduced: 1.1193
- threshold: 1.0085

### Calibración
- forcing_scale: 0.8030
- macro_coupling: 0.7241
- damping: 0.9500
- ode_alpha: 0.1366
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8078

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: False
- c5_uncertainty: False

