# Protocolo de Simulacion (Clima Regional)

## 1. Definicion de escenario
- Objetivo: demostrar persistencia estructural y no-localidad funcional.
- Delimitacion: region funcional, cohesion interna > externa.

## 2. Diseno de agentes
- Agentes: celdas con `T` y `H`.
- Reglas: difusion local + forcing exogeno + acople macro.

## 3. Inicializacion
- Grilla con distribucion inicial y semillas documentadas.
- Parametros base definidos en `src/validate.py`.
- Split sintetica: 2000-2009 / 2010-2019.
- Split real: 1990-2010 / 2011-2024.

## 4. Ejecucion
- Escenario base y contrafactuales.
- Criterio de paro: estabilidad de patrones (varianza de `T_bar` estabilizada) y costo marginal > beneficio.
- Se usa nudging con observacion rezagada (t-1) para evaluacion de corto plazo.

## 5. Evaluacion
- Comparacion en dos fases:
- Fase sintetica: verificacion interna y calibracion base.
- Fase real: evaluacion final con datos reales regionales.
- C1-C5 obligatorios.

## 6. Tests Adversariales (Iteracion 2)

Resultados reportados en debate para responder criticas de nudging y causalidad:

- Autonomia a largo plazo: 1000 pasos con `assimilation_strength=0.0` y `assimilation_series=None`.
- Causalidad inversa: ODE forzada con `grid_means_ABM` como input.
- Gradiente de acoplamiento: barrido de `forcing_scale` para observar respuesta no monotona del ABM.
- Hallazgo C5: `macro_coupling` inactivo en Clima por baja varianza espacial; acoplamiento efectivo via `forcing_scale`.

Detalle y parametros: `repos/Simulaciones/caso_clima/docs/tests_adversariales_iteracion_2.md`.
