# Caso Riesgo Biológico Global (Modelo y Simulación)

**Nivel de cierre operativo:** 1 (trend)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:23:53.333391Z

> Tendencia no confirmada (Nivel 1): EDI positivo pero sin significancia estadística

## Ejecución

```bash
cd repos/Simulaciones/27_caso_riesgo_biologico/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.442 | 0.105 |
| IC 95%  | [0.373, 0.527] | [0.079, 0.126] |
| Corr ABM | 0.7938 | 0.1358 |
| Corr ODE | 0.7939 | 0.1373 |
| CR (Symploké) | 1.0127 | 1.0019 |
| RMSE ABM | 0.949 | 0.722 |
| overall_pass | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=0.365, significativo=❌
**Corrección de sesgo:** reverted
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
