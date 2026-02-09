# Reporte de Validación — Falsación: Exogeneidad

- generated_at: 2026-02-09T11:14:20.266962

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.6147
- bootstrap_mean: -0.6142
- CI 95%: [-0.6522, -0.5796]
- weighted_value (LoE factor 0.20): -0.1229
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.8596
- CR: 1.1622
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 3.6990
- rmse_abm_no_ode: 2.2908
- rmse_ode: 3.8519
- rmse_reduced: 2.1760
- threshold: 0.1595

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

