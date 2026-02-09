# Reporte de Validación — Falsación: Observabilidad Escasa

- generated_at: 2026-02-08T23:16:12.531926

## Fase real
- **overall_pass**: False

### EDI
- valor: -4.0215
- bootstrap_mean: -4.0455
- CI 95%: [-4.6579, -3.4822]
- weighted_value (LoE factor 0.20): -0.8043
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9982
- external: 0.7948
- CR: 1.2559
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4645
- rmse_abm_no_ode: 0.6899
- rmse_ode: 3.9494
- rmse_reduced: 2.5137
- threshold: 0.9023

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

