# Indicadores, Métricas y Reglas — Acidificación Oceánica

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: -0.000008
- **Bootstrap mean**: -1.1457795869889383e-05
- **IC 95%**: [-3.774937073363045e-05, -1.9200181808893775e-06]
- **p-value permutación**: 0.0
- **Significativo**: ❌ No
- **Trend bias**:
  - Detrended EDI: -0.0
  - Trend R²: 0.861
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
- Cohesión interna: 0.9991715001160858
- Cohesión externa: 0.824987235378047
- CR (internal/external): 1.2111357088552037
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.002521951124363079
- Pass: ✅ Sí

## Persistencia
- Model std: 0.10003147562675087
- Obs std: 2.3255543500548246
- Std ratio: 0.043014034750205966
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
