# Caso 28 — Fuga de Cerebros (Brain Drain)

## Hiperobjeto

La fuga de cerebros global como hiperobjeto: masivamente distribuida
(afecta a todos los países en desarrollo), no-local (la decisión individual
de migrar depende de condiciones globales), viscosa (path dependency
en formación de capital humano) y con la paradoja del brain drain
(Docquier & Rapoport 2012).

## Modelo ODE — Dinámica de Capital Humano

$$\frac{dH}{dt} = \alpha(E - \beta H) + \gamma F - \delta \cdot \max(0, H - \text{threshold})^{1.5} + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.06 | Acumulación capital humano ~6%/año (Barro & Lee 2013) |
| β | 0.02 | Depreciación natural ~2%/año (obsolescencia de skills) |
| γ | 0.08 | Sensibilidad a forcing exógeno (PIB, remesas, inversión) |
| δ | 0.015 | Intensidad brain drain ~1.5% (Docquier & Rapoport 2012) |
| threshold | 1.5 | Umbral H para migración masiva (brain drain paradox) |
| exponente | 1.5 | Sub-cuadrático: aceleración moderada sobre umbral |
| noise_std | 0.01 | Variabilidad baja (I+D es relativamente estable) |
| p₀ | 1.2 | Stock inicial de capital humano |

### Brain Drain Paradox

El término `δ·max(0, H−threshold)^1.5` modela que países con más capital
humano pierden proporcionalmente más por migración (incentivo prospect).
El exponente 1.5 (sub-cuadrático) evita divergencia.

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 25 | 625 celdas (países/regiones) |
| forcing_gradient_type | `random_hubs` | Polos académicos/tecnológicos (Docquier & Rapoport 2012) |
| forcing_gradient_strength | 0.65 | Gradiente fuerte (Beine et al. 2001: >60% migrantes cualificados concentrados) |
| heterogeneity_strength | 0.30 | Alta variabilidad I+D (UNESCO 2021: GERD varía 0.1–4.5% del PIB) |

## Datos Reales

- **Fuente**: World Bank (múltiples indicadores)
  - `GB.XPD.RSDV.GD.ZS` — Gasto en I+D (% del PIB) — **variable objetivo**
  - `SP.POP.SCIE.RD.P6` — Investigadores por millón
  - `SE.TER.ENRR` — Matrícula terciaria bruta
  - `BX.TRF.PWKR.DT.GD.ZS` — Remesas recibidas (% PIB)
  - `NY.GDP.PCAP.KD` — PIB per cápita
  - `SM.POP.NETM` — Migración neta
- **Cobertura**: 1980–2022

## Forcing Sintético

```
F(t) = 0.01·t + 0.002·t^1.1
```

- 0.01·t: tendencia secular (UNESCO 2021: crecimiento matrícula terciaria)
- 0.002·t^1.1: aceleración por globalización (Docquier & Rapoport 2012)

## Resultados

| Fase | EDI | Resultado |
|------|-----|-----------|
| Sintética | 0.491 | PASS ✓ (emergencia fuerte) |
| Real | 0.213 | REJECT (EDI < 0.30) |

**Interpretación**: EDI sintético sólido confirma que el modelo ODE captura
la dinámica brain drain en datos controlados. EDI real bajo (0.213) sugiere
que el indicador I+D/PIB es insuficiente como proxy del fenómeno completo
de fuga de cerebros (necesitaría datos de migración cualificada directos).

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador |
| `abm.py` | Wrapper con gradiente random_hubs |
| `ode.py` | Docquier-Rapoport con brain drain paradox |
| `data.py` | World Bank multi-indicador |

## Correcciones Aplicadas

1. Documentación completa de parámetros ODE con referencias
2. Documentación de parámetros ABM con referencias
3. Documentación de forcing sintético y extra_base_params
