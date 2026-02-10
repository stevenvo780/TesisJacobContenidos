# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-10T16:42:32.062848Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8800
- bootstrap_mean: 0.8801
- CI 95%: [0.8727, 0.8883]
- weighted_value (LoE factor 0.60): 0.5280
- válido (0.30-0.90): True
- detrended_edi: 0.8800
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9763
- CR: 1.0243
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1522
- rmse_abm_no_ode: 1.2686
- rmse_ode: 6.2543
- rmse_reduced: 3.7881
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3668
- macro_coupling: 0.3785
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3656
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1169
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.6339
- bootstrap_mean: 0.6378
- CI 95%: [0.5348, 0.7525]
- weighted_value (LoE factor 0.60): 0.3803
- válido (0.30-0.90): True
- detrended_edi: 0.6339
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9998
- external: 0.9785
- CR: 1.0218
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5056
- rmse_abm_no_ode: 1.3809
- rmse_ode: 2.6720
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.6588
- macro_coupling: 0.3581
- ode_coupling_strength: 0.2865
- abm_feedback_gamma: 0.0500
- damping: 0.7095
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1872
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

