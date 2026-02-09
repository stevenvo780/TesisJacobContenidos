# Caso 23 — Erosión Dialéctica

## Hiperobjeto

Pérdida progresiva de diversidad lingüística dialectal bajo presión mediática
y globalización. La erosión dialectal opera como hiperobjeto: es no-local
(afecta simultáneamente comunidades distantes), viscosa (los hablantes no
perciben el cambio generacional) y masivamente distribuida (Crystal 2000).

## Modelo ODE — Abrams-Strogatz Linguistic Competition (2003)

$$\frac{dx}{dt} = \alpha(F - \beta x) + \text{prestige} \cdot \max(F,0) \cdot (1 + 0.3|x|) + \varepsilon$$

| Símbolo | Valor | Referencia |
|---------|-------|------------|
| α | 0.03 | Tasa transición lingüística ~3%/generación (Abrams & Strogatz 2003) |
| β | 0.01 | Resistencia dialectal/revitalización ~1%/año (Crystal 2000) |
| prestige | 0.008 | Asimetría prestigio lengua vehicular (Mufwene 2001: bias ~0.5–1.5%) |
| 0.3 | — | Amplificación no-lineal proporcional al estado (Nettle 1999: tipping point en pérdida lingüística) |
| noise_std | 0.015 | Variabilidad interanual |
| p₀ | 0.1 | Estado inicial (10% de erosión basal) |

### Término de Prestigio

El término `prestige·max(F,0)·(1+0.3|x|)` modela la retroalimentación positiva:
a mayor erosión dialectal previa (|x| grande), mayor facilidad para erosión
adicional. El factor 0.3 (~30% de amplificación) corresponde a la observación
empírica de que lenguas en declive aceleran su desaparición (Nettle 1999).

## Modelo ABM — abm_core.py

| Parámetro | Valor | Referencia |
|-----------|-------|------------|
| grid_size | 20 | Estándar |
| forcing_gradient_type | `random_hubs` | Centros mediáticos y culturales como focos de erosión |
| forcing_gradient_strength | 0.65 | Gradiente fuerte: ciudades vs. rural (Crystal 2000) |
| heterogeneity_strength | 0.30 | Alta variabilidad sociolingüística (Mufwene 2001) |
| forcing_scale | 0.15 | Sensibilidad ABM a driver mediático |
| macro_coupling | 0.30 | Acoplamiento macro→micro moderado |

## Datos Reales

- **Fuente**: `data_universal.py` → `fetch_case_data` con fallback sintético
- **Proxy**: Indicadores de diversidad lingüística / uso de lenguas minoritarias
- **Resolución**: Mensual (interpolado si fuente anual)

## Forcing Sintético

```
F(t) = 0.008·t + 0.0002·t^1.2
```

- 0.008·t: tendencia secular ~0.8%/año (Crystal 2000: ritmo de pérdida dialectal)
- 0.0002·t^1.2: aceleración por media digital (Nettle 1999)

## Resultados

| Fase | EDI | Resultado |
|------|-----|-----------|
| Sintética | 0.293 | REJECT (EDI < 0.30 marginal) |
| Real | −9.084 | REJECT |

**Interpretación**: El EDI sintético casi alcanza el umbral (0.293 ≈ 0.30) pero
no supera la barrera, indicando emergencia débil en la fase controlada. El EDI
real fuertemente negativo sugiere que la variable proxy disponible no captura
adecuadamente la dinámica Abrams-Strogatz a escala global.

## Archivos

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador |
| `abm.py` | Wrapper con gradiente random_hubs |
| `ode.py` | Abrams-Strogatz con término de prestigio asimétrico |
| `data.py` | fetch_case_data + fallback sintético |

## Correcciones Aplicadas

1. `import random` → `np.random.default_rng(seed)` (reproducibilidad NumPy)
2. `metrics.py` eliminado (código muerto)
3. Factor 0.3 documentado (Nettle 1999)
4. Todos los parámetros numéricos documentados con referencias
