# Indicadores, Métricas y Reglas — Ciclo del Fósforo

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: -1.000000
- **Bootstrap mean**: -2.7133499515133725
- **IC 95%**: [-3.3266935514549334, -2.1635471934374295]
- **p-value permutación**: 1.0
- **Significativo**: ❌ No
- **Trend bias**:
  - Detrended EDI: -1.0
  - Trend R²: 0.774
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
- Cohesión interna: 0.9985702696729309
- Cohesión externa: 0.9380055265036884
- CR (internal/external): 1.0645675760514877
- Pass: ✅ Sí
- CR valid: ❌ No

## No-localidad
- Dominance share: 0.0016037485275738773
- Pass: ✅ Sí

## Persistencia
- Model std: 0.08246731565608661
- Obs std: 0.21969127258314236
- Std ratio: 0.3753782054536408
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
