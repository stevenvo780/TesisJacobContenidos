# Indice Maestro de la Tesis (Desarrollo)

Lectura recomendada en orden:

1. 00 Marco Conceptual: `00_Marco_Conceptual/00_00_Marco_Conceptual.md`
2. 01 Metodologia de Medicion: `01_Metodologia_Medicion/01_00_Metodologia_Medicion.md`
3. 02 Modelado y Simulacion: `02_Modelado_Simulacion/02_Modelado_Simulacion.md`
4. 03 Validacion y Praxis: `03_Validacion_Praxis/03_Validacion_Praxis.md`
5. 04 Casos de Estudio: `04_Casos_De_Estudio/04_Casos_De_Estudio.md`
6. 05 Bibliografía Nuclear: `05_Bibliografia/05_Bibliografia.md`
7. Anexos (auditorias, ejercicios criticos, documentacion): `Anexos.md`
8. Ejercicios Criticos (Gladiadores, Partida 1):
   - `EjerciciosCriticos/Ejercicio_Critico_Gladiadores_Partida1.md`
   - `EjerciciosCriticos/Trazas_Mejoras_Possibles_Dudas.md`

Documentos de referencia:
- Resumen general del repositorio: `README.md`
- Tesis final: `../TesisFinal/Tesis.md`

---

## Lista Completa de Casos (29 casos oficiales)

> **Estado actual:** overall_pass = 5/29 (Energía, Deforestación, Urbanización, Fósforo, Microplásticos). Significancia: 14/29. El paisaje completo de 29 puntos (Niveles 0-4) es el resultado principal bajo irrealismo operativo.

### Bloque I: Emergencia fuerte (strong) — overall_pass=True
04. `04_caso_energia/` — Energía eléctrica (OPSD) — EDI=0.650 — **Validado**
16. `16_caso_deforestacion/` — Área forestal (World Bank) — EDI=0.580 — **Validado**
18. `18_caso_urbanizacion/` — Población urbana (World Bank) — EDI=0.337 — **Validado**
22. `22_caso_fosforo/` — Uso de fertilizantes (World Bank) — EDI=0.322 — **Validado**
24. `24_caso_microplasticos/` — Producción plástica (OWID) — EDI=0.806 — **Validado**

### Bloque II: Componente funcional (weak) — p<0.05, 0.10≤EDI<0.30
05. `05_caso_epidemiologia/` — COVID-19 (OWID) — EDI=0.129 — Weak
11. `11_caso_movilidad/` — Tráfico aéreo (World Bank) — EDI=0.128 — Weak
13. `13_caso_politicas_estrategicas/` — Gasto militar (World Bank) — EDI=0.288 — Weak
14. `14_caso_postverdad/` — SIS Desinformación — EDI=0.252 — Weak
20. `20_caso_kessler/` — Desechos orbitales (CelesTrak) — EDI=0.299 — Weak
27. `27_caso_riesgo_biologico/` — Mortalidad (World Bank) — EDI=0.294 — Weak

### Bloque III: Señal sugestiva (suggestive) — p<0.05, EDI>0.01
09. `09_caso_finanzas/` — Finanzas globales (Yahoo Finance) — EDI=0.081
15. `15_caso_wikipedia/` — Ediciones Wiki (Wikimedia) — EDI=0.080
21. `21_caso_salinizacion/` — Tierras irrigadas (World Bank) — EDI=0.058

### Bloque IV: Tendencia no significativa (trend)
01. `01_caso_clima/` — Clima regional (Meteostat) — EDI=0.011
10. `10_caso_justicia/` — Estado de Derecho (World Bank) — EDI=0.227
26. `26_caso_starlink/` — Mega-constelaciones (CelesTrak) — EDI=0.690
28. `28_caso_fuga_cerebros/` — I+D (World Bank) — EDI=0.025

### Bloque V: Sin evidencia (null)
02. `02_caso_conciencia/` — Conciencia global (Fallback) — EDI=-0.116
03. `03_caso_contaminacion/` — PM2.5 (AQICN) — EDI=-0.004
12. `12_caso_paradigmas/` — Ciencia (OpenAlex) — EDI=-0.006
17. `17_caso_oceanos/` — Temperatura oceánica (WMO proxy) — EDI=-0.043
19. `19_caso_acidificacion_oceanica/` — CO2 y Océanos (PMEL proxy) — EDI=-0.000
23. `23_caso_erosion_dialectica/` — Alfabetización (World Bank) — EDI=-1.000
25. `25_caso_acuiferos/` — Acceso al agua (GRAVIS+USGS) — EDI=-0.020
29. `29_caso_iot/` — Suscripciones móviles (World Bank) — EDI=-0.899

### Bloque VI: Controles de Falsación (Correctamente rechazados)
06. `06_caso_falsacion_exogeneidad/` — Ruido puro — EDI=0.055
07. `07_caso_falsacion_no_estacionariedad/` — Random Walk — EDI=-0.882
08. `08_caso_falsacion_observabilidad/` — Estado oculto — EDI=-1.000

> **Nota:** Los casos Estética (antiguo 06), Moderación (antiguo 12) y RTB (antiguo 17) fueron removidos por inviabilidad de datos reales.
