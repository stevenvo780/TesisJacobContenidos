# Reporte de Validación — RTB Publicidad Programática

- generated_at: 2026-02-06T21:59:38.193758Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.8583
- bootstrap_mean: 0.8582
- CI 95%: [0.8387, 0.8764]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9931
- CR: 1.0069
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 0.5052
- rmse_ode: 0.7844
- rmse_reduced: 3.5651
- threshold: 0.6909

### Calibración
- forcing_scale: 0.1164
- macro_coupling: 0.2603
- damping: 0.1526
- ode_alpha: 0.3604
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.4445

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4244
- bootstrap_mean: 0.4620
- CI 95%: [0.3141, 0.6183]
- válido (0.30-0.90): True

### Symploké y CR
- internal: 1.0000
- external: 0.9642
- CR: 1.0371
- CR válido (>2.0): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: False
- c3_replication: True
- c4_validity: True
- c5_uncertainty: False

### Errores
- rmse_abm: 6.6244
- rmse_ode: 7.2716
- rmse_reduced: 11.5093
- threshold: 5.0154

### Calibración
- forcing_scale: 0.1723
- macro_coupling: 0.1767
- damping: 0.1690
- ode_alpha: 0.5000
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.9235

