# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T20:55:58.944416Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.3453
- bootstrap_mean: 0.3482
- CI 95%: [0.3191, 0.3858]
- weighted_value (LoE factor 0.60): 0.2072
- válido (0.30-0.90): True
- detrended_edi: 0.3453
- trend_ratio: 1.000
- trend_r2: 0.960

### Symploké y CR
- internal: 0.9999
- external: 0.9952
- CR: 1.0046
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.8747
- rmse_abm_no_ode: 1.3359
- rmse_ode: 0.4912
- rmse_reduced: 3.5591
- threshold: 0.8987

### Calibración
- forcing_scale: 0.9465
- macro_coupling: 0.2935
- ode_coupling_strength: 0.2348
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.1286
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2112
- ode_rolling: None

### Interpretación
Los resultados **sugieren** emergencia macro significativa. El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística. No obstante, estos resultados deben interpretarse en el contexto de las limitaciones del proxy utilizado y del nivel de evidencia (LoE) del caso.

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.0000
- bootstrap_mean: -2.7133
- CI 95%: [-3.3267, -2.1635]
- weighted_value (LoE factor 0.60): -0.6000
- válido (0.30-0.90): False
- detrended_edi: -1.0000
- trend_ratio: 1.000
- trend_r2: 0.774

### Symploké y CR
- internal: 0.9986
- external: 0.9380
- CR: 1.0646
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.2117
- rmse_abm_no_ode: 0.3288
- rmse_ode: 3.7863
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9385
- macro_coupling: 0.5000
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2782
- ode_rolling: None

### Interpretación
Categoría de emergencia: **null**. No se detecta estructura macro significativa con los datos y parámetros actuales.

