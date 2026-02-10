# CLAUDE.md

Este archivo proporciona orientación a Claude Code (claude.ai/code) para trabajar con el código de este repositorio.

**IMPORTANTE:** Responder siempre en español.

## Descripción del Proyecto

Investigación de tesis doctoral ("Irrealismo Operativo de Hiperobjetos") que clasifica el grado de cierre operativo de fenómenos masivamente distribuidos (Clima, Deforestación, Pandemias) mediante modelado híbrido ABM+ODE. La tesis adopta un **irrealismo operativo**: no afirma ni niega existencia metafísica — mide suficiencia operativa de constructos macro.

**Hipótesis Central (H1):** Un fenómeno exhibe cierre operativo de grado G cuando la eliminación de su constructo macro degrada la predicción micro en una proporción EDI ≥ G/100, verificable mediante el protocolo C1-C5 con zero-nudging.

## Comandos Principales

### Instalar dependencias
```bash
pip install -r repos/Simulaciones/requirements.txt
```

### Ejecutar validaciones de simulación
```bash
cd repos/Simulaciones/01_caso_clima/src && python3 validate.py
cd repos/Simulaciones/16_caso_deforestacion/src && python3 validate.py
```

### Auditar todos los casos de simulación
```bash
python3 repos/scripts/auditar_simulaciones.py
python3 repos/scripts/_audit_fresh.py
```

### Evaluar, actualizar tablas y construir tesis
```bash
python3 repos/scripts/actualizar_tablas_002.py
python3 repos/scripts/evaluar_simulaciones.py --write
python3 repos/scripts/tesis.py build
```

## Arquitectura

### Estructura del Repositorio

- **TesisDesarrollo/** — Contenido de la tesis en 5 módulos (00-04): Marco Conceptual, Metodología, Modelado y Simulación, Validación, Casos de Estudio
- **TesisFinal/Tesis.md** — Documento final compilado de la tesis
- **repos/Simulaciones/** — Código fuente Python de las simulaciones (modelos híbridos ABM+ODE), 29 casos
- **Artifacts/** — Documentos de auditoría y artefactos de trabajo (fase 1 y fase 2)
- **repos/scripts/** — Scripts utilitarios para auditoría, evaluación y actualización de datos de simulación

### Estructura del Código de Simulación (por caso)

Cada caso en `repos/Simulaciones/{NN}_caso_*/` sigue:
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

1. **Macro (ODE):** `dX/dt = alpha(F(t) - beta*X)` con nudging observacional (desactivado en evaluación)
2. **Micro (ABM):** Agentes en retícula con difusión espacial + acoplamiento al estado macro
3. **Pipeline de validación:** Datos sintéticos (verdad conocida) → Calibración de parámetros → Validación con datos reales → Ablación (mc=0, fs=0)
4. **EDI** = `(rmse_reduced - rmse_abm) / rmse_reduced` — solo en ventana de validación

### Umbrales Críticos de Validación (Reglas de Rechazo)

| Métrica | Umbral | Significado |
|---------|--------|-------------|
| EDI < 0.30 | Por debajo de Nivel 4 | Sin cierre operativo fuerte |
| EDI > 0.90 | RECHAZO | Tautología / error de calibración |
| Coupling < 0.10 | RECHAZO | Epifenomenalismo |
| RMSE < 1e-10 | RECHAZO | Fraude por sobreajuste |
| CR > 2.0 | Informativo | Cohesión interna supera la externa |

### Taxonomía de Niveles de Emergencia Operativa

| Nivel | Categoría | EDI | Interpretación |
|:-----:|:----------|:----|:---------------|
| 4 | strong | ≥0.30 + C1-C5 | Cierre operativo fuerte |
| 3 | weak | 0.10-0.30 + sig | Componente funcional |
| 2 | suggestive | >0.01 + sig | Señal sugestiva |
| 1 | trend | >0 pero no sig | Tendencia |
| 0 | null | ≤0 o no sig | Sin señal |
| — | falsification | — | Control negativo correcto |

## 29 Casos de Simulación

Ubicados en `repos/Simulaciones/{NN}_caso_*/src/`. **overall_pass = 2/29** (Deforestación EDI=0.633, Microplásticos EDI=0.427). Significancia: 6/29. Niveles: {0: 13, 1: 7, 2: 3, 3: 1, 4: 2}. 3 controles de falsación correctos. El paisaje completo de 29 puntos en el gradiente de emergencia es el resultado principal.

### Casos con Cierre Operativo (Nivel 4)
- **Deforestación** (16): EDI=0.633, p=0.000, overall_pass=True. Modelo von Thünen + BC full.
- **Microplásticos** (24): EDI=0.427, p=0.000, overall_pass=True. Modelo Jambeck. Sin BC.

### Caso Notable
- **Clima** (01): EDI=0.010, Nivel 1. Sonda insuficiente, no refutación del fenómeno.
- **Finanzas** (09): EDI=0.040, Nivel 2. Reflexividad y aliasing temporal.

## Notas sobre Lenguaje y Contenido

- El contenido de la tesis está escrito en **español**; los comentarios de código y nombres de variables mezclan español e inglés
- **Irrealismo operativo**: nunca afirmamos "X *es* un hiperobjeto"; afirmamos "X exhibe cierre operativo de grado G según este instrumento"
- **Analogía del ribosoma**: los niveles 2-3 son como ribosomas — componentes funcionales que no constituyen un nivel autónomo
- Zero-nudging: assimilation_strength=0 en todas las evaluaciones (verificado en 9 puntos del código)
- Dependencias: numpy, pandas, scipy, meteostat (datos climáticos), yfinance (datos financieros)
