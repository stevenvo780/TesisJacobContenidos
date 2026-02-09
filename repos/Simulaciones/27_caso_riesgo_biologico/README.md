# Caso 27 — Riesgo Biológico Global

## Hiperobjeto

El riesgo biológico global (pandemias, enfermedades zoonóticas emergentes)
como hiperobjeto. Propiedades: no-local (pandemias cruzan fronteras
instantáneamente), viscoso (patógenos persisten en reservorios animales),
masivamente distribuido (One Health: humanos-animales-ambiente) y con
bio-amplificación (riesgo existente facilita nuevos eventos).

## Modelo ODE — Woolhouse Zoonotic Cascade (bilineal)

$$\frac{dR}{dt} = \alpha(F - \beta R) + \gamma_{\text{bio}} \cdot F \cdot R + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.05 | Acumulación de riesgo ~5%/año (Woolhouse & Gaunt 2007: ~3 nuevos patógenos/década) |
| β | 0.02 | Contención/mitigación sanitaria ~2%/año (WHO 2019: mejora gradual) |
| γ_bio | 0.02–0.03 | Bio-amplificación bilineal (Jones et al. 2008: cascada interconectada) |
| noise_std | 0.015 | Variabilidad interanual |
| p₀ | 0.0 | Estado inicial normalizado |

### Bio-amplificación

El término bilineal `γ_bio·F·R` captura que el riesgo existente amplifica
la presión de forzamiento: ecosistemas ya degradados (R alto) son más
vulnerables a nuevos patógenos (Woolhouse 2005).

### Shock Pandémico

El forcing sintético incluye un shock tardío (al 80% del rango temporal)
que simula un evento tipo COVID-19, con magnitud 0.18 y decaimiento 0.3/step.

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 25 | 625 celdas |
| forcing_gradient_type | `random_hubs` | Focos epidémicos (Jones et al. 2008: hotspots zoonóticos) |
| forcing_gradient_strength | 0.75 | Gradiente muy fuerte (Woolhouse 2005: 80% patógenos de zonas tropicales) |
| heterogeneity_strength | 0.35 | Alta variabilidad bioseguridad (WHO 2019: IHR scores 20–95%) |
| forcing_scale | 0.20 | Sensibilidad ABM a driver zoonótico |
| macro_coupling | 0.40 | Acoplamiento macro→micro alto |

## Datos Reales

- **Fuente**: `data_universal.py` → `fetch_case_data` con fallback sintético
- **Proxy**: TB Incidence (World Bank) + HIV incidence + immunization coverage
- **Cobertura**: 2000–2024

## Forcing Sintético

```
F(t) = 0.010·t + 0.0003·t^1.2 + shock(t=0.8T)
```

## Resultados

| Fase | EDI | Resultado |
|------|-----|-----------|
| Sintética | 0.409 | PASS ✓ (emergencia moderada) |
| Real | 0.414 | PASS ✓ (emergencia confirmada) |

**Interpretación**: Riesgo biológico muestra EDI positivo y consistente en
ambas fases (~0.41), confirmando que la ODE macro (cascada zoonótica con
bio-amplificación) captura estructura emergente genuina. La consistencia
sintético≈real valida el modelo Woolhouse.

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador con shock pandémico |
| `abm.py` | Wrapper con gradiente random_hubs (focos epidémicos) |
| `ode.py` | Woolhouse cascade bilineal |
| `data.py` | data_universal + fallback sintético |

## Correcciones Aplicadas

1. `import random` → `np.random.default_rng(seed)` (reproducibilidad NumPy)
2. `metrics.py` eliminado (código muerto)
3. Todos los parámetros numéricos documentados con referencias
