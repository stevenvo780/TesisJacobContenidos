# 04 Casos de Estudio (29 Casos)

## Resumen de Clasificación Operativa
El motor de simulación ha sido ejecutado sobre un universo de **29 casos**, tras la remoción de 3 casos por inviabilidad de datos reales (Estética, Moderación Adversarial, RTB Publicidad). El protocolo C1-C5 + 6 criterios adicionales actúan como instrumento de **clasificación operativa**, no de demarcación ontológica. La evaluación se realiza con `assimilation_strength=0.0` y 999 permutaciones (seed=42).

> **Estado actual:** Bajo el pipeline limpio: **2/29 en Nivel 4** (Deforestación y Microplásticos). El paisaje de emergencia operativa queda completamente mapeado.

| Categoría | Nivel | Conteo | Resultado operativo |
|-----------|:-----:|--------|---------------------|
| **strong** (EDI ≥ 0.30, overall_pass=True) | 4 | 2 | Cierre operativo fuerte |
| **weak** (0.10 ≤ EDI < 0.30, p < 0.05) | 3 | 1 | Componente funcional |
| **suggestive** (EDI > 0.01, p < 0.05) | 2 | 3 | Señal detectable |
| **trend** (EDI > 0, p ≥ 0.05) | 1 | 7 | Tendencia sin confirmación |
| **null** (EDI ≤ 0 o sin señal) | 0 | 13 | Sin señal operativa |
| **falsification** (Controles negativos) | — | 3 | Rechazados correctamente |

---

## 1. Nivel 4 — Cierre Operativo Fuerte (overall_pass = True)

Estos casos alcanzan el nivel máximo verificable por el instrumento: el constructo macro es operativamente indispensable. Su eliminación degrada la predicción micro en >40%.

| ID | Caso | Fuente de Datos | EDI | p-perm | BC | Interpretación operativa |
|----|------|-----------------|----:|-------:|:---|:---|
| 16 | **Deforestación** | World Bank (Área forestal) | **0.633** | 0.000 | full | ODE von Thünen captura frontera agrícola. 63% reducción RMSE |
| 24 | **Microplásticos** | OWID (Plastic Production) | **0.427** | 0.000 | none | Modelo Jambeck de acumulación persistente. Sin BC necesario |

**Deforestación Global** es el caso con mayor cierre operativo del corpus: la ODE modela la expansión de la frontera agrícola (modelo de von Thünen), y el Bias Correction full corrigió el sesgo de escala sin amplificar la señal. C1-C5 todos satisfechos, persistencia temporal estable. Bajo irrealismo operativo: el constructo "deforestación como hiperobjeto" es operativamente indispensable — no afirmamos su realidad ontológica, sino que funciona como si tuviera autonomía causal sobre los agentes.

**Microplásticos Oceánicos** es notable porque no requiere Bias Correction — la señal macro emerge directamente del acoplamiento ABM-ODE. El modelo Jambeck de acumulación persistente genera una constricción que reduce el RMSE en 43%. Analogía del ribosoma: el sistema funciona con cierre operativo sin que necesitemos postular una entidad separada de sus componentes materiales.

---

## 2. Nivel 3 — Componente Funcional

| ID | Caso | Fuente de Datos | EDI | p-perm | BC | Interpretación operativa |
|----|------|-----------------|----:|-------:|:---|:---|
| 28 | **Fuga de Cerebros** | World Bank (I+D % PIB) | **0.183** | 0.001 | bias_only | Modelo Docquier-Rapoport. Señal significativa pero sub-umbral |

El constructo macro mejora la predicción (18.3%) pero es prescindible. La migración de capital humano exhibe inercia demográfica detectable. Bajo la analogía del ribosoma: un componente que facilita la función global sin constituir un nivel autónomo. Candidato para reclasificación con forcing multivariado (variables adicionales: patentes/PIB, gasto en educación, migración neta).

---

## 3. Nivel 2 — Señal Sugestiva

| ID | Caso | Fuente de Datos | EDI | p-perm | Interpretación operativa |
|----|------|-----------------|----:|-------:|:---|
| 09 | **Finanzas (SPY)** | Yahoo Finance | 0.040 | 0.000 | Serie ruidosa, señal mínima pero significativa |
| 17 | **Océanos** | Proxy WMO | 0.053 | 0.000 | Señal detectable, proxy poco representativo |
| 29 | **IoT** | World Bank (Suscripciones) | 0.020 | 0.000 | Señal se atenúa en datos reales |

Estos casos presentan significancia estadística (p < 0.05 y EDI > 0.01) pero la magnitud no alcanza para atribuir cierre operativo. El instrumento los detecta como posibles candidatos — futuros trabajos con modelos ODE específicos por dominio y forcing multivariado podrían reclasificarlos.

**Nota sobre Finanzas:** La reflexividad inherente a los mercados (Soros, 1987) dificulta la separación macro/micro. El EDI de 0.040 es consistente con la hipótesis de que los mercados financieros son sistemas con acoplamiento débil y alta reflexividad, donde la "constricción macro" se disuelve rápidamente por la retroalimentación de los agentes.

---

## 4. Nivel 1 — Tendencia no Significativa

