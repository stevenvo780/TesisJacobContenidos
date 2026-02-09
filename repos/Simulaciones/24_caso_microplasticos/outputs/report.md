# Reporte de Validación — Microplásticos Oceánicos (Jambeck Persistent Accumulation)

- generated_at: 2026-02-09T04:43:46.736790Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.6768
- bootstrap_mean: 0.6760
- CI 95%: [0.6361, 0.7071]
- weighted_value (LoE factor 0.80): 0.5414
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.6103
- external: 0.8477
- CR: 0.7200
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.5037
- rmse_abm_no_ode: 1.5583
- rmse_ode: 2.8335
- rmse_reduced: 0.9659
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9469
- macro_coupling: 0.6115
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2170

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.5906
- bootstrap_mean: 0.5917
- CI 95%: [0.5738, 0.6208]
- weighted_value (LoE factor 0.80): 0.4725
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9966
- CR: 1.0034
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 7.3764
- rmse_abm_no_ode: 18.0173
- rmse_ode: 2.5599
- rmse_reduced: 4.5301
- threshold: 1.4633

### Calibración
- forcing_scale: 0.7461
- macro_coupling: 1.0000
- damping: 0.4276
- ode_alpha: 0.0444
- ode_beta: 0.0134
- assimilation_strength: 0.0000
- calibration_rmse: 0.3875

