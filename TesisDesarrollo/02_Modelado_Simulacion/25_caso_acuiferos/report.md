# Reporte de Validación — Depleción de Acuíferos (Darcy-Theis)

- generated_at: 2026-02-09T14:20:12.170609Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4870
- bootstrap_mean: 0.4875
- CI 95%: [0.4722, 0.5062]
- weighted_value (LoE factor 0.60): 0.2922
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9927
- CR: 1.0073
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6830
- rmse_abm_no_ode: 1.3314
- rmse_ode: 0.5715
- rmse_reduced: 1.3952
- threshold: 0.1000

### Calibración
- forcing_scale: 0.3174
- macro_coupling: 0.5721
- damping: 0.3078
- ode_alpha: 0.0055
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1427

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.2711
- bootstrap_mean: -0.2709
- CI 95%: [-0.2940, -0.2468]
- weighted_value (LoE factor 0.60): -0.1627
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.0829
- external: 0.6052
- CR: 0.1370
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 23.8038
- rmse_abm_no_ode: 18.7266
- rmse_ode: 29.3864
- rmse_reduced: 35.7618
- threshold: 14.8563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 1.0000
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5404

