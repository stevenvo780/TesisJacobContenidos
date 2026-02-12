# 04 Casos de Estudio: El Emergentómetro en Acción

Un instrumento de medición se valida por su capacidad de discriminar. Un termómetro que siempre marca 37°C es inútil. El Emergentómetro se aplicó a **29 fenómenos de dominios radicalmente distintos** — desde la física de debris orbital (Kessler) hasta la dinámica de postverdad en redes sociales — y produjo un gradiente amplio: desde EDI=-1.000 (sin señal, Erosión Dialéctica) hasta EDI=0.806 (señal muy fuerte, Microplásticos). Esta diversidad de resultados es la mejor evidencia de que el instrumento no está diseñado para "confirmar" hiperobjetos, sino para medirlos sin sesgos.

## Paisaje de Emergencia Operativa
El motor de simulación ha sido ejecutado sobre un universo de **29 casos**, tras la remoción de 3 casos por inviabilidad de datos reales. El protocolo C1-C5 + 8 criterios adicionales actúan como instrumento de **clasificación operativa**, permitiendo mapear el fenómeno en un gradiente de cierre.

Los resultados cuantitativos detallados (EDI, p-valores, CR) y la clasificación técnica definitiva se consolidan exclusivamente en la **Sección 03 Validación y Praxis**. Esta sección provee el contexto cualitativo y la justificación de las fuentes de datos para los casos más relevantes del paisaje.

---

## 1. Casos de Cierre Operativo Fuerte (Nivel 4 — overall_pass=True)

Representan los fenómenos donde el constructo macro es operativamente indispensable para la predicción micro. Cinco casos alcanzan este nivel con EDI ≥ 0.30 y las 13 condiciones simultáneas satisfechas.

*   **Microplásticos Oceánicos (ID 24):** Datos de OWID (Plastic Production). EDI=0.806 — el EDI más alto del corpus entre los overall_pass=True. El modelo Jambeck de acumulación persistente genera una constricción fuerte. BC=bias_only.
*   **Energía (ID 04):** Datos OPSD (producción energética). Modelo Lotka-Volterra de competencia energética con adopción tecnológica tipo TIMES. EDI=0.650. La constricción macro es fuertemente indispensable. BC=bias_only.
*   **Deforestación Global (ID 16):** Datos del World Bank (Área forestal). EDI=0.580. La ODE de frontera agrícola (von Thünen) captura la inercia del desplazamiento físico de la frontera forestal. BC=full.
*   **Urbanización (ID 18):** Datos World Bank (Población urbana). Logística con atracción económica y Preferential Attachment. EDI=0.337. Los patrones de urbanización exhiben cierre operativo. BC=full.
*   **Fósforo (ID 22):** Datos World Bank (Uso de fertilizantes). Ciclo biogeoquímico Carpenter. EDI=0.322. El ciclo del fósforo exhibe constricción macro robusta. BC=full.

---

## 2. Componentes Funcionales (Nivel 3 — weak)

Fenómenos con señal estadísticamente significativa y EDI entre 0.10-0.30 pero que no alcanzan overall_pass=True.

*   **Kessler (ID 20):** Datos CelesTrak (Desechos orbitales). Cascada cuadrática Kessler-Liou. EDI=0.299, p=0.000. La dinámica de debris orbital presenta constricción macro fuerte, marginalmente sub-umbral (0.30).
*   **Riesgo Biológico (ID 27):** Datos World Bank (Mortalidad). Cascada zoonótica Woolhouse. EDI=0.294, p=0.003. La dinámica One Health exhibe señal significativa sub-umbral.
*   **Políticas Estratégicas (ID 13):** Datos World Bank (Gasto militar). Inercia Institucional basada en North (1990). EDI=0.289, p=0.000. Las instituciones exhiben constricción macro significativa sub-umbral.
*   **Postverdad (ID 14):** Modelo SIS de Campo Medio para cascadas de desinformación. EDI=0.252, p=0.000. Señal significativa pero sub-umbral para cierre pleno.
*   **Epidemiología (ID 05):** Datos OWID (COVID-19). SEIR Kermack-McKendrick. EDI=0.129, p=0.000. Señal significativa pero sub-umbral para cierre operativo pleno.
*   **Movilidad (ID 11):** Datos World Bank (Tráfico aéreo). MFD con dinámica Greenshields. EDI=0.128, p=0.002. Constricción detectable pero insuficiente para overall_pass.

---

## 3. Señales Sugestivas (Nivel 2)

Fenómenos donde el instrumento detecta una señal estadísticamente significativa pero de magnitud insuficiente o con criterios técnicos no satisfechos.

*   **Finanzas (ID 09):** Datos de Yahoo Finance (SPY). EDI=0.081. La reflexividad inherente a los mercados (Soros, 1987) dificulta la separación macro/micro. Señal significativa (p=0.000) pero falla C4. CR=2.616 (único caso con CR > 2.0).
*   **Wikipedia (ID 15):** Datos Wikimedia. Lotka-Volterra aplicado a la dinámica calidad-controversia. EDI=0.080, p=0.000. Señal significativa pero EDI por debajo del umbral de componente funcional.
*   **Salinización (ID 21):** Datos World Bank (Tierras irrigadas). EDI=0.058. Señal detectable (p=0.004) pero magnitud insuficiente.

---

## 4. Otros Fenómenos del Paisaje (Niveles 0-1)

Incluye el caso paradigmático de **Clima Regional (ID 01)** (datos Meteostat/NOAA, EDI=0.011). Bajo el modelo Budyko-Sellers y la resolución actual, el instrumento no detecta un cierre operativo fuerte. Bajo irrealismo operativo, esto no refuta el fenómeno, sino que diagnostica la insuficiencia de la sonda particular para detectarlo en esta escala regional.

Caso notable en Nivel 1 con EDI nominalmente alto pero sin significancia estadística: **Starlink (EDI=0.690, p=1.000)** — carece de significancia, indicando señal artefactual.

8 casos se sitúan en Nivel 0, incluyendo Conciencia (EDI=-0.117), indicando que el modelo híbrido no detecta constricción macro o que el acoplamiento es incluso destructivo (anti-emergencia).

---

## 5. Controles de Falsación (3/3 Correctos)
Sistemas diseñados para probar la selectividad del protocolo: **Exogeneidad (06)**, **No-estacionariedad (07)** y **Observabilidad (08)**. Los tres controles son correctamente rechazados (falsification), confirmando que el instrumento no es un "rubber-stamp" y requiere estructura genuina para validar un caso.

---

## 6. Casos Removidos (Archivo)
Descartados por falta de fuentes de datos reales verificables: **Estética Global**, **Moderación Adversarial** y **RTB Publicidad**. Archivados en `Artifacts/casos_removidos/`.

---

## Conclusión: El Paisaje como Resultado Principal
La distribución actual (5 overall_pass, 6 weak, 3 suggestive, 4 trend, 8 null, 3 falsification) constituye un paisaje rico y discriminante. Los 3 controles de falsación correctamente rechazados garantizan que las clasificaciones positivas representan cierre operativo genuino. El mapa completo constituye el resultado principal de la tesis: un mapeo honesto y riguroso de la eficacia causal en el paisaje de los fenómenos masivamente distribuidos.