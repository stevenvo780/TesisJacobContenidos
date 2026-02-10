# Caso Conciencia (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:18:19.042409Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/02_caso_conciencia/src && python3 validate.py
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
| EDI     | 0.018 | -0.024 |
| IC 95%  | [0.010, 0.026] | [-0.035, -0.012] |
| Corr ABM | 0.3616 | 0.4490 |
| Corr ODE | 0.5856 | 0.3360 |
| CR (Symploké) | 0.8576 | 0.9190 |
| RMSE ABM | 1.102 | 0.803 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ❌ | **No-localidad:** ❌ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=0.938, significativo=❌
**Corrección de sesgo:** reverted
**Sensibilidad al ruido:** estable=✅, CV=0.0561

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
