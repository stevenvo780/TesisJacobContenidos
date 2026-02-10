# Indicadores, Métricas y Reglas — Agotamiento de Acuíferos

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: -0.178754
- **Bootstrap mean**: -0.17847569128735769
- **IC 95%**: [-0.19375511461608586, -0.16291552272684262]
- **p-value permutación**: 1.0
- **Significativo**: ❌ No
- **Trend bias**:
  - Detrended EDI: -0.1788
  - Trend R²: 0.984
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
- Cohesión interna: 0.9999356968209154
- Cohesión externa: 0.9986960686228218
- CR (internal/external): 1.0012412466986107
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.0016001132582576525
- Pass: ✅ Sí

## Persistencia
- Model std: 3.9170528890302365
- Obs std: 8.049604661766022
- Std ratio: 0.486614318792007
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
