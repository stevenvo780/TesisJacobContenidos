# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-09T02:33:10.770205Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.1425
- bootstrap_mean: -0.1453
- CI 95%: [-0.2049, -0.0968]
- weighted_value (LoE factor 0.20): -0.0285
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9817
- external: 0.5407
- CR: 1.8158
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.4294
- rmse_abm_no_ode: 3.0016
- rmse_ode: 1.3662
- rmse_reduced: 2.8463
- threshold: 0.9858

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0068
- ode_beta: 0.7284
- assimilation_strength: 0.0000
- calibration_rmse: 2.1251

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0690
- bootstrap_mean: -0.0715
- CI 95%: [-0.1270, -0.0221]
- weighted_value (LoE factor 0.20): -0.0138
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9824
- external: 0.5190
- CR: 1.8928
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.9249
- rmse_abm_no_ode: 2.7360
- rmse_ode: 0.8567
- rmse_reduced: 2.6139
- threshold: 1.1913

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0082
- ode_beta: 0.9450
- assimilation_strength: 0.0000
- calibration_rmse: 2.1823

