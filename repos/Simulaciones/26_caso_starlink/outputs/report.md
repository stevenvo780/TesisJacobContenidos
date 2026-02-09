# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T01:59:27.393333Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.3233
- bootstrap_mean: -1.3233
- CI 95%: [-1.4137, -1.1993]
- weighted_value (LoE factor 0.80): -1.0587
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.2685
- external: 0.6904
- CR: 0.3889
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 38.7808
- rmse_abm_no_ode: 16.6919
- rmse_ode: 3.0210
- rmse_reduced: 0.8840
- threshold: 0.8159

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.7141
- damping: 0.7569
- ode_alpha: 0.1483
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5780

## Fase real
- **overall_pass**: False

### EDI
- valor: -103.8349
- bootstrap_mean: -103.8276
- CI 95%: [-120.4245, -89.6882]
- weighted_value (LoE factor 0.80): -83.0679
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.8995
- external: 0.0000
- CR: inf
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0133
- rmse_abm_no_ode: 0.0001
- rmse_ode: 0.1259
- rmse_reduced: 0.0001
- threshold: 0.1000

### Calibración
- forcing_scale: 0.1239
- macro_coupling: 0.1073
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.0002

