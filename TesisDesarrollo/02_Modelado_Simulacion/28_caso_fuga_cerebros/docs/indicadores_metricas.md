# Indicadores, Métricas y Reglas — Fuga de Cerebros (Brain Drain)

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: 0.182896
- **Bootstrap mean**: 0.18046712481104582
- **IC 95%**: [0.035858835481145684, 0.28805630734121307]
- **p-value permutación**: 0.001001001001001001
- **Significativo**: ✅ Sí
- **Trend bias**:
  - Detrended EDI: 0.1829
  - Trend R²: 0.794
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
- Cohesión interna: 0.9995221338913012
- Cohesión externa: 0.9915364586907822
- CR (internal/external): 1.008053839201297
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.0016009390894499177
- Pass: ✅ Sí

## Persistencia
- Model std: 2.474354520038907
- Obs std: 5.572598399139133
- Std ratio: 0.44402168303051426
- Threshold: 5.0
- Pass: ✅ Sí

## Nivel de emergencia
- **Nivel**: 3
- **Overall pass**: ❌ No

## Taxonomía de niveles
| Nivel | Categoría | EDI | Significado |
|:-----:|:----------|:----|:------------|
| 4 | strong | ≥0.30 + C1-C5 | Clausura operativa fuerte |
| 3 | weak | 0.10-0.30 + sig | Componente funcional |
| 2 | suggestive | >0.01 + sig | Señal sugestiva |
| 1 | trend | >0 pero no sig | Tendencia no significativa |
| 0 | null | ≤0 o no sig | Sin señal |
