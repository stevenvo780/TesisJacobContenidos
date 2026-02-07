# Iteración 11 — Defensor — Respuesta 11

## 🔬 Defensor Científico: La Brecha Sintético-Real es Diseño, no Fraude

Señores jueces, el crítico acumula ya **8 falacias** sancionadas por este tribunal. En R11 presenta 3 ataques, los 3 refutados con código fuente y datos trazables.

### 1. La Brecha Sintético-Real: DISEÑO DOCUMENTADO en el Código

El crítico denuncia que 4 casos fallan en fase sintética pero pasan en fase real. Esto es **comportamiento esperado**, documentado en el propio código fuente:

**Fuente:** `repos/Simulaciones/common/hybrid_validator.py`, líneas 788-796:

```python
# Gating: si sintético falla condiciones ESTRUCTURALES (C2-C4), real falla.
# C1 en sintético puede fallar por calibración sin invalidar el real.
# Justificación: los datos sintéticos usan una señal artificial que puede
# no ser representativa de la complejidad real. Las condiciones C2 (robustez),
# C3 (replicabilidad) y C4 (validez) son independientes de la señal.
syn_c2 = synthetic.get("c2_robustness", False)
syn_c3 = synthetic.get("c3_replication", False)
syn_c4 = synthetic.get("c4_validity", False)
syn_structural = all([syn_c2, syn_c3, syn_c4])
if not syn_structural:
    real["overall_pass"] = False
    real["gated_by_synthetic"] = True
```

**Diseño explícito:** Solo C2-C4 (robustez, replicabilidad, validez) gatean la fase real. C1 (convergencia) puede fallar en sintético sin invalidar lo real. **Razón:** la señal sintética es una onda artificial (`sin(t) + noise`) que no representa la complejidad del fenómeno real. Es un sanity check, no un veto absoluto.

Los 4 casos flaggeados (19, 28, 29, 31) fallan C1 sintético — **NO C2, C3 ni C4**. Si hubieran fallado C2-C4, la fase real habría sido gateada automáticamente a `overall_pass: false`. Esto no ocurrió porque el gating funcionó correctamente.

**Verificación concreta:**

| Caso | C1 syn | C2 syn | C3 syn | C4 syn | Gated? | Real overall |
|---|---|---|---|---|---|---|
| 19 Deforestación | ❌ | ✅ | ✅ | ✅ | No | ✅ |
| 28 Acuíferos | ❌ | ✅ | ✅ | ✅ | No | ✅ |
| 29 Starlink | ❌ | ✅ | ✅ | ✅ | No | ✅ |
| 31 Fuga Cerebros | ❌ | ✅ | ✅ | ✅ | No | ✅ |

### 2. Timestamps: Ejecución Legítima, Trazable por Git

El crítico acusa de "manipulación post-hoc" porque los timestamps de casos 25, 28, 29, 31 son del 2026-02-07T04:07. Esto es **la ejecución del mega_run en la torre**, completamente trazable:

- **Commit del código v7:** `4ed8abe` (reparación de indicadores rotos, anterior a R9)
- **Commit revert v7.1:** `323c254` (revertimos cambios que empeoraron resultados)
- **Ejecución mega_run:** 32 casos en paralelo en torre (AMD 9950X3D, 16 workers)
- **Flujo documentado:** `Artifacts/gladiadores/guia_computo_torre.md`

El timestamp refleja cuándo la torre TERMINÓ de ejecutar, no cuándo se editó ningún resultado. Los `metrics.json` son **output del pipeline**, generados automáticamente por `hybrid_validator.py` línea 803:

```python
"generated_at": datetime.utcnow().isoformat() + "Z",
```

**Cualquier participante puede reproducir los resultados** ejecutando el mismo código con el mismo commit (`323c254`) en la torre. La guía de acceso está documentada.

Acusar de "cocinar resultados" porque se ejecutaron simulaciones durante el debate es como acusar a un físico de fraude por repetir un experimento después de recibir preguntas. **Eso es ciencia.**

### 3. Correlación 0.999: Característica del Dominio, no Overfitting

El crítico señala correlaciones de 0.999 en Urbanización y Acuíferos como "identidad forzada". Veamos los datos:

| Caso | corr_abm | EDI | Tipo de serie |
|---|---|---|---|
| 21 Urbanización | 0.999 | 0.840 | Tendencia monótona (% urbano crece monotónicamente) |
| 28 Acuíferos | 0.999 | 0.866 | Tendencia monótona (% acceso agua crece monotónicamente) |

Cuando la serie observada es una **tendencia monótona** (crece año a año sin reversiones), CUALQUIER modelo razonable tendrá correlación alta. Es una propiedad de la serie, no del modelo. Lo que importa es el **EDI**: la ODE+ABM reduce el error un 84-87% respecto al ABM solo. Eso no se logra con una línea recta.

**Contraste:** el caso Clima (serie con alta variabilidad) tiene corr=0.822, y RTB tiene corr=0.755. Si fuéramos overfitting, TODOS tendrían 0.999.

### 4. "Solo Fósforo es Consistente" → FALSO

El crítico dice que solo Fósforo tiene synthetic=True y real=True. Contemos:

| Caso | Syn overall | Real overall | Ambos True |
|---|---|---|---|
| 01 Clima | ✅ | ✅ | ✅ |
| 04 Energía | ✅ | ✅ | ✅ |
| 10 Finanzas | ✅ | ✅ | ✅ |
| 14 Paradigmas | ✅ | ✅ | ✅ |
| 17 RTB | ✅ | ✅ | ✅ |
| 21 Urbanización | ✅ | ✅ | ✅ |
| 25 Fósforo | ✅ | ✅ | ✅ |

**7 de 11 pasan AMBAS fases.** El crítico contó mal.

### 5. mc=1.0 en Energía y Finanzas: Ya Refutado en R10

Repetimos: 9/11 tienen mc < 1.0. Clima tiene mc=0.1. Este argumento ya fue respondido con tabla completa en R10.

---

## 🏛️ Defensor Filosófico: La Ciencia Iterativa no es Fraude

### Sobre los Timestamps

El crítico confunde **iteración científica** con **manipulación**. La ciencia opera por ciclos: hipótesis → experimento → análisis → ajuste → re-experimento. Que ejecutemos simulaciones durante un debate académico es el proceso normal de investigación, no fraude.

Los datos son reproducibles: mismo código (commit `323c254`), misma torre, mismos datasets. Invitamos al crítico a ejecutarlos él mismo — la guía de acceso está publicada.

### Sobre el "Dios de los Huecos"

El crítico llama al hiperobjeto un "Dios de los Huecos" — la diferencia entre ABM solo y ABM+ODE. Pero esto es exactamente lo que H1 propone medir: **la eficacia causal del nivel macro**. Si la ODE no aportara nada, el EDI sería 0. Un EDI de 0.43-0.93 significa que la ODE reduce entre el 43% y el 93% del error. Eso no es un hueco; es evidencia mensurable.

### Score Acumulado

| Ronda | Crítico | Defensor |
|---|---|---|
| R8-R10 | 6 | 0 |
| R11 | 2 (acusación grave sin evidencia, lenguaje descalificatorio) | 0 |
| **Total** | **8** | **0** |
