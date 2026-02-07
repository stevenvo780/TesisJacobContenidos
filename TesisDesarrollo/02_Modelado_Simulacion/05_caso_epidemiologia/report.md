# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-07T07:42:25.973411Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0067
- bootstrap_mean: 0.0067
- CI 95%: [0.0009, 0.0124]
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9970
- external: 0.0025
- CR: 405.4669
- CR válido (>2.0): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9412
- rmse_ode: 0.9470
- rmse_reduced: 0.9475
- threshold: 0.9475

### Calibración
- forcing_scale: 0.6997
- macro_coupling: 0.8644
- damping: 0.8503
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9637

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1758
- bootstrap_mean: 0.1634
- CI 95%: [-0.0242, 0.2787]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9997
- CR: 1.0001
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 3.7269
- rmse_ode: 4.5222
- rmse_reduced: 4.5220
- threshold: 4.3680

### Calibración
- forcing_scale: 0.7202
- macro_coupling: 0.6392
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4346

