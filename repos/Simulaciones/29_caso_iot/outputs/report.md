# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-10T05:33:16.064602Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.4100
- bootstrap_mean: 0.4123
- CI 95%: [0.3720, 0.4588]
- weighted_value (LoE factor 0.80): 0.3280
- válido (0.30-0.90): True
- detrended_edi: 0.4100
- trend_ratio: 1.000
- trend_r2: 0.898

### Symploké y CR
- internal: 0.9999
- external: 0.9704
- CR: 1.0305
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.5727
- rmse_abm_no_ode: 4.3602
- rmse_ode: 1.3227
- rmse_reduced: 6.3551
- threshold: 2.4845

### Calibración
- forcing_scale: 0.5461
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5767
- ode_alpha: 0.3876
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5235
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0174
- bootstrap_mean: 0.0174
- CI 95%: [-0.0066, 0.0362]
- weighted_value (LoE factor 0.80): 0.0139
- válido (0.30-0.90): False
- detrended_edi: 0.0174
- trend_ratio: 1.000
- trend_r2: 0.874

### Symploké y CR
- internal: 1.0000
- external: 0.9380
- CR: 1.0661
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.2753
- rmse_abm_no_ode: 34.8822
- rmse_ode: 34.5000
- rmse_reduced: 40.8516
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5613
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.2688
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6006
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

