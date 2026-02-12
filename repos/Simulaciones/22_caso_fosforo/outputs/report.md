# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-12T01:19:54.255537Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.1162
- bootstrap_mean: 0.1176
- CI 95%: [0.0966, 0.1450]
- weighted_value (LoE factor 0.60): 0.0697
- válido (0.30-0.90): True
- detrended_edi: 0.1162
- trend_ratio: 1.000
- trend_r2: 0.534

### Symploké y CR
- internal: 0.9987
- external: 0.9929
- CR: 1.0058
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5737
- rmse_abm_no_ode: 1.7807
- rmse_ode: 2.4494
- rmse_reduced: 2.5775
- threshold: 0.9097

### Calibración
- forcing_scale: 0.9384
- macro_coupling: 0.1000
- ode_coupling_strength: 0.0800
- abm_feedback_gamma: 0.0500
- damping: 0.8906
- ode_alpha: 0.0401
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8076
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.3760
- bootstrap_mean: 0.3751
- CI 95%: [0.1714, 0.5367]
- weighted_value (LoE factor 0.60): 0.2256
- válido (0.30-0.90): True
- detrended_edi: 0.3760
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9997
- external: 0.9979
- CR: 1.0018
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.2321
- rmse_abm_no_ode: 0.3719
- rmse_ode: 1.5484
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9192
- macro_coupling: 0.2673
- ode_coupling_strength: 0.2138
- abm_feedback_gamma: 0.0500
- damping: 0.8389
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2824
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

