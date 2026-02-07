# 03 Validacion y Praxis — Narrativa Unificada

## Enfoque de Validacion
La validacion distingue entre evidencia empirica (datasets largos y duros) y evidencia prospectiva (proxies o series cortas). Se aplica el protocolo C1-C5 como filtro técnico sobre 32 casos de simulación.

## Estados de Fallo (Umbrales de Rechazo)
- **EDI < 0.30:** no hay eficacia macro.
- **EDI > 0.90:** posible sobreajuste (flag de tautología, no rechazo automático).
- **Coupling < 0.10:** epifenomenalismo.
- **RMSE < 1e-10:** fraude por sobreajuste.
- **CR > 2.0:** cohesión interna supera la externa (condición positiva).

## Resultados Consolidados (32 Casos)

### Validados — 11 de 29 genuinos (38%)
| Caso | EDI | corr | EI | Dominio |
|------|-----|------|-----|---------|
| 01 Clima | 0.425 | 0.822 | 0.542 | Físico-ambiental |
| 04 Energía | 0.351 | 0.789 | 0.327 | Infraestructura |
| 10 Finanzas | 0.880 | 0.996 | 1.218 | Económico |
| 14 Paradigmas | 0.657 | 0.953 | 0.882 | Epistémico |
| 17 RTB Publicidad | 0.426 | 0.755 | 0.464 | Digital |
| 19 Deforestación | 0.846 | 0.919 | 0.850 | Ambiental |
| 21 Urbanización | 0.840 | 0.999 | 1.411 | Social |
| 25 Fósforo | 0.901 | 0.881 | 0.711 | Biogeoquímico |
| 28 Acuíferos | 0.866 | 1.000 | 0.815 | Hídrico |
| 29 Starlink | 0.928 | 0.994 | 1.984 | Tecnológico |
| 31 Fuga Cerebros | 0.433 | 0.970 | 0.631 | Socioeconómico |

### Controles de Falsación (3/3 correctamente rechazados)
- 07 Falsación Exogeneidad: ruido sin estructura → rechazado.
- 08 Falsación No-Estacionariedad: deriva temporal sin causalidad → rechazado.
- 09 Falsación Observabilidad: límites de medición micro → rechazado.

### Parciales (9 casos) — EDI alto pero fallan 1-2 condiciones
Casos con EDI > 0.30 que no superan todas las 11 condiciones del pipeline (C1-C5, Symploké, no-localidad, persistencia, emergencia, acoplamiento).

### Rechazados (9 casos) — Sin estructura macro
EDI < 0.30 o múltiples condiciones no satisfechas. Confirman la capacidad discriminante del marco.

## Análisis Crítico

### Tasa de Validación del 38%
La tasa del 38% es evidencia de rigor, no de debilidad. El marco rechaza más casos de los que acepta, demostrando selectividad genuina. Los 3 controles de falsación refuerzan que los éxitos no son artefactos del código.

### Diversidad de Dominios
Los 11 casos validados cubren 7 dominios distintos: físico-ambiental, infraestructura, económico, epistémico, digital, social, biogeoquímico, hídrico, tecnológico y socioeconómico. Esta diversidad confirma que la emergencia computacional no es un fenómeno restringido a un tipo de sistema.

### La Paradoja de la Inercia
El marco detecta **estabilidad de flujo informacional**, no "importancia social". Sistemas con inercia física alta (clima, deforestación) validan fácilmente, mientras que sistemas de alta fricción social (justicia, postverdad) requieren adaptaciones del modelo que están fuera del alcance del ODE lineal actual.

## Conclusiones

La praxis no busca confirmar la hipótesis, sino sobrevivir intentos de refutación. Con 11 validaciones positivas y 3 falsaciones correctas sobre 32 experimentos, el marco demuestra capacidad discriminante robusta para identificar dominios con estructura macro emergente estable.
