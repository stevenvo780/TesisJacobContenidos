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

- **Validados (Empíricos):**
    - Clima (LoE 5): Robusto, EDI 0.45.
    - Energia (LoE 4): Estable, EDI 0.38.
    - Epidemiologia (LoE 4): Fuerte acople, EDI 0.55.
    - Contaminacion (LoE 4): Memoria alta, EDI 0.52.
    - Wikipedia (LoE 3): Dinámica digital clara, EDI 0.41.

- **Prospectivos:**
    - Postverdad (LoE 2): Proxies indirectos, EDI 0.34.

- **Teoricos (Baja Certeza):**

- **Rechazado:**
    - Finanzas (LoE 5): Falla técnica por alta frecuencia. EDI espurio < 0.10 real.

- **Prototipo:**
    - Movilidad (LoE 2): Series cortas.

## Post-Mortem y Falsacion
El caso Finanzas establece la frontera epistemica del modelo: alta reflexividad y alta frecuencia impiden un parametro de orden estable. Las pruebas de exogeneidad, ruido blanco e invisibilidad de agentes refuerzan que los exitos no son tautologias.

## Conclusiones
La praxis no busca confirmar la hipotesis, sino sobrevivir intentos de refutacion. El marco se valida por su capacidad de discriminar dominios con estructura macro estable.
