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

### Validados — 11 de 29 casos genuinos (38%)
| Caso | EDI | corr | EI | Dominio |
|------|-----|------|-----|---------|
| 01 Clima | 0.425 | 0.822 | 0.542 | Físico-ambiental |
| 04 Energía | 0.351 | 0.789 | 0.327 | Infraestructura |
| 10 Finanzas | 0.880 | 0.996 | 1.218 | Económico |
| 14 Paradigmas | 0.656 | 0.953 | 0.882 | Cultural |
| 17 RTB Publicidad | 0.426 | 0.755 | 0.464 | Mercado digital |
| 19 Deforestación | 0.846 | 0.919 | 0.850 | Ambiental |
| 21 Urbanización | 0.840 | 0.999 | 1.411 | Social |
| 25 Fósforo | 0.901 | 0.881 | 0.711 | Biogeoquímico |
| 28 Acuíferos | 0.866 | 1.000 | 0.815 | Hídrico |
| 29 Starlink | 0.928 | 0.994 | 1.984 | Tecnológico |
| 31 Fuga Cerebros | 0.433 | 0.970 | 0.631 | Capital intelectual |

### Controles de Falsación (3/3 correctamente rechazados)
- 07 Falsación Exogeneidad: ruido sin estructura → rechazado.
- 08 Falsación No-Estacionariedad: deriva temporal sin causalidad → rechazado.
- 09 Falsación Observabilidad: límites de medición micro → rechazado.

### Rechazados con EDI alto — Prueba de no-tautología
8 casos tienen EDI > 0.30 pero son rechazados por fallar criterios adicionales del protocolo:

| Caso | EDI | Criterios que fallan | Interpretación |
|------|-----|---------------------|----------------|
| 30 Riesgo Biológico | 0.917 | Sym, Per | Señal macro fuerte pero sin coherencia topológica |
| 26 Erosión Dialéctica | 0.739 | C1, Per | Tendencia global pero convergencia insuficiente |
| 20 Océanos | 0.737 | C1 | EDI alto pero ABM no converge |
| 22 Acidificación | 0.737 | C1 | Estructura macro pero calibración insuficiente |
| 23 Kessler | 0.704 | C1 | Shock COVID-19 destruye convergencia |
| 32 IoT | 0.477 | C1 | ABM no alcanza RMSE suficiente |
| 27 Microplásticos | 0.432 | C5, Sym | Coherencia topológica insuficiente |
| 16 Postverdad | 0.310 | C1 | EDI marginal, señal macro débil |

### Rechazados con EDI bajo (10 casos)
Conciencia (-0.323), Contaminación (0.124), Epidemiología (0.172), Estética (0.032), Justicia (-0.237), Moderación (0.004), Movilidad (0.070), Wikipedia (0.017), Salinización (0.164), Políticas (0.294).

## Análisis de Selectividad

### Distribución de modos de fallo (18 rechazados genuinos)
| Criterio | Fallos | % |
|----------|--------|---|
| C1 (Convergencia) | 14/18 | 78% |
| Emergence | 7/18 | 39% |
| Symploké | 7/18 | 39% |
| Persistencia | 3/18 | 17% |
| C5 (Incertidumbre) | 2/18 | 11% |
| C2 (Robustez) | 1/18 | 6% |

C1 es el filtro más selectivo: exige que el RMSE del modelo acoplado sea menor que la desviación estándar de las observaciones en escala Z-normalizada. Esto es equivalente al criterio NC1 (RMSE/obs_std < 1.0) propuesto en la literatura.

### Diversidad de Dominios
Los 11 casos validados cubren dominios físicos (clima, acuíferos), biológicos (deforestación, fósforo), económicos (finanzas, energía), tecnológicos (starlink, RTB), culturales (paradigmas) y sociales (urbanización, fuga de cerebros).

### La Paradoja de la Inercia
El marco detecta **estabilidad de flujo informacional**, no "importancia social". Sistemas con inercia física alta (clima, deforestación) validan fácilmente, mientras que sistemas de alta fricción social (justicia, postverdad) requieren adaptaciones del modelo que están fuera del alcance del ODE lineal actual.

## Conclusiones

La praxis no busca confirmar la hipótesis, sino sobrevivir intentos de refutación. Con 11 validaciones positivas, 8 rechazos de alto EDI (prueba de no-tautología), 3 falsaciones correctas y 10 rechazos genuinos sobre 32 experimentos, el marco demuestra capacidad discriminante robusta: un EDI alto no garantiza validación — el protocolo C1-C5 actúa como filtro multi-criterio que elimina falsos positivos.
