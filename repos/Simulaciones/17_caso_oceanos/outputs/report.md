# Reporte de Validación — Ocean (Stommel + Thermohaline ABM)

- generated_at: 2026-02-09T16:16:57.724483Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1095
- bootstrap_mean: 0.1073
- CI 95%: [0.0691, 0.1385]
- weighted_value (LoE factor 0.20): 0.0219
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9703
- external: 0.2697
- CR: 3.5976
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 4.9276
- rmse_abm_no_ode: 5.5337
- rmse_ode: 1.4691
- rmse_reduced: 5.1439
- threshold: 0.9858

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0024
- ode_beta: 0.8191
- assimilation_strength: 0.0000
- calibration_rmse: 2.2767

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.1193
- bootstrap_mean: 0.1571
- CI 95%: [0.0815, 0.2807]
- weighted_value (LoE factor 0.20): 0.0239
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9677
- external: -0.7777
- CR: 1.2443
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.3330
- rmse_abm_no_ode: 3.7846
- rmse_ode: 2.7954
- rmse_reduced: 3.8040
- threshold: 2.7353

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.2690
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 2.5036

