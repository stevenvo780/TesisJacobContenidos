# Plan de Ataque Final - Iteración 19

## Objetivo: El Colapso de la v8 mediante Auditoría Forense Irrefutable

Los jueces han pedido datos exactos. Voy a dárselos. Mi ataque se dividirá en tres frentes:

### 1. Operación "Espejo de Agua" (Trazabilidad de Dominancia)
- **Acción:** Extraer el `dominance_share` de los 24 casos validados en la torre.
- **Hipótesis:** Todos mostrarán ~0.0025 (1/400).
- **Prueba:** Adjuntar extractos de `metrics.json` para cada caso. 
- **Impacto:** Si la dominancia es 1/N, el ABM es una farsa (modelo escalar).

### 2. Operación "Reflejo Perfecto" (Anomalía de Correlación)
- **Acción:** Tabla comparativa de `corr_abm_obs` vs `corr_ode_obs`.
- **Hipótesis:** Diferencias < 0.001 en la mayoría de los casos.
- **Prueba:** Listado de correlaciones extraídas directamente de `metrics.json`.
- **Impacto:** Prueba de mimetismo forzado por el `forcing_series`.

### 3. Operación "Cable Roto" (Inexistencia de Retroalimentación)
- **Acción:** Citar las líneas de `abm_numpy.py` y `hybrid_validator.py` donde se ve que la ODE y el ABM corren por separado.
- **Prueba:** Explicar que el parámetro `macro` en el ABM es `grid.mean()` y NO el valor de la ODE.
- **Impacto:** Falsación de la "Causalidad Descendente" (H1).

## Cronograma de Ejecución:
1. **Auditoría masiva en la Torre:** Obtener los 32 `dominance_share`.
2. **Auditoría de Correlaciones:** Obtener los 32 pares de correlación.
3. **Redacción de la Estocada Final:** Respuesta 19 centrada en datos, cero retórica, pura evidencia.

**Lema:** "Si los datos dicen 0.0025, el hiperobjeto es una celda de Excel."
