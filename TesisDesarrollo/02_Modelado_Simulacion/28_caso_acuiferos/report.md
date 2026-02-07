# Reporte de Validación — Nivel Freático de Acuíferos

- generated_at: 2026-02-07T11:54:54.153793Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.9722
- bootstrap_mean: 0.9721
- CI 95%: [0.9697, 0.9745]
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
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0935
- rmse_ode: 0.6041
- rmse_reduced: 3.3592
- threshold: 0.8708

### Calibración
- forcing_scale: 0.6339
- macro_coupling: 0.1672
- damping: 0.9500
- ode_alpha: 0.1939
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0887

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9586
- bootstrap_mean: 0.9586
- CI 95%: [0.9549, 0.9626]
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
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1334
- rmse_ode: 0.6828
- rmse_reduced: 3.2243
- threshold: 0.8161

### Calibración
- forcing_scale: 0.6001
- macro_coupling: 0.6416
- damping: 0.9005
- ode_alpha: 0.3122
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1226

