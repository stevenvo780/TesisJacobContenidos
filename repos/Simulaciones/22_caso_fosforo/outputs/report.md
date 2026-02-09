# Reporte de Validación — Ciclo del Fósforo (Carpenter Biogeoquímico)

- generated_at: 2026-02-09T02:21:02.795692Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1670
- bootstrap_mean: 0.1682
- CI 95%: [0.1509, 0.1910]
- weighted_value (LoE factor 0.60): 0.1002
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9998
- external: 0.9990
- CR: 1.0008
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.9371
- rmse_abm_no_ode: 1.1250
- rmse_ode: 0.5140
- rmse_reduced: 3.2930
- threshold: 0.8072

### Calibración
- forcing_scale: 0.9465
- macro_coupling: 0.3435
- damping: 0.9500
- ode_alpha: 0.1841
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2314

## Fase real
- **overall_pass**: False

### EDI
- valor: -3.6125
- bootstrap_mean: -3.6565
- CI 95%: [-4.3298, -3.0948]
- weighted_value (LoE factor 0.60): -2.1675
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9914
- external: 0.9932
- CR: 0.9983
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5089
- rmse_abm_no_ode: 0.3271
- rmse_ode: 3.4114
- rmse_reduced: 2.3362
- threshold: 0.4564

### Calibración
- forcing_scale: 0.9398
- macro_coupling: 0.6239
- damping: 0.9500
- ode_alpha: 0.0114
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2782

