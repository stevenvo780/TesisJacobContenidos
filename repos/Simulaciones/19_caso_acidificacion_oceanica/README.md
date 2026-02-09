# Caso 19 — Acidificación Oceánica (CO2SYS + Revelle Factor)

## Propósito

Evaluar si la acidificación oceánica global exhibe propiedades de
hiperobjeto: no-localidad (afecta todos los océanos), viscosidad temporal
(cambios químicos persisten milenios), y causalidad descendente del
«sistema carbonato» sobre organismos calcificadores individuales.

---

## Modelos

### ODE — Revelle Factor (Buffering Oceánico)

$$\frac{d[\text{pH}]}{dt} = -\gamma \cdot \frac{\ln(pCO_2 / pCO_{2,\text{ref}})}{RF(pCO_2, T)} + \varepsilon$$

$$RF(pCO_2, T) = \underbrace{10.0}_{RF_\pi} + 5.0 \cdot \ln\left(\frac{pCO_2}{280}\right) \cdot \left(1 + 0.01 \cdot (T - 15)\right)$$

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| $RF_\pi$ | 10.0 | Factor Revelle pre-industrial (Revelle & Suess 1957; GEOSECS ≈9-11) |
| Factor 5.0 | 5.0 | Ajuste empírico a datos GLODAP (Egleston et al. 2010: RF moderno 12-15) |
| Sens. térmica | 0.01/°C | ~1%/°C (Egleston 2010) |
| $\gamma$ | 0.5 | Sensibilidad pH-pCO₂ (Zeebe & Wolf-Gladrow 2001) |
| `pCO2_ref` | 280 ppm | Pre-industrial |
| `ode_noise` | 0.005 | Variabilidad estacional |
| Clip pH | [7.5, 8.3] | Rango océano abierto (Doney et al. 2009) |

### ABM — Calcificadores Marinos

Grilla 2D donde cada celda representa una población de calcificadores
(corales, pterópodos, foraminíferos). La masa de concha crece o se
disuelve según Ω aragonita local.

| Parámetro | Valor | Justificación |
|-----------|-------|---------------|
| `grid_size` | 20 | Grilla 20×20 = 400 poblaciones |
| `abm_calc_rate` | 0.02 | ~2%/mes crecimiento concha (Ries et al. 2009, Geology) |
| `abm_diss_rate` | 0.05 | ~5%/mes disolución bajo Ω<1 (Kroeker et al. 2013, GCB) |
| `abm_stress_thresh` | 1.0 | Umbral Ω=1: sub-saturación (Feely et al. 2004, Science) |
| Zonas upwelling | 3 | Regiones con Ω reducida (−0.3 Gaussiana) |
| Baseline Ω | 2.5 | Media global actual (Jiang et al. 2015) |

### Datos sintéticos

Química de carbonatos simplificada (CO2SYS-style):
- Curva Keeling: pCO₂ = 280 + 2.5·t/12 ppm/año
- Equilibrio: K₀, K₁, K₂ con dependencia de T (Zeebe & Wolf-Gladrow 2001)
- TA ≈ 2300 µmol/kg (constante), iteración Newton-Raphson para pH

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | −0.141 | ODE no reduce error ABM |
| Real | −0.002 | Neutral |

## Archivos eliminados

- `metrics.py`: código muerto (nunca importado)
- `data.py.bak`: backup obsoleto

## Referencias

- Revelle, R. & Suess, H. E. (1957). Carbon dioxide exchange. *Tellus*, 9(1), 18–27.
- Zeebe, R. E. & Wolf-Gladrow, D. A. (2001). *CO₂ in Seawater*. Elsevier.
- Orr, J. C. et al. (2005). Anthropogenic ocean acidification. *Nature*, 437, 681–686.
- Egleston, E. S. et al. (2010). Revelle revisited. *GBC*, 24(1), GB1015.
- Ries, J. B. et al. (2009). Marine calcifiers exhibit mixed responses. *Geology*, 37(12), 1131–1134.
- Kroeker, K. J. et al. (2013). Impacts of ocean acidification. *GCB*, 19(6), 1884–1896.
- Feely, R. A. et al. (2004). Impact of CO₂ on the CaCO₃ system. *Science*, 305, 362–366.
