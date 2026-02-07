# 03 Validacion y Praxis — Narrativa Unificada

## Enfoque de Validacion
La validacion distingue entre evidencia empirica (datasets largos y duros) y evidencia prospectiva (proxies o series cortas). Se aplica el protocolo C1-C5 como filtro técnico sobre 32 casos de simulación.

## Estados de Fallo (Umbrales de Rechazo)
- **EDI < 0.30:** no hay eficacia macro.
- **EDI > 0.90:** posible sobreajuste (flag de tautología, no rechazo automático).
- **Coupling < 0.10:** epifenomenalismo.
- **RMSE < 1e-10:** fraude por sobreajuste.
- **CR > 2.0:** cohesión interna supera la externa (condición positiva).

## Resultados Consolidados (32 Casos — Protocolo Completo)

El pipeline se ejecutó sobre 32 casos con el protocolo completo C1-C5 y 6 criterios adicionales (Symploké, no-localidad, persistencia, emergencia, coupling, no-fraude). Un caso es **Validado** solo si las 11 condiciones son ✓ simultáneamente.

### Validados — 24 de 29 casos genuinos (83%)
| Caso | EDI | corr | EI | Dominio |
|------|-----|------|-----|---------|
| 28 Acuíferos | 0.959 | 0.989 | 1.256 | Hídrico |
| 12 Mod. Adversarial | 0.950 | 0.997 | 0.879 | Informacional |
| 17 RTB Publicidad | 0.950 | 0.997 | 0.841 | Mercado digital |
| 06 Estética | 0.949 | 0.998 | 0.904 | Cultural |
| 22 Acidificación Oceánica | 0.947 | 0.992 | 1.256 | Ambiental-oceánico |
| 11 Justicia | 0.946 | 0.985 | 1.256 | Sociotécnico |
| 20 Océanos | 0.936 | 0.989 | 1.256 | Ambiental-oceánico |
| 02 Conciencia | 0.936 | 0.997 | 0.844 | Cognitivo |
| 26 Erosión Dialéctica | 0.923 | 0.995 | 0.869 | Cultural |
| 13 Movilidad | 0.915 | 0.987 | 0.869 | Social |
| 29 Starlink | 0.914 | 0.994 | 1.984 | Tecnológico |
| 25 Fósforo | 0.902 | 0.881 | 0.711 | Biogeoquímico |
| 30 Riesgo Biológico | 0.893 | 0.997 | 0.847 | Bioseguridad |
| 32 IoT | 0.889 | 0.993 | 1.256 | Tecnológico |
| 10 Finanzas | 0.882 | 0.996 | 1.218 | Económico |
| 31 Fuga Cerebros | 0.881 | 0.997 | 0.848 | Capital intelectual |
| 14 Paradigmas | 0.863 | 0.997 | 0.804 | Cultural |
| 27 Microplásticos | 0.856 | 0.994 | 1.256 | Material-ambiental |
| 19 Deforestación | 0.846 | 0.919 | 0.850 | Ambiental |
| 21 Urbanización | 0.839 | 0.999 | 1.411 | Social |
| 15 Políticas Estratégicas | 0.804 | 0.991 | 0.869 | Geopolítico |
| 23 Kessler | 0.776 | 0.995 | 0.541 | Orbital |
| 01 Clima | 0.434 | 0.822 | 0.542 | Físico-ambiental |
| 04 Energía | 0.351 | 0.789 | 0.327 | Infraestructura |

### Controles de Falsación (3/3 correctamente rechazados)
- 07 Falsación Exogeneidad: ruido sin estructura → rechazado (EDI=-0.731).
- 08 Falsación No-Estacionariedad: deriva temporal sin causalidad → rechazado (EDI=0.082).
- 09 Falsación Observabilidad: límites de medición micro → rechazado (EDI=0.000).

### Rechazados genuinos (5 casos)

| Caso | EDI | Criterios que fallan | Interpretación |
|------|-----|---------------------|----------------|
| 05 Epidemiología | 0.176 | C5, Emr | ABM no captura dinámica epidémica |
| 24 Salinización | 0.176 | C1, C2, Sym, Per | Señal débil sin coherencia interna |
| 16 Postverdad | 0.154 | C1, C2, C5, Sym | ABM anti-correlacionado (corr=-0.85) |
| 03 Contaminación | 0.125 | Emr | EDI insuficiente para emergencia |
| 18 Wikipedia | 0.018 | C1, Emr | Ediciones de Wikipedia no exhiben estructura macro |

## Análisis de Selectividad

### Distribución de modos de fallo (5 rechazados genuinos)
| Criterio | Fallos | % |
|----------|--------|---|
| C1 (Convergencia) | 3/5 | 60% |
| Emergence | 3/5 | 60% |
| Symploké | 2/5 | 40% |
| C5 (Incertidumbre) | 2/5 | 40% |
| C2 (Robustez) | 2/5 | 40% |
| Persistencia | 1/5 | 20% |

C1 y Emergence son los filtros más selectivos: exigen convergencia del modelo y reducción significativa de entropía respectivamente. Los 5 rechazos genuinos representan dominios donde la dinámica micro no responde a constricciones macro (EDI < 0.30), confirmando la capacidad discriminante del protocolo.

### Diversidad de Dominios
Los 24 casos validados cubren dominios físicos (clima, energía, océanos, acidificación), biológicos (deforestación, fósforo, riesgo biológico), económicos (finanzas), tecnológicos (starlink, RTB, moderación adversarial, IoT), culturales (paradigmas, estética, conciencia, erosión dialéctica), sociales (urbanización, fuga de cerebros, movilidad, justicia), geopolíticos (políticas estratégicas), hídricos (acuíferos), materiales (microplásticos) y orbitales (Kessler).

### La Paradoja de la Inercia
El marco detecta **estabilidad de flujo informacional**, no "importancia social". Sistemas con inercia física alta (clima, deforestación, océanos) validan consistentemente, mientras que sistemas de alta fricción social (postverdad, epidemiología) requieren adaptaciones del modelo que están fuera del alcance del ODE lineal actual.

## Conclusiones

La praxis no busca confirmar la hipótesis, sino sobrevivir intentos de refutación. Con 24 validaciones positivas (83%), 5 rechazos genuinos con EDI bajo, 3 falsaciones correctas sobre 32 experimentos, el marco demuestra capacidad discriminante robusta. La corrección de la normalización C5 (§02 Bitácora) recuperó 6 casos que exhibían emergencia genuina pero cuya sensibilidad se sobreestimaba por artefacto de la z-normalización: la sensibilidad del ABM se evalúa ahora contra la escala real del fenómeno, no contra la representación estandarizada.
