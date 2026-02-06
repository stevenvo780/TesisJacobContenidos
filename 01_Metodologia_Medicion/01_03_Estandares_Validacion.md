# 01_03 Estándares de Validación: El Linter de la Ciencia

En programación, un Linter asegura que el código sea limpio. En esta tesis, los **Estandares de Validación** aseguran que los resultados sean creíbles.

## 1. El Estándar C1-C5 (Protocolo Obligatorio)
Ningún resultado se acepta si no pasa estas 5 pruebas. Es nuestro `pre-commit hook`.

## 2. Umbrales de Aceptación (Thresholds)
*   **RMSE:** Debe ser menor al 60% de la desviación estándar de los datos reales. Si el error es mayor, el modelo se marca como "Legacy/No Válido".
*   **Correlación:** El coeficiente de Pearson debe ser > 0.70. Menos que eso es considerado "Ruido".

## 3. Formato de Salida
Todos los resultados deben exportarse en `JSON` para permitir el procesamiento automático por otros scripts de validación.
