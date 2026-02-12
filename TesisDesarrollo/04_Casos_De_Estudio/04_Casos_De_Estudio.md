# 04 Casos de Estudio (29 Casos)

## Paisaje de Emergencia Operativa
El motor de simulación ha sido ejecutado sobre un universo de **29 casos**, tras la remoción de 3 casos por inviabilidad de datos reales. El protocolo C1-C5 + 6 criterios adicionales actúan como instrumento de **clasificación operativa**, permitiendo mapear el fenómeno en un gradiente de cierre.

Los resultados cuantitativos detallados (EDI, p-valores, CR) y la clasificación técnica definitiva se consolidan exclusivamente en la **Sección 03 Validación y Praxis**. Esta sección provee el contexto cualitativo y la justificación de las fuentes de datos para los casos más relevantes del paisaje.

---

## 1. Casos de Cierre Operativo Fuerte (Nivel 4 — overall_pass=True)

Representan los fenómenos donde el constructo macro es operativamente indispensable para la predicción micro. Nueve casos alcanzan este nivel tras el afinamiento de las herramientas de investigación.

*   **Epidemiología (ID 05):** Datos OWID (COVID-19). El modelo SEIR Kermack-McKendrick captura la dinámica epidémica. EDI=0.129. La constricción macro es operativamente necesaria para predecir la evolución del contagio.
*   **Movilidad (ID 11):** Datos World Bank (Tráfico aéreo). Diagrama Fundamental Macroscópico (MFD) con dinámica Greenshields. EDI=0.128. El patrón de tráfico presenta constricción macro significativa.
*   **Políticas Estratégicas (ID 13):** Datos World Bank (Gasto militar). Inercia Institucional basada en North (1990). EDI=0.288. Las instituciones exhiben constricción macro robusta sobre la dinámica individual.
*   **Postverdad (ID 14):** Modelo SIS de Campo Medio para cascadas de desinformación. EDI=0.325. La dinámica de propagación de desinformación exhibe cierre operativo fuerte.
*   **Wikipedia (ID 15):** Datos Wikimedia. Lotka-Volterra aplicado a la dinámica calidad-controversia. EDI=0.160. La dinámica colaborativa online exhibe constricción macro detectable.
*   **Urbanización (ID 18):** Datos World Bank (Población urbana). Logística con atracción económica y Preferential Attachment. EDI=0.151. Los patrones de urbanización exhiben cierre operativo.
*   **Kessler (ID 20):** Datos CelesTrak (Desechos orbitales). Cascada cuadrática Kessler-Liou. EDI=0.381. La dinámica de debris orbital presenta constricción macro fuerte — la cascada colisional impone un patrón macro irreducible.
*   **Fósforo (ID 22):** Datos World Bank (Uso de fertilizantes). Ciclo biogeoquímico Carpenter. EDI=0.376. El ciclo del fósforo exhibe constricción macro robusta.
*   **Riesgo Biológico (ID 27):** Datos World Bank (Mortalidad). Cascada zoonótica Woolhouse. EDI=0.257. La dinámica One Health exhibe cierre operativo significativo.

### Casos Strong sin overall_pass (falla C2 — Robustez)

*   **Deforestación Global (ID 16):** Datos del World Bank (Área forestal). EDI=0.579 — el segundo EDI más alto del corpus. La ODE de frontera agrícola (von Thünen) captura la inercia del desplazamiento físico de la frontera forestal. Falla C2 (robustez ante perturbación de parámetros), candidato prioritario para investigación futura.
*   **Microplásticos Oceánicos (ID 24):** Datos de OWID (Plastic Production). EDI=0.656 — el EDI más alto del corpus. El modelo Jambeck de acumulación persistente genera una constricción fuerte. Falla C2, indicando sensibilidad a perturbaciones.

---

## 2. Señales Sugestivas (Nivel 2)

Fenómenos donde el instrumento detecta una señal estadísticamente significativa pero de magnitud insuficiente o con criterios técnicos no satisfechos.

*   **Finanzas (ID 09):** Datos de Yahoo Finance (SPY). EDI=0.081. La reflexividad inherente a los mercados (Soros, 1987) dificulta la separación macro/micro. Señal significativa (p=0.000) pero falla C4. CR=2.616 (único caso con CR > 2.0).
*   **Salinización (ID 21):** Datos World Bank (Tierras irrigadas). EDI=0.058. Señal detectable (p=0.004) pero magnitud insuficiente.

---

## 3. Otros Fenómenos del Paisaje (Niveles 0-1)

Incluye el caso paradigmático de **Clima Regional (ID 01)** (datos Meteostat/NOAA, EDI=0.002). Bajo el modelo Budyko-Sellers y la resolución actual, el instrumento no detecta un cierre operativo fuerte. Bajo irrealismo operativo, esto no refuta el fenómeno, sino que diagnostica la insuficiencia de la sonda particular para detectarlo en esta escala regional.

Casos notables en Nivel 1 con EDI nominalmente alto pero sin significancia estadística: **Energía (EDI=0.419, p=0.072)** y **Starlink (EDI=0.837, p=1.000)** — ambos carecen de significancia, indicando señales inestables.

7 casos se sitúan en Nivel 0, indicando que el modelo híbrido no detecta constricción macro o que el acoplamiento es incluso destructivo (anti-emergencia).

---

## 4. Controles de Falsación (3/3 Correctos)
Sistemas diseñados para probar la selectividad del protocolo: **Exogeneidad (06)**, **No-estacionariedad (07)** y **Observabilidad (08)**. Los tres controles son correctamente rechazados (falsification), confirmando que el instrumento no es un "rubber-stamp" y requiere estructura genuina para validar un caso.

---

## 5. Casos Removidos (Archivo)
Descartados por falta de fuentes de datos reales verificables: **Estética Global**, **Moderación Adversarial** y **RTB Publicidad**. Archivados en `Artifacts/casos_removidos/`.

---

## Conclusión: El Paisaje como Resultado Principal
La distribución actual (9 overall_pass, 2 strong sin C2, 2 suggestive, 6 trend, 7 null, 3 falsification) constituye un paisaje rico y discriminante. Los 3 controles de falsación correctamente rechazados garantizan que las clasificaciones positivas representan cierre operativo genuino. El mapa completo constituye el resultado principal de la tesis: un mapeo honesto y riguroso de la eficacia causal en el paisaje de los fenómenos masivamente distribuidos.