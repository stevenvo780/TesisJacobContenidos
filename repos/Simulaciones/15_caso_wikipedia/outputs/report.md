# Reporte de Validación — Wikipedia (Conocimiento Colectivo)

- generated_at: 2026-02-11T22:46:14.653862Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.2386
- bootstrap_mean: 0.2387
- CI 95%: [0.2340, 0.2439]
- weighted_value (LoE factor 0.60): 0.1432
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9978
- CR: 1.0022
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.2817
- rmse_abm_no_ode: 2.9967
- rmse_ode: 1.5580
- rmse_reduced: 1.6761
- threshold: 1.1374

### Calibración
- forcing_scale: 0.8250
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5746
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5061
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.1596
- bootstrap_mean: 0.1946
- CI 95%: [0.1001, 0.4676]
- weighted_value (LoE factor 0.60): 0.0958
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9996
- external: 0.9432
- CR: 1.0597
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0158
- rmse_abm_no_ode: 2.3986
- rmse_ode: 2.4926
- rmse_reduced: 3.3523
- threshold: 2.2194

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4216
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.5906
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8446
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

