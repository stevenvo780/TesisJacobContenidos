# Caso Constelaciones Satelitales (Starlink) (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:23:50.813387Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/26_caso_starlink/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.634 | -1.000 |
| IC 95%  | [0.564, 0.702] | [-587.795, -456.515] |
| Corr ABM | 0.0790 | 0.0000 |
| Corr ODE | 0.0651 | 0.0000 |
| CR (Symploké) | 1.0240 | inf |
| RMSE ABM | 0.403 | 0.066 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=❌ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=1.000, significativo=❌
**Corrección de sesgo:** none
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
