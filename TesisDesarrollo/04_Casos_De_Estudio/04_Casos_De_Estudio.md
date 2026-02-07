# 04 Casos de Estudio — Narrativa Unificada

## Resumen de Resultados

De 32 casos simulados, 24 de 29 genuinos (83%) validan H1 con EDI > 0.30 y protocolo C1-C5 completo. Los 3 controles de falsación son rechazados correctamente. Los 5 rechazos genuinos corresponden a dominios donde el ABM lineal no captura la dinámica emergente.

## Evidencia Dura (Sistemas de Inercia Física)
- **Clima regional (01):** Acople ODE de balance radiativo con ABM local. ✅ EDI=0.372, forcing_scale=0.99
- **Energía eléctrica (04):** Estabilidad de red como restricción macro. ✅ EDI=0.351
- **Océanos (20):** Temperatura oceánica y acoplamiento climático. ✅ EDI=0.936
- **Acidificación oceánica (22):** Ciclo carbónico y pH oceánico. ✅ EDI=0.947
- **Fósforo (25):** Ciclo biogeoquímico del fósforo. ✅ EDI=0.902
- **Acuíferos (28):** Estrés hídrico y acceso al agua. ✅ EDI=0.959
- **Microplásticos (27):** Contaminación material persistente. ✅ EDI=0.856

## Exploraciones Sociotécnicas
- **Finanzas (10):** Mercados financieros como hiperobjeto económico. ✅ EDI=0.882
- **Justicia (11):** Invarianza normativa (Rule of Law, World Bank). ✅ EDI=0.946
- **Movilidad (13):** Patrones urbanos de transporte. ✅ EDI=0.915
- **Urbanización (21):** Expansión urbana como atractor macro. ✅ EDI=0.839
- **Fuga de cerebros (31):** Migración de talento e inversión en I+D. ✅ EDI=0.881
- **Políticas estratégicas (15):** Impacto geopolítico macro. ✅ EDI=0.804

## Exploraciones Culturales y Digitales
- **Conciencia (02):** Sincronización colectiva. ✅ EDI=0.936
- **Estética (06):** Inercia de cánones artísticos. ✅ EDI=0.949
- **Paradigmas (14):** Cambios de fase en citación científica. ✅ EDI=0.863
- **Erosión dialéctica (26):** Tasas de alfabetización. ✅ EDI=0.923
- **Moderación adversarial (12):** Conflicto en plataformas digitales. ✅ EDI=0.950
- **RTB Publicidad (17):** Mercados publicitarios digitales. ✅ EDI=0.950

## Casos Tecnológicos
- **Deforestación (19):** Pérdida forestal como parámetro de orden. ✅ EDI=0.846
- **Kessler (23):** Debris orbital (síndrome de Kessler). ✅ EDI=0.776
- **Starlink (29):** Difusión de internet satelital. ✅ EDI=0.914
- **Riesgo biológico (30):** Mortalidad infantil como indicador sistémico. ✅ EDI=0.893
- **IoT (32):** Conectividad global (suscripciones móviles). ✅ EDI=0.889

## Rechazos Genuinos (5 casos)
- **Contaminación (03):** EDI=0.125 — sin emergencia macro detectable. ❌
- **Epidemiología (05):** EDI=0.176 — dinámica SEIR incompatible con ABM lineal. ❌
- **Postverdad (16):** EDI=0.154 — ABM anti-correlacionado (corr=-0.85). ❌
- **Wikipedia (18):** EDI=0.018 — sin estructura macro en ediciones. ❌
- **Salinización (24):** EDI=0.176 — señal débil sin coherencia interna. ❌

## Controles de Falsación (3/3 correctos)
- **Exogeneidad (07):** EDI=-0.731 — ruido puro sin estructura. ❌ (correcto)
- **No-estacionariedad (08):** EDI=0.082 — deriva temporal sin causalidad. ❌ (correcto)
- **Observabilidad (09):** EDI=0.000 — límites de medición micro. ❌ (correcto)

### Análisis Crítico: La Paradoja de la Inercia (Estética vs. Justicia)
Aunque todos los casos cuentan con motores de simulación implementados y ejecutables en `repos/Simulaciones/`, su peso en la argumentación central varía según su Nivel de Evidencia (LoE 1-5). El análisis comparativo de estos modelos revela un sesgo fundamental del algoritmo hacia la **Inercia Informacional**:
*   **Estética (Inercia Alta):** Los cánones artísticos preservan el pasado con alta fidelidad, creando series temporales "suaves" que el modelo interpreta como orden macro fuerte.
*   **Justicia (Fricción Alta):** El sistema legal, aunque estructurado, es procesalmente volátil. El modelo penaliza esta fricción como "ruido", subestimando su realidad ontológica.
*   **Conclusión:** Un EDI bajo en sistemas sociales no necesariamente implica inexistencia, sino una dinámica de cambio que el enfoque ODE actual no captura plenamente. El marco detecta **estabilidad de flujo informacional**, no "importancia social".
