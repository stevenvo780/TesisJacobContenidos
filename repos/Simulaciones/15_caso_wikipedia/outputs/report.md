# Reporte de Validación — Wikipedia (Conocimiento Colectivo)

- generated_at: 2026-02-11T16:13:19.267269Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.4669
- bootstrap_mean: 0.4682
- CI 95%: [0.4406, 0.4997]
- weighted_value (LoE factor 0.20): 0.0934
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9993
- external: 0.9737
- CR: 1.0263
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1645
- rmse_abm_no_ode: 2.8659
- rmse_ode: 2.8993
- rmse_reduced: 4.0602
- threshold: 1.4087

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.7622
- ode_alpha: 0.0485
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.7028
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.3078
- bootstrap_mean: 0.3558
- CI 95%: [0.1986, 0.5381]
- weighted_value (LoE factor 0.20): 0.0616
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9986
- external: 0.9794
- CR: 1.0196
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.3205
- rmse_abm_no_ode: 2.5213
- rmse_ode: 2.5167
- rmse_reduced: 3.3523
- threshold: 2.2194

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.7182
- ode_alpha: 0.0985
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8451
- ode_rolling: None

### Interpretación
**Nivel 3 — Cierre operativo weak.** La constricción macro es detectable pero no alcanza robustez suficiente para cierre operativo fuerte. El fenómeno muestra grados parciales de organización macro→micro.

