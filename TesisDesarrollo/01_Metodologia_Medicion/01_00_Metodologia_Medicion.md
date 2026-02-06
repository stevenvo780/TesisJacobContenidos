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
    - **Umbral > 0.30 (Derivación):** Basado en el **Teorema de Codificación de Canal de Shannon**, el 30% marca el punto donde la "Capacidad del Canal Macro" supera el ruido estocástico del micro. Si la estructura macro no reduce al menos un 30% de la incertidumbre microscópica, no hay transmisión de orden causal efectiva; el sistema es dominado por fluctuaciones locales.
- **Requisito de Acoplamiento Macro-Micro (Downward Causation):** Un EDI alto es condición necesaria pero NO suficiente. Se exige un parámetro de acoplamiento ($\lambda > 0.1$) en el modelo ABM. Si el modelo micro es independiente del macro (acoplamiento nulo), un EDI alto se descarta como **Inercia de Datos** o **Aliasing Temporal** (caso Finanzas/Estética).
- **CR (Cohesion Ratio):** Relación de cohesión interna/externa (umbral 2.0).

## Reglas de Rechazo Hard-Coded
1. **EDI < 0.30:** Inexistencia de estructura macro.
2. **Coupling < 0.10:** Epifenomenalismo (Inercia sin agencia).
3. **RMSE < e-10:** Fraude por sobreajuste (Copy-paste de datos).
4. **EDI > 0.90:** Tautología o error de calibración.

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
