# 03 Validacion y Praxis — Narrativa Unificada

## Enfoque de Validacion
La validacion distingue entre evidencia empirica (datasets largos y duros) y evidencia prospectiva (proxies o series cortas). Se aplica C1-C5 como filtro tecnico.

Las auditorias de validacion exigieron coherencia entre criterios y reportes. Por eso esta seccion sintetiza resultados y limites en un solo hilo.

## Estados de Fallo
- **EDI < 0.30:** no hay eficacia macro.
- **EDI > 0.90:** sobreajuste.
- **CR < 2.0:** ausencia de frontera.

## Resultados Clave con Nivel de Evidencia (LoE)
El sistema de clasificación LoE (1-5) indica la robustez de los datos (5 = Datos físicos >30 años; 1 = Datos sintéticos/teóricos).

- **Validados (con código ejecutable, superan umbrales):**
    - Contaminacion (LoE 4): EDI 0.423, CR 2.472.
    - Movilidad (LoE 2): EDI 0.740, CR 5.273. Series cortas, prototipo.

- **No validados (con código ejecutable, no superan ambos umbrales):**
    - Clima (LoE 5): EDI 0.103 (< 0.30), CR 2.355 (> 2.0). Cohesión interna adecuada pero estructura macro débil en zero-nudging.
    - Finanzas (LoE 5): EDI 0.769 (> 0.30), CR 1.078 (< 2.0). EDI alto pero sin frontera sistémica.
    - Casos Prospectivos (Energía, Wikipedia, Justicia, etc.): Aunque poseen código funcional y datos reales/sintéticos, sus métricas actuales no satisfacen simultáneamente EDI > 0.30 y CR > 2.0 bajo el protocolo estricto de Zero-Nudging, o presentan riesgos de sobreajuste que requieren mayor depuración paramétrica.

## Post-Mortem y Falsacion
La existencia de código ejecutable para los 18 casos permite una auditoría profunda de los estados de fallo. El caso Finanzas establece la frontera epistémica por reflexividad, mientras que los casos de Falsación (Exogeneidad, No-Estacionariedad) demuestran que el sistema es capaz de rechazar estructuras que no poseen una causalidad macro real. Las pruebas de exogeneidad, ruido blanco e invisibilidad de agentes refuerzan que los éxitos no son artefactos del código, sino propiedades detectadas en la dinámica del sistema.

## Conclusiones
La praxis no busca confirmar la hipotesis, sino sobrevivir intentos de refutacion. El marco se valida por su capacidad de discriminar dominios con estructura macro estable.
