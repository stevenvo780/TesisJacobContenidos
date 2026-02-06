# SimulacionClimatica: Ontología Operativa de Hiperobjetos

> **Tesis Doctoral:** Validación computacional de la existencia de entidades masivamente distribuidas mediante modelos híbridos (ABM + ODE).

Este repositorio contiene la implementación técnica y la fundamentación teórica para demostrar la **Eficacia Causal** de los hiperobjetos (Morton, 2013).

## 🚀 Instalación Rápida (Workspace)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
pip install -r repos/Simulaciones/requirements.txt
```

## 🧪 Experimentos Principales

### 1. Caso Clima (No Validado)
Modelo con cohesión interna adecuada pero estructura macro débil en zero-nudging.
*   **Ejecución:** `python3 repos/Simulaciones/caso_clima/src/validate.py`
*   **Resultado:** EDI 0.103 (< 0.30), CR 2.355 (> 2.0).

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

## 🧭 Mapa Doc ↔ Código (Fuente de Verdad)

- La **tesis** vive en `TesisDesarrollo/` y se ensambla en `TesisFinal/Tesis.md`.
- El **código** vive en `repos/Simulaciones/` (cada caso en `repos/Simulaciones/caso_*`).
- Los **resultados** de simulación (`outputs/`) se generan en `repos/Simulaciones/caso_*/outputs/`.
- En `TesisDesarrollo/02_Modelado_Simulacion/*/` se conserva el resumen documental (`metrics.json`, `report.md`, `docs/`).

## ⚖️ Licencia
MIT License. Ver `LICENSE` para más detalles.


## Resumen Integrado desde No estructurado

# Proyecto: Ontologia y Validacion de Hiperobjetos

## Resumen

Este repositorio construye un aparato filosofico-cientifico para tratar los hiperobjetos como sistemas reales, emergentes y medibles. Se adopta un realismo inferencial, un emergentismo fuerte y un holismo critico, con un programa metodologico que operacionaliza la medicion y validacion empirica de propiedades emergentes.

## Posturas Filosoficas Adoptadas

- **Realismo inferencial:** las entidades no observables se justifican por la mejor explicacion disponible.
- **Emergentismo fuerte:** las propiedades macro poseen novedad ontologica organizacional.
- **Holismo critico:** la totalidad es real solo si se explica por mecanismos verificables.
- **Causalidad descendente debil:** lo macro restringe lo micro sin violar el cierre causal.

## Estructura General

- `00_Marco_Conceptual`: ontologia, epistemologia, axiomas, debates y glosarios.
- `01_Metodologia_Medicion`: protocolos cientificos, validacion, metricas y ejecucion.
- `02_Modelado_Simulacion`: arquitectura y protocolos de modelado.
- `03_Validacion_Praxis`: validacion en practica y auditoria empirica.
- `04_Casos_De_Estudio`: formato y ejemplos de casos de estudio.

## Lectura Recomendada

- Índice maestro: `Indice_Maestro.md`
- Secciones principales:
- `00_Marco_Conceptual/00_00_Marco_Conceptual.md`
- `01_Metodologia_Medicion/01_00_Metodologia_Medicion.md`
- `02_Modelado_Simulacion/02_Modelado_Simulacion.md`
- `03_Validacion_Praxis/03_Validacion_Praxis.md`
- `04_Casos_De_Estudio/04_Casos_De_Estudio.md`
- `Anexos.md`

## Uso Recomendado

1. Leer la sintesis de la seccion correspondiente.
2. Profundizar en anexos solo si es necesario.
3. Para implementacion empirica, revisar 01 y 03 antes de iniciar pilotos.

## Estado del Marco

El marco conceptual y metodologico es coherente y suficientemente completo para iniciar investigacion. La capa practica incluye pipeline, gobernanza de datos, casos piloto y checklist de ejecucion.

## Resumen Integrado desde No estructurado

# README_ULTRA

## Que es este proyecto

Un tratado filosofico-cientifico para validar hiperobjetos como sistemas emergentes reales.

## Posturas adoptadas

- Realismo inferencial.
- Emergentismo fuerte.
- Holismo critico.
- Causalidad descendente debil.

## Documentos Únicos

Actualmente la tesis consolida cada sección en un único documento narrativo
por carpeta (ver la sección de lectura recomendada).
