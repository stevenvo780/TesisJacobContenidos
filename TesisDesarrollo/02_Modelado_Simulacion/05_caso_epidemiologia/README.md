# Caso Epidemiología (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:19:58.066517Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/05_caso_epidemiologia/src && python3 validate.py
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
| EDI     | 0.528 | 0.000 |
| IC 95%  | [0.446, 0.594] | [0.000, 0.000] |
| Corr ABM | 0.0291 | 0.0000 |
| Corr ODE | 0.0558 | 0.4536 |
| CR (Symploké) | 1.5094 | 0.0000 |
| RMSE ABM | 2.013 | 4.522 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=❌ C3=❌ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ❌ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=1.000, significativo=❌
**Corrección de sesgo:** full
**Sensibilidad al ruido:** estable=❌, CV=0.7678

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
