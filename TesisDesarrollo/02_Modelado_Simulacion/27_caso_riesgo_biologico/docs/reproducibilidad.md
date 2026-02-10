# Reproducibilidad y Versionado — Riesgo Biológico Global

## Entorno requerido
- Python 3.10+
- Dependencias: `numpy`, `pandas`, `scipy`, `requests`
- Sin frameworks ML. Todo en NumPy/Pandas puro.

## Estructura de archivos
```
repos/Simulaciones/27_caso_riesgo_biologico/
├── src/
│   ├── validate.py    # Orquestador: calibrar → simular → evaluar C1–C5
│   ├── abm.py         # Capa micro: grilla NxN con difusión y acoplamiento
│   ├── ode.py         # Capa macro: mean_reversion + amplificación biológica
│   ├── metrics.py     # EDI, CR, EI, RMSE, correlación
│   └── data.py        # Obtención de datos (Proxy compuesto: indicadores World Bank de salud + urbanización + deforestación)
├── outputs/
│   ├── metrics.json   # Resultados completos de la validación
│   └── report.md      # Reporte legible con resumen de métricas
└── data/
    └── *.csv          # Datos cacheados localmente
```

## Ejecución
```bash
cd repos/Simulaciones/27_caso_riesgo_biologico/src
python3 validate.py
```

## Semillas y reproducibilidad
- Todas las simulaciones usan semillas explícitas (`seed` parameter).
- Los resultados son reproducibles dado el mismo entorno y versión de dependencias.
- Las semillas se fijan en: ABM (seed), ODE (seed), permutación (seed+1), bootstrap (seed+2).

## Validación de resultados
- `metrics.json` contiene todas las métricas y criterios evaluados.
- `report.md` contiene el resumen en formato legible.
- Ambos se generan automáticamente al ejecutar `validate.py`.

## Datos
- Fuente: Proxy compuesto: indicadores World Bank de salud + urbanización + deforestación
- Indicador: `Proxy compuesto multi-indicador (synthetic_fallback → cache)`
- Los datos se cachean en `data/` tras la primera descarga.
- La validación funciona con datos cacheados (no requiere conexión).

## Auditoría
- `repos/scripts/auditar_simulaciones.py` verifica todos los 29 casos.
- `repos/scripts/evaluar_simulaciones.py` genera tablas resumen.

## Resultado actual
- EDI: 0.105111
- Nivel: 1
- Overall pass: ❌ No
- Generado: 2026-02-10T01:23:53.333391Z
