# Caso Emisiones CO₂ Océanos (Modelo y Simulación)

**Nivel de cierre operativo:** 2 (suggestive)
**Estado:** ⚠️ Parcial — señal significativa pero protocolo incompleto
**Generado:** 2026-02-10T01:22:15.551490Z

> Cierre sugestivo (Nivel 2): EDI positivo y significativo pero muy bajo

## Ejecución

```bash
cd repos/Simulaciones/17_caso_oceanos/src && python3 validate.py
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
| EDI     | 0.115 | 0.053 |
| IC 95%  | [0.094, 0.131] | [0.036, 0.126] |
| Corr ABM | 0.9845 | -0.8870 |
| Corr ODE | 0.9830 | -0.7972 |
| CR (Symploké) | 6.5683 | 1.3336 |
| RMSE ABM | 4.898 | 3.582 |
| overall_pass | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Symploké:** ✅ | **No-localidad:** ✅ | **Persistencia:** ✅ | **Acoplamiento:** ❌

**Significancia:** p=0.000, significativo=✅
**Corrección de sesgo:** bias_only
**Sensibilidad al ruido:** estable=✅, CV=0.0215

## Modelo Híbrido

- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
