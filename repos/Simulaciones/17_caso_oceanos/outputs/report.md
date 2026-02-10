# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-10T04:21:50.582087Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2185
- bootstrap_mean: 0.2179
- CI 95%: [0.1941, 0.2386]
- weighted_value (LoE factor 0.20): 0.0437
- válido (0.30-0.90): False
- detrended_edi: 0.2185
- trend_ratio: 1.000
- trend_r2: 0.961

### Symploké y CR
- internal: 0.9669
- external: 0.1148
- CR: 8.4236
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.3243
- rmse_abm_no_ode: 5.5337
- rmse_ode: 1.6441
- rmse_reduced: 5.1439
- threshold: 0.9858

### Calibración
- forcing_scale: 0.6214
- macro_coupling: 0.0808
- ode_coupling_strength: 0.0646
- abm_feedback_gamma: 0.0500
- damping: 0.6093
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 0.1449
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2318
- bootstrap_mean: 0.2941
- CI 95%: [0.1655, 0.4942]
- weighted_value (LoE factor 0.20): 0.0464
- válido (0.30-0.90): False
- detrended_edi: 0.2318
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9841
- external: -0.8098
- CR: 1.2152
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9073
- rmse_abm_no_ode: 3.7846
- rmse_ode: 2.7927
- rmse_reduced: 3.8040
- threshold: 2.7353

### Calibración
- forcing_scale: 0.8319
- macro_coupling: 0.4888
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7501
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2796
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

