# Reporte de Validación — Deforestación Global

- generated_at: 2026-02-07T08:53:10.899861Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5821
- bootstrap_mean: 0.5843
- CI 95%: [0.5148, 0.6650]
- válido (0.30-0.90): True

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
- rmse_abm: 0.9102
- rmse_ode: 0.9161
- rmse_reduced: 2.1783
- threshold: 0.8200

### Calibración
- forcing_scale: 0.5393
- macro_coupling: 0.1234
- damping: 0.9500
- ode_alpha: 0.3103
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8214

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.8465
- bootstrap_mean: 0.8475
- CI 95%: [0.7891, 0.8939]
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
- rmse_abm: 0.5422
- rmse_ode: 0.6659
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.6269
- macro_coupling: 0.1015
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1506

