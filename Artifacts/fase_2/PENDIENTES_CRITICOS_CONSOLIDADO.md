# Pendientes Críticos Consolidados (Auditoría Brutal/Termonuclear)

Este documento centraliza las críticas de alto impacto que aún no han sido resueltas y que representan un riesgo para la defensa de la tesis.

## 1. Justificación Matemática y Metodológica
*   **[RESUELTO] Arbitrariedad del Umbral EDI > 0.30:** Justificado mediante la "Ventaja de Hoel" y el umbral de autonomía 0.05 en el marco conceptual.
*   **[RESUELTO] Estandarización de Parámetros:** Corregido validate.py en caso_clima y caso_finanzas para que el modelo reducido mantenga el mismo `assimilation_strength` que el modelo completo (comparación justa). Los 8 casos sin código ejecutable con rmse_abm ≈ 0 fueron marcados como TAUT.
*   **Calidad de Datasets:** Pendiente admitir la disparidad en la matriz 03_8.

## 2. Análisis de Fallos y Paradojas
*   **[RESUELTO] Profundización del Fracaso en Finanzas:** Eliminado el leakage de datos. El fallo es ahora genuino y técnico (C1 Failure).
*   **[RESUELTO] Poda de Casos Débiles:** Eliminados casos con LoE 1-2 (Justicia, Estética, etc.) para evitar dilución de rigor.

## 3. Rigor Expositivo y Técnico
*   **[RESUELTO] Tono de "Modo Dios":** Corregido el tono triunfalista. Se actualizaron las secciones de resultados para reflejar que solo 2 de 18 casos superan umbrales y se reconocen las limitaciones.
*   **Reproducibilidad (External Audit):** Falta un archivo `INSTALL.md` simplificado y un entorno que permita a un tercero replicar el EDI 0.103 del clima sin fricciones.
*   **[RESUELTO] Integridad de Enlaces:** Corregido el enlace `../Tesis.md` → `../TesisFinal/Tesis.md` en Indice_Maestro.md.

## 4. Reducción de Ambición
*   **Poda de Casos Débiles:** Evaluar seriamente la eliminación de casos con LoE (Level of Evidence) bajo (1-2) que diluyen la potencia del Caso Clima.

---
**Prioridad:** Alta. Estos puntos son el "punto débil" identificado en las últimas auditorías de estrés.
