# Reporte de Validación — Constelaciones Satelitales (Starlink)

- generated_at: 2026-02-07T15:41:28.265196Z

## Fase synthetic
- **overall_pass**: True

### EDI
- valor: 0.9700
- bootstrap_mean: 0.9699
- CI 95%: [0.9664, 0.9733]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.0856
- rmse_ode: 0.5068
- rmse_reduced: 2.8514
- threshold: 0.6180

### Calibración
- forcing_scale: 0.6339
- macro_coupling: 0.1672
- damping: 0.9500
- ode_alpha: 0.1952
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0880

## Fase real
- **overall_pass**: True

### EDI
- valor: 0.9144
- bootstrap_mean: 0.9170
- CI 95%: [0.8979, 0.9514]
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 1.0000
- CR: 1.0000
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: True
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.6740
- rmse_ode: 2.0294
- rmse_reduced: 7.8773
- threshold: 3.4570

### Calibración
- forcing_scale: 0.6774
- macro_coupling: 0.4557
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.2250

