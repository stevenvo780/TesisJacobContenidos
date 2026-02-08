# Plan Maestro de Reconciliación Ontológica

**Objetivo:** Alinear el aparato técnico y documental de la tesis con el veredicto de "Aprobación Condicionada" del ejercicio Gladiadores, implementando un realismo estructural de patrones y extendiendo el modelo para cubrir brechas ontológicas.

---

## Fase 1: Fundamento Filosófico (Completada)
- [x] Reformular H1 y definir Realismo Estructural de Patrones.
- [x] Mapear propiedades de Morton al aparato técnico.
- [x] Definir ODE como sonda ontológica.
- [x] Crear Glosario Maestro y Debate 05.

---

## Fase 2: Ajustes Metodológicos
**Meta:** Actualizar los documentos de metodología para que reflejen la nueva ontología honesta (descuento por LoE).

- [ ] **Regla de Descuento LoE:**
    - Insertar en `01_Metodologia_Medicion.md`. 
    - Fórmula: `EDI_ponderado = EDI * (LoE / 5)`.
    - Objetivo: Evitar reificación en casos con datos débiles (Conciencia, Estética).
- [ ] **Reinterpretación del EDI:**
    - Explicar en `01_Metodologia_Medicion.md` que EDI mide *indispensabilidad causal*, no "existencia" sustancial.
- [ ] **Ablación como Intervención:**
    - Documentar formalmente que poner `forcing_scale=0` es una intervención causal en sentido de Woodward.
- [ ] **Reclasificación de Casos:**
    - Actualizar `03_Validacion_Praxis.md` separando "Patrones Reales Robustos" (LoE alto) de "Prototipos Prospectivos" (LoE bajo).

---

## Fase 3: Extensiones Técnicas: Implementación de Variables Faltantes
**Meta:** Robustecer el motor `HybridModel` incorporando las **3 variables críticas** señaladas por la crítica de Gladiadores para romper la "tautología del diseño".

### 1. Variable Espacial: Topología de Red ($G_{ij}$)
- **Crítica:** "El modelo actual es un Punto Masivo con difusión isotrópica".
- **Implementación:** Reemplazar la grilla regular por grafos complejos (`networkx`).
    - **Métrica:** `Clustering Coefficient` y `Path Length`.
    - **Objetivo:** Demostrar que el Hiperobjeto persiste incluso cuando la topología cambia (Invarianza Topológica).

### 2. Variable Temporal: Viscosidad e Inercia ($\tau_{relax}$)
- **Crítica:** "El modelo es una marioneta que sigue el forcing sin resistencia".
- **Implementación:** Test de Perturbación.
    - Inyectar pulso exógeno momentáneo.
    - Medir tiempo de retorno al atractor (`relaxation_time`).
    - **Hipótesis:** Hiperobjetos reales tienen $\tau_{relax}$ alto (alta viscosidad), mientras que los agregados simples recuperan instantáneamente.

### 3. Variable Causal: Reflexividad ($\gamma$)
- **Crítica:** "La causalidad es unidireccional (forcing -> agentes)".
- **Implementación:** Feedback Loop Micro $\to$ Macro.
    - El estado agregado de los agentes modifica los parámetros de la ODE en $t+1$.
    - **Ecuación:** $ODE_{param}(t+1) = ODE_{param}(t) + \gamma \cdot \Delta Micro(t)$.
    - **Objetivo:** Capturar fenómenos antropogénicos (ej. Clima, Finanzas) donde el micro altera al macro.

### Tareas de Código:
- [ ] **Implementar Factor LoE en Validador:**
    - Modificar `metrics.json` para incluir `LoE` y `EDI_weighted`.
- [ ] **Nuevos Controles de Falsación (10, 11, 12).**
- [ ] **Implementar `HybridModel.set_topology(G)`:** Integración con NetworkX.
- [ ] **Implementar `HybridModel.perturb(magnitude)`:** Para test de viscosidad.
- [ ] **Implementar `HybridModel.set_feedback(gamma)`:** Para reflexividad.


---

## Fase 4: Validación con Extensiones
**Meta:** Ejecutar los experimentos necesarios para elevar el nivel de evidencia.

