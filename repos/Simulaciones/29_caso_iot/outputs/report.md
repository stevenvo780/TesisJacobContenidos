# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T02:32:44.690776Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1953
- bootstrap_mean: 0.1967
- CI 95%: [0.1745, 0.2221]
- weighted_value (LoE factor 0.80): 0.1563
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9988
- external: 0.9970
- CR: 1.0018
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1524
- rmse_abm_no_ode: 2.6749
- rmse_ode: 1.7475
- rmse_reduced: 4.2699
- threshold: 1.4803

### Calibración
- forcing_scale: 0.5838
- macro_coupling: 0.7084
- damping: 0.6642
- ode_alpha: 0.3321
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6511

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0384
- bootstrap_mean: -0.0384
- CI 95%: [-0.0522, -0.0263]
- weighted_value (LoE factor 0.80): -0.0307
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9563
- CR: 1.0456
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 35.9896
- rmse_abm_no_ode: 34.6601
- rmse_ode: 36.7904
- rmse_reduced: 40.8515
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5962
- macro_coupling: 1.0000
- damping: 0.2894
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5975

