# Caso 25 — Depleción de Acuíferos

## Hiperobjeto

Sobreexplotación global de acuíferos. Los acuíferos son hiperobjetos
mortonianos: masivamente distribuidos, con inercia temporal enorme (recarga
en escalas de décadas-siglos), invisibles (subterráneos) y con subsidencia
irreversible por debajo de umbrales críticos (Konikow & Kendy 2005).

## Modelo ODE — Balance Hídrico Darcy-Theis

$$\frac{dH}{dt} = \alpha(F - \beta H) - \frac{\text{extraction} \cdot H}{|H| + 1} + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.08 | Recarga neta ~8%/año (Horton infiltration; Scanlon et al. 2006: 0.1–30% de precipitación) |
| β | 0.03 | Descarga natural + evapotranspiración ~3%/año (De Marsily 2004) |
| extraction | 0.01 | Bombeo antrópico con saturación logística (Konikow & Kendy 2005: ~1% del stock/año) |
| noise_std | 0.02 | Variabilidad interanual |
| p₀ | 0.0 | Estado inicial normalizado |

### Saturación de Extracción

El término `extraction·H/(|H|+1)` modela que el bombeo se autoregula: cuando
el nivel freático H es bajo, el rendimiento del pozo disminuye (Theis 1935).

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 25 | 625 celdas espaciales |
| forcing_gradient_type | `radial` | Recarga desde bordes (flujo lateral Darcy; De Marsily 2004) |
| forcing_gradient_strength | 0.60 | Gradiente moderado-alto (Scanlon et al. 2006) |
| heterogeneity_strength | 0.25 | Variabilidad geológica (permeabilidad; Freeze & Cherry 1979) |
| forcing_scale | 0.12 | Sensibilidad ABM a precipitación |
| macro_coupling | 0.28 | Acoplamiento macro→micro |

## Datos Reales

- **Fuente primaria**: GRACE (Gravity Recovery and Climate Experiment) — groundwater storage
- **Fuente secundaria**: World Bank + USGS groundwater withdrawals
- **Proxy**: Precipitación + extracción (indicadores WB)
- **Fallback**: Serie sintética

## Forcing Sintético

```
F(t) = 0.008·t + 0.0003·t^1.2
```

- 0.008·t: tendencia secular ~0.8%/año (Scanlon et al. 2006)
- 0.0003·t^1.2: aceleración por cambio climático (IPCC AR6)

## Resultados

| Fase | EDI | Resultado |
|------|-----|-----------|
| Sintética | 0.405 | PASS ✓ (emergencia moderada) |
| Real | −0.272 | REJECT |

**Interpretación**: El EDI sintético positivo confirma que la ODE captura
estructura macro en datos controlados. El EDI real negativo refleja que los
proxies hidrológicos disponibles (WB) no capturan adecuadamente la dinámica
subterránea real (necesitaría datos GRACE directos).

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador |
| `abm.py` | Wrapper con gradiente radial (flujo lateral Darcy) |
| `ode.py` | Darcy-Theis con extracción saturada |
| `data.py` | GRACE + World Bank + USGS + fallback |

## Correcciones Aplicadas

1. `import random` → `np.random.default_rng(seed)` (reproducibilidad NumPy)
2. `metrics.py` eliminado (código muerto)
3. `data.py.bak` eliminado (backup residual)
4. Todos los parámetros numéricos documentados con referencias
