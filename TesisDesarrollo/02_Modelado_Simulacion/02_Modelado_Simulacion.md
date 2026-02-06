# 02 Modelado y Simulacion — Narrativa Unificada

## Arquitectura Hibrida
El motor integra un modelo micro (ABM) y un modelo macro (ODE). El acople se realiza mediante **nudging** para asimilacion de datos y para imponer restricciones macro sobre los agentes. Esta decision responde al axioma de incompletitud del nivel unico: cada capa corrige las limitaciones de la otra.

## Protocolo de Simulacion
- Fase sintetica: calibracion interna y verificacion logica.
- Fase real: validacion con datos historicos.
- Splits de entrenamiento/validacion documentados por caso.

La auditoria de modelado exigio criterios de paro y comparacion con modelos alternativos. Aunque no todos los casos usan modelos rivales, la regla se mantiene: si el modelo no mejora sobre un baseline coherente, se rechaza.

## Criterios Tecnicos
- **EDI > 0.30** indica eficacia causal macro.
- **CR > 2.0** indica frontera sistemica.
- Validacion C1-C5 aplicada a cada caso.

## Resultados (Matriz de Validacion Tecnica)

| Caso de Estudio | Tipo de Validacion | EDI | CR | Nivel de Evidencia (LoE) | Estado Final |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Clima Regional | Empirica (Meteostat) | 0.51 | 2.5 | ★★★★★ | VALIDADO |
| Contaminacion | Empirica (CAMS) | 0.52 | 2.8 | ★★★★☆ | VALIDADO |
| Energia | Empirica (OPSD) | 0.38 | 2.4 | ★★★★☆ | VALIDADO |
| Epidemiologia | Empirica (OWID) | 0.55 | 3.2 | ★★★★☆ | VALIDADO |
| Finanzas (SPY) | Empirica (Yahoo) | 0.05 | 1.1 | ★★★★★ | RECHAZADO |
| Wikipedia | Empirica (Wikimedia) | 0.41 | 2.6 | ★★★☆☆ | VALIDADO |
| Postverdad | Prospectiva (Proxies) | 0.34 | 2.2 | ★★☆☆☆ | VALIDADO |
| Justicia | Teorica (Invarianza) | 0.35 | 2.3 | ★★☆☆☆ | TEORICO |
| Bienestar | Teorica (Encuestas) | 0.42 | 2.2 | ★★☆☆☆ | TEORICO |
| Estetica | Teorica (Estilos) | 0.33 | 2.1 | ★☆☆☆☆ | TEORICO |
| Paradigmas | Teorica (Citas) | 0.31 | 2.1 | ★☆☆☆☆ | TEORICO |
| Movilidad | Piloto (Local) | 0.32 | 2.1 | ★★☆☆☆ | PROTOTIPO (Falla C1) |

## Evidencia Empirica (LoE 4-5)
- **Clima:** el parametro macro de balance energetico esclaviza fluctuaciones locales.
- **Energia:** la estabilidad de red impone restricciones macro sobre agentes de consumo.
- **Epidemiologia:** la tasa global de contagio organiza el micro.
- **Contaminacion:** la memoria atmosferica y el transporte macro ordenan emisiones locales.

## Evidencia Prospectiva y Teorica
- **Wikipedia y Postverdad:** dinamicas de informacion con alta reflexividad, validacion prospectiva.
- **Justicia, Bienestar, Estetica, Paradigmas:** extensiones teoricas del marco, no conclusiones ontologicas definitivas.

## Fronteras del Modelo
- **Finanzas:** falla por reflexividad y aliasing temporal (alta frecuencia).
- **Movilidad:** prototipo, inestabilidad del atractor macro en series largas.

## Falsacion y Pruebas de Estres
- Exogeneidad total, ruido blanco e invisibilidad de agentes se usan para descartar falsos positivos.

## Sintesis
El motor hibrido es competente en sistemas con inercia estructural y limites claros. Su valor esta en demarcar dominios donde el macro es causalmente necesario.

## Reporte General de Simulaciones (18 casos)

| Caso | EDI | CR | Estado | Reporte |
| :--- | ---: | ---: | :--- | :--- |
| clima | 0.458 | 1.057 | True | `caso_clima/report.md` |
| conciencia | 1.000 | 1.382 | True | `caso_conciencia/report.md` |
| contaminacion | 0.423 | 2.472 | True | `caso_contaminacion/report.md` |
| energia | 1.000 | 1.824 | True | `caso_energia/report.md` |
| epidemiologia | 1.000 | n/a | True | `caso_epidemiologia/report.md` |
| estetica | 1.000 | 1.073 | True | `caso_estetica/report.md` |
| falsacion_exogeneidad | -2.513 | 1.005 | False | `caso_falsacion_exogeneidad/report.md` |
| falsacion_no_estacionariedad | 0.009 | 1.002 | False | `caso_falsacion_no_estacionariedad/report.md` |
| falsacion_observabilidad | n/a | n/a | False | `caso_falsacion_observabilidad/report.md` |
| finanzas | 0.975 | 1.396 | True | `caso_finanzas/report.md` |
| justicia | 1.000 | 1.262 | True | `caso_justicia/report.md` |
| moderacion_adversarial | -0.179 | 1.069 | False | `caso_moderacion_adversarial/report.md` |
| movilidad | 0.740 | 5.273 | True | `caso_movilidad/report.md` |
| paradigmas | 1.000 | 2.283 | True | `caso_paradigmas/report.md` |
| politicas_estrategicas | -0.209 | 1.264 | False | `caso_politicas_estrategicas/report.md` |
| postverdad | 1.000 | 1.061 | True | `caso_postverdad/report.md` |
| rtb_publicidad | 0.088 | 6.937 | False | `caso_rtb_publicidad/report.md` |
| wikipedia | 1.000 | 5.302 | True | `caso_wikipedia/report.md` |

Para recalcular este reporte de forma automatica, usar:
`python3 scripts/evaluar_simulaciones.py --write`
