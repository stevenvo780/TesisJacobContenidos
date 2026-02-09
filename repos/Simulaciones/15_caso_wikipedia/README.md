# Caso 15 — Wikipedia (Lotka-Volterra Calidad vs Controversia)

## Propósito

Evaluar si Wikipedia, como proyecto colectivo de conocimiento, exhibe
propiedades de hiperobjeto: dinámica predador-presa entre calidad editorial
y controversia, viscosidad temporal, causalidad descendente del «proyecto
enciclopédico» sobre editores individuales.

---

## Modelos

### ODE — Lotka-Volterra (Calidad vs Controversia)

$$\frac{dQ}{dt} = 0.1\bigl[r\,Q(1-Q) - \alpha\,Q\,C\bigr] + \varepsilon_Q$$
$$\frac{dC}{dt} = 0.1\bigl[\beta\,Q\,C - \gamma\,C + F\bigr] + \varepsilon_C$$

Adaptación del modelo depredador-presa: la controversia (C) se alimenta
de la calidad (Q); la calidad crece logísticamente pero es «consumida»
por la controversia.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $r$ | 0.5 | Crecimiento logístico de calidad |
| $\alpha$ | 0.3 | Impacto de controversia sobre calidad (Kittur & Kraut 2008) |
| $\beta$ | 0.2 | Controversia incentivada por calidad |
| $\gamma$ | 0.1 | Decaimiento de controversia |
| $\sigma$ | 0.05 | Ruido |

### ABM — Modelo Cultural Axelrod

Agentes con vectores culturales (features × traits) que interactúan
preferentemente con vecinos similares. Captura la homogeneización vs.
fragmentación editorial.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `n_features` | 5 | Dimensiones culturales (Axelrod 1997) |
| `n_traits` | 3 | Valores por dimensión |
| `n_agents` | 50 | Red de editores |
| `grid_size` | 7 | Mapeo a grilla 7×7 |
| `driver_cols` | `[]` | Sin driver externo |

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | 0.317 | Acoplamiento macro débil pero significativo |
| Real | 0.000 | Sin estructura macro |

Nota: EDI_syn=0.317 sugiere que el modelo Lotka-Volterra aporta estructura
en condiciones controladas, pero no se transfiere a datos reales.

## Correcciones: `DEBUG` print eliminado.

## Referencias

- Kittur, A. & Kraut, R. E. (2008). Harnessing the wisdom of crowds in Wikipedia. *CSCW '08*, 37–46.
- Axelrod, R. (1997). *The Dissemination of Culture*. J. Conflict Resolution, 41(2), 203–226.
- Lotka, A. J. (1925). *Elements of Physical Biology*. Williams & Wilkins.
- Volterra, V. (1926). Fluctuations in the abundance of a species considered mathematically. *Nature*, 118, 558–560.
