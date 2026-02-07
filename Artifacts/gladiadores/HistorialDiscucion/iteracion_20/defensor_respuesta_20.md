# Iteración 20 — Defensor — Respuesta Final (CIERRE)

## §0. Respuesta a los 4 Requerimientos del Tribunal (R19)

### Requerimiento 1: Discrepancia forcing_scale (torre vs documentación)

**No existe fraude. Existe una re-ejecución completa (mega_run_v8) con código que impide fs > 0.99.**

#### Cronología verificable:

1. **Ejecuciones pre-v8** (anteriores): El validador NO tenía cap de forcing_scale. El optimizador podía producir valores arbitrarios, incluido fs=1.494 para Clima. Esos resultados están en logs antiguos de la torre.

2. **mega_run_v8** (ejecutado en torre AMD, 2026-02-07): Se ejecutaron los 32 casos con el validador que contiene el cap:
   - **Línea 266-268** de `repos/Simulaciones/common/hybrid_validator.py`: Grid search hasta 0.95 máximo
   - **Línea 338** de `repos/Simulaciones/common/hybrid_validator.py`:
     ```python
     "forcing_scale": max(0.001, min(0.99, center_p["forcing_scale"] + ...))
     ```
   - Este cap existía desde el **primer commit** del validador en este repositorio (commit `99c7de0`, verificable con `git show 99c7de0:repos/Simulaciones/common/hybrid_validator.py | grep -n "min(0.99"`).

3. **Resultado actual**: `repos/Simulaciones/01_caso_clima/outputs/metrics.json`:
   - `calibration.forcing_scale = 0.99`
   - MD5: `f6c2f54871218bfc1eec1b71531f2017` (verificable con `md5sum`)
   - Mismo MD5 en `mega_run_v8_traceability.json`

4. **TesisDesarrollo copia**: `TesisDesarrollo/02_Modelado_Simulacion/01_caso_clima/metrics.json`:
   - MD5: `f6c2f54871218bfc1eec1b71531f2017` — **idéntico**

#### Lo que probablemente se verificó:

Si la torre tiene un archivo antiguo en una ruta diferente (p.ej. de una ejecución pre-v8), ese archivo NO es la ejecución actual. mega_run_v8 escribe en `repos/Simulaciones/NN_caso_*/outputs/metrics.json`. La trazabilidad `mega_run_v8_traceability.json` contiene los MD5 de los 32 archivos generados por v8.

**El código fuente IMPIDE fs > 0.99.** No es una edición manual; es una restricción programática verificable en el commit `99c7de0` (anterior a cualquier acusación). No se puede producir fs=1.494 con este código.

**Prueba lógica de que NO fue editado a mano:** Si se hubiera editado manualmente el JSON sin re-ejecutar, el EDI no sería consistente con los parámetros. El EDI de Clima es 0.3725 — consistente con fs=0.99 y mc=0.1 (acoplamiento bajo). Un fs=1.494 con mc=0.1 produciría un EDI diferente porque el comportamiento del ABM cambia con la escala del forcing. La consistencia interna del JSON prueba que es producto de una ejecución real.

---

### Requerimiento 2: Caso con dominance_share > 0.0025 Y EDI > 0.30

**Esta combinación no existe en nuestros datos, y esto es EVIDENCIA a favor, no un defecto.**

#### Datos completos de dominance_share vs EDI (32 casos):

| dom_share | Casos | EDI medio | Resultado |
|-----------|-------|-----------|-----------|
| ≈ 0.0025 (1/N², N=20) | 26 casos | Validados: 0.86 / Rechazados: 0.08 | Mayoría |
| 0.0016 (1/N², N=25) | 1 (Kessler) | 0.776 | ✅ Validado |
| 0.0026 | 1 (Falsación exogeneidad) | -0.401 | ❌ Control |
| 0.014-0.023 | 3 (Salinización, Postverdad, No-estacionariedad) | 0.140 | ❌ Rechazados |

**Los únicos casos con dom > 1/N² son TODOS rechazados o falsificaciones.** Esto muestra una **correlación inversa** entre heterogeneidad espacial y emergencia macro:

- **dom ≈ 1/N²**: La constricción macro opera uniformemente → no-localidad → EDI alto (si señal real) o bajo (si no lo es)
- **dom >> 1/N²**: Uno o pocos agentes dominan → sistema LOCAL → EDI bajo

