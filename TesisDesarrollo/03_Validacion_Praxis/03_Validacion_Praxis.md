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

- **No validados (con código ejecutable, no superan umbrales):**
    - Clima (LoE 5): EDI 0.074 (< 0.30), CR 1.102 (< 2.0). Estructura macro débil.
    - Finanzas (LoE 5): EDI -0.020, macro_coupling=0.0. Falla por reflexividad.

- **Tautológicos (sin código ejecutable, métricas invalidadas):**
    - Energia (LoE 4), Epidemiologia (LoE 4), Conciencia, Estetica, Justicia, Paradigmas, Postverdad (LoE 2), Wikipedia (LoE 3): rmse_abm ≈ 0 por assimilation_strength inflado en modelo reducido. EDI previo (1.000) era artefacto de comparación injusta.

## Post-Mortem y Falsacion
El caso Finanzas establece la frontera epistemica del modelo: alta reflexividad y alta frecuencia impiden un parametro de orden estable. Las pruebas de exogeneidad, ruido blanco e invisibilidad de agentes refuerzan que los exitos no son tautologias.

## Conclusiones
La praxis no busca confirmar la hipotesis, sino sobrevivir intentos de refutacion. El marco se valida por su capacidad de discriminar dominios con estructura macro estable.
