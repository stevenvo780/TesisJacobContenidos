# SimulacionClimatica: Ontología Operativa de Hiperobjetos

> **Tesis Doctoral:** Validación computacional de la existencia de entidades masivamente distribuidas mediante modelos híbridos (ABM + ODE).

Este repositorio contiene la implementación técnica y la fundamentación teórica para demostrar la **Eficacia Causal** de los hiperobjetos (Morton, 2013).

## 🚀 Instalación Rápida

```bash
cd /workspace
pip install -r repos/Simulaciones/requirements.txt
```

## 🧪 Experimentos Principales

### 1. Caso Clima (No Validado)
Modelo con cohesión interna adecuada pero estructura macro débil en zero-nudging.
*   **Ejecución:** `python3 repos/Simulaciones/caso_clima/src/validate.py`
*   **Resultado:** EDI 0.103 (< 0.30), CR 2.355 (> 2.0).

**Actualizacion (Iteracion 2 - Debate):**
Se reportaron tests adversariales adicionales en el caso Clima (autonomia a 1000 pasos sin nudging, causalidad inversa y barrido de `forcing_scale`). Ver `repos/Simulaciones/caso_clima/docs/tests_adversariales_iteracion_2.md`.

### 2. Caso Finanzas (No Validado)
Modelo con EDI alto pero sin frontera sistémica.
*   **Ejecución:** `python3 repos/Simulaciones/caso_finanzas/src/validate.py`
*   **Resultado:** EDI 0.769 (> 0.30), CR 1.078 (< 2.0).

## 📚 Estructura de la Tesis (Versión Consolidada)

La documentación se ha condensado en 5 módulos de alta densidad académica:

*   **00_Marco_Conceptual:** Fundamentos filosóficos (OOO, Sinergética).
*   **01_Metodologia:** Protocolos de rigor C1-C5.
*   **02_Modelado:** Arquitectura del motor `HybridModel`.
*   **03_Validacion:** Matriz de evidencia y análisis de fallos.
*   **04_Casos:** Catálogo detallado de los 18 experimentos.

## ⚖️ Licencia
MIT License. Ver `LICENSE` para más detalles.
