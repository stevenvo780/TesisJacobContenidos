# Caso 16 — Deforestación Global (von Thünen Frontier)

## Propósito

Evaluar si la deforestación tropical global exhibe propiedades de
hiperobjeto: no-localidad (frontera de deforestación migratoria),
viscosidad temporal (irreversibilidad a escalas humanas), y causalidad
descendente del «frente de deforestación» sobre parcelas locales.

---

## Modelos

### ODE — Accumulation-Decay (Acumulación con Regeneración)

$$\frac{dD}{dt} = \text{inflow} \cdot F(t) - \text{decay} \cdot D + \varepsilon$$

Modelo de balance: la deforestación acumulada crece con el forcing
(presión agrícola) y se reduce lentamente por regeneración natural.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `ode_inflow` | 0.06 | ≈6%/año de conversión en frentes activos (Hansen et al. 2013, Science) |
| `ode_decay` | 0.008 | ≈0.8%/año de regeneración natural (Chazdon et al. 2016, Science) |
| `ode_noise` | 0.04 | Variabilidad interanual (sequías, políticas) |

**Forcing sintético:**
$$F(t) = 0.025\,t + 0.0005\,t^{1.3}$$

- Componente lineal: tendencia secular de expansión agrícola (FAO 2020)
- Componente super-lineal: retroalimentación tala→carreteras→más tala
  (Laurance et al. 2002, Science: fish-bone pattern)

### ABM — Grid con Gradiente Radial (abm_core.py)

Celdas representan parcelas forestales. La deforestación avanza desde la
periferia (modelo de von Thünen 1826: land rent decreasing from center).

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `grid_size` | 25 | Grilla 25×25 = 625 parcelas |
| `forcing_gradient_type` | `"radial"` | Avance desde periferia (von Thünen 1826) |
| `forcing_gradient_strength` | 0.65 | Gradiente fuerte centro→periferia (Laurance 2002) |
| `heterogeneity_strength` | 0.30 | Alta variabilidad regional (Hansen 2013: CV observado) |
| `forcing_scale` | 0.10 | Sensibilidad ABM a driver externo |
| `macro_coupling` | 0.25 | Acoplamiento macro→micro |

### Datos reales

World Bank API: indicador `AG.LND.FRST.ZS` (% superficie forestal), 1990–2022.
Cache local: `data/wb_deforestation.csv`.

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | −3.715 | ODE no reduce error ABM |
| Real | −1.001 | Sin estructura macro |

## Archivos eliminados

- `verify_scale_counter.py`: Script de contra-experimento de escala (debug)
- `verify_synthetic_isolated.py`: Test aislado de varianza (debug)
- `verify_synthetic_variance.py`: Test de alta varianza (debug)
- `metrics.py`: Código muerto (nunca importado; `hybrid_validator.py` maneja métricas)

## Referencias

- von Thünen, J. H. (1826). *Der isolierte Staat*.
- Hansen, M. C. et al. (2013). High-resolution global maps of forest cover change. *Science*, 342(6160), 850–853.
- Chazdon, R. L. et al. (2016). Carbon sequestration potential of second-growth forest regeneration. *Science Advances*, 2(5), e1501639.
- Laurance, W. F. et al. (2002). Predictors of deforestation in the Brazilian Amazon. *J. Biogeography*, 29, 737–748.
- FAO (2020). *Global Forest Resources Assessment*.
