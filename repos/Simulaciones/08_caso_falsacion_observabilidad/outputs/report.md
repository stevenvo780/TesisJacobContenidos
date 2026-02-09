# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-09T00:10:29.268244

## Fase real
- **overall_pass**: False

### EDI
- valor: -4.0019
- bootstrap_mean: -4.0267
- CI 95%: [-4.5903, -3.5387]
- weighted_value (LoE factor 0.20): -0.8004
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9981
- external: 0.8025
- CR: 1.2437
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4831
- rmse_abm_no_ode: 0.6964
- rmse_ode: 3.9638
- rmse_reduced: 2.5686
- threshold: 0.9132

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

