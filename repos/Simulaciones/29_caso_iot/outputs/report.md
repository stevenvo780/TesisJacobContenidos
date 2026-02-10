# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-10T04:21:30.751779Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3913
- bootstrap_mean: 0.3950
- CI 95%: [0.3575, 0.4403]
- weighted_value (LoE factor 0.80): 0.3131
- válido (0.30-0.90): True
- detrended_edi: 0.3913
- trend_ratio: 1.000
- trend_r2: 0.898

### Symploké y CR
- internal: 0.9999
- external: 0.9720
- CR: 1.0286
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.6510
- rmse_abm_no_ode: 4.3556
- rmse_ode: 1.3192
- rmse_reduced: 6.3551
- threshold: 2.4845

### Calibración
- forcing_scale: 0.5978
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6296
- ode_alpha: 0.3876
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5184
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0186
- bootstrap_mean: 0.0184
- CI 95%: [-0.0026, 0.0364]
- weighted_value (LoE factor 0.80): 0.0149
- válido (0.30-0.90): False
- detrended_edi: 0.0186
- trend_ratio: 1.000
- trend_r2: 0.874

### Symploké y CR
- internal: 1.0000
- external: 0.9414
- CR: 1.0622
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.3750
- rmse_abm_no_ode: 35.0273
- rmse_ode: 34.5035
- rmse_reduced: 40.8516
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5787
- macro_coupling: 0.4688
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.2870
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5971
- ode_rolling: None

### Interpretación
**Nivel 2 — Cierre operativo suggestive.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