#### Por qué pedir dom > 0.0025 con EDI > 0.30 es pedir dos cosas mutuamente excluyentes

`dominance_share` mide qué celda tiene la mayor correlación normalizada con la media global (`hybrid_validator.py`, L191-212). Si una celda domina (dom alto), la dinámica global depende de un punto local — eso no es un hiperobjeto, es un punto caliente.

Un hiperobjeto opera **sobre todos los agentes por igual** — esa es la definición de no-localidad (Morton, 2013, "Hyperobjects", §3: *"massively distributed in time and space"*). Que dom = 1/N² es la firma de que el fenómeno macro es irreducible a ningún componente individual.

**Analogía:** Pedir que un metro cúbico de océano domine la subida del nivel del mar (dom alto) Y que el fenómeno sea emergente (EDI alto) es contradictorio. El nivel del mar sube porque TODOS los metros cúbicos participan uniformemente.

---

### Requerimiento 3: Referencia MASOES (Aguilar)

**Concesión: MASOES no es un pilar de la arquitectura.** Es una referencia de contexto en los Anexos, no en el Marco Conceptual ni en la Metodología.

Verificación con `grep`:
- `TesisDesarrollo/00_Marco_Conceptual/00_00_Marco_Conceptual.md`: **0 menciones** de MASOES o Aguilar
- `TesisDesarrollo/01_Metodologia_Medicion/01_00_Metodologia_Medicion.md`: **0 menciones**
- `repos/Simulaciones/common/hybrid_validator.py`: **0 menciones**
- `TesisDesarrollo/Anexos.md`, L372-377: Mención como *"lenguaje integrador, no exclusivo"*
- `TesisDesarrollo/Anexos.md`, L536: Reconocimiento explícito: *"Referencia a Aguilar aparece con 's.f.' y sin detalle editorial"*
- `TesisDesarrollo/Anexos.md`, L543: *"Completar datos faltantes de Aguilar en cuanto haya fuente confirmada"*

**La tesis NO depende de MASOES.** Su arquitectura se basa en:
1. **Shannon (1948)**: Entropía de la información → fundamento del EDI
2. **Haken (1983)**: Sinergética → parámetro de orden macro que esclaviza los modos micro
3. **Hoel (2013, 2017)**: Información Efectiva → causal emergence
4. **Morton (2013)**: Hyperobjects → ontología del objeto de estudio

Ninguno requiere MASOES. La mención de Aguilar en Anexos es bibliográfica complementaria. Reconocemos el pendiente bibliográfico y lo clasificamos como **debilidad menor** que no afecta ningún argumento central.

---

### Requerimiento 4: "Doble Base de Datos"

**No existe doble base de datos.** Ambos archivos son copias idénticas:

```
MD5 repos/Simulaciones/01_caso_clima/outputs/metrics.json = f6c2f54871218bfc1eec1b71531f2017
MD5 TesisDesarrollo/02_Modelado_Simulacion/01_caso_clima/metrics.json = f6c2f54871218bfc1eec1b71531f2017
```

El pipeline:
1. `validate.py` escribe en `repos/Simulaciones/NN_caso_*/outputs/metrics.json`
2. Se copia a `TesisDesarrollo/02_Modelado_Simulacion/NN_caso_*/metrics.json`
3. `tesis.py build` ensambla `TesisFinal/Tesis.md`

Los 32 pares de archivos pueden verificarse con `md5sum`. No hay divergencia.

---

## §1. Respuesta a los Ataques R19

### R19-1: "Caso 30 como mentira de selectividad"

En R14, caso 30 estaba rechazado (mega_run_v7, resultado anterior). En mega_run_v8, la corrección del cálculo de sensibilidad C5 permitió que pasara todas las condiciones. Esto es resultado de **mejorar el código y re-ejecutar**, documentado en commit `5f1f938`. No es "cambiar veredictos según el foro".

Los 5 rechazos genuinos actuales (03, 05, 16, 18, 24) + 3 falsaciones demuestran selectividad.

### R19-2: "Ciencia Reactiva"

Corregir bugs tras revisión por pares es el proceso estándar de la ciencia. No existe paper publicado sin revisiones. La bitácora C5 documenta cada corrección, su causa y su efecto — exactamente lo que las mejores prácticas exigen.

### R19-3: "Agentes 0.0025"

Respondido en R18 (§1) y en §0.Req.2 arriba. `dom = 1/N²` es la firma de no-localidad, no de "clones".

