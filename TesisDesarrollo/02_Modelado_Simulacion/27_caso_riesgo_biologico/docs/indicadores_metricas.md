# Indicadores, Métricas y Reglas — Riesgo Biológico Global

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: 0.105111
- **Bootstrap mean**: 0.10160817850735879
- **IC 95%**: [0.07854836713983084, 0.1263744402263029]
- **p-value permutación**: 0.36536536536536535
- **Significativo**: ❌ No
- **Trend bias**:
  - Detrended EDI: None
  - Trend R²: None
  - Warning: ❌ No

## Criterios C1–C5
| Criterio | Resultado |
|----------|-----------|
| C1 (Convergencia) | ✅ Sí |
| C2 (Beneficio acoplamiento) | — |
| C3 (Ablación EDI) | — |
| C4 (Robustez ruido) | — |
| C5 (Parsimonia) | — |

## Symploké
- Cohesión interna: 0.9999089008920491
- Cohesión externa: 0.9980345771342468
- CR (internal/external): 1.0018780148511328
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.0016001971972706155
- Pass: ✅ Sí

## Persistencia
- Model std: 0.3512412131465594
- Obs std: 0.07758123103226275
- Std ratio: 4.527399326784245
- Threshold: 5.0
- Pass: ✅ Sí

## Nivel de emergencia
- **Nivel**: 1
- **Overall pass**: ❌ No

## Taxonomía de niveles
| Nivel | Categoría | EDI | Significado |
|:-----:|:----------|:----|:------------|
| 4 | strong | ≥0.30 + C1-C5 | Clausura operativa fuerte |
| 3 | weak | 0.10-0.30 + sig | Componente funcional |
| 2 | suggestive | >0.01 + sig | Señal sugestiva |
| 1 | trend | >0 pero no sig | Tendencia no significativa |
| 0 | null | ≤0 o no sig | Sin señal |
