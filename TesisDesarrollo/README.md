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

**29 casos evaluados** con protocolo completo (11 criterios simultáneos). **overall_pass = 0/29** con el pipeline limpio (sin data leakage, zero-nudging). La hipótesis H1 queda **no confirmada** bajo criterios estrictos, pero el marco demuestra capacidad discriminante (3/3 falsaciones correctas).

| Caso | EDI_real | Dominio | Estado |
|------|----------|---------|--------|
| 24 Microplásticos | 0.586 | Material | ⚠️ Señal parcial |
| 27 Riesgo Biológico | 0.414 | Bioseguridad | ⚠️ Señal parcial |
| 28 Fuga Cerebros | 0.213 | Capital int. | ⚠️ Débil |
| 17 Océanos | 0.119 | Ambiental | ⚠️ Marginal |
| 09 Finanzas | 0.051 | Económico | ❌ Nulo |
| 29 IoT | 0.014 | Tecnológico | ❌ Nulo |
| 01 Clima | -0.299 | Físico | ❌ Anti-emergencia |
| 16 Deforestación | -1.001 | Ambiental | ❌ Anti-emergencia |
| 20 Kessler | -3.419 | Orbital | ❌ Anti-emergencia |
| 26 Starlink | -546.587 | Tecnológico | ❌ Colapso |

**Nota:** Solo Microplásticos (0.586) y Riesgo Biológico (0.414) alcanzan EDI_real > 0.30, pero fallan otros criterios del protocolo de 11 condiciones.

Ejecución: `repos/Simulaciones/{NN}_caso_*/src/validate.py`

## Estructura de la Tesis

- **00_Marco_Conceptual:** Fundamentos filosoficos.
- **01_Metodologia_Medicion:** Protocolos C1-C5, metricas EDI/CR.
- **02_Modelado_Simulacion:** Arquitectura del motor HybridModel y 29 casos.
- **03_Validacion_Praxis:** Matriz de evidencia y análisis de fallos.
- **04_Casos_De_Estudio:** Catálogo detallado de casos.
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
