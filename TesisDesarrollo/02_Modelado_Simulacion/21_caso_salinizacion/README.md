# Caso Salinización de Suelos (Modelo y Simulación)

**Nivel de cierre operativo:** 1 (trend)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:22:45.837960Z

> Tendencia no confirmada (Nivel 1): EDI positivo pero sin significancia estadística

## Ejecución

```bash
cd repos/Simulaciones/21_caso_salinizacion/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.322 | 0.027 |
| IC 95%  | [0.268, 0.395] | [0.023, 0.031] |
| Corr ABM | 0.9279 | 0.2015 |
| Corr ODE | 0.9300 | 0.0128 |
| CR (Symploké) | 1.0013 | inf |
| RMSE ABM | 0.489 | 2.156 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=❌ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=0.724, significativo=❌
**Corrección de sesgo:** bias_only
**Sensibilidad al ruido:** estable=✅, CV=0.0011

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
