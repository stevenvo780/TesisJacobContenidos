# Indicadores, Métricas y Reglas — Salinización de Suelos

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: 0.026546
- **Bootstrap mean**: 0.026734391473988955
- **IC 95%**: [0.02277365728590113, 0.030862031579078825]
- **p-value permutación**: 0.7237237237237237
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
- Cohesión interna: 0.9991883318298056
- Cohesión externa: 0.0
- CR (internal/external): inf
- Pass: ✅ Sí
- CR valid: ✅ Sí

## No-localidad
- Dominance share: 0.0016014533742892138
- Pass: ✅ Sí

## Persistencia
- Model std: 0.004772944705769527
- Obs std: 0.45765424288654494
- Std ratio: 0.010429149909471651
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