- [ ] **Ejecución Test Viscosidad:** Correr en los 24 casos validados.
- [ ] **Ejecución Topología Heterogénea:** Correr en Grupo A (Clima, Océanos, Acuíferos) para buscar fronteras.
- [ ] **Re-ejecución Mega Run:** Correr todo con las nuevas métricas y falsaciones.

---

## Anexo A: Distribución de Casos (Grupos de Trabajo)

Para organizar las extensiones y optimizaciones, los 32 casos se dividen en 6 grupos funcionales:

### Grupo A — Sistemas de Inercia Física (7 casos)
*Prioridad: Alta (Core de H1)*
- **Casos:** 01 (Clima), 04 (Energía), 20 (Océanos), 22 (Acidificación), 25 (Fósforo), 27 (Microplásticos), 28 (Acuíferos).
- **Acción:** Implementar topología heterogénea y test de viscosidad.
- **Dato:** Series físicas de larga duración.

### Grupo B — Sistemas Sociotécnicos con Gobernanza (6 casos)
*Prioridad: Media-Alta*
- **Casos:** 10 (Finanzas), 11 (Justicia), 13 (Movilidad), 15 (Políticas), 21 (Urbanización), 31 (Fuga Cerebros).
- **Acción:** Implementar retroalimentación micro→macro (reflexividad).

### Grupo C — Sistemas Tecnológicos-Digitales (6 casos)
*Prioridad: Media*
- **Casos:** 12 (Moderación), 17 (RTB), 23 (Kessler), 29 (Starlink), 30 (Riesgo Bio), 32 (IoT).
- **Acción:** Topología de red real (Kessler/Starlink) y detección de umbrales.

### Grupo D — Sistemas Culturales-Epistémicos (5 casos)
*Prioridad: Baja (Prototipos)*
- **Casos:** 02 (Conciencia), 06 (Estética), 14 (Paradigmas), 19 (Deforestación), 26 (Erosión).
- **Acción:** Aplicar descuento LoE severo.

### Grupo E — Rechazos Genuinos (5 casos)
- **Casos:** 03 (Contaminación), 05 (Epidemiología), 16 (Postverdad), 18 (Wikipedia), 24 (Salinización).
- **Acción:** Escribir post-mortem ontológico.

### Grupo F — Controles de Falsación (3 casos)
- **Casos:** 07 (Exogeneidad), 08 (No-estacionariedad), 09 (Observabilidad).
- **Acción:** Mantener como baseline de rechazo.

---

## Anexo B: Estrategia de Optimización y Rendimiento

La ejecución de 32 casos con extensiones (topología, viscosidad) aumentará la carga computacional. Se implementará el siguiente plan de optimización:

### 1. Paralelización de Ejecución (Nivel Caso)
- **Problema:** Ejecución secuencial de 32 casos tarda >2 horas.
- **Solución:** Implementar `multiprocessing` en el script maestro (`mega_run.py`) para ejecutar casos en paralelo aprovechando todos los núcleos de la CPU.
- **Meta:** Reducir tiempo total a <30 minutos.

### 2. Vectorización del Núcleo ABM (Nivel Agente)
- **Problema:** Bucles Python en `HybridModel.step()` son lentos para N>1000 agentes.
- **Solución:** Reemplazar iteraciones por operaciones vectoriales de `numpy` (broadcasting) para el cálculo de distancias y actualizaciones de estado.
- **Meta:** Speedup de 10x en el step del ABM.

### 3. JIT Compilation (Numba)
- **Problema:** Funciones de coste y ecuaciones diferenciales complejas.
- **Solución:** Decorar funciones críticas (`calculate_entropy`, `ode_step`) con `@numba.jit(nopython=True)`.

### 4. Gestión de Memoria y I/O
- **Problema:** Carga redundante de datasets grandes (Clima, Finanzas) en validaciones repetidas.
- **Solución:** Implementar caché de datos pre-procesados (pickles/parquet) y liberar memoria explícitamente tras cada caso.

## Fase 5: Cierre Documental y Académico
**Meta:** Producir la versión final defendible de la tesis.

- [ ] **Actualizar Tesis.md:** Incorporar todos los cambios narrativos y de resultados.
- [ ] **Post-mortem Ontológico:** Escribir por qué fallaron los casos rechazados bajo la nueva luz.
- [ ] **Replay Total Optimizada:** Ejecutar script maestro paralelo y registrar tiempos.

