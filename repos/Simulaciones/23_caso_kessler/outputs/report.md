# Reporte de Validación — Síndrome de Kessler

- generated_at: 2026-02-07T15:20:54.397849Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9746
- bootstrap_mean: 0.9747
- CI 95%: [0.9718, 0.9774]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.0622
- rmse_ode: 0.4648
- rmse_reduced: 2.4547
- threshold: 0.4056

### Calibración
- forcing_scale: 0.6345
- macro_coupling: 0.5939
- damping: 0.9500
- ode_alpha: 0.1298
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0657

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

