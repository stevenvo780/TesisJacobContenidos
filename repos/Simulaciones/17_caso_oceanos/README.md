# Caso 17 — Océanos (Stommel + Termohalina)

## Propósito

Evaluar si el océano global —como sistema termohalino— exhibe propiedades
de hiperobjeto: no-localidad (corrientes redistribuyen calor globalmente),
viscosidad temporal (inercia térmica de décadas), y causalidad descendente
de la «circulación termohalina» sobre parcelas oceánicas locales.

---

## Modelos

### ODE — Modelo de Caja de Stommel (1961)

$$\frac{dT}{dt} = \eta_1^{\text{eff}} - T - |q| \cdot T$$
$$\frac{dS}{dt} = \eta_2 - S - |q| \cdot S$$
$$q = T - S$$

Modelo clásico de dos cajas (ecuador–polo) con flujo termohalino $q$.
Exhibe bistabilidad: régimen térmico (AMOC activa) vs. halino (AMOC colapsada).

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\eta_1$ | 3.0 | Forzamiento térmico (Stommel 1961, Tellus 13:224; Rahmstorf 1996) |
| $\eta_2$ | 1.0 | Forzamiento halino (Stommel 1961) |
| $\eta_1/\eta_2$ | 3.0 | Ratio que produce régimen bistable con saddle-node |
| `dt` | 0.1 | Paso de integración (adimensional Stommel) |
| `ode_noise` | 0.01 | Fluctuaciones estocásticas |
| Factor modulación | 0.5 | Sensibilidad climática: ~mitad del forcing→gradiente T (Cessi 1994) |
| Clip T | [0.1, 10] | Régimen físico (adimensional) |
| Clip S | [0.1, 5] | Régimen físico (adimensional) |

**OHC proxy:** $\text{OHC}_{t+1} = \text{OHC}_t + 0.01 \cdot T + \varepsilon$
(integración temporal; Levitus et al. 2012)

### ABM — Circulación Termohalina en Grilla

Agentes = parcelas oceánicas en grilla 2D con campos de temperatura $T$ y
salinidad $S$. Dinámica: difusión calórica, convección vertical,
forzamiento atmosférico.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `grid_size` | 15 | Grilla 15×15 = 225 celdas |
| `abm_diffusion` | 0.1 | Coef. difusión calórica (Stewart 2008, Oceanography) |
| `abm_convection` | 0.5 | Umbral inestabilidad convectiva (densidad) |
| T inicial | 25 − 2·|lat| °C | Gradiente ecuatorial→polar (Stewart 2008) |
| S inicial | 35.0 ± 0.5 psu | Media oceánica global (TEOS-10; Durack & Wijffels 2010) |
| $\alpha_T$ (densidad) | 0.1 | Expansión térmica escalada (Gill 1982) |
| $\beta_S$ (densidad) | 0.8 | Contracción halina escalada (Gill 1982) |
| $\beta_S / \alpha_T$ | 8.0 | Dominancia halina en alta latitud |
| Heat flux factor | 0.1 | Fracción forcing→capa mezcla (~100m; Trenberth 2009) |

### Datos reales

CSV local: `data/dataset.csv` (OHC proxy vía World Bank).

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | 0.110 | Acoplamiento macro débil |
| Real | 0.119 | Acoplamiento macro débil |

## Correcciones

- `DEBUG` print eliminado de `validate.py`
- Docstring erróneo en `data.py` corregido ("Fossil fuel" → "Ocean Heat Content")
- `data.py.bak` eliminado
- `metrics.py` eliminado (código muerto)
- Todos los números mágicos documentados con referencias

## Referencias

- Stommel, H. (1961). Thermohaline convection with two stable regimes of flow. *Tellus*, 13(2), 224–230.
- Cessi, P. (1994). A simple box model of stochastically forced thermohaline flow. *JPO*, 24(8), 1911–1920.
- Rahmstorf, S. (1996). On the freshwater forcing and transport of the Atlantic thermohaline circulation. *Climate Dynamics*, 12, 799–811.
- Rahmstorf, S. (2002). Ocean circulation and climate during the past 120,000 years. *Nature*, 419, 207–214.
- Levitus, S. et al. (2012). World ocean heat content and thermosteric sea level change. *GRL*, 39, L10603.
- Gill, A. E. (1982). *Atmosphere-Ocean Dynamics*. Academic Press.
- Trenberth, K. E. (2009). An imperative for climate change planning. *Climate Change*, 96, 263–268.
- Stewart, R. H. (2008). *Introduction to Physical Oceanography*. Texas A&M.
- Durack, P. J. & Wijffels, S. E. (2010). Fifty-year trends in global ocean salinities. *J. Climate*, 23, 4342–4362.
