# Reporte de Validación — Deforestación Global

- generated_at: 2026-02-08T20:50:56.932278Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.7590
- bootstrap_mean: -1.7601
- CI 95%: [-1.8374, -1.6972]
- weighted_value (LoE factor 0.20): -0.3518
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9999
- CR: 1.0000
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.8875
- rmse_abm_no_ode: 0.6841
- rmse_ode: 3.1246
- rmse_reduced: 3.1666
- threshold: 0.7096

### Calibración
- forcing_scale: 0.6059
- macro_coupling: 0.5906
- damping: 0.5954
- ode_alpha: 0.0112
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.0698

## Fase real
- **overall_pass**: False

### EDI
- valor: -1.6399
- bootstrap_mean: -1.6464
- CI 95%: [-1.8016, -1.5242]
- weighted_value (LoE factor 0.20): -0.3280
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.4198
- external: 0.8050
- CR: 0.5214
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 3.0345
- rmse_abm_no_ode: 1.1495
- rmse_ode: 5.4783
- rmse_reduced: 3.5314
- threshold: 0.8479

### Calibración
- forcing_scale: 0.9418
- macro_coupling: 0.7726
- damping: 0.9500
- ode_alpha: 0.0010
- ode_beta: 0.0010
- assimilation_strength: 0.0000
- calibration_rmse: 0.1371

