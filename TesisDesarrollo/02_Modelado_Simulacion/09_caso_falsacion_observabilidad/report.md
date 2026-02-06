# Reporte de Falsacion - Observabilidad Insuficiente

## Metadata
- generated_at: 2026-02-06T02:03:27.406845Z
- git_commit: 59e0ac2d28887926e1af89161073daf99653a607
- git_dirty: True

## Fase synthetic
- overall_pass: False

### Datos
- start: 2011-01-01
- end: 2023-12-31
- split: 2018-01-01
- obs_mean: -0.00816460692606617
- obs_std_raw: 0.19644408284460085
- steps: 13
- val_steps: 6
- expected_years: 13
- observed_years: 13
- coverage: 1.0
- outlier_share: 0.0

### Criterios
- c1_convergence: False
- c5_uncertainty: True

## Fase real
- overall_pass: False

### Datos
- start: 2011-01-01
- end: 2023-12-31
- split: 2018-01-01
- obs_mean: 0.0
- obs_std_raw: 0.0
- steps: 4
- val_steps: 0
- expected_years: 13
- observed_years: 4
- coverage: 0.3076923076923077
- outlier_share: 0.0

### Criterios
- c1_convergence: False
- c5_uncertainty: False

## Notas
- Cobertura deliberadamente insuficiente para falsacion.

## Datos Necesarios para Resolver la Observabilidad
Este caso falla por falta de observaciones suficientes (coverage 0.31 en fase real). Para completarlo sin forzar resultados, se requiere un dataset con:
- Cobertura temporal continua.
- Observables directos o proxies confiables.
- Metadata para diferenciar interaccion interna vs externa.

Fuentes sugeridas (ejemplos de alta observabilidad):
```
GDELT 2.1 (eventos globales): https://www.gdeltproject.org/
Wikipedia Pageviews (actividad agregada): https://dumps.wikimedia.org/other/pageviews/
World Bank WDI (indicadores estructurales): https://datacatalog.worldbank.org/
```
