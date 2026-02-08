# Reporte de Validación — Ecosistema IoT Global

- generated_at: 2026-02-07T15:58:52.757390Z

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
- valor: 0.8886
- bootstrap_mean: 0.8886
- CI 95%: [0.8840, 0.8936]
- válido (0.30-0.90): True

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
- rmse_abm: 0.4343
- rmse_ode: 0.3031
- rmse_reduced: 3.8974
- threshold: 1.1533

### Calibración
- forcing_scale: 0.5587
- macro_coupling: 0.1000
- damping: 0.8369
- ode_alpha: 0.3840
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1573

