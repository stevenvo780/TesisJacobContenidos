# Indicadores, Métricas y Reglas — Síndrome de Kessler (Basura Espacial)

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: -0.420251
- **Bootstrap mean**: -0.4205499962201608
- **IC 95%**: [-0.43061058553584647, -0.4133584932998488]
- **p-value permutación**: 1.0
- **Significativo**: ❌ No
- **Trend bias**:
  - Detrended EDI: -0.4203
  - Trend R²: 0.932
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
- Cohesión interna: 0.7986968422670293
- Cohesión externa: 0.663626358591086
- CR (internal/external): 1.2035339343101217
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.03613817194188076
- Pass: ✅ Sí

## Persistencia
- Model std: 110639.4305761287
- Obs std: 0.39974224909619116
- Std ratio: 276776.9251968791
- Threshold: 5.0
- Pass: ❌ No

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
