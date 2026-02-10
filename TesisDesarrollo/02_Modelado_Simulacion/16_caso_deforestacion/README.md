# Caso Deforestación Global (Modelo y Simulación)

**Nivel de cierre operativo:** 4 (strong)
**Estado:** ✅ Validado — cierre operativo confirmado
**Generado:** 2026-02-10T01:22:11.136333Z

> Cierre operativo fuerte (Nivel 4): la macro constriñe significativamente la dinámica micro

## Ejecución

```bash
cd repos/Simulaciones/16_caso_deforestacion/src && python3 validate.py
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
| EDI     | 0.847 | 0.633 |
| IC 95%  | [0.830, 0.860] | [0.522, 0.734] |
| Corr ABM | 0.9993 | 0.8810 |
| Corr ODE | 0.9991 | 0.8776 |
| CR (Symploké) | 1.0325 | 1.0170 |
| RMSE ABM | 0.194 | 0.427 |
| overall_pass | ✅ | ✅ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=0.000, significativo=✅
**Corrección de sesgo:** full
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
