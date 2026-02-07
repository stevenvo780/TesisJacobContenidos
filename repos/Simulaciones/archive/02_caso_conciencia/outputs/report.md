# Reporte de Validación — Conciencia (Bienestar Global)

- generated_at: 2026-02-06T21:57:08.698171Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0372
- bootstrap_mean: -0.0461
- CI 95%: [-1.4035, 0.6612]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9244
- CR: 1.0816
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9613
- rmse_ode: 1.2698
- rmse_reduced: 0.9984
- threshold: 0.3846

### Calibración
- forcing_scale: 0.1212
- macro_coupling: 0.8532
- damping: 0.1738
- ode_alpha: 0.4569
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9402

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0247
- bootstrap_mean: -0.1453
- CI 95%: [-1.3641, 0.4115]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9200
- CR: 1.0869
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.1386
- rmse_ode: 1.9148
- rmse_reduced: 2.0870
- threshold: 0.7591

### Calibración
- forcing_scale: 0.2069
- macro_coupling: 0.1218
- damping: 0.1754
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8845

