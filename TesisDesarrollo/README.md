# Hiperobjetos: Ontología Operativa de Hiperobjetos

> **Tesis Doctoral:** Validacion computacional de la existencia de entidades masivamente distribuidas mediante modelos hibridos (ABM + ODE).

Este repositorio contiene la implementacion tecnica y la fundamentacion teorica para demostrar la **Eficacia Causal** de los hiperobjetos (Morton, 2013) bajo un marco operacional falsable.

## Instalacion Rapida

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r repos/Simulaciones/requirements.txt
```

## Resultados Principales

**29 casos evaluados** con protocolo completo (11 criterios simultaneos). **21 validados** (81%), 5 rechazados genuinos, 3 controles de falsacion correctos.

| Caso | EDI | Dominio | Estado |
|------|-----|---------|--------|
| 28 Acuiferos | 0.959 | Hidrico | ✅ |
| 12 Mod. Adversarial | 0.950 | Informacional | ✅ |
| 17 RTB Publicidad | 0.950 | Mercado digital | ✅ |
| 06 Estetica | 0.949 | Cultural | ✅ |
| 22 Acidificacion | 0.947 | Oceanico | ✅ |
| 11 Justicia | 0.946 | Sociotecnico | ✅ |
| 02 Conciencia | 0.936 | Cognitivo | ✅ |
| 20 Oceanos | 0.936 | Ambiental | ✅ |
| 26 Erosion Dial. | 0.923 | Cultural | ✅ |
| 13 Movilidad | 0.915 | Social | ✅ |
| 29 Starlink | 0.914 | Tecnologico | ✅ |
| 25 Fosforo | 0.902 | Biogeoquimico | ✅ |
| 30 Riesgo Bio | 0.893 | Bioseguridad | ✅ |
| 32 IoT | 0.889 | Tecnologico | ✅ |
| 10 Finanzas | 0.882 | Economico | ✅ |
| 31 Fuga Cerebros | 0.881 | Capital int. | ✅ |
| 14 Paradigmas | 0.863 | Cultural | ✅ |
| 27 Microplasticos | 0.856 | Material | ✅ |
| 19 Deforestacion | 0.846 | Ambiental | ✅ |
| 21 Urbanizacion | 0.839 | Social | ✅ |
| 15 Politicas | 0.804 | Geopolitico | ✅ |
| 23 Kessler | 0.776 | Orbital | ✅ |
| 01 Clima | 0.372 | Fisico | ✅ |
| 04 Energia | 0.354 | Infraestructura | ✅ |

**Nota:** Clima tiene el EDI mas bajo pero usa datos reales con forcing_scale <= 0.99 — la emergencia mas conservadora del portafolio.

Ejecucion: `repos/Simulaciones/{NN}_caso_*/src/validate.py`

## Estructura de la Tesis

- **00_Marco_Conceptual:** Fundamentos filosoficos.
- **01_Metodologia_Medicion:** Protocolos C1-C5, metricas EDI/CR.
- **02_Modelado_Simulacion:** Arquitectura del motor HybridModel y 32 casos.
- **03_Validacion_Praxis:** Matriz de evidencia y analisis de fallos.
- **04_Casos_De_Estudio:** Catalogo detallado de casos.
- **EjersiciosCriticos:** Sintesis del ejercicio Gladiadores.

## Mapa Doc - Codigo

- **Tesis:** `TesisDesarrollo/` -> `TesisFinal/Tesis.md`
- **Codigo:** `repos/Simulaciones/{NN}_caso_*/src/`
- **Resultados:** `repos/Simulaciones/{NN}_caso_*/outputs/`
- **Docs por caso:** `TesisDesarrollo/02_Modelado_Simulacion/{NN}_caso_*/`

## Ejercicios Criticos (Gladiadores)

- **Partida 1 (20 rondas):** `EjersiciosCriticos/Ejercicio_Critico_Gladiadores_Partida1.md`
- **Trazas, Posibles y Dudas:** `EjersiciosCriticos/Trazas_Mejoras_Possibles_Dudas.md`

## Licencia
MIT License.
