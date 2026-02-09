# Caso 24 — Microplásticos Oceánicos

## Hiperobjeto

Contaminación por microplásticos en los océanos. Paradigma de hiperobjeto
mortoniano: persistencia extrema (t½ ≈ 300–450 años), distribución masiva
(gyres, sedimentos, columna de agua), invisibilidad a escala humana y
retroalimentación con cadenas tróficas (Jambeck et al. 2015; Geyer et al. 2017).

## Modelo ODE — Jambeck Persistent Accumulation

$$\frac{dM}{dt} = \alpha(F - \beta M) - \text{burial} \cdot M + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.09 | Input desde tierra ~9% del flujo plástico llega al océano (Jambeck et al. 2015, Science) |
| β | 0.003 | Degradación fotoquímica/mecánica ~0.3%/año (Ward et al. 2019: t½ ≈ 300–450 años para PE/PP) |
| burial | 0.002 | Sedimentación marina ~0.2%/año (Woodall et al. 2014: microplásticos en sedimentos profundos) |
| noise_std | 0.025 | Variabilidad estocástica |
| p₀ | 0.0 | Estado inicial normalizado |

### Persistencia Extrema

La combinación β=0.003 + burial=0.002 implica una remoción total de apenas
0.5%/año, haciendo que la acumulación sea cuasi-irreversible en escalas humanas.

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 20 | Estándar |
| forcing_gradient_type | `random_hubs` | Desembocaduras de ríos y zonas costeras industriales |
| forcing_gradient_strength | 0.70 | Gradiente muy fuerte (Lebreton et al. 2017: 15 ríos → 80% input oceánico) |
| heterogeneity_strength | 0.30 | Alta variabilidad (Cózar et al. 2014: concentración varía en órdenes de magnitud) |
| forcing_scale | 0.10 | Sensibilidad ABM a driver externo |
| macro_coupling | 0.25 | Acoplamiento macro→micro |
| driver_cols | `["mismanaged_waste", "river_discharge"]` | Drivers externos |

## Datos Reales

- **Fuente primaria**: OWID Grapher (producción plástica global)
- **Fuente secundaria**: World Bank (indicadores de residuos sólidos)
- **Proxy**: Producción plástica + residuos mal gestionados + caudal fluvial
- **Fallback**: Serie sintética si APIs fallan

## Forcing Sintético

```
F(t) = 0.010·t + 0.0003·t^1.2
```

- 0.010·t: tendencia secular ~1%/año (Geyer et al. 2017: producción plástica crece ~8.4%/año acumulado)
- 0.0003·t^1.2: aceleración por economías emergentes (Jambeck 2015)

## Resultados

| Fase | EDI | Resultado |
|------|-----|-----------|
| Sintética | 0.679 | PASS ✓ (emergencia fuerte) |
| Real | 0.586 | PASS ✓ (emergencia sostenida) |

**Interpretación**: Microplásticos muestra EDI positivo y robusto en ambas fases,
confirmando que la ODE macro (acumulación persistente) reduce significativamente
el error del ABM. La persistencia extrema (β + burial ≈ 0.5%/año de remoción)
genera un atractor macroscópico genuino. Este caso valida la hipótesis del
hiperobjeto: la acumulación global de microplásticos constituye una estructura
emergente irreducible a los agentes individuales.

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador |
| `abm.py` | Wrapper con gradiente random_hubs |
| `ode.py` | Jambeck persistent accumulation con burial |
| `data.py` | OWID + World Bank + fallback sintético |

## Correcciones Aplicadas

1. `import random` → `np.random.default_rng(seed)` (reproducibilidad NumPy)
2. `metrics.py` eliminado (código muerto)
3. `data.py.bak` eliminado (backup residual)
4. Todos los parámetros numéricos documentados con referencias
