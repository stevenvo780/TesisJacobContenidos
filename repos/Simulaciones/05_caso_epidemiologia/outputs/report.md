# Reporte de Validación — Epidemiología (COVID-19 SEIR)

- generated_at: 2026-02-08T20:58:08.116822Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [-0.0001, 0.0001]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.1747
- external: 0.0884
- CR: 1.9766
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9348
- rmse_abm_no_ode: 0.9348
- rmse_ode: 0.9348
- rmse_reduced: 0.9348
- threshold: 0.9348

### Calibración
- forcing_scale: 0.0013
- macro_coupling: 0.4595
- damping: 0.4309
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9998

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.1627
- bootstrap_mean: -0.1681
- CI 95%: [-0.2216, -0.1257]
- weighted_value (LoE factor 0.20): -0.0325
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9984
- external: -0.0000
- CR: 281553.5001
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 247.2297
- rmse_abm_no_ode: 212.6327
- rmse_ode: 4.5217
- rmse_reduced: 4.5220
- threshold: 4.3680

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.8068
- damping: 0.8949
- ode_alpha: 0.0010
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4376

