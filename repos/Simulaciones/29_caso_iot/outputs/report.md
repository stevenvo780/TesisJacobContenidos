# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe Bilineal)

- generated_at: 2026-02-12T04:09:43.349502Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0093
- bootstrap_mean: -0.0093
- CI 95%: [-0.0114, -0.0066]
- weighted_value (LoE factor 0.60): -0.0056
- válido (0.30-0.90): False
- detrended_edi: -0.0093
- trend_ratio: 1.000
- trend_r2: 0.627

### Symploké y CR
- internal: 0.9952
- external: 0.9965
- CR: 0.9987
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.2343
- rmse_abm_no_ode: 2.2137
- rmse_ode: 3.0449
- rmse_reduced: 2.6686
- threshold: 0.9559

### Calibración
- forcing_scale: 0.9282
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8854
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.8989
- bootstrap_mean: -0.9240
- CI 95%: [-1.2520, -0.7336]
- weighted_value (LoE factor 0.60): -0.5394
- válido (0.30-0.90): False
- detrended_edi: -0.8989
- trend_ratio: 1.000
- trend_r2: 0.815

### Symploké y CR
- internal: 0.9999
- external: 0.9937
- CR: 1.0063
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1104
- rmse_abm_no_ode: 0.5847
- rmse_ode: 5.5141
- rmse_reduced: 2.5474
- threshold: 0.1285

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8201
- ode_alpha: 0.1365
- ode_beta: 0.6821
- assimilation_strength: 0.0000
- calibration_rmse: 0.2951
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

