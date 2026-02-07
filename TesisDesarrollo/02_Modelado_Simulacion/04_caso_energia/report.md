# Reporte de Validación — Energía (OPSD GB Grid)

- generated_at: 2026-02-06T21:57:33.066003Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5834
- bootstrap_mean: 0.5838
- CI 95%: [0.5766, 0.5917]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.8007
- CR: 1.2488
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 2.9424
- rmse_ode: 1.8845
- rmse_reduced: 7.0636
- threshold: 1.5448

### Calibración
- forcing_scale: 0.0804
- macro_coupling: 0.8865
- damping: 0.1483
- ode_alpha: 0.0241
- ode_beta: 0.8965
- assimilation_strength: 0.0000
- calibration_rmse: 0.2274

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1682
- bootstrap_mean: 0.1655
- CI 95%: [0.1136, 0.2046]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.8168
- CR: 1.2243
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3456
- rmse_ode: 2.5480
- rmse_reduced: 1.6176
- threshold: 0.7351

### Calibración
- forcing_scale: 0.0214
- macro_coupling: 0.8852
- damping: 0.1758
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9435

