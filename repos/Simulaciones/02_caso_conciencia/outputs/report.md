# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-07T13:51:17.785976Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7155
- bootstrap_mean: 0.7157
- CI 95%: [0.7097, 0.7229]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0003
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.6199
- rmse_ode: 1.8447
- rmse_reduced: 5.6932
- threshold: 1.9803

### Calibración
- forcing_scale: 0.3786
- macro_coupling: 0.5903
- damping: 0.5484
- ode_alpha: 0.0192
- ode_beta: 0.8210
- assimilation_strength: 0.0000
- calibration_rmse: 0.1475

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9361
- bootstrap_mean: 0.9363
- CI 95%: [0.9293, 0.9443]
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
- rmse_abm: 0.1917
- rmse_ode: 1.6465
- rmse_reduced: 3.0011
- threshold: 0.7461

### Calibración
- forcing_scale: 0.6321
- macro_coupling: 0.4893
- damping: 0.9500
- ode_alpha: 0.3414
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1474

