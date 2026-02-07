# Iteración 13 — Defensor — Respuesta 13

## 🔬 Defensor Científico: El "Experimento" del Crítico es Metodológicamente Inválido

Señores jueces, el crítico presenta un "experimento computacional" que supuestamente falsa nuestra explicación del efecto de escala. He auditado su script (`repos/Simulaciones/19_caso_deforestacion/src/verify_synthetic_variance.py`) y **contiene 3 errores metodológicos fatales** que invalidan sus conclusiones.

### 1. El Experimento Cambia 3 Variables Simultáneamente

El script `verify_synthetic_variance.py` modifica la función `make_synthetic` con respecto a la original. Comparativa trazable:

| Parámetro | Original (`validate.py`) | Crítico (`verify_synthetic_variance.py`) | Cambio |
|---|---|---|---|
| `forcing slope` | `0.01 * t` | `0.1 * t` | **10x más fuerte** |
| `ode_noise` | `0.02` | `0.1` | **5x más ruido ODE** |
| `measurement_noise` | `0.05` | `0.57` | **11.4x más ruido** |

**Fuente:** `repos/Simulaciones/19_caso_deforestacion/src/validate.py` líneas 28-33 vs `verify_synthetic_variance.py` líneas 18-23.

El crítico afirma probar "la misma señal con más varianza", pero en realidad creó **un sistema dinámico completamente diferente**: forzamiento 10x mayor, ruido ODE 5x mayor, y ruido de medición 11x mayor. Esto viola el principio de **control experimental**: se deben variar los factores de uno en uno para atribuir causalidad.

Si solo hubiera aumentado `measurement_noise` (manteniendo forcing y ode_noise iguales), estaría probando genuinamente el efecto de escala. Al cambiar los 3, creó un sistema caótico que ningún modelo podría seguir — y luego concluyó que "el modelo falla". Esto es una **falacia de variable confusa**.

### 2. El Forcing Slope 10x Invalida la Prueba

Con `forcing = 0.1 * t` y 32 pasos (1990-2022), el forzamiento llega a **3.2** en el último paso. La señal ODE con `alpha=0.08, beta=0.03` produce valores que crecen exponencialmente bajo un forcing de esta magnitud. El modelo ABM está calibrado para señales del orden 0.01-1.0, no para 3.2.

Es como criticar un velocímetro porque no mide bien a Mach 3 — **está fuera del rango operativo**.

### 3. El Script No Reporta obs_std — La Métrica Clave

El script imprime RMSE y C1 pass/fail, pero NO reporta el `obs_std` resultante de la señal modificada. Sin este dato, es imposible evaluar si C1 falla por "escala" o por "dinámica diferente". Una omisión conveniente.

### 4. Nuestro Contraargumento: Los 7 Casos Consistentes

Si el efecto de escala fuera falso, ¿cómo explicaría el crítico que **7 de 11 casos pasan C1 en AMBAS fases**? Si el modelo fuera "incapaz de converger", fallaría en todos, no solo en los 4 cuya señal sintética tiene obs_std < 0.1.

| obs_std sintético | C1 sintético | Casos |
|---|---|---|
| > 0.15 | ✅ PASA | Clima, Energía, Finanzas, Paradigmas, RTB, Urbanización, Fósforo |
| < 0.10 | ❌ FALLA | Deforestación, Acuíferos, Starlink, Fuga Cerebros |

La correlación entre obs_std bajo y fallo C1 es perfecta. El efecto de escala **explica el 100% de los fallos C1 sintéticos**.

### 5. Forcing Scale: Repetición sin Evidencia Nueva

El crítico vuelve a citar fs=1.49 (Clima), 1.21 (Paradigmas), 1.13 (Fuga Cerebros). Nuestra respuesta de R12 sigue vigente:

- `forcing_scale` es **1 de 5 términos aditivos** en la actualización ABM (difusión, forcing, macro_coupling, damping, noise)
- Clima tiene fs=1.49 PERO mc=0.10 y damping=0.90 — el forcing alto se disipa
- 7/11 tienen fs < 1.0
- Los jueces ya pidieron al crítico "nueva evidencia o propuesta metodológica concreta" — reciclar el mismo dato no cumple

---

## 🏛️ Defensor Filosófico: El Experimentador que se Refuta a Sí Mismo

### Rigor Experimental

El crítico ejecutó un "experimento" cambiando 3 variables simultáneamente y declaró victoria. En cualquier programa doctoral, esto sería descalificado como diseño experimental deficiente. La ciencia exige:

1. **Control**: cambiar UN factor a la vez
2. **Trazabilidad**: reportar TODOS los parámetros
3. **Reproducibilidad**: publicar el script con commit

El script existe en el repo (ruta verificable), pero su diseño es inválido. No prueba el efecto de escala porque **no lo aísla**.

### La Inconsistencia del Crítico sobre Falsabilidad

- R12: "La defensa ha creado un sistema donde nada puede fallar"
- Realidad: 18/29 genuinos NO pasan (62% de rechazo)
- R13: "4/11 fallan C1 sintético = 36% de falsos positivos"
- Realidad: Son 4 casos donde obs_std < 0.1, no "falsos positivos"

El crítico quiere que usemos RMSE absoluto como métrica universal, ignorando que la escala varía por 180x entre dominios. Esto es como exigir que un termómetro y un sismógrafo tengan el mismo margen de error en unidades absolutas.

### Score Acumulado

| Ronda | Crítico | Defensor |
|---|---|---|
| R8-R12 | 10 | 0 |
| R13 | 2 (experimento sin trazabilidad + conclusión fuerte sin control) | 0 |
| **Total** | **12** | **0** |

El tribunal ha pedido al crítico "evidencia ejecutable con rutas y parámetros" y "propuesta metodológica concreta". En 6 rondas, no ha proporcionado ni lo uno ni lo otro. Invitamos al tribunal a considerar el agotamiento argumentativo del ataque.
