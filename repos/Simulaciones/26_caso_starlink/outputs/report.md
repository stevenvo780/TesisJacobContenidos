# Reporte de Validación — Constelaciones Satelitales Starlink (Mega-Constellation)

- generated_at: 2026-02-09T03:48:11.836139Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.7401
- bootstrap_mean: 0.7402
- CI 95%: [0.7239, 0.7553]
- weighted_value (LoE factor 0.80): 0.5921
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9998
- external: 0.9905
- CR: 1.0094
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3339
- rmse_abm_no_ode: 1.2848
- rmse_ode: 1.8959
- rmse_reduced: 0.8035
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9651
- macro_coupling: 0.4991
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2839

## Fase real
- **overall_pass**: False

### EDI
- valor: -839.5615
- bootstrap_mean: -841.0004
- CI 95%: [-945.7809, -735.8446]
- weighted_value (LoE factor 0.80): -671.6492
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9869
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
- rmse_abm: 0.1064
- rmse_abm_no_ode: 0.0001
- rmse_ode: 1.0108
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

