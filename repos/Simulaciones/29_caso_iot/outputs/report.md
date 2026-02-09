# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T02:47:13.711893Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1900
- bootstrap_mean: -0.1979
- CI 95%: [-0.3841, -0.0520]
- weighted_value (LoE factor 0.80): -0.1520
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9989
- external: 0.9089
- CR: 1.0990
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.1586
- rmse_abm_no_ode: 2.6543
- rmse_ode: 3.8343
- rmse_reduced: 4.1676
- threshold: 1.4567

### Calibración
- forcing_scale: 0.5512
- macro_coupling: 0.7490
- damping: 0.6407
- ode_alpha: 0.1000
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.6687

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0377
- bootstrap_mean: -0.0378
- CI 95%: [-0.0511, -0.0261]
- weighted_value (LoE factor 0.80): -0.0302
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9583
- CR: 1.0434
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 35.9675
- rmse_abm_no_ode: 34.6601
- rmse_ode: 36.7596
- rmse_reduced: 40.8515
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5962
- macro_coupling: 1.0000
- damping: 0.2894
- ode_alpha: 0.1000
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.5975

