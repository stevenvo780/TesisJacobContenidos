# Indicadores, Metricas y Reglas — Deforestacion Global

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Indice de Dependencia Efectiva)
- Formula: `EDI = (rmse_reduced - rmse_abm) / rmse_reduced`
- Interpretacion: fraccion de error explicada por la capa macro.
- Umbral de aceptacion: `0.30 < EDI < 0.90`.
- EDI < 0.30 → RECHAZO (sin estructura macro detectada).
- EDI > 0.90 → RECHAZO (tautologia / error de calibracion).

## CR (Ratio de Cohesion)
- Formula: cohesion interna / cohesion externa.
- Regla: CR > 2.0 indica que la cohesion interna supera la externa.
- Verifica la propiedad Symploke del hiperobjeto.

## EI (Informacion Efectiva)
- Metrica de Hoel para cuantificar la informacion causal.
- Compara la informacion generada por el nivel macro vs micro.
- Mayor EI macro → evidencia de emergencia fuerte.

## RMSE (Error Cuadratico Medio)
- Evaluado sobre ventana de validacion exclusivamente.
- Umbral de fraude: RMSE < 1e-10 → RECHAZO (sobreajuste).
- Permite comparar modelo completo vs modelo reducido.

## Correlacion
- Pearson entre serie observada y serie simulada.
- Umbral minimo: correlacion > 0.70 para C1.

## Bootstrap CI (Intervalos de Confianza)
- Muestreo bootstrap para estimar incertidumbre del EDI.
- Se reporta intervalo de confianza al 95%.
- Verifica estabilidad estadistica de las metricas.

## Symploke (cohesion)
- Correlacion media de vecinos internos vs correlacion con forcing externo.
- Regla: cohesion interna > externa con diferencia positiva.

## No-localidad funcional
- Dominancia de fuentes (max share de influencia).
- Regla: ninguna fuente supera el umbral definido por caso.

## Persistencia estructural
- Estabilidad de regimen (varianza de `D_bar` en ventanas largas).
- Regla: estabilidad bajo perturbaciones razonables.
