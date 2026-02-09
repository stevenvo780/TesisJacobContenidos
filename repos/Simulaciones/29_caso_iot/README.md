# Caso 29 — Ecosistema IoT Global

## Hiperobjeto

El ecosistema global del Internet de las Cosas como hiperobjeto.
Propiedades: masivamente distribuido (miles de millones de dispositivos),
no-local (interconexión global), viscoso (path dependency tecnológica,
lock-in) y con efectos de red Metcalfe (valor ∝ N²).

## Modelo ODE — Bass-Metcalfe Network Effects (bilineal)

$$\frac{dN}{dt} = \alpha(F - \beta N) + \gamma_{\text{net}} \cdot F \cdot N + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.05 | Tasa adopción base ~5%/año (ITU 2020: crecimiento medio global) |
| β | 0.02 | Obsolescencia/churn ~2%/año (Rogers 2003: reemplazo tecnológico) |
| γ_net | 0.08 | Efecto red Metcalfe: N amplifica F (Metcalfe 2013; Bass 1969: imitación) |
| noise_std | 0.015 | Variabilidad estocástica |
| p₀ | 0.0 | Estado inicial normalizado |

### Efecto de Red

El término bilineal `γ_net·F·N` captura los rendimientos crecientes de red:
cada dispositivo conectado aumenta el valor de la red completa (Metcalfe 2013),
acelerando la adopción. Este efecto genera una curva S característica
(Rogers 2003: Diffusion of Innovations).

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 25 | 625 celdas (regiones/mercados) |
| forcing_gradient_type | `random_hubs` | Ciudades/hubs tecnológicos |
| forcing_gradient_strength | 0.70 | Gradiente fuerte (Goldenberg et al. 2001) |
| heterogeneity_strength | 0.25 | Diferencias regionales (países ricos vs. pobres) |
| forcing_scale | 0.15 | Sensibilidad ABM a driver económico |
| macro_coupling | 0.40 | Acoplamiento macro→micro alto |

## Datos Reales

- **Fuente**: World Bank (múltiples indicadores)
  - `IT.CEL.SETS.P2` — Suscripciones móviles/100 hab (**variable objetivo**)
  - `IT.NET.USER.ZS` — Usuarios internet (%)
  - `IT.NET.BBND.P2` — Banda ancha fija/100 hab
  - `IT.NET.SECR.P6` — Servidores seguros/millón
  - `NY.GDP.PCAP.KD` — PIB per cápita
  - `NY.GDP.MKTP.KD.ZG` — Crecimiento PIB (%)
- **Cobertura**: 1980–2022

## Forcing Sintético

```
F(t) = 0.010·t + 0.0003·t^1.2
```

- 0.010·t: tendencia secular ~1%/año (ITU 2020)
- 0.0003·t^1.2: aceleración por efectos de red (Metcalfe 2013)

## Resultados

| Fase | EDI | CR | Viscosity | Resultado |
|------|-----|----|-----------|-----------|
| Sintética | 0.415 | 1.024 | 4 | PASS ✓ |
| Real | 0.014 | 1.088 | 3 | REJECT |

**Interpretación**: EDI sintético sólido confirma el modelo Bass-Metcalfe.
EDI real muy bajo (0.014) sugiere que la serie de suscripciones móviles es
demasiado suave (curva S ya saturada en muchos países), lo que hace que el
ABM-solo sea casi tan bueno como ABM+ODE. La ODE aporta poco valor agregado
sobre datos ya en fase de saturación.

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador con métricas extendidas |
| `abm.py` | ABM difusión tecnológica (Goldenberg + Delre) |
| `ode.py` | Bass-Metcalfe bilineal |
| `data.py` | World Bank multi-indicador |

## Correcciones Aplicadas

1. `import random` → `np.random.default_rng(seed)` (reproducibilidad NumPy)
2. `data.py.bak` eliminado (backup residual)
3. Todos los parámetros numéricos documentados con referencias
