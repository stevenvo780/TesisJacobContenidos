# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T03:14:13.671575Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1146
- bootstrap_mean: 0.1152
- CI 95%: [0.1038, 0.1284]
- weighted_value (LoE factor 0.80): 0.0917
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9989
- external: 0.9949
- CR: 1.0040
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.0068
- rmse_abm_no_ode: 3.3961
- rmse_ode: 2.3325
- rmse_reduced: 5.0246
- threshold: 1.8075

### Calibración
- forcing_scale: 0.8944
- macro_coupling: 0.4745
- damping: 0.9500
- ode_alpha: 0.2760
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7091

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0074
- bootstrap_mean: -0.0076
- CI 95%: [-0.0327, 0.0143]
- weighted_value (LoE factor 0.80): -0.0059
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9330
- CR: 1.0718
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.9159
- rmse_abm_no_ode: 34.6601
- rmse_ode: 35.4331
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

