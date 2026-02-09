# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-09T09:45:46.384061

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.8346
- bootstrap_mean: -3.8582
- CI 95%: [-4.4070, -3.3431]
- weighted_value (LoE factor 0.20): -0.7669
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9981
- external: 0.8132
- CR: 1.2274
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4436
- rmse_abm_no_ode: 0.7123
- rmse_ode: 3.9272
- rmse_reduced: 2.5610
- threshold: 0.9230

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

