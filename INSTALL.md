# Guía de Instalación y Reproducción (Auditoría Externa)

Este documento permite replicar el entorno de simulación para validar el **Caso Clima**.

## 1. Requisitos Previos
*   Python 3.10+
*   pip
*   git

## 2. Instalación
Si no estás usando el entorno pre-configurado:

```bash
pip install -r repos/Simulaciones/requirements.txt
```

## 3. Ejecución Rápida (Demo)
Hemos incluido un script para ejecutar la validación del caso principal (Clima):

```bash
chmod +x run_demo.sh
./run_demo.sh
```

O manualmente:

```bash
python3 repos/Simulaciones/01_caso_clima/src/validate.py
```

*Nota:* La primera ejecución puede tardar varios minutos mientras descarga los datos históricos (Meteostat/Yahoo Finance).

## 4. Resultados Esperados
El sistema validará la hipótesis H1 (EDI > 0.30) para el caso Clima.
Salida típica:
> `EDI: 0.103 | CR: 2.355` (Valores aproximados dependiendo de la fecha de los datos)
