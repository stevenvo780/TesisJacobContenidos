# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) para trabajar con el código de este repositorio.

**IMPORTANTE:** Responder siempre en español.

## Descripcion del Proyecto

Investigación de tesis doctoral ("Ontología Operativa de Hiperobjetos") que valida la existencia computacional de hiperobjetos (entidades masivas y distribuidas como Clima, Economía, Pandemias) mediante modelado híbrido que combina Modelos Basados en Agentes (ABM) y Ecuaciones Diferenciales Ordinarias (ODE). La tesis conecta el realismo especulativo (Morton, Harman) con validación computacional usando teoría de la información (Shannon, Hoel).

**Hipótesis Central (H1):** Un hiperobjeto es computacionalmente real si un modelo macro (ODE) reduce la entropía de los componentes micro (ABM) en >30%, medido mediante el Índice de Dependencia Efectiva (EDI > 0.30).

## Comandos Principales

### Instalar dependencias
```bash
pip install -r repos/Simulaciones/requirements.txt
```

### Ejecutar validaciones de simulación
```bash
python3 repos/Simulaciones/caso_clima/src/validate.py
python3 repos/Simulaciones/caso_finanzas/src/validate.py
```

### Auditar todos los casos de simulación
```bash
python3 repos/scripts/auditar_simulaciones.py
```

### Evaluar y actualizar tablas de simulación
```bash
python3 repos/scripts/evaluar_simulaciones.py
python3 repos/scripts/actualizar_tablas_002.py
```

## Arquitectura

### Estructura del Repositorio

- **TesisDesarrollo/** — Contenido de la tesis en 5 módulos (00-04): Marco Conceptual, Metodología, Modelado y Simulación, Validación, Casos de Estudio
- **TesisFinal/Tesis.md** — Documento final compilado de la tesis
- **repos/Simulaciones/** — Código fuente Python de las simulaciones (modelos híbridos ABM+ODE)
- **Artifacts/** — Documentos de auditoría y artefactos de trabajo (fase 1 y fase 2)
- **repos/scripts/** — Scripts utilitarios para auditoría, evaluación y actualización de datos de simulación
- **GEMINI.md** — Documento maestro de contexto con visión del proyecto y reglas de ejecución

### Estructura del Código de Simulación (por caso)

Cada caso en `repos/Simulaciones/caso_*/` sigue:
```
src/
  validate.py   # Orquestador: calibración → simulación → métricas → reporte
  abm.py        # Modelo basado en agentes (difusión en retícula con acoplamiento)
  ode.py        # Solver ODE macro (balance energético con asimilación de datos)
  metrics.py    # Cómputo de EDI, CR, RMSE, correlación
  data.py       # Obtención y preprocesamiento de datos
outputs/
  metrics.json  # Métricas de validación computadas
  report.md     # Resultados narrativos
docs/           # Documentación específica del caso (arquitectura, protocolos, reproducibilidad)
```

### Lógica de Acoplamiento del Modelo Híbrido

1. **Macro (ODE):** `dX/dt = alpha(F(t) - beta*X)` con nudging observacional
2. **Micro (ABM):** Agentes en retícula con difusión espacial + acoplamiento al estado macro
3. **Pipeline de validación:** Datos sintéticos (verdad conocida) → Calibración de parámetros → Validación con datos reales → Pruebas de perturbación de robustez

### Umbrales Críticos de Validación (Reglas de Rechazo)

| Métrica | Umbral | Significado |
|---------|--------|-------------|
| EDI < 0.30 | RECHAZO | Sin estructura macro detectada |
| EDI > 0.90 | RECHAZO | Tautología / error de calibración |
| Coupling < 0.10 | RECHAZO | Epifenomenalismo |
| RMSE < 1e-10 | RECHAZO | Fraude por sobreajuste |
| CR > 2.0 | PASA | Cohesión interna supera la externa |

### Protocolo de Validación C1-C5

- **C1:** Convergencia — ABM y ODE deben converger sobre datos reales
- **C2:** Robustez — Estabilidad bajo perturbación de parámetros
- **C3:** Aleatoriedad determinista — Semillas fijas para reproducibilidad
- **C4:** Linter de realidad — Coherencia con leyes del dominio
- **C5:** Reporte de fallos — Sensibilidad y límites explícitos

## 18 Casos de Simulación

Ubicados en `TesisDesarrollo/02_Modelado_Simulacion/`. Incluyen casos exitosos (clima, contaminación, movilidad, paradigmas), casos de falsación intencional (exogeneidad, no-estacionariedad, observabilidad) y un caso de fallo deliberado (finanzas, EDI=0.05). Solo `caso_clima` y `caso_finanzas` tienen código Python ejecutable completo en `repos/Simulaciones/`.

## Notas sobre Lenguaje y Contenido

- El contenido de la tesis está escrito en **español**; los comentarios de código y nombres de variables mezclan español e inglés
- El proyecto usa **emergencia metaestable** como concepto ontológico central — los hiperobjetos son atractores metaestables, no atractores fuertes autónomos
- El nudging (asimilación de datos) está justificado teóricamente como la formalización matemática del acoplamiento hiperobjeto-materia, no como un artefacto computacional
- Dependencias: numpy, pandas, scipy, meteostat (datos climáticos), yfinance (datos financieros)
