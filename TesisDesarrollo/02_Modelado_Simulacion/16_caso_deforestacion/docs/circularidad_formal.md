# Análisis de Circularidad: Caso 16 — Deforestación

## La objeción

> El caso 16 (Deforestación) es el único con overall_pass=True. ¿No es circular que la ODE prediga deforestación usando datos de deforestación como input?

## Respuesta estructurada

### 1. Qué es y qué NO es circular

**Circularidad real** sería: "el modelo predice X porque le damos X como dato de entrenamiento y evaluación sobre los mismos puntos". Esto violaría el protocolo train/validation split.

**Lo que hace el caso 16**:
- Train: [2001, 2012] → calibra α, β de la ODE
- Validation: [2012, 2023] → evalúa métricas (EDI, C1-C5) **sin look-ahead**
- assimilation_strength = 0.0 en la fase de evaluación
- Forcing: datos de pérdida forestal (Global Forest Watch) alimentan el ABM como perturbación externa
- Target: la misma variable agregada (tree cover loss anual)

### 2. El forcing NO es el target

El forcing proviene de datos observados de deforestación anual que entran al ABM como señal exógena (incendios, tala, expansión agrícola). El target de la ODE es la **evolución del estado macro**: la dinámica acumulada de pérdida/regeneración forestal modelada como:

$$\frac{dX}{dt} = \alpha (F - \beta X) + \text{noise}$$

Donde:
- $F$ = forcing exógeno (perturbaciones anuales observadas)
- $X$ = estado del sistema (cobertura neta)
- $\alpha$ = tasa de respuesta del ecosistema
- $\beta$ = capacidad de regeneración

La ODE **NO** predice el forcing; predice la respuesta dinámica del sistema al forcing. La diferencia es análoga a:
- Circular: "la temperatura mañana será la temperatura de hoy"
- No circular: "dado el input de radiación solar (forcing), la temperatura responde con inercia (ODE)"

### 3. El test de ablación confirma la no-circularidad

El EDI = 0.633 con p-value = 0.0 (permutation test) demuestra que:
- ABM **con** ODE: RMSE significativamente menor
- ABM **sin** ODE: RMSE 63% mayor

Si fuera circular, el ABM sin ODE también capturaría la señal trivialmente (porque el forcing ya contiene la información). El gap de 63% indica que la ODE aporta estructura dinámica no redundante con el forcing directo.

### 4. Cross-check con falsificaciones

Los 3 casos de falsación (06, 07, 08) usan exactamente el mismo framework y protocolo:
- 06: EDI rechazado → exogeneidad no genera emergencia falsa
- 07: EDI rechazado → no-estacionariedad no genera emergencia falsa  
- 08: EDI rechazado → baja observabilidad no genera emergencia falsa

Si el framework fuera circular por diseño, TODOS los casos pasarían (incluyendo las falsificaciones). Los 3 rechazos demuestran que el EDI > 0.30 del caso 16 es genuino.

### 5. Diagnóstico cuantitativo

| Métrica | Valor | Interpretación |
|---------|-------|---------------|
| EDI | 0.633 | Rango válido [0.325, 0.90] |
| Bootstrap CI | [0.522, 0.734] | Intervalo no incluye 0 |
| p-value (permut.) | 0.000 | Altamente significativo |
| Corr ODE-obs | > 0.7 | Calidad ODE "good" |
| LoE | 3 | Datos satelitales directos (GFW) |
| EDI ponderado | 0.380 | > umbral mínimo |

### 6. Limitación reconocida

El caso 16 **sí** tiene una ventaja estructural: el indicador de deforestación (GFW tree cover loss) es una medición directa, no un proxy. Esto reduce el ruido de medición y facilita que la ODE capture la dinámica. Otros casos (ej: 21_salinización, 10_justicia) usan proxies indirectos, lo cual penaliza sus EDI.

Esta es una limitación de **calidad de datos**, no de circularidad lógica.

## Conclusión

El caso 16 no es circular. Es el caso con **mejor calidad de datos** (medición directa satelital, LoE=3) y **dinámica más limpia** (tendencia monotónica con variabilidad interanual clara). Su overall_pass=True refleja que, cuando los datos son buenos y la dinámica es clara, el framework detecta correctamente la emergencia.

---

*Referencia cruzada*: Falsificaciones (06, 07, 08), Protocolo C2 (EDI), §01 Metodología (train/val split)
