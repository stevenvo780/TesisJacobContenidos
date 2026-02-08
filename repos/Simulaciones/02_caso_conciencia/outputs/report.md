# Reporte de Validación — Conciencia Colectiva

- generated_at: 2026-02-08T22:00:54.413982Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8258
- bootstrap_mean: 0.8263
- CI 95%: [0.8088, 0.8446]
- weighted_value (LoE factor 0.20): 0.1652
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9993
- external: 0.9992
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1468
- rmse_abm_no_ode: 0.8425
- rmse_ode: 1.2308
- rmse_reduced: 1.5980
- threshold: 0.2755

### Calibración
- forcing_scale: 0.9335
- macro_coupling: 0.5535
- damping: 0.9500
- ode_alpha: 0.0559
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2505

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.3945
- bootstrap_mean: -0.3961
- CI 95%: [-0.4529, -0.3338]
- weighted_value (LoE factor 0.20): -0.0789
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9994
- external: 0.9913
- CR: 1.0081
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.3772
- rmse_abm_no_ode: 0.9876
- rmse_ode: 1.6698
- rmse_reduced: 1.7655
- threshold: 0.9404

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.6207
- damping: 0.4003
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6063

