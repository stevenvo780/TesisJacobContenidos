# Reporte de Validación — Energía (Consumo Per Cápita)

- generated_at: 2026-02-11T15:28:36.378115Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.5001
- bootstrap_mean: 0.4990
- CI 95%: [0.4599, 0.5367]
- weighted_value (LoE factor 0.20): 0.1000
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9876
- external: 0.9788
- CR: 1.0090
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2594
- rmse_abm_no_ode: 0.4903
- rmse_ode: 2.4548
- rmse_reduced: 2.5191
- threshold: 0.8006

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7225
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2764
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.7890
- bootstrap_mean: 0.7908
- CI 95%: [0.7328, 0.8453]
- weighted_value (LoE factor 0.20): 0.1578
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9996
- external: 0.9993
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5504
- rmse_abm_no_ode: 1.1442
- rmse_ode: 2.7727
- rmse_reduced: 2.6081
- threshold: 0.3586

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6746
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2688
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

