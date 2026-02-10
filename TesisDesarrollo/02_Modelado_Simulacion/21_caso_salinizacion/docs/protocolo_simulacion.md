# Protocolo de Simulación — Salinización de Suelos

## 1. Definición de escenario
- Objetivo: evaluar si salinización global de suelos agrícolas como proceso macro distribuido exhibe clausura operativa
  medible a través del protocolo C1–C5.
- Variable objetivo: S (índice de salinización global).
- Indicador empírico: `AG.LND.IRIG.AG.ZS (% tierras bajo riego)`.
- Fuente: World Bank — AG.LND.IRIG.AG.ZS (irrigated land %) + ER.H2O.FWTL.ZS (freshwater withdrawal).

## 2. Fases de validación

### Fase sintética (ground truth controlado)
1. Generar serie sintética con parámetros conocidos.
2. Calibrar ABM + ODE sobre serie sintética.
3. Evaluar C1–C5 contra ground truth.
4. **Gate**: C2, C3, C4 sintéticos deben pasar para habilitar fase real.

### Fase real (datos empíricos)
1. Obtener datos de World Bank — AG.LND.IRIG.AG.ZS (irrigated land %) + ER.H2O.FWTL.ZS (freshwater withdrawal).
2. Dividir en train (pre-split) y validation (post-split).
3. Calibrar:
   - ABM: grid search (144 combinaciones) + refinamiento adaptativo (5000 iter).
   - ODE: least-squares con regularización Tikhonov.
4. Modelo completo (ABM + ODE acoplado) → predicción.
5. Modelo reducido (ABM sin ODE: macro_coupling=0, forcing_scale=0) → baseline.
6. EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido.
7. Test de permutación (n=999) + bootstrap CI (n=500).
8. Evaluar C1–C5 + Symploké + no-localidad + persistencia.

## 3. Parámetros de simulación
- **ODE**: α (tasa de salinización, ~0.05), β (lixiviación natural, ~0.015), ode_inflow=0.05, ode_decay=0.015.
- **ABM**: forcing_scale, macro_coupling, damping (calibrados por grid search).
- **Acoplamiento**: gamma=0.05, 2 iteraciones bidireccionales.
- **Assimilation_strength**: 0.0 en todas las evaluaciones (zero-nudging).

## 4. Controles de leakage
- Forcing calculado solo con datos de entrenamiento.
- Período de validación usa extrapolación por persistencia.
- No se usa assimilation en evaluación (assimilation_strength=0).
- ODE calibrada con regularización Tikhonov (previene overfitting).

## 5. Resultado
- EDI: 0.026546.
- Nivel de emergencia: 1.
- Overall pass: ❌ No.
