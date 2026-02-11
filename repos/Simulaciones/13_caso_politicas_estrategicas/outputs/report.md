# Reporte de Validación — Políticas Estratégicas (Bass Diffusion + Inertia)

- generated_at: 2026-02-11T22:21:26.395038Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1709
- bootstrap_mean: -0.1781
- CI 95%: [-0.5645, 0.1622]
- weighted_value (LoE factor 0.60): -0.1025
- válido (0.30-0.90): False
- detrended_edi: -0.1709
- trend_ratio: 1.000
- trend_r2: 0.794

### Symploké y CR
- internal: 0.9970
- external: 0.9876
- CR: 1.0095
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2562
- rmse_abm_no_ode: 0.2188
- rmse_ode: 0.6014
- rmse_reduced: 2.5670
- threshold: 0.2856

### Calibración
- forcing_scale: 0.9562
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8079
- ode_alpha: 0.2951
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2319
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.2879
- bootstrap_mean: 0.2868
- CI 95%: [0.2402, 0.3252]
- weighted_value (LoE factor 0.60): 0.1727
- válido (0.30-0.90): True
- detrended_edi: 0.2879
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9986
- external: 0.9901
- CR: 1.0085
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5079
- rmse_abm_no_ode: 0.7133
- rmse_ode: 0.9070
- rmse_reduced: 0.9596
- threshold: 0.1452

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8875
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3550
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

