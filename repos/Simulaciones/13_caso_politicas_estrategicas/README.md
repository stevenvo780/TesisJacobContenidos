# Caso 13 — Políticas Estratégicas (Inercia Institucional)

## Propósito

Evaluar si la inercia institucional que gobierna la adopción y persistencia
de políticas estratégicas constituye un hiperobjeto: viscosidad temporal,
resistencia al cambio, y causalidad descendente del entorno institucional
sobre actores individuales.

---

## Modelos

### ODE — Inercia Institucional

$$\frac{dE}{dt} = 0.1\bigl[\alpha(E^{*} - E) + \beta\,\text{Policy} - \gamma\,E^2\bigr] + \varepsilon$$

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\alpha$ | 0.3 | Velocidad de ajuste institucional (North 1990) |
| $E^{*}$ | 0.5 | Nivel de equilibrio institucional |
| $\beta$ | 0.2 | Sensibilidad a intervención (Rodrik 2007) |
| $\gamma$ | 0.1 | Rendimientos decrecientes (Acemoglu 2001) |
| $\sigma$ | 0.05 | Ruido |

### ABM — Difusión Bass en Red

Modelo de adopción con innovadores ($p$) e imitadores ($q$), sobre red
Barabási-Albert. Los agentes adoptan por presión social vecinal.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `p` | 0.01 | Coef. innovación (Bass 1969 ≈ 0.01–0.03) |
| `q` | 0.30 | Coef. imitación (Bass 1969 ≈ 0.3–0.5) |
| `grid_size` | 7 | Red 49 agentes |
| `driver_cols` | `[]` | Sin driver externo |

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | −0.003 | Sin estructura macro |
| Real | −0.022 | Sin estructura macro |

## Correcciones: `DEBUG` print eliminado.

## Referencias

- North, D. C. (1990). *Institutions, Institutional Change and Economic Performance*. Cambridge.
- Acemoglu, D. (2001). The colonial origins of comparative development. *AER*, 91(5), 1369–1401.
- Rodrik, D. (2007). *One Economics, Many Recipes*. Princeton.
- Bass, F. M. (1969). A new product growth model for consumer durables. *Management Science*, 15(5), 215–227.
