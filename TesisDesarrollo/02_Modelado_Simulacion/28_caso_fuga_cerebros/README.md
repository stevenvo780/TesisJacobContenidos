# Caso Fuga de Cerebros Global (Modelo y Simulación)

**Nivel de cierre operativo:** 3 (weak)
**Estado:** ⚠️ Parcial — señal significativa pero protocolo incompleto
**Generado:** 2026-02-10T01:23:55.521121Z

> Cierre operativo débil (Nivel 3): señal macro significativa pero bajo umbral robusto

## Ejecución

```bash
cd repos/Simulaciones/28_caso_fuga_cerebros/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.724 | 0.183 |
| IC 95%  | [0.663, 0.809] | [0.036, 0.288] |
| Corr ABM | 0.9752 | 0.7974 |
| Corr ODE | 0.9693 | 0.8186 |
| CR (Symploké) | 1.0305 | 1.0081 |
| RMSE ABM | 0.767 | 3.774 |
| overall_pass | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=0.001, significativo=✅
**Corrección de sesgo:** bias_only
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
