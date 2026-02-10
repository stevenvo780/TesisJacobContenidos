# Reproducibilidad y Versionado — Internet de las Cosas (IoT — Bass-Metcalfe)

## Entorno requerido
- Python 3.10+
- Dependencias: `numpy`, `pandas`, `scipy`, `requests`
- Sin frameworks ML. Todo en NumPy/Pandas puro.

## Estructura de archivos
```
repos/Simulaciones/29_caso_iot/
├── src/
│   ├── validate.py    # Orquestador: calibrar → simular → evaluar C1–C5
│   ├── abm.py         # Capa micro: grilla NxN con difusión y acoplamiento
│   ├── ode.py         # Capa macro: mean_reversion + efecto de red (Bass-Metcalfe)
│   ├── metrics.py     # EDI, CR, EI, RMSE, correlación
│   └── data.py        # Obtención de datos (World Bank (multi-indicador): IT.NET.BBND.P2 (banda ancha fija), IT.CEL.SETS.P2 (suscripciones móviles), IT.NET.USER.ZS (uso de Internet), TX.VAL.TECH.MF.ZS (exportaciones high-tech), EG.ELC.ACCS.ZS (acceso eléctrico))
├── outputs/
│   ├── metrics.json   # Resultados completos de la validación
│   └── report.md      # Reporte legible con resumen de métricas
└── data/
    └── *.csv          # Datos cacheados localmente
```

## Ejecución
```bash
cd repos/Simulaciones/29_caso_iot/src
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
- Fuente: World Bank (multi-indicador): IT.NET.BBND.P2 (banda ancha fija), IT.CEL.SETS.P2 (suscripciones móviles), IT.NET.USER.ZS (uso de Internet), TX.VAL.TECH.MF.ZS (exportaciones high-tech), EG.ELC.ACCS.ZS (acceso eléctrico)
- Indicador: `IT.NET.BBND.P2 + IT.CEL.SETS.P2 + IT.NET.USER.ZS + TX.VAL.TECH.MF.ZS + EG.ELC.ACCS.ZS`
- Los datos se cachean en `data/` tras la primera descarga.
- La validación funciona con datos cacheados (no requiere conexión).

## Auditoría
- `repos/scripts/auditar_simulaciones.py` verifica todos los 29 casos.
- `repos/scripts/evaluar_simulaciones.py` genera tablas resumen.

## Resultado actual
- EDI: 0.020387
- Nivel: 2
- Overall pass: ❌ No
- Generado: 2026-02-10T01:23:58.387657Z
