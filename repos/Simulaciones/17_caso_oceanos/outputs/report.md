# Reporte de Validación — Océanos (OHC proxy)

- generated_at: 2026-02-11T22:45:41.929103Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.1714
- bootstrap_mean: 0.1754
- CI 95%: [0.1529, 0.2099]
- weighted_value (LoE factor 0.60): 0.1028
- válido (0.30-0.90): True
- detrended_edi: 0.1714
- trend_ratio: 1.000
- trend_r2: 0.982

### Symploké y CR
- internal: 0.9998
- external: 0.9987
- CR: 1.0010
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8231
- rmse_abm_no_ode: 2.2002
- rmse_ode: 1.1859
- rmse_reduced: 4.5141
- threshold: 1.2593

### Calibración
- forcing_scale: 0.6384
- macro_coupling: 0.4216
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5906
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.3181
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0316
- bootstrap_mean: -0.0391
- CI 95%: [-0.0652, -0.0221]
- weighted_value (LoE factor 0.60): -0.0189
- válido (0.30-0.90): False
- detrended_edi: -0.0316
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9999
- external: 0.9975
- CR: 1.0024
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.1755
- rmse_abm_no_ode: 4.0476
- rmse_ode: 4.5526
- rmse_reduced: 2.7605
- threshold: 2.7353

### Calibración
- forcing_scale: 0.6384
- macro_coupling: 0.2216
- ode_coupling_strength: 0.1772
- abm_feedback_gamma: 0.0500
- damping: 0.5906
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2831
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

