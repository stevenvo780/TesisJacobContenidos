# Reporte de Validación — Contaminación por Microplásticos

- generated_at: 2026-02-08T20:25:23.522412Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.9721
- bootstrap_mean: 0.9720
- CI 95%: [0.9696, 0.9744]
- weighted_value (LoE factor 0.20): 0.1944
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.0938
- rmse_ode: 0.6041
- rmse_reduced: 3.3592
- threshold: 0.8708

### Calibración
- forcing_scale: 0.6336
- macro_coupling: 0.5971
- damping: 0.9500
- ode_alpha: 0.1939
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0887

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.8558
- bootstrap_mean: 0.8559
- CI 95%: [0.8509, 0.8606]
- weighted_value (LoE factor 0.20): 0.1712
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6005
- rmse_ode: 0.1852
- rmse_reduced: 4.1651
- threshold: 1.2517

### Calibración
- forcing_scale: 0.5502
- macro_coupling: 0.5187
- damping: 0.8237
- ode_alpha: 0.3092
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1486

