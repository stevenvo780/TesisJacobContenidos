# Sesgo de Predictibilidad: Diagnóstico y Mitigación

## Definición

El **sesgo de predictibilidad** (predictability bias) ocurre cuando una serie temporal con tendencia lineal fuerte produce un EDI artificialmente alto. Dado que la ODE captura la tendencia trivialmente, el modelo completo "gana" contra el reducido no porque detecte estructura emergente genuina, sino porque predecir una recta es fácil.

## Indicador implementado: `trend_bias` (Fix T6)

Desde el commit actual, `hybrid_validator.py` calcula automáticamente:

```json
"trend_bias": {
    "detrended_edi": 0.1234,    // EDI sobre residuos sin tendencia lineal
    "trend_ratio": 0.45,         // detrended_edi / edi_original
    "trend_r2": 0.92,            // R² de la tendencia lineal de la serie obs
    "warning": true               // ratio < 0.5 AND R² > 0.7
}
```

### Interpretación

| `trend_ratio` | `trend_r2` | Diagnóstico |
|--------------|-----------|------------|
| > 0.7 | cualquiera | EDI robusto: la estructura macro va más allá de la tendencia |
| 0.5 – 0.7 | > 0.7 | Precaución: parte del EDI proviene de la tendencia |
| < 0.5 | > 0.7 | **Warning**: la mayoría del EDI es sesgo de tendencia |
| cualquiera | < 0.5 | N/A: la serie no tiene tendencia fuerte |

## Casos afectados

Casos con tendencias monotónicas fuertes que requieren atención especial:

1. **18_caso_urbanizacion** — Urbanización global crece monotónicamente desde 1960
2. **29_caso_iot** — Adopción IoT con curva S pronunciada
3. **22_caso_fosforo** — Acumulación gradual
4. **24_caso_microplasticos** — Crecimiento monotónico

## Mitigación

El `trend_bias.warning` es **informativo, no bloqueante**:
- Un warning NO invalida el EDI por sí solo
- Indica que la interpretación de emergencia debe considerar que parte de la señal es tendencia
- El test de permutación (`permutation_pvalue < 0.05`) sigue siendo el gate estadístico formal
- Para tesis: se recomienda reportar ambos EDI (original y detrended) en los casos afectados

## Justificación filosófica

Desde el marco de la tesis: que un hiperobjeto tenga tendencia no lo hace menos real. La urbanización es un fenómeno genuinamente emergente con tendencia. Pero operativamente, necesitamos distinguir:

- **Emergencia genuina**: la ODE captura estructura que va más allá de la inercia/tendencia
- **Predicción trivial**: la ODE solo captura lo que una regresión lineal capturaría

El `trend_ratio` cuantifica exactamente esta distinción.

---

*Implementado en*: `repos/Simulaciones/common/hybrid_validator.py` (Fix T6)
*Referencia cruzada*: T5 (inercia vs ontología), Glosario ("Emergencia Metaestable")
