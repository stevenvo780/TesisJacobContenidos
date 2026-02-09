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
- **EDI (Effective Dependence Index):** Mide la **indispensabilidad causal** del nivel macro. No es simplemente una reducción de entropía, sino la demostración de que el comportamiento observado no puede explicarse solo por interacciones locales.
- **Interpretación Ontológica del EDI:** Un EDI > 0.30 indica que eliminar el nivel macro (ablación) causa una pérdida de información irrecuperable.
- **Ablación como Intervención Causal:** Siguiendo a Woodward (2003), la manipulación de `forcing_scale=0` es una intervención controlada. Si el sistema colapsa predictivamente bajo esta intervención, se demuestra la realidad causal de la variable intervenida (el hiperobjeto).
- **Regla de Descuento por Nivel de Evidencia (LoE):** Para evitar la reificación de constructos débiles, el EDI se pondera por la calidad de los datos subyacentes.
  $$EDI_{ponderado} = EDI \times \frac{LoE}{5}$$
  Esto penaliza hipótesis con datos indirectos (ej. Conciencia, LoE=1) frente a sistemas físicos robustos (ej. Clima, LoE=5).

## Niveles de Evidencia (LoE)
1. **LoE 1 (Especulativo):** Proxies indirectos, encuestas subjetivas, o datos sintéticos sin ground truth físico. (Ej. Conciencia).
2. **LoE 2 (Débil):** Datos digitales traza (Google Trends, Twitter) con alto ruido semántico.
3. **LoE 3 (Medio):** Datos estructurados pero incompletos o de corto plazo (< 5 años).
4. **LoE 4 (Fuerte):** Series temporales consistentes, múltiples fuentes, > 10 años.
5. **LoE 5 (Robusto):** Datos físicos directos (sensores), estandarizados internacionalmente, > 30 años. (Ej. Clima, Océanos).


## Reglas de Rechazo y Validación Ponderada
1. **EDI_ponderado < 0.20:** Inexistencia de estructura macro robusta → **RECHAZO**
2. **EDI > 0.30 pero LoE < 3:** Emergencia especulativa → **PROTOTIPO** (No validada ontológicamente)
3. **Coupling < 0.10:** Epifenomenalismo (Inercia sin agencia) → **RECHAZO**
4. **RMSE < 1e-10:** Fraude por sobreajuste (Copy-paste de datos) → **RECHAZO**
5. **EDI > 0.90:** Flag de tautología — revisión manual.
6. **forcing_scale ≥ 1.0:** Cap en calibración — forzamiento externo no amplifica por encima de la unidad.
7. **C1-C5 protocolo completo:** Condición necesaria para validez técnica. (EDI ponderado es condición para validez ontológica).

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
