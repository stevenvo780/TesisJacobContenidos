# Caso Erosión Dialéctica del Discurso (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:23:00.943138Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/23_caso_erosion_dialectica/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.047 | -1.000 |
| IC 95%  | [0.046, 0.048] | [-4.353, -3.236] |
| Corr ABM | 0.9949 | 0.9990 |
| Corr ODE | 0.9945 | 0.9861 |
| CR (Symploké) | 1.0008 | 1.0007 |
| RMSE ABM | 3.952 | 0.983 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=1.000, significativo=❌
**Corrección de sesgo:** bias_only
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
