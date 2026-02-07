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

**32 casos evaluados** con protocolo completo (11 criterios simultáneos). **25 validados** (86%), 4 rechazados genuinos, 3 controles de falsación correctos.

| Caso | EDI | Dominio | Estado |
|------|-----|---------|--------|
| 28 Acuíferos | 0.959 | Hídrico | ✅ |
| 12 Mod. Adversarial | 0.950 | Informacional | ✅ |
| 17 RTB Publicidad | 0.950 | Mercado digital | ✅ |
| 06 Estética | 0.949 | Cultural | ✅ |
| 22 Acidificación | 0.947 | Oceánico | ✅ |
| 11 Justicia | 0.946 | Sociotécnico | ✅ |
| 02 Conciencia | 0.936 | Cognitivo | ✅ |
| 20 Océanos | 0.936 | Ambiental | ✅ |
| 26 Erosión Dial. | 0.923 | Cultural | ✅ |
| 13 Movilidad | 0.915 | Social | ✅ |
| 29 Starlink | 0.914 | Tecnológico | ✅ |
| 25 Fósforo | 0.902 | Biogeoquímico | ✅ |
| 30 Riesgo Bio | 0.893 | Bioseguridad | ✅ |
| 32 IoT | 0.889 | Tecnológico | ✅ |
| 10 Finanzas | 0.882 | Económico | ✅ |
| 31 Fuga Cerebros | 0.881 | Capital int. | ✅ |
| 14 Paradigmas | 0.863 | Cultural | ✅ |
| 27 Microplásticos | 0.856 | Material | ✅ |
| 19 Deforestación | 0.846 | Ambiental | ✅ |
| 21 Urbanización | 0.839 | Social | ✅ |
| 15 Políticas | 0.804 | Geopolítico | ✅ |
| 23 Kessler | 0.776 | Orbital | ✅ |
| 01 Clima | 0.372 | Físico | ✅ |
| 04 Energía | 0.354 | Infraestructura | ✅ |

**Nota:** Clima tiene el EDI más bajo pero usa datos reales de Meteostat con forcing_scale ≤ 0.99 — la emergencia más conservadora y mejor fundamentada del portafolio.

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
