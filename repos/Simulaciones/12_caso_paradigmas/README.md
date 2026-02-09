# Caso 12 — Paradigmas Científicos (Ising)

## Propósito

Evaluar si los cambios de paradigma científico (Kuhn 1962) exhiben
propiedades de hiperobjeto: transición de fase, viscosidad temporal, y
causalidad descendente del «paradigma dominante» sobre investigadores.

---

## Modelos

### ODE — Landau-Ginzburg (Transición de Fase de Campo Medio)

$$\frac{dm}{dt} = 0.1 \cdot (\alpha\,m - \beta\,m^3 + H) + \varepsilon$$

Potencial: $V(m) = -\frac{1}{2}\alpha m^2 + \frac{1}{4}\beta m^4 - Hm$

- $\alpha > 0$: doble pozo (orden) → paradigma dominante
- $\alpha < 0$: pozo único (desorden) → crisis kuhniana

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\alpha$ | 1.0 | Distancia a Tc (Hohenberg & Halperin, Model A) |
| $\beta$ | 1.0 | No-linealidad |
| $\sigma$ | 0.1 | Fluctuaciones |

### ABM — Ising con Red Scale-Free

Agentes en red Barabási-Albert con spin ±1, interacción ferromagnética,
temperatura controla desorden vs. consenso.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `abm_temperature` | 2.0 | Cercano a Tc (transición paramagnética) |
| `n_agents` | 50 | Red reducida |
| `grid_size` | 10 | Mapeo a grilla 10×10 |

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | 0.000 | Sin estructura macro |
| Real | −0.000 | Neutral |

## Correcciones: `DEBUG` print eliminado.

## Referencias

- Kuhn, T. S. (1962). *The Structure of Scientific Revolutions*. UChicago Press.
- Landau, L. D. (1937). On the theory of phase transitions. *Zh. Eksp. Teor. Fiz.*, 7, 19–32.
- Hohenberg, P. C. & Halperin, B. I. (1977). Theory of dynamic critical phenomena. *RMP*, 49(3), 435.
