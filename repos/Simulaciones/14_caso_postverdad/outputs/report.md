# Reporte de Validación — Postverdad y Desinformación

- generated_at: 2026-02-08T20:49:32.335007Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -1.9563
- bootstrap_mean: -1.9628
- CI 95%: [-2.1767, -1.7817]
- weighted_value (LoE factor 0.20): -0.3913
- válido (0.30-0.90): False

### Symploké y CR
- internal: -0.9983
- external: 0.0001
- CR: 6795.9761
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: False
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 12.0100
- rmse_abm_no_ode: 4.0625
- rmse_ode: 1.2224
- rmse_reduced: 1.5833
- threshold: 0.2248

### Calibración
- forcing_scale: 0.9702
- macro_coupling: 0.7555
- damping: 0.9416
- ode_alpha: 0.0573
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.2323

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.4648
- bootstrap_mean: -0.4746
- CI 95%: [-0.8372, -0.1722]
- weighted_value (LoE factor 0.20): -0.0930
- válido (0.30-0.90): False

### Symploké y CR
- internal: 1.0000
- external: 0.0479
- CR: 20.8616
- CR indicador (>2.0 = frontera nítida): True

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: False
- c5_uncertainty: True

### Errores
- rmse_abm: 1.5619
- rmse_abm_no_ode: 1.0663
- rmse_ode: nan
- rmse_reduced: 1.5619
- threshold: 0.8784

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.4279
- damping: 0.3597
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.6061

