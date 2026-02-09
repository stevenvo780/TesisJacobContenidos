# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-09T05:10:33.241111Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0748
- bootstrap_mean: 0.0755
- CI 95%: [0.0653, 0.0858]
- weighted_value (LoE factor 0.20): 0.0150
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6181
- external: 0.7198
- CR: 0.8586
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7894
- rmse_abm_no_ode: 0.8532
- rmse_ode: 0.6818
- rmse_reduced: 0.5677
- threshold: 0.5474

### Calibración
- forcing_scale: 0.2776
- macro_coupling: 0.1511
- damping: 0.0000
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.1656

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0298
- bootstrap_mean: -0.0298
- CI 95%: [-0.0480, -0.0108]
- weighted_value (LoE factor 0.20): -0.0060
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.6173
- external: 0.7152
- CR: 0.8632
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.0664
- rmse_abm_no_ode: 1.0355
- rmse_ode: 1.6419
- rmse_reduced: 1.2949
- threshold: 1.0562

### Calibración
- forcing_scale: 0.8023
- macro_coupling: 0.2133
- damping: 0.0482
- ode_alpha: 0.5000
- ode_beta: 0.8000
- assimilation_strength: 0.0000
- calibration_rmse: 1.2788

