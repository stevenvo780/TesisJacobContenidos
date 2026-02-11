# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-11T02:08:41.566142Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.5485
- bootstrap_mean: 0.5567
- CI 95%: [0.5111, 0.6194]
- weighted_value (LoE factor 0.80): 0.4388
- válido (0.30-0.90): True
- detrended_edi: 0.5485
- trend_ratio: 1.000
- trend_r2: 0.898

### Symploké y CR
- internal: 0.9995
- external: 0.9789
- CR: 1.0211
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8691
- rmse_abm_no_ode: 4.2313
- rmse_ode: 1.3092
- rmse_reduced: 6.3551
- threshold: 2.4845

### Calibración
- forcing_scale: 0.8890
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8872
- ode_alpha: 0.3876
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5087
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1524
- bootstrap_mean: 0.1507
- CI 95%: [0.1268, 0.1628]
- weighted_value (LoE factor 0.80): 0.1220
- válido (0.30-0.90): False
- detrended_edi: 0.1524
- trend_ratio: 1.000
- trend_r2: 0.874

### Symploké y CR
- internal: 1.0000
- external: 0.9727
- CR: 1.0280
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.6242
- rmse_abm_no_ode: 34.8716
- rmse_ode: 34.5042
- rmse_reduced: 40.8516
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5929
- macro_coupling: 0.1541
- ode_coupling_strength: 0.1233
- abm_feedback_gamma: 0.0500
- damping: 0.2783
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5990
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