| ID | Caso | Fuente de Datos | EDI | p-perm | Interpretación operativa |
|----|------|-----------------|----:|-------:|:---|
| 01 | **Clima Regional** | Meteostat (NOAA) | 0.010 | 0.591 | ODE Budyko-Sellers insuficiente |
| 11 | **Movilidad** | World Bank | 0.003 | 0.361 | Señal marginal |
| 13 | **Políticas Estratégicas** | World Bank | 0.011 | 0.719 | Señal débil |
| 14 | **Postverdad** | Fallback sintético | 0.001 | 0.030 | Marginal, datos limitados |
| 18 | **Urbanización** | World Bank | 0.000 | 0.220 | Sin señal práctica |
| 21 | **Salinización** | World Bank | 0.027 | 0.724 | Proxy inadecuado |
| 27 | **Riesgo Biológico** | World Bank (Mortalidad) | 0.105 | 0.365 | Señal positiva, no significativa |

**Nota sobre Clima:** El caso paradigmático de Morton (2013) queda en Nivel 1 bajo este instrumento. Bajo irrealismo operativo, esto es informativo: el modelo Budyko-Sellers con datos de una estación regional no detecta cierre operativo fuerte. Esto no refuta el cambio climático como hiperobjeto — refuta la capacidad de esta sonda particular para detectarlo en esta resolución. La honestidad de reportar EDI=0.010 para el caso más emblemático es la mejor demostración del rigor del instrumento.

---

## 5. Nivel 0 — Sin Señal Operativa (13 Casos)

Casos donde la constricción macro no mejora (o empeora) la predicción del ABM:

| ID | Caso | EDI | Interpretación operativa |
|----|------|----:|:---|
| 02 | Conciencia | -0.024 | Fallback sintético, sin ground truth físico (LoE=1) |
| 03 | Contaminación PM2.5 | -0.000 | Sin señal macro detectable |
| 04 | Energía | -0.003 | Señal nula |
| 05 | Epidemiología | 0.000 | SEIR no capturada por el framework |
| 10 | Justicia | 0.000 | Sin señal — dominio normativo, no físico |
| 12 | Paradigmas | 0.000 | Señal nula — dominio cultural |
| 15 | Wikipedia | 0.000 | Sin estructura macro detectable |
| 19 | Acidificación Oceánica | -0.000 | Proxy inadecuado |
| 20 | Kessler | -0.420 | Anti-emergencia con datos CelesTrak |
| 22 | Fósforo | -1.000 | Anti-emergencia severa |
| 23 | Erosión Dialéctica | -1.000 | Anti-emergencia severa |
| 25 | Acuíferos | -0.179 | Señal no capturada |
| 26 | Starlink | -1.000 | Colapso del modelo |

Los casos con EDI fuertemente negativo (Fósforo, Erosión, Starlink) indican que el acoplamiento macro *destruye* información útil del ABM — un resultado que confirma la selectividad del instrumento. Bajo irrealismo operativo, Nivel 0 no afirma "no existe" — afirma "no detectado por este instrumento con esta sonda".

---

## 6. Controles de Falsación (3/3 Correctos)
Sistemas diseñados para probar la selectividad del protocolo C1-C5:

| ID | Caso | Propósito | EDI | Estado |
|----|------|-----------|----:|:---|
| 06 | **Exogeneidad** | Probar respuesta ante ruido puro | 0.055 | ❌ Rechazado ✓ |
| 07 | **No-estacionariedad** | Probar respuesta ante Random Walk | -1.000 | ❌ Rechazado ✓ |
| 08 | **Observabilidad** | Probar respuesta ante estados ocultos | -1.000 | ❌ Rechazado ✓ |

Los tres controles son correctamente rechazados con categoría `falsification`, confirmando que el instrumento no es un rubber-stamp.

---

## 7. Casos Removidos (Archivo)
Descartados por falta de fuentes de datos reales verificables:
- **Estética Global:** Inviabilidad de API pública de subastas de arte.
- **Moderación Adversarial:** Opacidad de datos de plataformas (Big Tech).
- **RTB Publicidad:** Datos propietarios protegidos por NDAs de industria.

Archivados en `Artifacts/casos_removidos/`.

---

## Conclusión: El Paisaje como Resultado

El resultado principal no es "2/29 pasan" — es un **paisaje completo** de 29 fenómenos clasificados en un gradiente de cierre operativo:

- **Cierre fuerte** donde hay inercia material (deforestación, microplásticos)
- **Componente funcional** donde hay inercia demográfica (fuga de cerebros)
- **Señal sugestiva** donde hay datos pero resolución insuficiente (finanzas, océanos, IoT)
- **Tendencia** donde la sonda no tiene suficiente potencia (clima, movilidad, etc.)
- **Sin señal** donde la sonda es inadecuada o el fenómeno no exhibe cierre (13 casos)
- **Falsificación correcta** donde los controles funcionan (3 casos)

La selectividad del instrumento (rechazo del 92.3% de casos genuinos para Nivel 4) es la garantía de que las clasificaciones positivas representan cierre operativo genuino, no artefactos de modelado. Bajo irrealismo operativo, cada caso es un dato en el mapa — ninguno es un "fracaso". El mapa completo, con sus 13 ceros y sus 2 fuertes, es más informativo que un resultado inflado donde "todo pasa".
