# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-11T02:09:39.356395Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7808
- bootstrap_mean: 0.7810
- CI 95%: [0.7736, 0.7922]
- weighted_value (LoE factor 0.20): 0.1562
- válido (0.30-0.90): True
- detrended_edi: 0.7808
- trend_ratio: 1.000
- trend_r2: 0.961

### Symploké y CR
- internal: 1.0000
- external: 0.9988
- CR: 1.0012
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8049
- rmse_abm_no_ode: 1.0387
- rmse_ode: 1.3807
- rmse_reduced: 3.6713
- threshold: 0.9858

### Calibración
- forcing_scale: 0.9095
- macro_coupling: 0.3151
- ode_coupling_strength: 0.2521
- abm_feedback_gamma: 0.0500
- damping: 0.8866
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 0.1436
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.4416
- bootstrap_mean: -0.5586
- CI 95%: [-1.4946, -0.1855]
- weighted_value (LoE factor 0.20): -0.0883
- válido (0.30-0.90): False
- detrended_edi: -0.4416
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9999
- external: 0.9998
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.9795
- rmse_abm_no_ode: 4.0596
- rmse_ode: 2.8161
- rmse_reduced: 2.7605
- threshold: 2.7353

### Calibración
- forcing_scale: 0.8725
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.8070
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2809
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

