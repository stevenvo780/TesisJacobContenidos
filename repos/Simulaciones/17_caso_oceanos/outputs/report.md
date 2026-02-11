# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-11T01:38:38.806810Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.7327
- bootstrap_mean: 0.7329
- CI 95%: [0.7244, 0.7419]
- weighted_value (LoE factor 0.20): 0.1465
- válido (0.30-0.90): True
- detrended_edi: 0.7327
- trend_ratio: 1.000
- trend_r2: 0.961

### Symploké y CR
- internal: 1.0000
- external: 0.9998
- CR: 1.0002
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9814
- rmse_abm_no_ode: 1.0783
- rmse_ode: 1.3596
- rmse_reduced: 3.6713
- threshold: 0.9858

### Calibración
- forcing_scale: 0.7718
- macro_coupling: 0.0888
- ode_coupling_strength: 0.0710
- abm_feedback_gamma: 0.0500
- damping: 0.7565
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 0.1440
- ode_rolling: None

### Interpretación
**Nivel 4 — Cierre operativo fuerte.** El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística, indicando constricción macro→micro robusta. No obstante, estos resultados no implican compromiso ontológico: el cierre es operativo, no sustancial.

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.2847
- bootstrap_mean: -0.3504
- CI 95%: [-0.8892, -0.0809]
- weighted_value (LoE factor 0.20): -0.0569
- válido (0.30-0.90): False
- detrended_edi: -0.2847
- trend_ratio: 1.000
- trend_r2: 0.615

### Symploké y CR
- internal: 0.9995
- external: 0.9997
- CR: 0.9998
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.5463
- rmse_abm_no_ode: 4.1000
- rmse_ode: 2.8085
- rmse_reduced: 2.7605
- threshold: 2.7353

### Calibración
- forcing_scale: 0.7500
- macro_coupling: 0.4501
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.6654
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2786
- ode_rolling: None

### Interpretación
**Nivel 0 — Sin cierre operativo.** No se detecta constricción macro→micro significativa con los datos y parámetros actuales.

