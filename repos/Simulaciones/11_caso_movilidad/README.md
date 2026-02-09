# Caso 11 — Movilidad Urbana

## Propósito

Evaluar si el tráfico urbano agregado exhibe propiedades de hiperobjeto:
viscosidad temporal (congestión persistente), no-localidad (efectos en
toda la red), y causalidad descendente (MFD constriñe velocidades locales).

---

## Arquitectura (5 archivos)

| Archivo      | Rol                                              |
|-------------|---------------------------------------------------|
| `validate.py`| Orquestador: pipeline C1-C5 sintético→real       |
| `ode.py`     | MFD (Diagrama Fundamental Macroscópico)            |
| `abm.py`     | Tráfico en red Barabási-Albert con Greenshields    |
| `data.py`    | Datos reales vía `data_universal` + generador MFD |
| `metrics.py` | Métricas estándar                                 |

---

## ODE — Diagrama Fundamental Macroscópico (MFD)

Modelo parabólico de Greenshields (1935):

$$Q(K) = v_f \cdot K \cdot \left(1 - \frac{K}{K_j}\right)$$

$$\frac{dK}{dt} = 0.1 \cdot (\text{Inflow}(t) - Q(K))$$

| Parámetro | Clave | Valor | Justificación |
|-----------|-------|-------|---------------|
| $v_f$ | `mfd_vf` | 60 km/h | Vel. libre flujo típica urbana (HCM 2010) |
| $K_j$ | `mfd_kj` | 150 veh/km | Densidad de atasco (HCM 2010) |
| $\sigma$ | `ode_noise` | 5.0 | Ruido observacional |
| $\times 0.1$ | hardcoded | 0.1 | Escalamiento temporal (paso simulación) |
| Inflow base | hardcoded | 50 veh/paso | Demanda base modulada por forcing |

---

## ABM — Tráfico en Red Scale-Free

Red Barabási-Albert (2 enlaces preferentes por nodo), agentes con
origen-destino, ruteo Dijkstra, congestión tipo Greenshields por arista.

### Parámetros

| Parámetro | Clave | Valor | Justificación |
|-----------|-------|-------|---------------|
| $n_{nodes}$ | `n_nodes` | 50 | Nodos de red (en config) |
| $n_{agents}$ | `n_agents` | 200 | Vehículos simultáneos |
| Capacidad hub | hardcoded | 2000 veh/h | Arterias principales (HCM 2010) |
| Capacidad local | hardcoded | 500 veh/h | Calles secundarias |
| Vel. libre hub | hardcoded | 60 km/h | Arterias |
| Vel. libre local | hardcoded | 30 km/h | Residenciales |
| Longitud aristas | `rng.uniform` | 0.5–5.0 km | Distancias urbanas típicas |

---

## Datos

Fuente: World Bank GDP per capita como proxy de demanda de movilidad.
Período real: 1970–2023, split 2005.
Sintético: MFD con ciclo rush-hour (doble joroba 8am + 6pm), freq horaria.

---

## Resultado

| Fase | EDI | Interpretación |
|------|-----|----------------|
| Sintética | 0.020 | Muy bajo |
| Real | 0.003 | Sin emergencia detectable |

---

## Correcciones Aplicadas (Auditoría)

| Problema | Corrección |
|----------|------------|
| `validate.py`: `print(f"DEBUG: ...")` en producción | Eliminado |
| `validate.py`: docstring genérico | Reescrito con contexto |

---

## Referencias

- Greenshields, B. D. (1935). A study of traffic capacity. *Highway Research Board Proceedings*, 14, 448–477.
- Daganzo, C. F. (2007). Urban gridlock: Macroscopic modeling and mitigation approaches. *Transportation Research Part B*, 41(1), 49–62.
- Geroliminis, N. & Daganzo, C. F. (2008). Existence of urban-scale macroscopic fundamental diagrams. *Transportation Research Part B*, 42(9), 759–770.
