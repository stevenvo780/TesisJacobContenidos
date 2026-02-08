# Validacion C1–C5 — Emisiones CO2 (Oceanos)

## C1 Convergencia
- Fase sintetica: ABM y ODE deben ajustar la serie sintetica con error bajo umbral.
- Fase real: ABM y ODE deben ajustar la serie real con error bajo umbral.
- Datos reales: World Bank API — `EN.ATM.CO2E.KT` (1960–2022).
- Umbral: `0.6 * sigma` del conjunto de validacion.
- Correlacion minima: > 0.70 entre serie observada y simulada.

### Verificacion (escenario controlado)
- La fase sintetica funciona como escenario simple con resultado conocido.
- Si falla, el modelo se invalida antes de pasar a datos reales.

## C2 Robustez
- Parametros se perturban en rango ±10%.
- Resultados deben permanecer estables (regimen y metricas).
- Se verifican al menos 5 perturbaciones independientes.
- El EDI no debe variar mas de ±0.05 bajo perturbacion.

## C3 Replicacion
- Dos semillas/condiciones iniciales distintas.
- Se espera misma conclusion cualitativa (persistencia y no-localidad).
- Independencia de semilla: resultados consistentes entre ejecuciones.

## C4 Validez
- Sensibilidad al forcing: el modelo debe responder coherentemente
  a cambios en las emisiones de CO2 y politicas energeticas.
- Coherencia con datos del dominio (tasas de emision observadas).
- Acoplamiento minimo: `coupling > 0.10` (si no, epifenomenalismo).

## C5 Cuantificacion de incertidumbre
- Bootstrap CI al 95% para EDI y metricas principales.
- Reporte explicito de limites y sensibilidad del modelo.
- Documentacion de fallos y condiciones de borde.
