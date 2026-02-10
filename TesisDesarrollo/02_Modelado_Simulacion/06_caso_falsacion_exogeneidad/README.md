# Caso Falsación: Exogeneidad (Modelo y Simulación)

**Nivel de cierre operativo:** —
**Estado:** 🔬 Control negativo (falsación)
**Generado:** 2026-02-09T20:20:00.829110

> Control de falsación: rechazo esperado por diseño experimental

## Ejecución

```bash
cd repos/Simulaciones/06_caso_falsacion_exogeneidad/src && python3 validate.py
```

## Estructura

- `docs/arquitectura.md`: capas y supuestos del modelo híbrido.
- `docs/protocolo_simulacion.md`: protocolo de simulación y criterio de paro.
- `docs/indicadores_metricas.md`: indicadores, métricas y reglas de rechazo.
- `docs/validacion_c1_c5.md`: validación operativa C1–C5.
- `docs/reproducibilidad.md`: versionado, entorno y sensibilidad.
- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | N/A | 0.055 |
| IC 95%  | N/A | [0.034, 0.074] |
| Corr ABM | N/A | 0.6005 |
| Corr ODE | N/A | 0.5264 |
| CR (Symploké) | N/A | 1.0059 |
| RMSE ABM | N/A | 2.165 |
| overall_pass | — | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=❌ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=1.000, significativo=❌
**Corrección de sesgo:** bias_only
**Sensibilidad al ruido:** estable=✅, CV=0.0041

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
