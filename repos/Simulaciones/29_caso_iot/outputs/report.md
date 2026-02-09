# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T02:14:39.300419Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3155
- bootstrap_mean: 0.3147
- CI 95%: [0.2956, 0.3282]
- weighted_value (LoE factor 0.80): 0.2524
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9969
- external: 0.9916
- CR: 1.0053
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8666
- rmse_abm_no_ode: 1.2659
- rmse_ode: 0.2176
- rmse_reduced: 1.0718
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9237
- macro_coupling: 0.5990
- damping: 0.9500
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.2011

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1276
- bootstrap_mean: -0.1276
- CI 95%: [-0.1367, -0.1182]
- weighted_value (LoE factor 0.80): -0.1021
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9993
- external: 0.9901
- CR: 1.0093
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 39.0814
- rmse_abm_no_ode: 34.6601
- rmse_ode: 40.6569
- rmse_reduced: 40.8515
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5962
- macro_coupling: 1.0000
- damping: 0.2894
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5975

