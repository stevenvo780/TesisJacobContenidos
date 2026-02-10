# Caso Emergencia IoT (Modelo y Simulación)

**Nivel de cierre operativo:** 2 (suggestive)
**Estado:** ⚠️ Parcial — señal significativa pero protocolo incompleto
**Generado:** 2026-02-10T01:23:58.387657Z

> Cierre sugestivo (Nivel 2): EDI positivo y significativo pero muy bajo

## Ejecución

```bash
cd repos/Simulaciones/29_caso_iot/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.301 | 0.020 |
| IC 95%  | [0.264, 0.350] | [-0.002, 0.035] |
| Corr ABM | 0.9373 | 0.9213 |
| Corr ODE | 0.9331 | 0.9166 |
| CR (Symploké) | 1.0184 | 1.0533 |
| RMSE ABM | 2.953 | 33.930 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=0.000, significativo=✅
**Corrección de sesgo:** bias_only
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
