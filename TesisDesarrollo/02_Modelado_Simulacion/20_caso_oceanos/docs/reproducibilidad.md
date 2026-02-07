# Reproducibilidad y Versionado — Emisiones CO2 (Oceanos)

## Entorno requerido
- Python 3.10+
- Dependencias: `numpy`, `pandas`, `scipy`, `requests`
- Instalacion: `pip install -r repos/Simulaciones/requirements.txt`

## Determinismo basado en semillas
- Todas las ejecuciones usan semillas explicitas (`np.random.seed`).
- Las semillas quedan registradas en `metrics.json`.
- Resultados reproducibles bit a bit con misma semilla y entorno.

## Fuente de datos
- World Bank API: indicador `EN.ATM.CO2E.KT` (emisiones CO2 en kt).
- Rango: 1960–2022, frecuencia anual.
- Cache local: los datos descargados se almacenan localmente para
  evitar dependencia de conectividad durante la ejecucion.

## Normalizacion
- Z-normalizacion aplicada sobre la ventana de entrenamiento.
- Media y desviacion estandar calculadas exclusivamente en datos de train.
- La ventana de validacion usa los mismos parametros de normalizacion.

## Versionado
- El codigo vive en el repositorio y se reporta el commit en `report.md`.
- Los parametros base y semillas quedan registrados en `metrics.json`.

## Ejecucion
- Comando unico: `cd repos/Simulaciones/caso_oceanos/src && python3 validate.py`
- Salidas en `outputs/`: `metrics.json` y `report.md`.

## Sensibilidad
- Se reporta rango de sensibilidad en `metrics.json`.
- La fase sintetica sirve como verificacion en escenario controlado.
