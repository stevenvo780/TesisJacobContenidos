# Reporte de Validación — Acidificación Oceánica (CO2SYS + Revelle Factor)

- generated_at: 2026-02-09T17:03:59.568211Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0931
- bootstrap_mean: -0.0929
- CI 95%: [-0.0997, -0.0868]
- weighted_value (LoE factor 0.20): -0.0186
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9974
- external: 0.4534
- CR: 2.1995
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 1.5452
- rmse_abm_no_ode: 1.4135
- rmse_ode: 8.3145
- rmse_reduced: 2.0224
- threshold: 1.0107

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.0823
- ode_coupling_strength: 0.0658
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.0170
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.3061

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0018
- bootstrap_mean: -0.0028
- CI 95%: [-0.0102, 0.0003]
- weighted_value (LoE factor 0.20): -0.0004
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9993
- external: 0.8556
- CR: 1.1680
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3492
- rmse_abm_no_ode: 3.3431
- rmse_ode: 9.2096
- rmse_reduced: 3.2742
- threshold: 2.3256

### Calibración
- forcing_scale: 0.8576
- macro_coupling: 0.1720
- ode_coupling_strength: 0.1376
- abm_feedback_gamma: 0.0500
- damping: 0.0000
- ode_alpha: 0.1492
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9496

