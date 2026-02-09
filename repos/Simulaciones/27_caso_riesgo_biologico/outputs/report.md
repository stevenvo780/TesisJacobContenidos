# Reporte de Validación — Riesgo Biológico Global (TB Incidence — Woolhouse)

- generated_at: 2026-02-09T14:45:49.647211Z

## Fase synthetic
- **overall_pass**: False

### EDI
- valor: -0.0937
- bootstrap_mean: -0.0852
- CI 95%: [-0.1484, 0.0100]
- weighted_value (LoE factor 0.80): -0.0749
- válido (0.30-0.90): False

### Symploké y CR
- internal: 0.9887
- external: 0.9756
- CR: 1.0134
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 1.1896
- rmse_abm_no_ode: 1.0877
- rmse_ode: 1.4691
- rmse_reduced: 1.9006
- threshold: 0.7958

### Calibración
- forcing_scale: 0.8433
- macro_coupling: 0.5364
- damping: 0.9236
- ode_alpha: 0.0968
- ode_beta: 1.0000
- assimilation_strength: 0.0000
- calibration_rmse: 0.8632

## Fase real
- **overall_pass**: False

### EDI
- valor: 0.4006
- bootstrap_mean: 0.3685
- CI 95%: [0.1236, 0.5061]
- weighted_value (LoE factor 0.80): 0.3205
- válido (0.30-0.90): True

### Symploké y CR
- internal: 0.9999
- external: 0.9965
- CR: 1.0034
- CR indicador (>2.0 = frontera nítida): False

### Criterios C1-C5
- c1_convergence: False
- c2_robustness: True
- c3_replication: True
- c4_validity: True
- c5_uncertainty: True

### Errores
- rmse_abm: 0.4856
- rmse_abm_no_ode: 0.8103
- rmse_ode: 1.0987
- rmse_reduced: 2.1157
- threshold: 0.1000

### Calibración
- forcing_scale: 0.9900
- macro_coupling: 0.2904
- damping: 0.6059
- ode_alpha: 0.1288
- ode_beta: 0.5822
- assimilation_strength: 0.0000
- calibration_rmse: 0.1920

