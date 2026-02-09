# Caso 05 — Epidemiología (COVID-19 SEIR)

## Descripción

Modela la **pandemia COVID-19** como hiperobjeto emergente usando el
modelo compartimental SEIR a nivel macro y un ABM de red epidémica a
nivel micro. La dinámica pandémica exhibe propiedades de hiperobjeto:
no-localidad, viscosidad temporal y phasing.

**Dominio:** Epidemiología  
**Variable observable:** Incidencia semanal de casos (OWID, global)  
**Resultado típico:** EDI_syn ≈ 0.45, EDI_real ≈ 0.00 (parcialmente validado)

---

## Modelo ODE — SEIR de Kermack-McKendrick

### Ecuaciones

$$\frac{dS}{dt} = -\beta(t) \cdot \frac{S \cdot I}{N}$$
$$\frac{dE}{dt} = \beta(t) \cdot \frac{S \cdot I}{N} - \sigma \cdot E$$
$$\frac{dI}{dt} = \sigma \cdot E - \gamma \cdot I$$
$$\frac{dR}{dt} = \gamma \cdot I$$

### Transmisión modulada

$$\beta(t) = R_0 \cdot \gamma \cdot \text{clip}(1 + f_s \cdot z_t,\; 0.1,\; 2.0)$$

### Variable de salida

$$\text{incidence}(t) = \sigma \cdot E(t)$$

### Parámetros ODE

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| $R_0$ | 2.5 | COVID-19 wild-type. Li et al. (2020, NEJM 382:1199) |
| $T_{latente}$ | 5 días | Mediana 5.2 días (IC 95%: 4.1-7.0). Li et al. (2020) |
| $T_{infeccioso}$ | 7 días | He et al. (2020, Nat. Med.): infectividad ~7-10 días |
| $\sigma$ | 0.2 día⁻¹ | $= 1/T_{latente}$ |
| $\gamma$ | 0.143 día⁻¹ | $= 1/T_{infeccioso}$ |
| $\beta$ | 0.357 día⁻¹ | $= R_0 \cdot \gamma$ |
| $\sigma_{noise}$ | 0.01 | ~1%, proporcional al estado. Variabilidad en super-spreaders |

---

## Modelo ABM — SEIR en Red Scale-Free

### Arquitectura

- **Red:** Barabási-Albert ($m=3$, $\langle k \rangle = 6$)
- **Agentes:** $n = 1000$ individuos con estado S/E/I/R
- **Transmisión vectorizada** usando matriz de adyacencia sparse

### Transiciones

| Transición | Probabilidad |
|------------|-------------|
| S → E | $1 - (1 - \beta_{eff})^{n_{vecinos\_I}}$ |
| E → I | Después de $T_{latente}$ pasos |
| I → R | Después de $T_{infeccioso}$ pasos |
| R → S | Waning immunity: $p = 0.02$ por paso ($\tau \approx 50$ pasos ≈ 1 año) |

### Parámetros ABM

| Parámetro | Valor | Derivación |
|-----------|-------|------------|
| $n_{agents}$ | 1000 | Escalado computacional |
| $m$ (Barabási) | 3 | $\langle k \rangle = 6$ contactos. Mossong et al. (2008): ~10-15/día |
| `abm_beta` | 0.3 | Secondary Attack Rate ~0.3. Bi et al. (2020, Lancet ID) |
| `abm_latent` | 3 días | Periodo latente COVID. Li et al. (2020) |
| `abm_infectious` | 7 días | Periodo infeccioso. He et al. (2020) |
| `immunity_waning` | 0.02 | $\tau = 1/0.02 = 50$ pasos. Reinfección COVID ~1 año |

---

## Datos

### Variable principal
- **Fuente:** Our World in Data (OWID) COVID-19 dataset
- **Variable:** `new_cases_smoothed`, agregado semanal global
- **Rango:** 2020-03 a 2023-12

### Drivers
- **deaths**: Muertes suavizadas (OWID)
- **vaccinated**: Personas vacunadas acumuladas (OWID)
- **stringency**: Índice de stringencia de Oxford (OWID)

### Split temporal
- Entrenamiento: 2020-03 a 2021-12 (~96 semanas)
- Validación: 2022-01 a 2023-12 (~104 semanas)

---

## Calibración

| Componente | Método |
|------------|--------|
| ODE (R₀, latente, infeccioso) | **Fijos** desde literatura epidemiológica |
| ABM (forcing_scale, macro_coupling, damping) | **Grid search** vía `hybrid_validator.calibrate_abm()` |

---

## Archivos del caso

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador: configura, ejecuta C1-C5, escribe outputs |
| `ode.py` | Macro: SEIR Kermack-McKendrick |
| `abm.py` | Micro: SEIR en red Barabási-Albert (vectorizado con sparse matrix) |
| `data.py` | Carga OWID COVID-19 dataset |
| `metrics.py` | Correlación, RMSE, dominancia, varianza ventana |

---

## Auditoría (correcciones aplicadas)

1. **Dead parameters**: `beta=0.3, sigma=0.2, gamma=0.1, e0=0.001` estaban en
   `extra_base_params` pero la ODE SEIR lee `ode_R0, ode_latent, ode_infectious`
   (no ode_alpha/ode_beta). Eliminados para evitar confusión.
2. **Documentación ODE**: Agregadas derivaciones con referencias (Li 2020, He 2020).
3. **Impresión simplificada**: Resumen verbose con C1-C5 reemplazado por formato
   estándar consistente con otros casos.

---

## Referencias

- Anderson, R. M. & May, R. M. (1991). *Infectious Diseases of Humans*. OUP.
- Bi, Q. et al. (2020). Epidemiology and Transmission of COVID-19 in Shenzhen. *Lancet Infect. Dis.*, 20(8), 911-919.
- He, X. et al. (2020). Temporal dynamics in viral shedding. *Nature Medicine*, 26, 672-675.
- Keeling, M. J. & Eames, K. T. D. (2005). Networks and epidemic models. *J. R. Soc. Interface*, 2(4), 295-307.
- Kermack, W. O. & McKendrick, A. G. (1927). A Contribution to the Mathematical Theory of Epidemics. *Proc. R. Soc. A*, 115(772), 700-721.
- Li, Q. et al. (2020). Early Transmission Dynamics in Wuhan. *NEJM*, 382(13), 1199-1207.
- Mossong, J. et al. (2008). Social Contacts and Mixing Patterns. *PLoS Med.*, 5(3), e74.
