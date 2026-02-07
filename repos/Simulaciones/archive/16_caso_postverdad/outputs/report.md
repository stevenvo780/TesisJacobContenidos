# Reporte de Validación — Postverdad (Fake News)

- generated_at: 2026-02-06T21:59:15.872748Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8603
- bootstrap_mean: 0.8603
- CI 95%: [0.8464, 0.8755]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9953
- CR: 1.0047
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.5837
- rmse_ode: 0.9039
- rmse_reduced: 4.1783
- threshold: 0.8700

### Calibración
- forcing_scale: 0.1164
- macro_coupling: 0.2603
- damping: 0.1526
- ode_alpha: 0.3604
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4445

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0000
- bootstrap_mean: -0.0000
- CI 95%: [-0.0000, -0.0000]
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.1543
- external: -0.3469
- CR: 0.4449
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 5.5303
- rmse_ode: 9.3895
- rmse_reduced: 5.5301
- threshold: 1.8142

### Calibración
- forcing_scale: 0.0000
- macro_coupling: 0.8604
- damping: 0.0543
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.0001

