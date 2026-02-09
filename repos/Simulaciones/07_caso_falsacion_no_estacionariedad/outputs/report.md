# Reporte de Validación — Falsación: No-Estacionariedad

- generated_at: 2026-02-09T00:10:29.269678

## Fase real
- **overall_pass**: False

### EDI
- valor: -7.4914
- bootstrap_mean: -7.5338
- CI 95%: [-8.5013, -6.6138]
- weighted_value (LoE factor 0.20): -1.4983
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9989
- external: 0.8718
- CR: 1.1459
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.5808
- rmse_abm_no_ode: 0.5395
- rmse_ode: 5.2502
- rmse_reduced: 3.6841
- threshold: 1.0417

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

