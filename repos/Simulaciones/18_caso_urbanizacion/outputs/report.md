# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-09T16:17:13.382275Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0001
- bootstrap_mean: 0.0001
- CI 95%: [0.0000, 0.0001]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0007
- external: 0.0002
- CR: 4.0421
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0439
- rmse_abm_no_ode: 2.0440
- rmse_ode: 2.0427
- rmse_reduced: 2.0406
- threshold: 0.4782

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0710
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 1.1699

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0000
- bootstrap_mean: 0.0000
- CI 95%: [0.0000, 0.0000]
- weighted_value (LoE factor 0.20): 0.0000
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0018
- external: 0.0012
- CR: 1.4720
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.6843
- rmse_abm_no_ode: 2.6844
- rmse_ode: 2.6832
- rmse_reduced: 2.6812
- threshold: 0.8867

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 1.1743

