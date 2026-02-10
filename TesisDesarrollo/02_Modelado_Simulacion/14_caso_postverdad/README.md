# Caso Postverdad (Modelo y Simulación)

**Nivel de cierre operativo:** 1 (trend)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:21:48.694718Z

> Tendencia no confirmada (Nivel 1): EDI positivo pero sin significancia estadística

## Ejecución

```bash
cd repos/Simulaciones/14_caso_postverdad/src && python3 validate.py
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
| EDI     | 0.000 | 0.001 |
| IC 95%  | [0.000, 0.000] | [0.000, 0.002] |
| Corr ABM | 0.0000 | -0.5630 |
| Corr ODE | 0.0000 | 0.5318 |
| CR (Symploké) | 0.0000 | 1.0544 |
| RMSE ABM | 2.885 | 2.962 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=0.030, significativo=❌
**Corrección de sesgo:** bias_only
**Sensibilidad al ruido:** estable=✅, CV=0.3970

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
