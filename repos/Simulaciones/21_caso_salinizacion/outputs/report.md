# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T04:22:54.504408Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3453
- bootstrap_mean: 0.3415
- CI 95%: [0.1661, 0.4856]
- weighted_value (LoE factor 0.60): 0.2072
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9988
- CR: 1.0011
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4710
- rmse_abm_no_ode: 0.7195
- rmse_ode: 1.0744
- rmse_reduced: 2.8625
- threshold: 0.7810

### Calibración
- forcing_scale: 0.9529
- macro_coupling: 0.3091
- damping: 0.9500
- ode_alpha: 0.3333
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3621

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.5836
- bootstrap_mean: -1.5911
- CI 95%: [-3.5192, -0.3256]
- weighted_value (LoE factor 0.60): -0.9501
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9269
- external: 0.0516
- CR: 17.9695
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 2.2590
- rmse_abm_no_ode: 0.8744
- rmse_ode: 4.4630
- rmse_reduced: 1.0780
- threshold: 0.1357

### Calibración
- forcing_scale: 0.9487
- macro_coupling: 0.7718
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2739

