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

> **Estado actual (2026-02-09):** overall_pass = 0/29. H1 no confirmada bajo criterios estrictos.

### Bloque I: Señal parcial (EDI_real > 0)
24. `24_caso_microplasticos/` — Producción plástica (OWID) — EDI_real=0.586
27. `27_caso_riesgo_biologico/` — Mortalidad (World Bank) — EDI_real=0.414
28. `28_caso_fuga_cerebros/` — I+D (World Bank) — EDI_real=0.213
17. `17_caso_oceanos/` — Temperatura oceánica (WMO proxy) — EDI_real=0.119
09. `09_caso_finanzas/` — Finanzas globales (Yahoo Finance) — EDI_real=0.051
29. `29_caso_iot/` — Suscripciones móviles (World Bank) — EDI_real=0.014
11. `11_caso_movilidad/` — Tráfico aéreo (World Bank) — EDI_real=0.003
14. `14_caso_postverdad/` — Fallback sintético — EDI_real=0.003

### Bloque II: Sin emergencia (EDI_real ≤ 0)
01. `01_caso_clima/` — Clima regional (Meteostat) — EDI_real=-0.299
02. `02_caso_conciencia/` — Conciencia global (Fallback) — EDI_real=-0.063
03. `03_caso_contaminacion/` — PM2.5 (AQICN) — EDI_real=-0.000
04. `04_caso_energia/` — Energía eléctrica (OPSD) — EDI_real=-0.005
05. `05_caso_epidemiologia/` — COVID-19 (OWID) — EDI_real=0.000
10. `10_caso_justicia/` — Estado de Derecho (World Bank) — EDI_real=0.000
12. `12_caso_paradigmas/` — Ciencia (OpenAlex) — EDI_real=-0.000
13. `13_caso_politicas_estrategicas/` — Gasto militar (World Bank) — EDI_real=-0.022
15. `15_caso_wikipedia/` — Ediciones Wiki (Wikimedia) — EDI_real=0.000
16. `16_caso_deforestacion/` — Área forestal (World Bank) — EDI_real=-1.001
18. `18_caso_urbanizacion/` — Población urbana (World Bank) — EDI_real=0.000
19. `19_caso_acidificacion_oceanica/` — CO2 y Océanos (PMEL proxy) — EDI_real=-0.002
20. `20_caso_kessler/` — Desechos orbitales (CelesTrak) — EDI_real=-3.419
21. `21_caso_salinizacion/` — Tierras irrigadas (World Bank) — EDI_real=-1.378
22. `22_caso_fosforo/` — Uso de fertilizantes (World Bank) — EDI_real=-4.269
23. `23_caso_erosion_dialectica/` — Alfabetización (World Bank) — EDI_real=-9.084
25. `25_caso_acuiferos/` — Acceso al agua (GRAVIS+USGS) — EDI_real=-0.272
26. `26_caso_starlink/` — Mega-constelaciones (CelesTrak) — EDI_real=-546.587

### Bloque III: Controles de Falsación (Correctamente rechazados)
06. `06_caso_falsacion_exogeneidad/` — Ruido puro — EDI=-0.615
07. `07_caso_falsacion_no_estacionariedad/` — Random Walk — EDI=-7.837
08. `08_caso_falsacion_observabilidad/` — Estado oculto — EDI=-3.771

> **Nota de Auditoría:** Los casos Estética (antiguo 06), Moderación (antiguo 12) y RTB (antiguo 17) fueron removidos por inviabilidad de datos reales.
