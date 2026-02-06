# Explicación Detallada del Sistema de Simulación Climática

Este documento contiene la explicación del modelo híbrido utilizado en el proyecto `SimulacionClimatica`, desglosado desde conceptos básicos hasta detalles técnicos y algoritmos.

## 1. Resumen para Principiantes (For Dummies)

Imagina que estamos tratando de entender cómo cambia la temperatura de un territorio usando dos "cerebros" diferentes que trabajan juntos:

*   **El Cerebro Micro (Agentes):** Divide la región en un tablero de ajedrez. Cada cuadrito es un "agente" con su propia temperatura que "habla" con sus vecinos. Si un cuadro se calienta, le pasa calor al de al lado.
*   **El Cerebro Macro (Ecuación Global):** Es una fórmula matemática que mira toda la región desde un satélite. Se encarga de las tendencias grandes: las estaciones del año y el calentamiento global.

**El truco especial:** Ambos cerebros se pasan información constantemente. El global le da un "norte" a los cuadritos, y los cuadritos le dicen al global qué está pasando en el suelo.

---

## 2. Detalles Técnicos (Para Informáticos)

El sistema es un modelo de **acoplamiento bidireccional** con **Asimilación de Datos (Nudging)**.

*   **Micro (ABM - Agent Based Model):** Implementado como una rejilla 2D (Lattice). Cada nodo tiene un estado $S = [T, H]$. Utiliza un Kernel de Moore para la difusión térmica y ruido gaussiano para la turbulencia.
*   **Macro (ODE - Ordinary Differential Equation):** Resuelve el balance energético regional. $\frac{dT}{dt} = \alpha(F(t) - T) + \beta \bar{S}_{micro}$.
*   **Datos:** Series temporales de **Meteostat** para la región **CONUS** (1990-2024).

### Métricas de éxito:
*   **RMSE (Error Cuadrático Medio):** 4.268 (Dentro del umbral de 4.717).
*   **Emergencia Fuerte:** El modelo híbrido es un **45% más preciso** que el modelo reducido (sin acoplamiento).

---

## 3. Lógica de los Cálculos (Algoritmos)

El sistema corre un bucle mensual con tres pasos clave:

### Paso A: El Calendario (Tendencia Global)
Calcula la temperatura teórica basada en la estación y el tiempo transcurrido.
```python
# Lógica: teoría = columpio_estacional + subida_calentamiento
teoria = 15 * sin(2 * pi * mes / 12) + (0.003 * mes)
# Nueva global = anterior + inercia * (teoria - anterior)
```

### Paso B: El Vecindario (Difusión Local)
Cada píxel de la rejilla se equilibra con los que tiene alrededor.
```python
# Lógica: mi_temperatura += 10% de (promedio_vecinos - mi_temperatura)
promedio_vecinos = sum(vecinos) / 4
difusion = 0.1 * (promedio_vecinos - temp_actual)
```

### Paso C: La Goma Elástica (Nudging/Acoplamiento)
Es el pegamento que evita que la rejilla local diverja de la realidad global.
```python
# Lógica: cada píxel se estira un poco hacia la temperatura global macro
fuerza_goma = 0.4
ajuste = fuerza_goma * (temp_global_macro - temp_pixel)
```

---

## 4. Conclusiones del Estado de la Tesis

1.  **Caso Clima:** Cohesión interna adecuada pero **no validado en zero-nudging** (EDI 0.103 < 0.30). La fase sintetica valida la estructura, pero la fase real reporta debilidad macro bajo autonomia pura.
2.  **Caso Finanzas:** En desarrollo. El modelo falla en el criterio C4 (Validez), indicando que las reglas del mercado financiero no son tan predecibles como las estaciones climáticas.

---

## 5. Actualizacion Iteracion 2 (Debate)

Resultados reportados para responder criticas de nudging y causalidad:

- **Autonomia a largo plazo (1000 pasos, zero-nudging):** la correlacion ABM-ODE crece y se estabiliza (~0.8172 global).
- **Causalidad inversa:** la ODE puede reconstruirse desde el micro (correlacion ~0.9969) usando `forcing = grid_means_ABM`.
- **Gradiente de acoplamiento:** respuesta no monotona en `forcing_scale`, con optimo alrededor de 0.10; sugiere dinamica propia micro.
- **Hallazgo C5:** en Clima, `macro_coupling` es operativamente inactivo por baja varianza espacial; el acoplamiento efectivo ocurre via `forcing_scale`.

Detalles: `repos/Simulaciones/caso_clima/docs/tests_adversariales_iteracion_2.md`.
