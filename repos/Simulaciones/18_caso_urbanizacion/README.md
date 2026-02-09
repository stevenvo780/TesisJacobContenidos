# Caso 18 — Urbanización Global (Bettencourt + Preferential Attachment)

## Propósito

Evaluar si el sistema urbano global exhibe propiedades de hiperobjeto:
no-localidad (ciudades conectadas por comercio, migración, ideas),
viscosidad temporal (infraestructura persiste siglos), y causalidad
descendente del «sistema urbano» sobre decisiones individuales de
migración.

---

## Modelos

### ODE — Urbanización Logística + Atracción Económica

$$\frac{dU}{dt} = r \cdot U \cdot \left(1 - \frac{U}{K}\right) + \gamma \cdot \text{GDP} \cdot (1 - U) + \varepsilon$$

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $r$ | 0.05 | Tasa de crecimiento urbano (~5%/año pico; UN WUP 2018: Asia 1960-80) |
| $K$ | 0.9 | Capacidad de carga ~90% (Japón 92%, UK 84%; UN WUP 2018) |
| $\gamma$ | 2.0 | Factor pull económico (Henderson 2003, JEG: elasticidad 1.5–3.0, mediana) |
| `ode_noise` | 0.005 | Variabilidad anual |
| `dt` | 1.0 | Paso temporal = 1 año |
| Clip U | [0.05, 0.99] | Régimen físico (no 0% ni 100% urbano) |

### ABM — Preferential Attachment / Simon-Yule

Agentes = ciudades con población; migrantes se asignan proporcionalmente
al tamaño (rich-get-richer / Zipf's Law).

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `n_initial_cities` | 10 | Ciudades iniciales |
| `abm_new_city_prob` | 0.02 | ~2%/año de emergencia de nuevos clusters (Rozenfeld et al. 2008, PNAS) |
| `abm_migration_rate` | 0.05 | ~5% rural migra/año (UN WUP 2018: tasa media 1-5%) |
| `abm_beta` | 1.15 | Exponente superlineal (Bettencourt 2007, PNAS: GDP~N^1.15) |
| Factor 5·f_t | 5.0 | Elasticidad migración-GDP (Henderson 2003: 3-7, punto medio) |
| `grid_size` | 20 | Grilla 20×20 para histograma de distribución de tamaños |
| Rural mínimo | 100 | Evita extinción de población rural |
| Cap migrantes/step | 1000 | Eficiencia computacional |

### Datos reales

World Bank: `data/wb_urbanization.csv` (% población urbana), 1960–2023.

### Datos sintéticos

Curva logística de urbanización calibrada a UN WUP:
$$S(t) = \frac{K}{1 + e^{-r(t - t_0)}}$$
con $K=0.9$, $r=0.08$, $t_0=\text{midpoint}$. Exponente Zipf 1.1 y
Bettencourt $\beta=1.15$ para complejidad urbana.

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | 0.000 | Sin estructura macro |
| Real | 0.000 | Sin estructura macro |

## Correcciones

- `DEBUG` print eliminado de `validate.py`
- `metrics.py` eliminado (código muerto)
- Todos los números mágicos documentados con referencias

## Referencias

- Bettencourt, L. M. A. et al. (2007). Growth, innovation, scaling, and the pace of life in cities. *PNAS*, 104(17), 7301–7306.
- Henderson, V. (2003). The urbanization process and economic growth. *J. Economic Geography*, 3(4), 275–303.
- UN (2018). *World Urbanization Prospects: The 2018 Revision*. UN DESA.
- Rozenfeld, H. D. et al. (2008). Laws of population growth. *PNAS*, 105(48), 18702–18707.
- Simon, H. A. (1955). On a class of skew distribution functions. *Biometrika*, 42, 425–440.
- Gabaix, X. (1999). Zipf's Law for cities: An explanation. *QJE*, 114(3), 739–767.
- Barabási, A.-L. & Albert, R. (1999). Emergence of scaling in random networks. *Science*, 286(5439), 509–512.
- Zipf, G. K. (1949). *Human Behavior and the Principle of Least Effort*.
