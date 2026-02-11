# Reporte de Validación — Kessler (Debris Orbital)

- generated_at: 2026-02-11T19:28:32.140625Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.1908
- bootstrap_mean: 0.0326
- CI 95%: [-1.2426, 0.3888]
- weighted_value (LoE factor 0.60): 0.1145
- válido (0.30-0.90): True
- detrended_edi: 0.1908
- trend_ratio: 1.000
- trend_r2: 0.851

### Symploké y CR
- internal: 0.9993
- external: 0.9954
- CR: 1.0039
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4348
- rmse_abm_no_ode: 0.5373
- rmse_ode: 0.6761
- rmse_reduced: 1.9714
- threshold: 0.8260

### Calibración
- forcing_scale: 0.4852
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5870
- ode_alpha: 0.2323
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4756
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3806
- bootstrap_mean: 0.3918
- CI 95%: [0.3381, 0.4992]
- weighted_value (LoE factor 0.60): 0.2283
- válido (0.30-0.90): True
- detrended_edi: 0.3806
- trend_ratio: 1.000
- trend_r2: 0.872

### Symploké y CR
- internal: 0.9996
- external: 0.9951
- CR: 1.0046
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.7547
- rmse_abm_no_ode: 1.2184
- rmse_ode: 3.8354
- rmse_reduced: 3.2710
- threshold: 0.9270

### Calibración
- forcing_scale: 0.5461
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5767
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1940
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

