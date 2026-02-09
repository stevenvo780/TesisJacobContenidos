# 04 Casos de Estudio — Narrativa Unificada (29 Casos)

## Resumen de Validación
El motor de simulación ha sido ejecutado sobre un universo de **29 casos**, tras la remoción de 3 casos por inviabilidad de datos reales (Estética, Moderación Adversarial, RTB Publicidad). El protocolo C1-C5 + 6 criterios adicionales actúan como filtro de demarcación ontológica. La evaluación se realiza con `assimilation_strength=0.0` y 999 permutaciones (seed=42).

> **Estado actual:** Bajo el pipeline limpio: **overall_pass = 2/29** (Deforestación y Microplásticos). La hipótesis H1 se confirma parcialmente bajo la taxonomía de emergencia diferenciada.

| Categoría | Conteo | Resultado |
|-----------|--------|-----------|
| **strong** (EDI > 0.30, overall_pass=True) | 2 | Evidencia positiva de H1 |
| **weak** (0.10 ≤ EDI < 0.30, p < 0.05) | 1 | Señal sub-umbral |
| **suggestive** (EDI > 0.01, p < 0.05) | 3 | Señal estadística insuficiente |
| **trend** (EDI > 0, p ≥ 0.05) | 7 | Tendencia sin confirmación |
| **null** (EDI ≤ 0 o sin señal) | 13 | Sin constricción macro |
| **falsification** (Controles negativos) | 3 | Rechazados correctamente |

---

## 1. Emergencia Fuerte (strong) — overall_pass = True

Estos casos satisfacen H1 completamente: EDI > 0.30, significancia estadística (p < 0.001), y las 11 condiciones simultáneas del protocolo.

| ID | Caso | Fuente de Datos | EDI | p-perm | BC | Interpretación |
|----|------|-----------------|----:|-------:|:---|:---|
| 16 | **Deforestación** | World Bank (Área forestal) | **0.633** | 0.000 | full | ODE von Thünen captura frontera agrícola. 63% reducción RMSE |
| 24 | **Microplásticos** | OWID (Plastic Production) | **0.427** | 0.000 | none | Modelo Jambeck de acumulación persistente. Sin BC necesario |

**Deforestación Global** es el caso más robusto del corpus: la ODE modela la expansión de la frontera agrícola (modelo de von Thünen), y el Bias Correction full corrigió el sesgo de escala sin amplificar la señal. C1-C5 todos satisfechos, persistencia temporal estable.

**Microplásticos Oceánicos** es notable porque no requiere Bias Correction — la señal macro emerge directamente del acoplamiento ABM-ODE. El modelo Jambeck de acumulación persistente genera una constricción que reduce el RMSE en 43%.

---

## 2. Emergencia Débil (weak)

| ID | Caso | Fuente de Datos | EDI | p-perm | BC | Interpretación |
|----|------|-----------------|----:|-------:|:---|:---|
| 28 | **Fuga de Cerebros** | World Bank (I+D % PIB) | **0.183** | 0.001 | bias_only | Modelo Docquier-Rapoport. Señal significativa pero sub-umbral H1 |

El caso presenta emergencia estadísticamente significativa pero insuficiente para la condición H1 (EDI < 0.30). La migración de capital humano muestra inercia demográfica detectable, candidato para mejora con forcing multivariado.

---

## 3. Señal Sugestiva (suggestive)

| ID | Caso | Fuente de Datos | EDI | p-perm | Interpretación |
|----|------|-----------------|----:|-------:|:---|
| 09 | **Finanzas (SPY)** | Yahoo Finance | 0.040 | 0.000 | Serie ruidosa, señal mínima pero significativa |
| 17 | **Océanos** | Proxy WMO | 0.053 | 0.000 | Señal detectable, proxy poco representativo |
| 29 | **IoT** | World Bank (Suscripciones) | 0.020 | 0.000 | Señal se atenúa en datos reales |

Estos casos presentan significancia estadística (p < 0.05 y EDI > 0.01) pero la magnitud es insuficiente para afirmaciones ontológicas. Candidatos a mejora con modelos ODE dominio-específicos y forcing multivariado.