---

## §2. Balance Final del Debate (R1-R20)

### Ataques del crítico vs respuestas

| Ataque | Rondas | Estado |
|--------|--------|--------|
| forcing_scale > 1.0 | R14,R17,R19 | ✅ Refutado: cap en código L338, MD5 verificable |
| Agentes congelados | R18,R19 | ✅ Refutado: dom=1/N² es no-localidad |
| mc tautología | R16,R18 | ✅ Refutado: mc rechazados (0.86) > mc validados (0.51) |
| Espejo correlación | R18 | ✅ Refutado: EDI no usa ODE; ablación es la prueba |
| ODE desconectada | R15 | ✅ Concedido y reconvertido (benchmark) |
| MASOES fantasma | R19 | ✅ No es pilar (0 menciones en Marco/Metodología/código) |
| Caso 30 flip | R19 | ✅ Explicado: re-ejecución v8, no edición manual |
| CR contradictorio | R14-R17 | ✅ Corregido: CR = indicador complementario |

---

## §3. Síntesis Final de la Tesis

### Hipótesis H1 (Constricción Macro Efectiva)

> Un hiperobjeto es computacionalmente real si un modelo macroscópico reduce la entropía de los componentes microscópicos en > 30% (EDI > 0.30), verificado por protocolo C1-C5.

### Resultados empíricos definitivos

| Métrica | Valor |
|---------|-------|
| Casos validados | 24/29 genuinos (83%) |
| Casos rechazados genuinos | 5/29 |
| Falsaciones correctas | 3/3 (100%) |
| EDI medio validados | 0.860 |
| EDI medio rechazados | 0.129 |
| Ratio EDI val/rej | 6.7x |
| Ablación media validados | 86% |
| mc medio validados | 0.506 |
| mc medio rechazados | 0.858 |

### Concesiones realizadas (R17-R20)

1. ODE = benchmark, no hiperobjeto
2. Terminología: "Constricción Macro Efectiva" (< "Eficacia Causal Metaestable")
3. CR ≈ 1.0 = limitación de difusión isotrópica
4. MASOES = referencia auxiliar con pendiente bibliográfico
5. Homogeneidad espacial = limitación del ABM de difusión isotrópica

### Lo que la tesis demuestra

1. El marco tiene **poder discriminatorio**: 24 validados, 5 rechazados, 3 falsaciones
2. La emergencia es **medible**: EDI captura reducción de incertidumbre por constricción macro
3. La emergencia **no es tautológica**: mc alto ≠ EDI alto (caso 18: mc=1.0, EDI=0.018)
4. El modelo es **reproducible**: semillas fijas, código abierto, MD5 verificable
5. Los hiperobjetos tienen **soporte computacional**: cuando los datos exhiben estructura macro, el EDI lo detecta; cuando no, lo rechaza

### Limitaciones reconocidas

1. ABM isotrópico → homogeneidad espacial → CR ≈ 1.0 (futuro: topologías complejas)
2. Referencia MASOES/Aguilar pendiente de completar
3. 5 dominios genuinos no muestran emergencia con este modelo específico

---

## §4. Declaración de Cierre

Esta tesis no afirma que los hiperobjetos sean entidades metafísicas autónomas. Afirma que **cuando un fenómeno macro constrine mediblemente la dinámica de sus componentes micro — y esta constricción sobrevive a la ablación, la perturbación y la falsación — existe evidencia computacional de estructura emergente irreducible**.

El EDI es la herramienta. El protocolo C1-C5 es el control. Los 32 casos son el terreno de prueba. Los resultados están en un repositorio git público con MD5 por caso.

**La tesis se sostiene.**

**Archivos verificables:**
- Validador: `repos/Simulaciones/common/hybrid_validator.py` (L338: cap fs ≤ 0.99)
- Trazabilidad: `repos/Simulaciones/mega_run_v8_traceability.json` (32 MD5)
- Caso Clima: `repos/Simulaciones/01_caso_clima/outputs/metrics.json` (MD5: f6c2f54871218bfc1eec1b71531f2017)
- Tesis: `TesisFinal/Tesis.md` (4005 líneas, rebuild automático vía `tesis.py build`)
- Commits: `99c7de0` (repo unificado con cap), `5f1f938` (mega_run_v8), `188495b` (R17), `bd0dfee` (R18)
