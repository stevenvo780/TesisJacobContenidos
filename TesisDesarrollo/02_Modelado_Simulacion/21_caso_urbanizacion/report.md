# Reporte de Validación — Urbanización Global

- generated_at: 2026-02-07T08:54:57.613365Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7954
- bootstrap_mean: 0.7978
- CI 95%: [0.7342, 0.8583]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9999
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5526
- rmse_ode: 0.5749
- rmse_reduced: 2.7010
- threshold: 0.7689

### Calibración
- forcing_scale: 0.6274
- macro_coupling: 0.1000
- damping: 0.9500
- ode_alpha: 0.4197
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4720

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.8392
- bootstrap_mean: 0.8394
- CI 95%: [0.8343, 0.8459]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5839
- rmse_ode: 0.3652
- rmse_reduced: 3.6324
- threshold: 0.8867

### Calibración
- forcing_scale: 0.6410
- macro_coupling: 0.5801
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0643