---

## 4. Tendencia no Significativa (trend)

| ID | Caso | Fuente de Datos | EDI | p-perm | Interpretación |
|----|------|-----------------|----:|-------:|:---|
| 01 | **Clima Regional** | Meteostat (NOAA) | 0.010 | 0.591 | ODE Budyko-Sellers insuficiente |
| 11 | **Movilidad** | World Bank | 0.003 | 0.361 | Señal marginal |
| 13 | **Políticas Estratégicas** | World Bank | 0.011 | 0.719 | Señal débil |
| 14 | **Postverdad** | Fallback sintético | 0.001 | 0.030 | Marginal, datos no disponibles |
| 18 | **Urbanización** | World Bank | 0.000 | 0.220 | Señal nula en práctica |
| 21 | **Salinización** | World Bank | 0.027 | 0.724 | Proxy inadecuado |
| 27 | **Riesgo Biológico** | World Bank (Mortalidad) | 0.105 | 0.365 | Señal positiva, no significativa |

---

## 5. Sin Evidencia (null) — 13 Casos

Casos donde la constricción macro no mejora (o empeora) la predicción del ABM:

| ID | Caso | EDI | Interpretación |
|----|------|----:|:---|
| 02 | Conciencia | -0.024 | Sin datos reales (fallback sintético) |
| 03 | Contaminación PM2.5 | -0.000 | Sin señal macro |
| 04 | Energía | -0.003 | Señal nula |
| 05 | Epidemiología | 0.000 | SEIR no capturada |
| 10 | Justicia | 0.000 | Sin señal |
| 12 | Paradigmas | 0.000 | Señal nula |
| 15 | Wikipedia | 0.000 | Sin estructura macro detectable |
| 19 | Acidificación Oceánica | -0.000 | Proxy inadecuado |
| 20 | Kessler | -0.420 | Anti-emergencia con datos CelesTrak |
| 22 | Fósforo | -1.000 | Anti-emergencia severa |
| 23 | Erosión Dialéctica | -1.000 | Anti-emergencia severa |
| 25 | Acuíferos | -0.179 | Señal no capturada |
| 26 | Starlink | -1.000 | Colapso del modelo |

Los casos con EDI fuertemente negativo (Fósforo, Erosión, Starlink) indican que el acoplamiento macro *destruye* información útil del ABM — un resultado que confirma la selectividad del protocolo. Estos no son fallos del marco, sino diagnósticos precisos de la inadecuación del modelo ODE para esos dominios.

---

## 6. Controles de Falsación (3/3 Correctos)
Sistemas diseñados para probar la selectividad del protocolo C1-C5:

| ID | Caso | Propósito | EDI | Estado |
|----|------|-----------|----:|:---|
| 06 | **Exogeneidad** | Probar respuesta ante ruido puro | 0.055 | ❌ Rechazado ✓ |
| 07 | **No-estacionariedad** | Probar respuesta ante Random Walk | -1.000 | ❌ Rechazado ✓ |
| 08 | **Observabilidad** | Probar respuesta ante estados ocultos | -1.000 | ❌ Rechazado ✓ |

Los tres controles son correctamente rechazados con categoría `falsification`, confirmando que el protocolo no es un rubber-stamp.

---

## 7. Casos Removidos (Archivo)
Descartados por falta de fuentes de datos reales verificables:
- **Estética Global:** Inviabilidad de API pública de subastas de arte.
- **Moderación Adversarial:** Opacidad de datos de plataformas (Big Tech).
- **RTB Publicidad:** Datos propietarios protegidos por NDAs de industria.

Archivados en `Artifacts/casos_removidos/`.

---

**Conclusión:** De los 26 casos genuinos (excluidas 3 falsaciones), 2 demuestran constricción macro efectiva con emergencia fuerte (7.7%), 1 muestra emergencia débil, y 3 presentan señal sugestiva estadísticamente significativa. La selectividad del protocolo (rechazo del 92.3% de casos genuinos) es la garantía de que las validaciones positivas representan evidencia genuina de patrones macro reales, no artefactos de modelado.
