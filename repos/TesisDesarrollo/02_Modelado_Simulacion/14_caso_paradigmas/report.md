# Reporte de Validación — Cambio de Paradigmas Científicos

- generated_at: 2026-02-07T06:12:27.285420Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5966
- bootstrap_mean: 0.5981
- CI 95%: [0.5481, 0.6464]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9807
- rmse_ode: 0.9183
- rmse_reduced: 4.9098
- threshold: 1.8339

### Calibración
- forcing_scale: 0.5805
- macro_coupling: 0.1000
- damping: 0.9000
- ode_alpha: 0.4199
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5955

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6322
- bootstrap_mean: 0.6347
- CI 95%: [0.5129, 0.7312]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9996
- external: 0.9953
- CR: 1.0043
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7202
- rmse_ode: 1.6370
- rmse_reduced: 1.9582
- threshold: 0.5141

### Calibración
- forcing_scale: 0.4045
- macro_coupling: 1.0000
- damping: 0.5805
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5112

