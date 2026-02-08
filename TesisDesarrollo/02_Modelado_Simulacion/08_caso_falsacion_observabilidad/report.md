# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-07T08:10:04.649786Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.2502
- bootstrap_mean: -0.4093
- CI 95%: [-1.6997, 0.3786]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0001
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4471
- rmse_ode: 1.2676
- rmse_reduced: 1.1575
- threshold: 0.9375

### Calibración
- forcing_scale: 0.5825
- macro_coupling: 0.1201
- damping: 0.9500
- ode_alpha: 0.2631
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6415

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- válido (0.30-0.90): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: False
- c5_uncertainty: False

