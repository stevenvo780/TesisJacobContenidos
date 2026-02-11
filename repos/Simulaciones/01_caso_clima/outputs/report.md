# Reporte de Validación — Clima Regional (CONUS)

- generated_at: 2026-02-11T04:39:50.925728Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3462
- bootstrap_mean: 0.3464
- CI 95%: [0.3386, 0.3562]
- weighted_value (LoE factor 1.00): 0.3462
- válido (0.30-0.90): True
- detrended_edi: 0.3462
- trend_ratio: 1.000
- trend_r2: 0.996

### Symploké y CR
- internal: 1.0000
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
- rmse_abm: 5.8018
- rmse_abm_no_ode: 5.8694
- rmse_ode: 4.6426
- rmse_reduced: 8.8737
- threshold: 3.5362

### Calibración
- forcing_scale: 0.6040
- macro_coupling: 0.4242
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8874
- ode_alpha: 0.1847
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2541
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1423
- bootstrap_mean: -0.1422
- CI 95%: [-0.1995, -0.0859]
- weighted_value (LoE factor 1.00): -0.1423
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9991
- external: 0.9990
- CR: 1.0001
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1009
- rmse_abm_no_ode: 1.1922
- rmse_ode: 1.6994
- rmse_reduced: 0.9637
- threshold: 0.9547

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.6353
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

