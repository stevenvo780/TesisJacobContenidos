# Reporte de Validación — Salinización de Suelos (Richards-Solute)

- generated_at: 2026-02-09T15:49:59.661287Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5048
- bootstrap_mean: 0.5038
- CI 95%: [0.3539, 0.6336]
- weighted_value (LoE factor 0.60): 0.3029
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9977
- CR: 1.0021
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3571
- rmse_abm_no_ode: 0.7211
- rmse_ode: 1.1240
- rmse_reduced: 2.9446
- threshold: 0.6860

### Calibración
- forcing_scale: 0.9459
- macro_coupling: 0.3913
- damping: 0.9500
- ode_alpha: 0.2739
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2983

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.3784
- bootstrap_mean: -1.3837
- CI 95%: [-3.1929, -0.1824]
- weighted_value (LoE factor 0.60): -0.8271
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9220
- external: 0.0742
- CR: 12.4242
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 2.0796
- rmse_abm_no_ode: 0.8744
- rmse_ode: 3.9088
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

