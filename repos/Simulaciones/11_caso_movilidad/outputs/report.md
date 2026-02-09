# Reporte de Validación — Movilidad Urbana (Traffic)

- generated_at: 2026-02-09T05:11:16.639421Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0196
- bootstrap_mean: 0.0194
- CI 95%: [-0.0022, 0.0409]
- weighted_value (LoE factor 0.20): 0.0039
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0000
- external: 0.0000
- CR: 0.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: False
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 33.9854
- rmse_abm_no_ode: 34.6640
- rmse_ode: 138.7294
- rmse_reduced: 89.1702
- threshold: 0.4998

### Calibración
- forcing_scale: 0.8052
- macro_coupling: 0.1256
- damping: 0.1005
- ode_alpha: 0.2695
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 93.3991

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 1.00): 0.0000
- válido (0.30-0.90): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: False
- c5_uncertainty: False

