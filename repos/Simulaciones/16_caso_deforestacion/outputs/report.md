# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-11T02:09:45.071921Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6887
- bootstrap_mean: 0.6883
- CI 95%: [0.6797, 0.6943]
- weighted_value (LoE factor 0.60): 0.4132
- válido (0.30-0.90): True
- detrended_edi: 0.6887
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9996
- CR: 1.0004
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1793
- rmse_abm_no_ode: 1.2695
- rmse_ode: 2.6828
- rmse_reduced: 3.7882
- threshold: 0.9651

### Calibración
- forcing_scale: 0.4382
- macro_coupling: 0.0500
- ode_coupling_strength: 0.0400
- abm_feedback_gamma: 0.0500
- damping: 0.4281
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1171
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.8612
- bootstrap_mean: 0.8599
- CI 95%: [0.8148, 0.9049]
- weighted_value (LoE factor 0.60): 0.5167
- válido (0.30-0.90): True
- detrended_edi: 0.8612
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9992
- external: 0.9758
- CR: 1.0240
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4903
- rmse_abm_no_ode: 1.2055
- rmse_ode: 2.6680
- rmse_reduced: 3.5313
- threshold: 0.8479

### Calibración
- forcing_scale: 0.8890
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.8872
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1495
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

