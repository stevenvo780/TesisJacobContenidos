# Indicadores, Métricas y Reglas — Mega-constelaciones Satelitales (Starlink)

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: -1.000000
- **Bootstrap mean**: -520.3015802438525
- **IC 95%**: [-587.7953081798722, -456.51540995279265]
- **p-value permutación**: 1.0
- **Significativo**: ❌ No
- **Trend bias**:
  - Detrended EDI: -1.0
  - Trend R²: 1.0
  - Warning: ❌ No

## Criterios C1–C5
| Criterio | Resultado |
|----------|-----------|
| C1 (Convergencia) | ❌ No |
| C2 (Beneficio acoplamiento) | — |
| C3 (Ablación EDI) | — |
| C4 (Robustez ruido) | — |
| C5 (Parsimonia) | — |

## Symploké
- Cohesión interna: 0.9864503062604317
- Cohesión externa: 0.0
- CR (internal/external): inf
- Pass: ✅ Sí
- CR valid: ✅ Sí

## No-localidad
- Dominance share: 0.001611099894992343
- Pass: ✅ Sí

## Persistencia
- Model std: 0.004048335037510662
- Obs std: 0.03162277660168379
- Std ratio: 0.12801959449996886
- Threshold: 5.0
- Pass: ✅ Sí

## Nivel de emergencia
- **Nivel**: 0
- **Overall pass**: ❌ No

## Taxonomía de niveles
| Nivel | Categoría | EDI | Significado |
|:-----:|:----------|:----|:------------|
| 4 | strong | ≥0.30 + C1-C5 | Clausura operativa fuerte |
| 3 | weak | 0.10-0.30 + sig | Componente funcional |
| 2 | suggestive | >0.01 + sig | Señal sugestiva |
| 1 | trend | >0 pero no sig | Tendencia no significativa |
| 0 | null | ≤0 o no sig | Sin señal |
