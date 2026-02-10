# Caso Finanzas Globales (Modelo y Simulación)

**Nivel de cierre operativo:** 2 (suggestive)
**Estado:** ⚠️ Parcial — señal significativa pero protocolo incompleto
**Generado:** 2026-02-10T01:20:05.225384Z

> Cierre sugestivo (Nivel 2): EDI positivo y significativo pero muy bajo

## Ejecución

```bash
cd repos/Simulaciones/09_caso_finanzas/src && python3 validate.py
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
| EDI     | -0.000 | 0.040 |
| IC 95%  | [-0.000, -0.000] | [0.039, 0.041] |
| Corr ABM | 0.4284 | 0.9872 |
| Corr ODE | 0.2504 | 0.8680 |
| CR (Symploké) | 0.0000 | 0.0000 |
| RMSE ABM | 20481509.712 | 36.420 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ❌ | **No-localidad:** ❌ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=0.000, significativo=✅
**Corrección de sesgo:** none
**Sensibilidad al ruido:** estable=✅, CV=0.0066

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
