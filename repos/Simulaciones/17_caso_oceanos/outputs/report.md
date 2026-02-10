# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-10T07:10:49.946449Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2580
- bootstrap_mean: 0.2574
- CI 95%: [0.2327, 0.2786]
- weighted_value (LoE factor 0.20): 0.0516
- válido (0.30-0.90): False
- detrended_edi: 0.2580
- trend_ratio: 1.000
- trend_r2: 0.961

### Symploké y CR
- internal: 0.9684
- external: 0.1005
- CR: 9.6390
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.1059
- rmse_abm_no_ode: 5.5337
- rmse_ode: 1.6378
- rmse_reduced: 5.1439
- threshold: 0.9858

### Calibración
- forcing_scale: 0.6940
- macro_coupling: 0.0927
- ode_coupling_strength: 0.0742
- abm_feedback_gamma: 0.0500
- damping: 0.6790
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 0.1444
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2288
- bootstrap_mean: 0.2908
- CI 95%: [0.1638, 0.4962]
- weighted_value (LoE factor 0.20): 0.0458
- válido (0.30-0.90): False
- detrended_edi: 0.2288
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9837
- external: -0.8111
- CR: 1.2128
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9185
- rmse_abm_no_ode: 3.7846
- rmse_ode: 2.7927
- rmse_reduced: 3.8040
- threshold: 2.7353

### Calibración
- forcing_scale: 0.7659
- macro_coupling: 0.4623
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6801
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2786
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

