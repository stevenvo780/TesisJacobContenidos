# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T16:18:55.696343Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4145
- bootstrap_mean: 0.4185
- CI 95%: [0.3640, 0.4840]
- weighted_value (LoE factor 0.80): 0.3316
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9996
- external: 0.9765
- CR: 1.0237
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4739
- rmse_abm_no_ode: 4.2249
- rmse_ode: 1.4341
- rmse_reduced: 6.3551
- threshold: 2.4845

### Calibración
- forcing_scale: 0.9038
- macro_coupling: 0.4787
- damping: 0.9500
- ode_alpha: 0.3876
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5084

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0140
- bootstrap_mean: 0.0135
- CI 95%: [-0.0151, 0.0364]
- weighted_value (LoE factor 0.80): 0.0112
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9187
- CR: 1.0884
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.1738
- rmse_abm_no_ode: 34.6601
- rmse_ode: 34.4858
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

