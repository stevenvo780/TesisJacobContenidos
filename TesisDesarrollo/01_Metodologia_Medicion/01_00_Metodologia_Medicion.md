# 01 Metodologia de Medicion — Narrativa Unificada

## Protocolo de Rigor (C1-C5)
1. **C1 Convergencia:** ABM y ODE convergen en datos reales.
2. **C2 Robustez:** estabilidad ante perturbaciones de parametros.
3. **C3 Determinismo aleatorio:** semillas fijas para replicabilidad.
4. **C4 Linter de realidad:** coherencia con leyes del dominio.
5. **C5 Reporte de fallos:** sensibilidad y limites explicitados.

Estos criterios surgen de auditorias internas: los protocolos deben ser visibles, comparables y verificables. La metodologia no se justifica por resultados favorables, sino por su capacidad para fallar de forma explicita cuando el dominio lo exige.

## Pipeline de Validacion
Observacion → Simulacion → Validacion. El modelo se mantiene solo si supera falsacion y produce mejoras no triviales sobre el micro. Esta secuencia responde al debate metodologico: no basta con evidencia convergente, se requiere una prueba operativa y un procedimiento de rechazo.

## Metricas y Justificación Teórica
- **EDI (Effective Dependence Index):** Mide la reducción de entropía del sistema micro gracias a la estructura macro.
    - **Umbral > 0.30 (Justificación):** Este valor no es arbitrario. Se deriva del concepto de **Redundancia ($R$)** de Shannon, donde $R = 1 - (H / H_{max})$. Una redundancia del 30% ($R \approx 0.3$) implica que casi un tercio de la libertad de los componentes microscópicos está restringida por correlaciones internas. En términos de la **Sinergética de Haken**, esto marca la transición de fase donde los *Parámetros de Orden* esclavizan a los grados de libertad individuales, indicando una "Emergencia Fuerte" y no solo ruido estadístico.
- **CR (Cohesion Ratio):** Relación de cohesión interna/externa (umbral 2.0).
- **Reglas de rechazo:** EDI < 0.30 (sin eficacia macro), EDI > 0.90 (sobreajuste), CR < 2.0 (sin frontera).

La auditoria de validacion resalto la dispersion de criterios; por eso se unificaron en este capitulo y se adoptaron como norma transversal.

## Reproducibilidad
- Hashing de datasets.
- Semillas fijas.
- Entornos replicables.

La reproducibilidad es un requisito epistemico, no un extra tecnico. Sin ella, la tesis no puede sostener afirmaciones ontologicas estables.

## Validez y Limites
- Riesgo de reificacion y de aliasing temporal.
- Clasificacion de datos por dureza: fisicos (nivel alto), proxies digitales (medio), encuestas (bajo).

Esta distincion evita confundir evidencia empirica con evidencia prospectiva.

## Riesgos y Edge Cases
- Sesgo de seleccion → multiples fuentes.
- Divergencia ABM → ajuste de nudging.
- Falta de memoria historica → series sinteticas.

Estas mitigaciones responden a auditorias sobre edge cases: cada riesgo debe tener una estrategia operativa asociada.

## Datos e Instrumentos
Python, numpy, pandas, math. Fuentes: Meteostat, Yahoo Finance, OWID, OPSD, Wikimedia (segun caso).

## Gobernanza de Datos
Filtro de nulos, normalizacion, uso exclusivo de datos abiertos. Esta gobernanza se incorpora como condicion de validez: si la calidad de datos no cumple criterios, la tesis debe abstenerse de validar.

## Casos Piloto
Clima sintetico, Finanzas sinteticas, y caso clima regional como MVP metodologico. Los pilotos prueban el pipeline antes de afirmar existencia ontologica.

## Sintesis
El pipeline discrimina sistemas con estructura macro de agregados caoticos. La metodologia se valida tanto por resultados positivos como por rechazos consistentes.
