# Indicadores, Métricas y Reglas — Contaminación por Microplásticos

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: 0.426505
- **Bootstrap mean**: 0.4272466757480588
- **IC 95%**: [0.41440509335965375, 0.44653959561753914]
- **p-value permutación**: 0.0
- **Significativo**: ✅ Sí
- **Trend bias**:
  - Detrended EDI: 0.4265
  - Trend R²: 0.97
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
- Cohesión interna: 0.9999897688076343
- Cohesión externa: 0.9983969402680483
- CR (internal/external): 1.0015953860387017
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.0016000606985038196
- Pass: ✅ Sí

## Persistencia
- Model std: 5.437771227168683
- Obs std: 1.206837358933709
- Std ratio: 4.505802863090997
- Threshold: 5.0
- Pass: ✅ Sí

## Nivel de emergencia
- **Nivel**: 4
- **Overall pass**: ✅ Sí

## Taxonomía de niveles
| Nivel | Categoría | EDI | Significado |
|:-----:|:----------|:----|:------------|
| 4 | strong | ≥0.30 + C1-C5 | Clausura operativa fuerte |
| 3 | weak | 0.10-0.30 + sig | Componente funcional |
| 2 | suggestive | >0.01 + sig | Señal sugestiva |
| 1 | trend | >0 pero no sig | Tendencia no significativa |
| 0 | null | ≤0 o no sig | Sin señal |
