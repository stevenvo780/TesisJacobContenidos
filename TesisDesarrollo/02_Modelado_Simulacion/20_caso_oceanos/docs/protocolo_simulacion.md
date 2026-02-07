# Protocolo de Simulacion — Emisiones CO2 (Oceanos)

## 1. Definicion de escenario
- Objetivo: demostrar que las emisiones globales de CO2 operan como hiperobjeto,
  constriniendo la actividad economica local mediante forcing macro.
- Señal: acumulacion secular de CO2 — el hiperobjeto quintesencial (Morton).
- Delimitacion: frontera funcional, cohesion interna > externa.

## 2. Fases de validacion

### Fase sintetica (verdad controlada)
- Serie sintetica generada con parametros conocidos.
- Permite verificar que el pipeline recupera la estructura macro esperada.
- Si la fase sintetica falla, la fase real se bloquea automaticamente.

### Fase real (datos World Bank)
- Fuente: World Bank API — indicador `EN.ATM.CO2E.KT`.
- Rango: 1960–2022, frecuencia anual.
- Normalizacion Z sobre la ventana de entrenamiento.

## 3. Division train/validacion
- Split temporal: datos divididos en entrenamiento y validacion.
- Todas las metricas se evaluan exclusivamente sobre `val_df`.
- Sin look-ahead: asimilacion usa observaciones rezagadas `[None] + obs[:-1]`.

## 4. Calibracion
- Grid search exhaustivo: 3135 combinaciones de parametros ABM.
  - `forcing_scale`, `macro_coupling`, `damping`.
- Ajuste por minimos cuadrados para parametros ODE (`alpha`, `beta`).
- Refinamiento iterativo sobre los mejores candidatos.

## 5. Ejecucion del modelo
- **Modelo completo:** ABM + ODE con `assimilation_strength=0.0`.
- **Modelo reducido:** ABM con `macro_coupling=0.0, forcing_scale=0.0` (ablacion).
- Grilla: 20×20 celdas.

## 6. Criterio de paro
- Estabilidad de patrones (varianza de `E_bar` estabilizada).
- Costo marginal de iteracion > beneficio.

## 7. Evaluacion
- EDI = `(rmse_reduced - rmse_abm) / rmse_reduced` sobre ventana de validacion.
- Protocolo C1–C5 completo + verificaciones Symploke, no-localidad, persistencia.
