# Caso 14 — Postverdad (SIS Misinformación)

## Propósito

Evaluar si la desinformación masiva (postverdad) exhibe propiedades de
hiperobjeto: persistencia temporal, viscosidad, y causalidad descendente
del «ecosistema informativo» sobre la opinión individual.

---

## Modelos

### ODE — SIS de Campo Medio

$$\frac{dI}{dt} = 0.1\bigl[\beta\,I(1-I) - \gamma\,I + F\bigr] + \varepsilon$$

Modelo epidémico de misinformación sin inmunidad permanente (re-infección).

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\beta$ | 0.3 | Tasa de transmisión (Daley & Kendall 1965; Moreno et al. 2004) |
| $\gamma$ | 0.15 | Tasa de recuperación ($R_0 = \beta/\gamma = 2.0$) |
| $\sigma$ | 0.02 | Ruido demográfico |

$R_0 = 2.0$ implica epidemia sostenida, consistente con la persistencia
observada de narrativas falsas en redes sociales.

### ABM — SIS en Red

Agentes con estado S/I sobre red Barabási-Albert, con transmisión
probabilística local y recuperación espontánea.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `abm_beta` | 0.2 | Tasa transmisión ABM (micro) |
| `abm_gamma` | 0.1 | Tasa recuperación ABM |
| `n_agents` | 100 | Red |
| `grid_size` | 10 | Mapeo a grilla 10×10 |
| `driver_cols` | `["mobile_subs"]` | Suscripciones móviles ≈ acceso digital |

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | 0.000 | Sin estructura macro |
| Real | 0.003 | Sin estructura macro |

## Correcciones: `DEBUG` print eliminado.

## Referencias

- Daley, D. J. & Kendall, D. G. (1965). Stochastic rumours. *IMA J. Appl. Math.*, 1(1), 42–55.
- Moreno, Y., Nekovee, M. & Pacheco, A. F. (2004). Dynamics of rumor spreading in complex networks. *PRE*, 69(6), 066130.
- Vosoughi, S., Roy, D. & Aral, S. (2018). The spread of true and false news online. *Science*, 359(6380), 1146–1151.
