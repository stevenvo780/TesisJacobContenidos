# 01_02 Indicadores y Métricas: Cómo medimos lo invisible

En esta tesis, para probar que un Hiperobjeto existe (H1), usamos un termómetro especial compuesto por varias métricas. Aquí explicamos qué significan para que cualquier informático o científico las entienda.

## 1. La Métrica de Error (RMSE)
**¿Qué es?** Es el "Margen de Pifia". Mide la distancia entre lo que dice nuestro modelo y lo que dice la realidad.
*   **En cristiano:** Si el modelo dice que hará 20° y hace 22°, el error es de 2°.
*   **Regla de Oro:** Si el error es más pequeño que la varianza natural del clima, el modelo es bueno.

## 2. El Criterio de Emergencia
Este es el punto más importante para demostrar la **H1**.
*   **La Prueba:** Corremos el modelo de dos formas:
    1.  **Completo:** Con comunicación entre lo pequeño y lo grande.
    2.  **Reducido:** Cortamos la comunicación (los píxeles no saben qué dice la ecuación global).
*   **Conclusión:** Si el modelo completo es mucho mejor que el reducido, hemos demostrado que **lo Macro existe y es necesario**. A esto lo llamamos "Emergencia Fuerte".

## 3. Cohesión Interna vs Externa (Symploke)
Queremos saber dónde termina el Hiperobjeto. 
*   **Analogía:** Un equipo de fútbol. Los jugadores (nodos internos) interactúan más entre ellos que con el público (nodos externos).
*   **Cálculo:** Si los píxeles de nuestra rejilla climática están más "conectados" entre sí que con el ruido de fuera, entonces hemos encontrado la frontera del sistema.

## 4. La Pentalogía C1-C5 (El examen final)

Explicamos en detalle qué buscamos en cada prueba:

### C1: Convergencia
No nos basta con una coincidencia. Si usamos una Ecuación Diferencial (Matemáticas puras) y un Modelo de Agentes (Programación de objetos) y ambos dan el mismo resultado, es muy probable que hayamos capturado una verdad del mundo.

### C2: Robustez
Un buen modelo no es un "castillo de naipes". Si cambiamos el 10% de los parámetros (ej. un poco más de viento o menos humedad), el modelo debería seguir dando resultados parecidos. Si se rompe por un pequeño cambio, es un modelo frágil que no sirve para la realidad.

### C3: Replicación
En informática, esto es como el "determinismo". Con la misma semilla aleatoria y los mismos datos, el resultado debe ser idéntico. Sin replicación, no hay ciencia, solo hay "me funcionó una vez en mi máquina".

### C4: Validez Estructural
Esto es el chequeo de "sentido común". ¿Las reglas del código respetan las leyes de la física? En el Clima (éxito), sí respetan la termodinámica. En Finanzas (fallo parcial), las reglas son humanas y cambian, por eso el C4 es más difícil de pasar.

### C5: Incertidumbre Explícita
Todo modelo miente un poco. Lo profesional es decir **cuánto**. Reportamos el margen de error para que el lector sepa qué tan fiable es la predicción en el futuro.
