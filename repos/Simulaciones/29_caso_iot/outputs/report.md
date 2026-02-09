# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T05:10:33.111016Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.3623
- bootstrap_mean: 0.3629
- CI 95%: [0.3398, 0.3942]
- weighted_value (LoE factor 0.80): 0.2898
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9995
- external: 0.9610
- CR: 1.0401
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.8170
- rmse_abm_no_ode: 4.4175
- rmse_ode: 0.6975
- rmse_reduced: 6.1851
- threshold: 2.4539

### Calibración
- forcing_scale: 0.9112
- macro_coupling: 0.5006
- damping: 0.9500
- ode_alpha: 0.2950
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6710

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0181
- bootstrap_mean: 0.0176
- CI 95%: [-0.0095, 0.0393]
- weighted_value (LoE factor 0.80): 0.0145
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9219
- CR: 1.0847
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.0326
- rmse_abm_no_ode: 34.6601
- rmse_ode: 34.2993
- rmse_reduced: 40.8515
- threshold: 10.9486

### Calibración
- forcing_scale: 0.5962
- macro_coupling: 1.0000
- damping: 0.2894
- ode_alpha: 0.0981
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.5975

