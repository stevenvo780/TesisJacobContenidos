# Reporte de Validación — Deforestación Global (von Thünen Frontier)

- generated_at: 2026-02-09T22:02:13.054909Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.8466
- bootstrap_mean: 0.8465
- CI 95%: [0.8296, 0.8603]
- weighted_value (LoE factor 0.60): 0.5079
- válido (0.30-0.90): True
- detrended_edi: 0.8466
- trend_ratio: 1.000
- trend_r2: 0.999

### Symploké y CR
- internal: 1.0000
- external: 0.9685
- CR: 1.0325
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.1942
- rmse_abm_no_ode: 1.2657
- rmse_ode: 6.9696
- rmse_reduced: 3.7882
- threshold: 0.9651

### Calibración
- forcing_scale: 0.3467
- macro_coupling: 0.4770
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.3368
- ode_alpha: 0.0105
- ode_beta: 0.9577
- assimilation_strength: 0.0000
- calibration_rmse: 0.1170
- ode_rolling: None

### Interpretación
Los resultados **sugieren** emergencia macro significativa. El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística. No obstante, estos resultados deben interpretarse en el contexto de las limitaciones del proxy utilizado y del nivel de evidencia (LoE) del caso.

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.6331
- bootstrap_mean: 0.6318
- CI 95%: [0.5221, 0.7344]
- weighted_value (LoE factor 0.60): 0.3799
- válido (0.30-0.90): True
- detrended_edi: 0.6331
- trend_ratio: 1.000
- trend_r2: 0.785

### Symploké y CR
- internal: 0.9994
- external: 0.9827
- CR: 1.0170
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4270
- rmse_abm_no_ode: 1.1639
- rmse_ode: 2.4862
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.8999
- macro_coupling: 0.4073
- ode_coupling_strength: 0.3000
- abm_feedback_gamma: 0.0500
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1431
- ode_rolling: None

### Interpretación
Los resultados **sugieren** emergencia macro significativa. El EDI se encuentra en el rango válido y el test de permutación confirma significancia estadística. No obstante, estos resultados deben interpretarse en el contexto de las limitaciones del proxy utilizado y del nivel de evidencia (LoE) del caso.

