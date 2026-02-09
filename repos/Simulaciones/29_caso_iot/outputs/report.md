# Reporte de Validación — Ecosistema IoT Global (Bass-Metcalfe)

- generated_at: 2026-02-09T03:04:05.424021Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: 0.1405
- bootstrap_mean: 0.1420
- CI 95%: [0.1248, 0.1638]
- weighted_value (LoE factor 0.80): 0.1124
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9990
- external: 0.9983
- CR: 1.0007
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 2.4406
- rmse_abm_no_ode: 2.8397
- rmse_ode: 1.9562
- rmse_reduced: 4.7267
- threshold: 1.6047

### Calibración
- forcing_scale: 0.7540
- macro_coupling: 0.5555
- damping: 0.7942
- ode_alpha: 0.3792
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.5879

## Fase real
- **overall_pass**: False

### EDI
- valor: -0.0406
- bootstrap_mean: -0.0407
- CI 95%: [-0.0536, -0.0293]
- weighted_value (LoE factor 0.80): -0.0325
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9999
- external: 0.9581
- CR: 1.0437
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 36.0663
- rmse_abm_no_ode: 34.6601
- rmse_ode: 36.8848
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

