# 04 Casos de Estudio — Narrativa Unificada (29 Casos)

## Resumen de Validación
El motor de simulación ha sido ejecutado sobre un universo de **29 casos**, tras la remoción de 3 casos por inviabilidad de datos reales. El protocolo C1-C5 actuó como filtro de demarcación ontológica.

| Categoría | Casos | Resultado |
|-----------|-------|-----------|
| **Validados (H1 ✓)** | 21 | Emergencia detectada (EDI > 0.30) |
| **Rechazos Genuinos** | 5 | Estructura macro débil (EDI < 0.30) |
| **Controles de Falsación** | 3 | Rechazados correctamente (Sintéticos) |

---

## 1. Bloque de Validación (21 Casos Genuinos)
Estos casos superaron el umbral de **EDI > 0.30** y el protocolo de 11 criterios simultáneos.

| ID | Caso | Fuente de Datos | EDI (Medio) | Estado |
|----|------|-----------------|-------------|--------|
| 01 | **Clima Regional** | Meteostat (NOAA) | 0.372 | ✅ Validado |
| 02 | **Conciencia Colectiva** | Google Trends (Proxy) | 0.936 | ✅ Validado |
| 04 | **Energía Eléctrica** | OPSD (ENTSOE) | 0.354 | ✅ Validado |
| 09 | **Finanzas (SPY)** | Yahoo Finance | 0.882 | ✅ Validado |
| 10 | **Justicia (Rule of Law)** | World Bank | 0.946 | ✅ Validado |
| 11 | **Movilidad Aérea** | World Bank | 0.915 | ✅ Validado |
| 12 | **Paradigmas Científicos** | OpenAlex | 0.863 | ✅ Validado |
| 13 | **Políticas Estratégicas** | World Bank | 0.804 | ✅ Validado |
| 16 | **Deforestación** | World Bank | 0.846 | ✅ Validado |
| 17 | **Océanos** | World Bank | 0.936 | ✅ Validado |
| 18 | **Urbanización** | World Bank | 0.839 | ✅ Validado |
| 19 | **Acidificación Oceánica** | World Bank | 0.947 | ✅ Validado |
| 20 | **Síndrome de Kessler** | CelesTrak | 0.776 | ✅ Validado |
| 22 | **Ciclo del Fósforo** | World Bank | 0.902 | ✅ Validado |
| 23 | **Erosión Dialéctica** | World Bank | 0.923 | ✅ Validado |
| 24 | **Microplásticos** | World Bank | 0.856 | ✅ Validado |
| 25 | **Acuíferos** | World Bank | 0.959 | ✅ Validado |
| 26 | **Starlink** | CelesTrak | 0.914 | ✅ Validado |
| 27 | **Riesgo Biológico** | World Bank | 0.893 | ✅ Validado |
| 28 | **Fuga de Cerebros** | World Bank | 0.881 | ✅ Validado |
| 29 | **Ecosistema IoT** | World Bank | 0.889 | ✅ Validado |

---

## 2. Bloque de Rechazos Genuinos (5 Casos)
Casos donde la dinámica micro (ABM) no colapsa en una estructura macro efectiva (EDI bajo).

| ID | Caso | Razón del Rechazo | EDI |
|----|------|-------------------|-----|
| 03 | **Contaminación PM2.5** | Dispersión local dominante; sin constricción macro. | 0.125 |
| 05 | **Epidemiología** | Dinámica SEIR estocástica no capturada por ODE lineal. | 0.176 |
| 14 | **Postverdad** | ABM anti-correlacionado con la tendencia macro. | 0.154 |
| 15 | **Wikipedia** | Ruido de ediciones sin reducción de entropía sistémica. | 0.018 |
| 21 | **Salinización** | Señal de datos reales muy débil/ruidosa. | 0.176 |

---

## 3. Bloque de Falsación (3 Controles)
Sistemas sintéticos diseñados para probar la selectividad del protocolo C1-C5.

| ID | Caso | Propósito | EDI | Estado |
|----|------|-----------|-----|--------|
| 06 | **Exogeneidad** | Probar respuesta ante ruido puro. | -0.731 | ❌ Rechazado |
| 07 | **No-estacionariedad** | Probar respuesta ante Random Walk. | 0.082 | ❌ Rechazado |
| 08 | **Observabilidad** | Probar respuesta ante estados ocultos. | 0.000 | ❌ Rechazado |

---

## 4. Casos Removidos (Archivo)
Estos casos fueron descartados por falta de fuentes de datos reales verificables que permitieran el cierre de la fase `real` del protocolo C1-C5.
- **Estética Global:** Inviabilidad de API pública de subastas de arte.
- **Moderación Adversarial:** Opacidad de datos de plataformas (Big Tech).
- **RTB Publicidad:** Datos propietarios protegidos por NDAs de industria.

Archivados en `Artifacts/casos_removidos/`.

---
**Conclusión:** La validación de 21 de 26 casos genuinos (81%) demuestra que el fenómeno del Hiperobjeto es una propiedad estructural recurrente en sistemas complejos masivamente distribuidos, siempre que exista una constricción macro efectiva (EDI > 0.30).