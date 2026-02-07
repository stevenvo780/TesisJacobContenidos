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

**32 casos evaluados** con protocolo completo (11 criterios simultáneos). **11 validados**, 8 rechazados con EDI alto (prueba de selectividad), 3 controles de falsación correctos.

| Caso | EDI | corr | Estado |
|------|-----|------|--------|
| Starlink | 0.928 | 0.994 | ✅ Validado |
| Fósforo | 0.901 | 0.881 | ✅ Validado |
| **Riesgo Biológico** | **0.917** | **0.988** | **❌ Rechazado (Sym, Per)** |
| Finanzas | 0.880 | 0.996 | ✅ Validado |
| Acuíferos | 0.866 | 1.000 | ✅ Validado |
| Deforestación | 0.846 | 0.919 | ✅ Validado |
| Urbanización | 0.840 | 0.999 | ✅ Validado |
| **Océanos** | **0.737** | **0.361** | **❌ Rechazado (C1)** |
| **Kessler** | **0.704** | **0.499** | **❌ Rechazado (C1)** |
| Paradigmas | 0.656 | 0.953 | ✅ Validado |
| Fuga Cerebros | 0.433 | 0.970 | ✅ Validado |
| RTB Publicidad | 0.426 | 0.755 | ✅ Validado |
| Clima | 0.425 | 0.822 | ✅ Validado |
| Energía | 0.351 | 0.789 | ✅ Validado |

**Nota:** Los casos en negrita tienen EDI > 0.30 pero son rechazados por fallar criterios C1-C5. Esto demuestra que el protocolo no es un *rubber stamp*.

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
