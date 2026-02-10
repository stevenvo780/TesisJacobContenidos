# Caso Ciclo del Fósforo (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:22:50.667751Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/22_caso_fosforo/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.345 | -1.000 |
| IC 95%  | [0.319, 0.386] | [-3.327, -2.164] |
| Corr ABM | 0.9816 | -0.5173 |
| Corr ODE | 0.9827 | -0.8015 |
| CR (Symploké) | 1.0046 | 1.0646 |
| RMSE ABM | 0.875 | 1.212 |
| overall_pass | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=1.000, significativo=❌
**Corrección de sesgo:** full
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
