# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T02:30:22.867690Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2423
- bootstrap_mean: 0.2451
- CI 95%: [0.2054, 0.2903]
- weighted_value (LoE factor 0.80): 0.1938
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9987
- external: 0.9843
- CR: 1.0146
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0486
- rmse_abm_no_ode: 2.7038
- rmse_ode: 1.5364
- rmse_reduced: 4.3177
- threshold: 1.4996

### Calibración
- forcing_scale: 0.5886
- macro_coupling: 0.6796
- damping: 0.6651
- ode_alpha: 0.3334
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6485

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0117
- bootstrap_mean: -0.0119
- CI 95%: [-0.0370, 0.0102]
- weighted_value (LoE factor 0.80): -0.0094
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9287
- CR: 1.0767
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 35.0655
- rmse_abm_no_ode: 34.6601
- rmse_ode: 35.6376
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

