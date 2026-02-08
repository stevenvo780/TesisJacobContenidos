# Reporte de Validación — Movilidad Urbana

- generated_at: 2026-02-08T20:48:38.171876Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5829
- bootstrap_mean: 0.5820
- CI 95%: [0.5312, 0.6254]
- weighted_value (LoE factor 0.20): 0.1166
- válido (0.30-0.90): True

### Symploké y CR
- internal: -1.0000
- external: 0.0001
- CR: 15434.5046
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.3080
- rmse_abm_no_ode: 0.7384
- rmse_ode: 1.2300
- rmse_reduced: 1.5734
- threshold: 0.2563

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.7045
- damping: 0.9500
- ode_alpha: 0.0517
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2654

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3732
- bootstrap_mean: -0.3814
- CI 95%: [-0.5645, -0.2556]
- weighted_value (LoE factor 0.20): -0.0746
- válido (0.30-0.90): False

### Symploké y CR
- internal: -1.0000
- external: 0.0000
- CR: 606691.6594
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 89.0065
- rmse_abm_no_ode: 64.8159
- rmse_ode: 1.6072
- rmse_reduced: 1.8218
- threshold: 0.9936

### Calibración
- forcing_scale: 0.8020
- macro_coupling: 1.0000
- damping: 0.6757
- ode_alpha: 0.4207
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8854

