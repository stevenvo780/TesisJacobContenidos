# Indicadores, Métricas y Reglas — Erosión de Suelos (Dialéctica Institucional)

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: -1.000000
- **Bootstrap mean**: -3.850439703827298
- **IC 95%**: [-4.352563885067536, -3.235870553447936]
- **p-value permutación**: 1.0
- **Significativo**: ❌ No
- **Trend bias**:
  - Detrended EDI: -1.0
  - Trend R²: 0.988
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
- Cohesión interna: 0.9974794078264356
- Cohesión externa: 0.9968052023662942
- CR (internal/external): 1.0006763663136398
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.001602749247081881
- Pass: ✅ Sí

## Persistencia
- Model std: 0.23233425240053562
- Obs std: 0.3672429897718933
- Std ratio: 0.6326444857255031
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
