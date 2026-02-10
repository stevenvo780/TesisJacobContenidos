# Indicadores, Métricas y Reglas — Internet de las Cosas (IoT — Bass-Metcalfe)

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: 0.020387
- **Bootstrap mean**: 0.02020365808589206
- **IC 95%**: [-0.001703779740021146, 0.03533916184548885]
- **p-value permutación**: 0.0
- **Significativo**: ✅ Sí
- **Trend bias**:
  - Detrended EDI: 0.0204
  - Trend R²: 0.874
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
- Cohesión interna: 0.9999878749440312
- Cohesión externa: 0.9494295700841231
- CR (internal/external): 1.053251243117937
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.0016004376176906867
- Pass: ✅ Sí

## Persistencia
- Model std: 0.5090633932871843
- Obs std: 1.7868473670150198
- Std ratio: 0.2848947272634648
- Threshold: 5.0
- Pass: ✅ Sí

## Nivel de emergencia
- **Nivel**: 2
- **Overall pass**: ❌ No

## Taxonomía de niveles
| Nivel | Categoría | EDI | Significado |
|:-----:|:----------|:----|:------------|
| 4 | strong | ≥0.30 + C1-C5 | Clausura operativa fuerte |
| 3 | weak | 0.10-0.30 + sig | Componente funcional |
| 2 | suggestive | >0.01 + sig | Señal sugestiva |
| 1 | trend | >0 pero no sig | Tendencia no significativa |
| 0 | null | ≤0 o no sig | Sin señal |
