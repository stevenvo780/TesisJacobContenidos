# Reporte de Validación — Riesgo Biológico Global (Woolhouse Bilineal)

- generated_at: 2026-02-12T04:09:02.541370Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0035
- bootstrap_mean: -0.0034
- CI 95%: [-0.0055, -0.0007]
- weighted_value (LoE factor 0.60): -0.0021
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9948
- external: 0.9957
- CR: 0.9991
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.9603
- rmse_abm_no_ode: 1.9535
- rmse_ode: 2.7220
- rmse_reduced: 2.3900
- threshold: 0.9305

### Calibración
- forcing_scale: 0.9489
- macro_coupling: 0.1275
- ode_coupling_strength: 0.1020
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8791
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2936
- bootstrap_mean: 0.2972
- CI 95%: [0.2568, 0.3559]
- weighted_value (LoE factor 0.60): 0.1762
- válido (0.30-0.90): False
- detrended_edi: 0.2936
- trend_ratio: 1.000
- trend_r2: 0.661

### Symploké y CR
- internal: 0.9999
- external: 0.9987
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.3726
- rmse_abm_no_ode: 0.5274
- rmse_ode: 2.7667
- rmse_reduced: 2.9798
- threshold: 0.3368

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8874
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1527
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

