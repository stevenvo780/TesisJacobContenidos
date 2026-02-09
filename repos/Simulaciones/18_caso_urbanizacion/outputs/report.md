# Reporte de Validación — Urbanización (Bettencourt + Preferential Attachment)

- generated_at: 2026-02-09T02:54:35.964860Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.0008
- bootstrap_mean: 0.0008
- CI 95%: [0.0006, 0.0010]
- weighted_value (LoE factor 0.20): 0.0002
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0020
- external: -0.0003
- CR: 5.5749
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0476
- rmse_abm_no_ode: 2.0493
- rmse_ode: 2.0480
- rmse_reduced: 2.0466
- threshold: 0.4782

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 1.2606

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0011
- bootstrap_mean: 0.0011
- CI 95%: [0.0010, 0.0012]
- weighted_value (LoE factor 0.20): 0.0002
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.0021
- external: 0.0005
- CR: 4.0528
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 2.0576
- rmse_abm_no_ode: 2.0598
- rmse_ode: 2.0601
- rmse_reduced: 2.0557
- threshold: 0.4748

### Calibración
- forcing_scale: 0.0010
- macro_coupling: 0.1000
- damping: 0.0000
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 1.2645

