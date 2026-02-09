# Reporte de Validación — Fuga de Cerebros Global (Docquier-Rapoport)

- generated_at: 2026-02-09T04:22:49.909819Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4913
- bootstrap_mean: 0.4940
- CI 95%: [0.4455, 0.5491]
- weighted_value (LoE factor 0.60): 0.2948
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9990
- external: 0.9707
- CR: 1.0291
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4177
- rmse_abm_no_ode: 2.7871
- rmse_ode: 0.7834
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
- valor: 0.2129
- bootstrap_mean: 0.2089
- CI 95%: [-0.0349, 0.4218]
- weighted_value (LoE factor 0.60): 0.1277
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9047
- external: 0.9355
- CR: 0.9670
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.6373
- rmse_abm_no_ode: 4.6212
- rmse_ode: 3.4863
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

