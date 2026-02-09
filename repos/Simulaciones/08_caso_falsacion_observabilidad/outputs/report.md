# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-08T21:31:20.657215

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.4142
- bootstrap_mean: -3.4376
- CI 95%: [-3.9910, -2.9780]
- weighted_value (LoE factor 0.20): -0.6828
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9978
- external: 0.8796
- CR: 1.1344
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.0684
- rmse_abm_no_ode: 0.6951
- rmse_ode: 3.5141
- rmse_reduced: 2.4947
- threshold: 0.8952

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

