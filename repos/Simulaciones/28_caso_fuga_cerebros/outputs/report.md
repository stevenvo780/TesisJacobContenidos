# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-09T02:14:36.367556Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.4627
- bootstrap_mean: -0.4712
- CI 95%: [-0.7159, -0.2424]
- weighted_value (LoE factor 0.60): -0.2776
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9415
- CR: 1.0620
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.0767
- rmse_abm_no_ode: 2.7871
- rmse_ode: 14.1017
- rmse_reduced: 5.3990
- threshold: 1.7147

### Calibración
- forcing_scale: 0.9498
- macro_coupling: 0.5970
- damping: 0.9500
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2390

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.9554
- bootstrap_mean: -2.0008
- CI 95%: [-2.9951, -1.2132]
- weighted_value (LoE factor 0.60): -1.1732
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9797
- external: 0.9190
- CR: 1.0661
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 13.6573
- rmse_abm_no_ode: 4.6212
- rmse_ode: 19.4737
- rmse_reduced: 6.7010
- threshold: 5.6455

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.6598
- ode_alpha: 0.0600
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.4375

