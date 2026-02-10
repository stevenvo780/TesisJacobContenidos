# Hiperobjetos: Irrealismo Operativo y Cierre Funcional

> **Tesis Doctoral:** Clasificación computacional del grado de cierre operativo de fenómenos masivamente distribuidos mediante modelos híbridos (ABM + ODE).

Este repositorio contiene la implementación técnica y la fundamentación teórica para medir el **cierre operativo** de hiperobjetos (Morton, 2013) bajo un marco de irrealismo operativo falsable. No se afirma ni se niega existencia metafísica; se clasifica el grado de constricción macro detectable.

## Instalación Rápida

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r repos/Simulaciones/requirements.txt
```

## Resultados Principales

**29 casos evaluados** con protocolo completo (11 criterios simultáneos, zero-nudging, permutation test).

| Nivel | Interpretación | Casos | Ejemplos destacados |
|:-----:|:---|:---:|:---|
| 4 | Cierre operativo fuerte | 2 | Deforestación (EDI=0.633), Microplásticos (EDI=0.427) |
| 3 | Componente funcional | 1 | Fuga de Cerebros (EDI=0.183) |
| 2 | Señal sugestiva | 3 | Finanzas, Océanos, IoT |
| 1 | Tendencia | 7 | Clima, Movilidad, Políticas, Postverdad, Urbanización, Salinización, Riesgo Biológico |
| 0 | Sin señal | 13 | Sin constricción macro detectable |
| — | Falsificación correcta | 3 | Controles negativos correctamente rechazados |

**overall_pass = 2/29** (Deforestación, Microplásticos). Significancia estadística (p<0.05): 6/29. El paisaje completo de 29 puntos en el gradiente de emergencia es el resultado principal.

Ejecución: `repos/Simulaciones/{NN}_caso_*/src/validate.py`

## Estructura de la Tesis

- **00_Marco_Conceptual:** Irrealismo operativo, emergentismo gradual, analogía del ribosoma.
- **01_Metodologia_Medicion:** Protocolos C1-C5, métricas EDI/CR, taxonomía de 6 niveles.
- **02_Modelado_Simulacion:** Arquitectura HybridModel y tabla auto-generada de 29 casos.
- **03_Validacion_Praxis:** Matriz de evidencia y paisaje de emergencia operativa.
- **04_Casos_De_Estudio:** Catálogo detallado por nivel de clasificación.
- **EjersiciosCriticos:** Síntesis del ejercicio Gladiadores.

## Mapa Doc - Código

- **Tesis:** `TesisDesarrollo/` → `TesisFinal/Tesis.md`
- **Código:** `repos/Simulaciones/{NN}_caso_*/src/`
- **Resultados:** `repos/Simulaciones/{NN}_caso_*/outputs/`
- **Docs por caso:** `TesisDesarrollo/02_Modelado_Simulacion/{NN}_caso_*/`

## Ejercicios Críticos (Gladiadores)

- **Partida 1 (20 rondas):** `EjersiciosCriticos/Ejercicio_Critico_Gladiadores_Partida1.md`
- **Trazas, Posibles y Dudas:** `EjersiciosCriticos/Trazas_Mejoras_Possibles_Dudas.md`

## Licencia
MIT License.
