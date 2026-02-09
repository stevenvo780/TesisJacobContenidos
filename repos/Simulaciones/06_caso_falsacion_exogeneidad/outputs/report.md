# Reporte de Validación — Falsación: Exogeneidad

- generated_at: 2026-02-09T00:10:31.542797

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1908
- bootstrap_mean: -0.1912
- CI 95%: [-0.2020, -0.1822]
- weighted_value (LoE factor 0.20): -0.0382
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9986
- external: 0.3548
- CR: 2.8148
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 7.3134
- rmse_abm_no_ode: 6.1418
- rmse_ode: 7.4406
- rmse_reduced: 6.1740
- threshold: 4.5214

### Calibración
- forcing_scale: 0.0500
- macro_coupling: 0.2000
- damping: 0.0200
- ode_alpha: 0.0500
- ode_beta: 0.0200
- assimilation_strength: 0.0000
- calibration_rmse: 0.0000

