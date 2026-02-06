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

## Metricas y Justificación Teórica: Emergencia Metaestable
- **EDI (Effective Dependence Index):** Mide la reducción de entropía del sistema micro gracias a la estructura macro.
- **Causalidad Acoplada (Nudging Constitutivo):** El descubrimiento fundamental de esta investigación es que los Hiperobjetos no operan como estructuras autónomas (Atractores Fuertes), sino como **Atractores Metaestables**. 
- **La Función del Nudging:** Se postula que el *Nudging* (asimilación activa) no es un artefacto de cálculo, sino la formalización matemática del acoplamiento causal entre el Hiperobjeto y su base material. La validación se obtiene si la estructura macro logra organizar el micro bajo condiciones de acoplamiento real, demostrando una **Eficacia Causal Mediada**.
- **Información Efectiva (EI):** Se mide si el sistema acoplado (Híbrido) es más informativo y predictivo que la suma de sus partes. El Hiperobjeto es real en tanto es una **capa de ordenamiento informacional** persistente.


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
