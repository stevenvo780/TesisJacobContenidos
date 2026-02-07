# Reporte de Validación — Paradigmas Científicos (OpenAlex)

- generated_at: 2026-02-06T21:58:58.875222Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8270
- bootstrap_mean: 0.8280
- CI 95%: [0.7801, 0.8688]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9798
- CR: 1.0206
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5379
- rmse_ode: 0.5537
- rmse_reduced: 3.1093
- threshold: 0.5325

### Calibración
- forcing_scale: 0.1238
- macro_coupling: 0.6372
- damping: 0.1559
- ode_alpha: 0.4197
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6520

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4600
- bootstrap_mean: 0.4592
- CI 95%: [0.4230, 0.4886]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9255
- CR: 1.0804
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5989
- rmse_ode: 1.9095
- rmse_reduced: 2.9612
- threshold: 0.7107

### Calibración
- forcing_scale: 0.1874
- macro_coupling: 0.1259
- damping: 0.1655
- ode_alpha: 0.2776
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8985

