# Caso 20 — Síndrome de Kessler (NASA LEGEND + ORDEM)

## Propósito

Evaluar si la nube de basura espacial en LEO exhibe propiedades de
hiperobjeto: no-localidad (debris orbita toda la Tierra), viscosidad
temporal (décadas-siglos a altitudes altas), y causalidad descendente
del «campo de debris» sobre objetos individuales (cascada colisional).

---

## Modelos

### ODE — Ecuación de Kessler-Liou (Cascada Cuadrática)

$$\frac{dN}{dt} = L + \alpha \cdot N^2 \cdot F_m - \beta \cdot N + \varepsilon$$

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $\alpha$ | 2.0×10⁻¹⁰ | Coef. colisión cuadrático (Kessler & Cour-Palais 1978; Liou 2006: ~1 col/década) |
| $\beta$ | 0.02 | Tasa decaimiento atmosférico ~2%/año en LEO <500km (NASA ORDEM 3.2) |
| $F_m$ | 500 | Fragmentos/colisión (NASA Standard Breakup Model: 500-1500 rastreables) |
| `ode_noise` | 50 | Variabilidad en eventos discretos |
| N₀ | 2000 | Catálogo 1970 (aprox. CSpOC) |
| Floor N | 1000 | Mínimo físico |
| `dt` | 1.0 | Paso temporal = 1 año |
| Baseline launches | 80 | ~80 lanzamientos/año media histórica (UCS Satellite Database) |

### ABM — Campo de Debris Orbital (NASA LEGEND-inspired)

Objetos en bandas de altitud con colisiones estocásticas,
fragmentación y decaimiento orbital.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `n_shells` | 10 | 10 bandas: 200-2000km (NASA ORDEM) |
| `n_size_classes` | 3 | Small <1cm, Medium 1-10cm, Large >10cm |
| `abm_collision_coeff` | 1×10⁻⁹ | ~1 col/década a densidad actual (Liou & Johnson 2006) |
| Pico densidad | shell 4-5 | 800-1000km (máxima densidad observada; ESA MASTER) |
| Población inicial | 50k/5k/1k | Small/Medium/Large ×peak_factor |
| `decay_rate` | [0.05...0.002] | Decreciente con altitud (drag ∝ ρ_atm) |
| Cap colisiones | 50/shell/step | Evita cascada numérica irreal |
| Launch distribution | [0.1, 0.3, 0.4, 0.2] | Preferencia 800-1100km (GEO/SSO) |

### Datos sintéticos

Eventos históricos discretos:
- 2007: ASAT chino (+3000 fragmentos)
- 2009: Iridium-Cosmos (+2000 fragmentos)
- 2021: ASAT ruso (+1500 fragmentos)

Tasa de lanzamiento por era: Cold War ~50, 1990-2010 ~60+, 2010+ ~100+.

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | −3.419 | ODE no reduce error ABM |
| Real | −3.420 | Sin estructura macro |

## Archivos eliminados

- `metrics.py`: código muerto

## Referencias

- Kessler, D. J. & Cour-Palais, B. G. (1978). Collision frequency of artificial satellites. *JGR*, 83(A6), 2637–2646.
- Liou, J.-C. & Johnson, N. L. (2006). Risks in future LEO from intact objects. *Science*, 311, 340–341.
- Johnson, N. L. et al. (2001). NASA's new breakup model. *Adv. Space Research*, 28(9), 1377–1384.
- Rossi, A. et al. (2020). Critical debris density in LEO. *Acta Astronautica*, 170, 379–389.
- NASA (2022). *ORDEM 3.2: Orbital Debris Engineering Model*.
