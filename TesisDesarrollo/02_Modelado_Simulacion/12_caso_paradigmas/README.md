# Caso Paradigmas (Modelo y Simulación)

**Nivel de cierre operativo:** 0 (null)
**Estado:** ❌ Sin señal — EDI insuficiente o no significativo
**Generado:** 2026-02-10T01:21:18.064066Z

> Sin cierre operativo (Nivel 0): sin evidencia de constricción macro efectiva

## Ejecución

```bash
cd repos/Simulaciones/12_caso_paradigmas/src && python3 validate.py
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
| EDI     | 0.000 | 0.000 |
| IC 95%  | [0.000, 0.000] | [0.000, 0.000] |
| Corr ABM | -0.0735 | -0.1041 |
| Corr ODE | -0.0312 | -0.9636 |
| CR (Symploké) | 0.0000 | 0.0000 |
| RMSE ABM | 1.103 | 9.706 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=❌ C3=✅ C4=✅ C5=❌

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=1.000, significativo=❌
**Corrección de sesgo:** none
**Sensibilidad al ruido:** estable=❌, CV=1.5007

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
