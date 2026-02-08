# Indice Maestro de la Tesis (Desarrollo)

Lectura recomendada en orden:

1. 00 Marco Conceptual — Narrativa Unificada: `00_Marco_Conceptual/00_00_Marco_Conceptual.md`
2. 01 Metodologia de Medicion — Narrativa Unificada: `01_Metodologia_Medicion/01_00_Metodologia_Medicion.md`
3. 02 Modelado y Simulacion — Narrativa Unificada: `02_Modelado_Simulacion/02_Modelado_Simulacion.md`
4. 03 Validacion y Praxis — Narrativa Unificada: `03_Validacion_Praxis/03_Validacion_Praxis.md`
5. 04 Casos de Estudio — Narrativa Unificada: `04_Casos_De_Estudio/04_Casos_De_Estudio.md`
6. Anexos (auditorias, ejercicios criticos, documentacion): `Anexos.md`
7. Ejercicios Criticos (Gladiadores, Partida 1):
   - `EjersiciosCriticos/Ejercicio_Critico_Gladiadores_Partida1.md`
   - `EjersiciosCriticos/Trazas_Mejoras_Possibles_Dudas.md`

Documentos de referencia:
- Resumen general del repositorio: `README.md`
- Tesis final: `../TesisFinal/Tesis.md`

---

## Lista Completa de Casos (29 casos oficiales)

### Bloque I: Validados (EDI > 0.30 + C1-C5)
01. `01_caso_clima/` — Clima regional (Meteostat)
02. `02_caso_conciencia/` — Conciencia global (Proxy Trends)
04. `04_caso_energia/` — Energía eléctrica (ENTSOE)
09. `09_caso_finanzas/` — Finanzas globales (Yahoo Finance)
10. `10_caso_justicia/` — Estado de Derecho (World Bank)
11. `11_caso_movilidad/` — Tráfico aéreo (World Bank)
12. `12_caso_paradigmas/` — Ciencia y citaciones (OpenAlex)
13. `13_caso_politicas_estrategicas/` — Recaudación fiscal (World Bank)
16. `16_caso_deforestacion/` — Área forestal (World Bank)
17. `17_caso_oceanos/` — Temperatura oceánica (World Bank)
18. `18_caso_urbanizacion/` — Población urbana (World Bank)
19. `19_caso_acidificacion_oceanica/` — CO2 y Océanos (World Bank)
20. `20_caso_kessler/` — Desechos orbitales (CelesTrak)
22. `22_caso_fosforo/` — Uso de fertilizantes (World Bank)
23. `23_caso_erosion_dialectica/` — Alfabetización (World Bank)
24. `24_caso_microplasticos/` — Emisiones GHG (World Bank)
25. `25_caso_acuiferos/` — Acceso al agua (World Bank)
26. `26_caso_starlink/` — Mega-constelaciones (CelesTrak)
27. `27_caso_riesgo_biologico/` — Mortalidad (World Bank)
28. `28_caso_fuga_cerebros/` — I+D (World Bank)
29. `29_caso_iot/` — Suscripciones móviles (World Bank)

### Bloque II: Rechazados Genuinos (EDI < 0.30)
03. `03_caso_contaminacion/` — PM2.5 (Sin emergencia macro)
05. `05_caso_epidemiologia/` — Mortalidad (Dinámica SEIR incompatible)
14. `14_caso_postverdad/` — Usuarios Internet (Sin estructura macro)
15. `15_caso_wikipedia/` — Ediciones Wiki (Sin reducción de entropía)
21. `21_caso_salinizacion/` — Tierras cultivables (Señal débil)

### Bloque III: Controles de Falsación (Sintéticos)
06. `06_caso_falsacion_exogeneidad/` — Ruido puro
07. `07_caso_falsacion_no_estacionariedad/` — Random Walk
08. `08_caso_falsacion_observabilidad/` — Estado oculto

> **Nota de Auditoría:** Los casos Estética (antiguo 06), Moderación (antiguo 12) y RTB (antiguo 17) fueron removidos por inviabilidad de datos reales.
