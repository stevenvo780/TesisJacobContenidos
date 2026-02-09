# Caso 22 — Ciclo del Fósforo

## Hiperobjeto

Acumulación global de fósforo reactivo en ecosistemas acuáticos y terrestres.
El fósforo antropogénico (fertilizantes, detergentes) se acumula de forma
prácticamente irreversible en sedimentos, generando eutrofización a escala
planetaria (Carpenter 2005; Cordell et al. 2009).

## Modelo ODE — Carpenter Biogeochemical P Cycle

Ecuación diferencial con término bilineal que captura la retroalimentación
concentración×runoff:

$$\frac{dP}{dt} = \alpha(F - \beta P) + \gamma \cdot F \cdot P + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.07 | Input fertilizantes ~7%/año (Cordell et al. 2009) |
| β | 0.02 | Sedimentación irreversible ~2%/año (Carpenter 2005) |
| γ | 0.015–0.02 | Amplificación bilineal runoff×concentración (Carpenter & Bennett 2011) |
| noise_std | 0.018 | Variabilidad interanual |
| p₀ | 0.0 | Estado inicial normalizado |

### Assimilation

Asimilación de datos con lag temporal (`_apply_assimilation`), desactivada
durante evaluación (`assimilation_strength=0.0`).

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 20 | Estándar (malla espacial) |
| forcing_gradient_type | `random_hubs` | Polos agrícolas de fertilización intensiva |
| forcing_gradient_strength | 0.60 | Gradiente moderado-alto (zonas de riego vs. secano; Carpenter 2005) |
| heterogeneity_strength | 0.25 | Variabilidad en prácticas de fertilización (FAO/FAOSTAT) |
| forcing_scale | 0.10 | Sensibilidad ABM a driver externo |
| macro_coupling | 0.40 | Acoplamiento macro→micro alto |

## Datos Reales

- **Fuente**: World Bank — `AG.CON.FERT.ZS` (Fertilizer consumption, kg/ha)
- **Cobertura**: 1960–2022, serie mundial (`WLD`)
- **Resolución**: Anual

## Forcing Sintético

```
F(t) = 0.012·t + 0.0004·t^1.3
```

- 0.012·t: tendencia secular ~1.2%/año (Cordell et al. 2009: crecimiento demanda P)
- 0.0004·t^1.3: aceleración por intensificación agrícola (FAO 2020)

## Resultados

| Fase | EDI | CR | Resultado |
|------|-----|----|-----------|
| Sintética | 0.386 | 1.006 | C1=True |
| Real | −4.269 | 1.003 | C1=False |

**Interpretación**: El EDI sintético positivo (0.386) indica que la ODE captura
estructura macro. Sin embargo, el EDI real fuertemente negativo señala que los
datos del World Bank no presentan la dinámica bilineal esperada a escala global
(los datos agregados mundiales lisan la heterogeneidad espacial que el ABM
intenta capturar).

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador: calibra → simula → evalúa → escribe outputs |
| `abm.py` | Wrapper sobre `abm_core.py` con gradiente random_hubs |
| `ode.py` | Carpenter P cycle con término bilineal γ·F·P |
| `data.py` | World Bank API (AG.CON.FERT.ZS) |

## Correcciones Aplicadas

1. `import random` → `np.random.default_rng(seed)` (reproducibilidad NumPy)
2. `metrics.py` eliminado (código muerto; hybrid_validator maneja métricas)
3. Documentación de todos los parámetros numéricos con referencias
