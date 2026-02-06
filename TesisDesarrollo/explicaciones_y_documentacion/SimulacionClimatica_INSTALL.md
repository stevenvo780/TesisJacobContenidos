# Guía de Reproducibilidad (INSTALL.md)

Este documento detalla los pasos para replicar las simulaciones y validaciones de la tesis.

## 1. Instalación Rápida
Requiere Python 3.8+.
```bash
cd /workspace
pip install -r repos/Simulaciones/requirements.txt
```

## 2. Ejecución
Para replicar los resultados:

*   **Caso Clima (Éxito):** Valida la inercia macro del clima regional.
    ```bash
    python3 repos/Simulaciones/caso_clima/src/validate.py
    ```
*   **Caso Finanzas (Fallo):** Demuestra el límite del modelo ante la reflexividad.
    ```bash
    python3 repos/Simulaciones/caso_finanzas/src/validate.py
    ```

## 3. Resultados
Los scripts generan:
- `outputs/metrics.json`: Valores numéricos (EDI, CR, RMSE).
- `outputs/report.md`: Análisis cualitativo.
