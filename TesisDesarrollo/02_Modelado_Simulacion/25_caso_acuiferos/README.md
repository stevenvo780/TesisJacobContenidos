# Caso Depleción de Acuíferos (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:23:27.489297Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/25_caso_acuiferos/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.380 | -0.179 |
| IC 95%  | [0.366, 0.400] | [-0.194, -0.163] |
| Corr ABM | 0.0145 | 0.9911 |
| Corr ODE | 0.0115 | 0.9679 |
| CR (Symploké) | 1.0045 | 1.0012 |
| RMSE ABM | 0.814 | 22.059 |
| overall_pass | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=1.000, significativo=❌
**Corrección de sesgo:** none
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
