# Reporte de Validación — Síndrome de Kessler

- generated_at: 2026-02-07T08:57:26.691702Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6999
- bootstrap_mean: 0.7071
- CI 95%: [0.6261, 0.7887]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0001
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7663
- rmse_ode: 0.7424
- rmse_reduced: 2.5531
- threshold: 0.7068

### Calibración
- forcing_scale: 0.6160
- macro_coupling: 0.3794
- damping: 0.9500
- ode_alpha: 0.3816
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5681

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.7764
- bootstrap_mean: 0.7771
- CI 95%: [0.7633, 0.7965]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9987
- CR: 1.0013
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8421
- rmse_ode: 0.8779
- rmse_reduced: 3.7654
- threshold: 1.0029

### Calibración
- forcing_scale: 0.4713
- macro_coupling: 0.5416
- damping: 0.6569
- ode_alpha: 0.0956
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1743

