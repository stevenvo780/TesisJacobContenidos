# Caso Energía (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:19:36.466863Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/04_caso_energia/src && python3 validate.py
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
| EDI     | 0.048 | -0.003 |
| IC 95%  | [0.040, 0.056] | [-0.004, -0.003] |
| Corr ABM | -0.1335 | -0.4433 |
| Corr ODE | -0.1153 | -0.3749 |
| CR (Symploké) | 1.0107 | 1.0959 |
| RMSE ABM | 0.403 | 1.601 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=0.937, significativo=❌
**Corrección de sesgo:** none
**Sensibilidad al ruido:** estable=✅, CV=0.0408

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
