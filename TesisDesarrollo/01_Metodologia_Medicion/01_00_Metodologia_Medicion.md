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
1. **EDI < 0.30:** Inexistencia de estructura macro → **RECHAZO**
2. **Coupling < 0.10:** Epifenomenalismo (Inercia sin agencia) → **RECHAZO**
3. **RMSE < 1e-10:** Fraude por sobreajuste (Copy-paste de datos) → **RECHAZO**
4. **EDI > 0.90:** Flag de tautología — revisión manual pero **no rechazo automático**
5. **forcing_scale ≥ 1.0:** Cap en calibración — forzamiento externo no amplifica por encima de la unidad
6. **C1-C5 protocolo completo:** 11 condiciones simultáneas requeridas para `overall_pass`

Nota: La regla 4 evolucionó de rechazo a flag tras verificar que EDI > 0.90 es alcanzable legítimamente en modelos bien calibrados con señales de tendencia (casos 12, 17, 28, entre otros). El protocolo C1-C5 discrimina tautología de emergencia genuina.

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
