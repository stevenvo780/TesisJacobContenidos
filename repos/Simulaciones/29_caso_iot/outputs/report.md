# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T02:22:18.734572Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -36.8234
- bootstrap_mean: -37.0972
- CI 95%: [-44.1633, -31.4031]
- weighted_value (LoE factor 0.80): -29.4587
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9401
- CR: 1.0637
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 47.8805
- rmse_abm_no_ode: 1.2659
- rmse_ode: 119.1662
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
- valor: -0.6210
- bootstrap_mean: -0.6289
- CI 95%: [-1.0457, -0.3243]
- weighted_value (LoE factor 0.80): -0.4968
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8450
- CR: 1.1834
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 56.1843
- rmse_abm_no_ode: 34.6601
- rmse_ode: 81.3663
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

