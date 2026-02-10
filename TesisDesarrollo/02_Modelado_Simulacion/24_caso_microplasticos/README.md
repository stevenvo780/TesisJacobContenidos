# Caso Contaminación por Microplásticos (Modelo y Simulación)

**Nivel de cierre operativo:** 4 (strong)
**Estado:** ✅ Validado — cierre operativo confirmado
**Generado:** 2026-02-10T01:23:15.512971Z

> Cierre operativo fuerte (Nivel 4): la macro constriñe significativamente la dinámica micro

## Ejecución

```bash
cd repos/Simulaciones/24_caso_microplasticos/src && python3 validate.py
```

## Estructura

- `metrics.json`: métricas de validación computadas.
- `report.md`: reporte narrativo de resultados.

## Resultados

| Métrica | Sintético | Real |
|---------|-----------|------|
| EDI     | 0.285 | 0.427 |
| IC 95%  | [0.278, 0.294] | [0.414, 0.447] |
| Corr ABM | 0.0166 | 0.9935 |
| Corr ODE | 0.0030 | 0.9810 |
| CR (Symploké) | 1.0019 | 1.0016 |
| RMSE ABM | 1.111 | 10.428 |
| overall_pass | ❌ | ✅ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ✅

**Significancia:** p=0.000, significativo=✅
**Corrección de sesgo:** none
**Sensibilidad al ruido:** estable=✅, CV=0.0000

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
