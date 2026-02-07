# SimulacionClimatica: Ontología Operativa de Hiperobjetos

> **Tesis Doctoral:** Validación computacional de la existencia de entidades masivamente distribuidas mediante modelos híbridos (ABM + ODE).

Este repositorio contiene la implementación técnica y la fundamentación teórica para demostrar la **Eficacia Causal** de los hiperobjetos (Morton, 2013).

## 🚀 Instalación Rápida

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r repos/Simulaciones/requirements.txt
```

## 🧪 Resultados Principales

**11 de 29 casos genuinos validados (38%)** + 3 controles de falsación correctamente rechazados.

| Caso | EDI | corr | Estado |
|------|-----|------|--------|
| Starlink | 0.928 | 0.994 | ✅ Validado |
| Fósforo | 0.901 | 0.881 | ✅ Validado |
| Finanzas | 0.880 | 0.996 | ✅ Validado |
| Acuíferos | 0.866 | 1.000 | ✅ Validado |
| Deforestación | 0.846 | 0.919 | ✅ Validado |
| Urbanización | 0.840 | 0.999 | ✅ Validado |
| Paradigmas | 0.657 | 0.953 | ✅ Validado |
| Fuga Cerebros | 0.433 | 0.970 | ✅ Validado |
| RTB Publicidad | 0.426 | 0.755 | ✅ Validado |
| Clima | 0.425 | 0.822 | ✅ Validado |
| Energía | 0.351 | 0.789 | ✅ Validado |

Ejecución: `repos/Simulaciones/{NN}_caso_*/src/validate.py`

## 📚 Estructura de la Tesis

*   **00_Marco_Conceptual:** Fundamentos filosóficos (OOO, Sinergética).
*   **01_Metodologia:** Protocolos de rigor C1-C5, métricas EDI/CR.
*   **02_Modelado:** Arquitectura del motor HybridModel y 32 casos.
*   **03_Validacion:** Matriz de evidencia y análisis de fallos.
*   **04_Casos:** Catálogo detallado de los 32 experimentos.

## 🧭 Mapa Doc ↔ Código

- **Tesis:** `TesisDesarrollo/` → `TesisFinal/Tesis.md`
- **Código:** `repos/Simulaciones/{NN}_caso_*/src/`
- **Resultados:** `repos/Simulaciones/{NN}_caso_*/outputs/`
- **Docs por caso:** `TesisDesarrollo/02_Modelado_Simulacion/{NN}_caso_*/`

## ⚖️ Licencia
MIT License.
