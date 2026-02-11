# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-11T01:01:09.104064Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2453
- bootstrap_mean: 0.2446
- CI 95%: [0.2197, 0.2663]
- weighted_value (LoE factor 0.20): 0.0491
- válido (0.30-0.90): False
- detrended_edi: 0.2453
- trend_ratio: 1.000
- trend_r2: 0.961

### Symploké y CR
- internal: 0.9679
- external: 0.1051
- CR: 9.2072
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.1763
- rmse_abm_no_ode: 5.5337
- rmse_ode: 1.6399
- rmse_reduced: 5.1439
- threshold: 0.9858

### Calibración
- forcing_scale: 0.7718
- macro_coupling: 0.0888
- ode_coupling_strength: 0.0710
- abm_feedback_gamma: 0.0500
- damping: 0.7565
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 0.1440
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.2273
- bootstrap_mean: 0.2879
- CI 95%: [0.1617, 0.4910]
- weighted_value (LoE factor 0.20): 0.0455
- válido (0.30-0.90): False
- detrended_edi: 0.2273
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9835
- external: -0.8115
- CR: 1.2119
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9243
- rmse_abm_no_ode: 3.7846
- rmse_ode: 2.7927
- rmse_reduced: 3.8040
- threshold: 2.7353

### Calibración
- forcing_scale: 0.7500
- macro_coupling: 0.4501
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6654
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2786
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

