# Reporte de Validación — Océanos (OHC proxy)

- generated_at: 2026-02-11T16:15:56.011783Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8084
- bootstrap_mean: 0.8087
- CI 95%: [0.7899, 0.8279]
- weighted_value (LoE factor 0.20): 0.1617
- válido (0.30-0.90): True
- detrended_edi: 0.8084
- trend_ratio: 1.000
- trend_r2: 0.533

### Symploké y CR
- internal: 0.9998
- external: 0.9991
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5033
- rmse_abm_no_ode: 0.5721
- rmse_ode: 0.4912
- rmse_reduced: 2.6265
- threshold: 0.7016

### Calibración
- forcing_scale: 0.9107
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0467
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2715
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.5362
- bootstrap_mean: -0.7174
- CI 95%: [-1.6351, -0.3508]
- weighted_value (LoE factor 0.20): -0.1072
- válido (0.30-0.90): False
- detrended_edi: -0.5362
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9998
- external: 0.9988
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.2407
- rmse_abm_no_ode: 4.1828
- rmse_ode: 4.5660
- rmse_reduced: 2.7605
- threshold: 2.7353

### Calibración
- forcing_scale: 0.7616
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.6956
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2769
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

