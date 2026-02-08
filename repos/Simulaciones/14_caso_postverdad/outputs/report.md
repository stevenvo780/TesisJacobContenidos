# Reporte de Validación — Postverdad y Desinformación

- generated_at: 2026-02-07T14:52:42.891645Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.7220
- bootstrap_mean: 0.7223
- CI 95%: [0.7148, 0.7303]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9997
- CR: 1.0003
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.4926
- rmse_ode: 1.2363
- rmse_reduced: 5.3700
- threshold: 1.8240

### Calibración
- forcing_scale: 0.4140
- macro_coupling: 0.5797
- damping: 0.5973
- ode_alpha: 0.0434
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1484

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1536
- bootstrap_mean: 0.1547
- CI 95%: [0.1322, 0.1806]
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9860
- external: 0.0295
- CR: 33.4263
- CR válido (>2.0): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8533
- rmse_ode: 1.2914
- rmse_reduced: 3.3713
- threshold: 0.8795

### Calibración
- forcing_scale: 0.5905
- macro_coupling: 0.7946
- damping: 0.8892
- ode_alpha: 0.3686
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.1595

