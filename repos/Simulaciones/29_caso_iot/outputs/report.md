# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T02:57:11.253062Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1743
- bootstrap_mean: 0.1762
- CI 95%: [0.1557, 0.2032]
- weighted_value (LoE factor 0.80): 0.1395
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9993
- external: 0.9987
- CR: 1.0006
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.3706
- rmse_abm_no_ode: 2.8711
- rmse_ode: 1.5949
- rmse_reduced: 5.1035
- threshold: 1.6857

### Calibración
- forcing_scale: 0.9087
- macro_coupling: 0.5078
- damping: 0.9500
- ode_alpha: 0.3906
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4597

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.0030
- bootstrap_mean: 0.0029
- CI 95%: [-0.0151, 0.0184]
- weighted_value (LoE factor 0.80): 0.0024
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.9582
- CR: 1.0436
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 34.5552
- rmse_abm_no_ode: 34.6601
- rmse_ode: 34.9547
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

