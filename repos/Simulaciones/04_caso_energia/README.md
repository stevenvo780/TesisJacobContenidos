# Caso 04 — Energía (OPSD GB Grid)

## Descripción

Modela la **transición energética** como hiperobjeto emergente. La
competencia entre fuentes fósiles y renovables en el mix energético
produce dinámicas de sustitución tecnológica que trascienden las
decisiones individuales de los productores.

**Dominio:** Energía / Sistemas eléctricos  
**Variable observable:** Demanda eléctrica mensual (log MW, UK)  
**Datos:** OPSD (Open Power System Data), GB Grid  
**Resultado típico:** EDI_syn ≈ 0.07, EDI_real ≈ -0.01 (no validado)

---

## Modelo ODE — Lotka-Volterra de Competencia Energética

### Ecuaciones

$$\frac{dF}{dt} = r_F \cdot F \cdot \left(1 - \frac{F}{K_F}\right) - \alpha \cdot F \cdot R$$

$$\frac{dR}{dt} = r_R^{eff} \cdot R \cdot \left(1 - \frac{R}{K_R}\right) + \beta \cdot F \cdot R$$

donde:
- $F$: cuota de mercado de combustibles fósiles
- $R$: cuota de mercado de renovables (variable de salida)
- $r_F, r_R$: tasas de crecimiento intrínseco
- $K_F, K_R$: capacidades de carga (market share máximo)
- $\alpha$: presión competitiva de renovables sobre fósiles
- $\beta$: beneficio de renovables por declive fósil

### Efecto de política

$$r_R^{eff} = r_R \cdot (1 + 0.5 \cdot (P - 1))$$

donde $P = \max(0.1, 1 + f_s \cdot z_t)$ es el factor de política.
La elasticidad 0.5 implica que un aumento de 50% en stringencia
política incrementa $r_R$ en 25%.

### Parámetros ODE

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| $r_F$ | 0.02 año⁻¹ | Crecimiento inercial de fósiles. IEA WEO 2020: ~2% anual |
| $r_R$ | 0.15 año⁻¹ | Crecimiento renovable. IRENA 2023: ~15-20% anual para solar/eólica |
| $K_F$ | 0.8 | Market share máximo fósiles ~80% (BP Statistical Review) |
| $K_R$ | 0.9 | Market share máximo renovables ~90% (IEA NZE 2050) |
| $\alpha$ | 0.1 | Presión competitiva. $\alpha > \beta$: fósiles más vulnerables |
| $\beta$ | 0.05 | Beneficio por declive fósil |
| $\sigma$ | 0.01 | ~1% ruido proporcional al estado |
| $F_0$ | 0.7 | Fósiles dominan ~70% circa 2000 |
| $R_0$ | 0.1 | Renovables ~10% circa 2000 |

---

## Modelo ABM — Adopción Tecnológica tipo TIMES

### Arquitectura

- 400 productores de energía (grid 20×20)
- 5 tecnologías: carbón, gas, solar, eólica, nuclear
- Decisión de inversión basada en costo nivelado (LCOE) + lock-in

### Dinámica de decisión

$$\text{preference}_i = \lambda \cdot \text{share}_{actual} + (1 - \lambda) \cdot \text{softmax}(-\text{cost}/T)$$

donde $\lambda = 0.8$ es el factor de lock-in y $T = 50$ la temperatura del softmax.

### Parámetros ABM

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| LCOE base ($/MWh) | [65, 55, 40, 35, 80] | Carbón, gas, solar, eólica, nuclear. Lazard LCOE Analysis v15 |
| Learning rates | [0.01, 0.02, 0.20, 0.15, 0.05] | Solar 20%, eólica 15% por duplicación. Way et al. (2022, Joule) |
| Carbon intensity (tCO₂/MWh) | [0.95, 0.45, 0, 0, 0] | IPCC AR5, Tabla A.III.2 |
| carbon_price_base | 20 $/tCO₂ | EU ETS ~20€ circa 2020 |
| lock_in | 0.8 | 80% inercia tecnológica. Unruh (2000), "carbon lock-in" |
| investment_rate | 0.05 | 5% de capacidad invertida por año |
| Softmax T | 50 | Temperatura de decisión ($/MWh) |

---

## Datos

### Variable principal
- **Fuente:** OPSD (Open Power System Data), time series 2020
- **Variable:** Demanda eléctrica real GB (log MW, mensual)
- **Rango:** 2015-01 a 2020-06

### Drivers
- **tavg**: Temperatura promedio mensual (Londres, Meteostat). Demanda estacional.
- **price**: Precio medio de electricidad (OPSD).
- ~~renewables_share~~: ELIMINADO como driver por circularidad (la ODE predice cuota renovable).

### Split temporal
- Entrenamiento: 2015-01 a 2018-12 (~48 meses)
- Validación: 2019-01 a 2020-06 (~18 meses)

---

## Calibración

| Componente | Método |
|------------|--------|
| ODE (L-V params) | **Fijos** desde literatura. `ode_calibration=False` |
| ABM (forcing_scale, macro_coupling, damping) | **Grid search** vía `hybrid_validator.calibrate_abm()` |

---

## Archivos del caso

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador: configura, ejecuta C1-C5, escribe outputs |
| `ode.py` | Macro: Lotka-Volterra competencia energética |
| `abm.py` | Micro: adopción tecnológica tipo TIMES (vectorizado) |
| `data.py` | Carga OPSD GB + temperatura Meteostat |
| `metrics.py` | LOLP, ROCOF, inertia, correlación, RMSE |

---

## Auditoría (correcciones aplicadas)

1. **Dead parameters eliminados**: `ode_H=5.0`, `ode_D=1.0`, `generation_cap=60000`
   estaban en `extra_base_params` pero la ODE Lotka-Volterra no los leía.
2. **Circularidad en drivers**: `renewables_share` era tanto variable de salida de la
   ODE como driver de forcing. Eliminado para evitar look-ahead leakage.
3. **Código diagnóstico eliminado**: Bloque de ROCOF, LOLP, Inertia que ejecutaba
   simulación separada con parámetros duplicados.
4. **Documentación**: Todos los parámetros ahora tienen derivación y referencia.

---

## Referencias

- Grübler, A. et al. (1999). Dynamics of Energy Technologies and Global Change. *Energy Policy*, 27(5), 247-280.
- IRENA (2023). Renewable Power Generation Costs in 2022.
- Lazard (2023). Lazard's Levelized Cost of Energy Analysis, v16.
- Loulou, R. et al. (2016). TIMES Model Documentation (IEA-ETSAP).
- Marchetti, C. (1977). Primary energy substitution models. *Tech. Forecast. Soc. Change*, 10(4), 345-356.
- Unruh, G. C. (2000). Understanding carbon lock-in. *Energy Policy*, 28(12), 817-830.
- Way, R. et al. (2022). Empirically grounded technology forecasts. *Joule*, 6(9), 2057-2082.
