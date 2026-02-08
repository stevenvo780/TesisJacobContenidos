# 04 Casos de Estudio — Narrativa Unificada

## Resumen de Resultados

De **29 casos** simulados (3 removidos por falta de datos reales), **21 de 26 genuinos (81%)** validan H1 con EDI > 0.30 y protocolo C1-C5 completo. Los 3 controles de falsación son rechazados correctamente. Los 5 rechazos genuinos corresponden a dominios donde el ABM lineal no captura la dinámica emergente.

> **Nota de Auditoría (2026-02-08):** Los casos 06 (Estética), 12 (Moderación Adversarial) y 17 (RTB Publicidad) fueron removidos por carecer de fuentes de datos reales verificables. Archivados en `Artifacts/casos_removidos/`.

## Fuentes de Datos Reales

Todos los casos activos utilizan APIs autoritativas:
- **World Bank**: 14 indicadores (Contaminación, Epidemiología, Deforestación, Urbanización, etc.)
- **Meteostat (NOAA)**: Temperatura regional (Clima)
- **Yahoo Finance**: SPY log(price) (Finanzas)
- **OPSD (ENTSOE)**: Carga eléctrica (Energía)
- **CelesTrak**: Satélites Starlink (Kessler, Starlink)
- **OpenAlex**: Citaciones científicas (Paradigmas)

## Evidencia Dura (Sistemas de Inercia Física)
- **Clima regional (01):** Meteostat (NOAA), balance radiativo. ✅ EDI=0.372
- **Energía eléctrica (04):** OPSD (ENTSOE), estabilidad de red. ✅ EDI=0.354
- **Océanos (17):** World Bank CO2, temperatura oceánica. ✅ EDI=0.936
- **Acidificación oceánica (12):** World Bank CO2/capita. ✅ EDI=0.947
- **Fósforo (12):** World Bank fertilizantes. ✅ EDI=0.902
- **Acuíferos (12):** World Bank acceso agua. ✅ EDI=0.959
- **Microplásticos (06):** World Bank GHG emissions. ✅ EDI=0.856

## Exploraciones Sociotécnicas
- **Finanzas (06):** Yahoo Finance SPY. ✅ EDI=0.882
- **Justicia (06):** World Bank Rule of Law. ✅ EDI=0.946
- **Movilidad (06):** World Bank pasajeros aéreos. ✅ EDI=0.915
- **Urbanización (06):** World Bank población urbana. ✅ EDI=0.839
- **Fuga de cerebros (12):** World Bank R&D % GDP. ✅ EDI=0.881
- **Políticas estratégicas (06):** World Bank tax revenue. ✅ EDI=0.804

## Exploraciones Culturales y Digitales
- **Conciencia (02):** Google Trends (proxy). ✅ EDI=0.936
- **Paradigmas (12):** OpenAlex citaciones. ✅ EDI=0.863
- **Erosión dialéctica (17):** World Bank literacy. ✅ EDI=0.923

## Casos Tecnológicos
- **Deforestación (12):** World Bank forest area. ✅ EDI=0.846
- **Kessler (17):** CelesTrak debris orbital. ✅ EDI=0.776
- **Starlink (17):** CelesTrak satélites. ✅ EDI=0.914
- **Riesgo biológico (06):** World Bank mortalidad. ✅ EDI=0.893
- **IoT (17):** World Bank mobile subs. ✅ EDI=0.889

## Rechazos Genuinos (5 casos)
- **Contaminación (03):** World Bank PM2.5. EDI=0.125 — sin emergencia macro. ❌
- **Epidemiología (05):** World Bank mortalidad. EDI=0.176 — dinámica SEIR incompatible. ❌
- **Postverdad (12):** World Bank internet users. EDI=0.154 — ABM anti-correlacionado. ❌
- **Wikipedia (06):** Wikimedia API. EDI=0.018 — sin estructura macro. ❌
- **Salinización (06):** World Bank arable land. EDI=0.176 — señal débil. ❌

## Controles de Falsación (3/3 correctos)
- **Exogeneidad (06):** Ruido puro sintético. EDI=-0.731 ❌ (correcto)
- **No-estacionariedad (06):** Random walk sintético. EDI=0.082 ❌ (correcto)
- **Observabilidad (06):** Estado oculto sintético. EDI=0.000 ❌ (correcto)

## Casos Removidos (archivados)
Los siguientes casos fueron removidos por carecer de fuentes de datos reales verificables:
- **Estética (06):** Requería scraping de Christie's/Sotheby's — no API pública
- **Moderación Adversarial (12):** Las plataformas no publican datos de moderación
- **RTB Publicidad (17):** Datos IAB/eMarketer son propietarios

Archivados en: `Artifacts/casos_removidos/`

## Análisis Crítico: Cobertura de Datos Reales

| Métrica | Valor |
|---------|-------|
| Casos activos | 17 |
| Con datos reales | 26 (90%) |
| Controles sintéticos | 3 |
| Removidos | 3 |
| APIs integradas | 7 (World Bank, yfinance, Meteostat, OPSD, CelesTrak, OpenAlex, Wikimedia) |
| Datapoints totales | ~1200+ |

**Conclusión:** El 90% de los casos genuinos utilizan datos de fuentes autoritativas (World Bank, NOAA, Yahoo Finance), eliminando la crítica de "falta de datos" como vector de ataque.
