# Caso 26 — Constelaciones Satelitales (Starlink)

## Hiperobjeto

Las mega-constelaciones satelitales como estructura emergente que modifica
irreversiblemente el entorno orbital. Propiedades de hiperobjeto: masivamente
distribuido (miles de objetos en LEO), no-local (afecta observaciones
astronómicas globales), viscoso (debris persiste décadas) y con transición
de fase Kessler (Kessler & Cour-Palais 1978).

## Modelo ODE — Dinámica Orbital Kessler-Lewis

$$\frac{dN}{dt} = \alpha(F - \beta N) - \text{saturation} \cdot N \cdot |N| + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.18 | Tasa lanzamiento alta ~18%/año (Lewis et al. 2011: mega-constelaciones) |
| β | 0.015 | Desorbitado controlado ~1.5%/año (vida útil ~5 años; SpaceX 2020) |
| saturation | 0.002 | Saturación orbital cuadrática (Kessler 1978: colisión ∝ N²) |
| noise_std | 0.02 | Variabilidad estocástica |
| p₀ | 0.0 | Estado inicial normalizado |

### Transición de Fase

El término cuadrático `saturation·N·|N|` captura la cascada de Kessler:
cuando N supera un umbral crítico, las colisiones generan más debris del
que se retira, creando un feedback positivo incontrolable.

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 25 | 625 celdas (regiones orbitales) |
| forcing_gradient_type | `radial` | Shells orbitales con densidad variable (Lewis 2011) |
| forcing_gradient_strength | 0.65 | Gradiente fuerte (Liou 2006: densidad varía >10x entre altitudes) |
| heterogeneity_strength | 0.20 | Variabilidad moderada entre planos orbitales |
| forcing_scale | 0.12 | Sensibilidad ABM a lanzamientos |
| macro_coupling | 0.28 | Acoplamiento macro→micro |

## Datos Reales

- **Fuente**: CelesTrak SATCAT (catálogo satelital)
- **Filtro**: Objetos con nombre "STARLINK"
- **Complemento**: CelesTrak debris timeseries
- **Cobertura**: 2018–2023

## Forcing Sintético

```
F(t) = 0.012·t + 0.0004·t^1.3
```

- 0.012·t: tendencia secular (SpaceX 2020: ~60 lanzamientos/año)
- 0.0004·t^1.3: aceleración por competencia multi-operador

## Resultados

| Fase | EDI | CR | Resultado |
|------|-----|----|-----------|
| Sintética | 0.564 | 1.006 | C1=False (emergencia moderada) |
| Real | −546.587 | ∞ | REJECT |

**Interpretación**: EDI sintético sólido (0.564), pero EDI real catastrófico.
La serie Starlink real es extremadamente corta (2019-2023) y con crecimiento
casi perfectamente lineal, lo que hace que el ABM-solo funcione mejor que
la combinación ABM+ODE. Caso donde la serie temporal es demasiado corta
para detectar estructura emergente.

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador |
| `abm.py` | Wrapper con gradiente radial (shells orbitales) |
| `ode.py` | Kessler-Lewis con saturación cuadrática |
| `data.py` | CelesTrak SATCAT (Starlink + debris) |

## Correcciones Aplicadas

1. `import random` → `np.random.default_rng(seed)` (reproducibilidad NumPy)
2. `metrics.py` eliminado (código muerto)
3. Todos los parámetros numéricos documentados con referencias
