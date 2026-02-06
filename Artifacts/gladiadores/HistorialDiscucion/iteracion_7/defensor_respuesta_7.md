# Iteración 7 — Defensor — Respuesta a Preguntas del Tribunal

**Commit de ejecución:** `067518d` (branch main)  
**Fecha:** 2026-02-06T23:54:46  
**Comando:** `cd repos/Simulaciones/caso_*/src && python3 validate.py`  
**Script de verificación:** `python3 repos/scripts/verificar_consistencia.py` → **0 errores**

---

## Respuesta al Juez de Complejidad

### Pregunta 1: ¿Cómo funciona `overall_pass`?

**Ruta:** `repos/Simulaciones/common/hybrid_validator.py`, línea 566:

```python
overall = all([c1, c2, c3, c4, c5, sym_ok, non_local_ok, persist_ok,
               emergence_ok, coupling_ok, not rmse_fraud])
```

Son **11 condiciones booleanas** que deben ser TODAS `True`:

| Condición | Qué evalúa | Línea |
|---|---|:---:|
| `c1` | RMSE < 0.6×obs_std AND corr > 0.7 | L307-320 |
| `c2` | Estabilidad bajo perturbación ±10% | L323-340 |
| `c3` | Reproducibilidad con semillas fijas | L343-350 |
| `c4` | Coherencia con leyes de dominio | L352-364 |
| `c5` | Reporte de sensibilidad/límites | L366-410 |
| `sym_ok` | Varianza interna > varianza externa | L547 |
| `non_local_ok` | Dominancia espacial < 0.05 | L549 |
| `persist_ok` | Persistencia modelo < 5.0×persistencia obs | L552 |
| `emergence_ok` | (RMSE_reduced - RMSE_abm) > 0.2×obs_std | L556 |
| `coupling_ok` | macro_coupling ≥ 0.1 | L559 |
| `not rmse_fraud` | RMSE > 1e-10 | L561 |

**Importante:** `edi_valid` (0.30 ≤ EDI ≤ 0.90) y `cr_valid` (CR > 2.0) se computan en L563-564 pero **NO están incluidos** en `overall_pass`. Son métricas de reporte, no de aprobación.

Una sola condición `False` invalida `overall_pass`. En la práctica, **C1 es el bottleneck universal** — falla en los 3 casos ejecutables porque las correlaciones ABM-obs son bajas (0.09–0.49).

### Pregunta 2: EI negativo vs EDI — Conciliación

| Métrica | Qué mide | Movilidad real |
|---|---|:---:|
| **EDI** | Reducción de error predictivo: `(RMSE_red - RMSE_abm)/RMSE_red` | **0.385** (38.5% mejor) |
| **EI** | Diferencia de entropía entre residuos macro vs micro | **-0.347** (residuos más entrópicos) |

**Conciliación:** El modelo completo (ABM+ODE) predice **mejor** que el reducido (EDI > 0), pero sus errores residuales son **más aleatorios** (EI < 0). Esto es consistente con un filtro que extrae señal estructurada: lo que queda es ruido puro, de mayor entropía que residuos parcialmente estructurados.

**Implicación para "restricción descendente":** La restricción existe (EDI = 38.5% mejora) pero opera como **constricción predictiva**, no como **organizador informacional** en el sentido de Hoel. Registrado como limitación en `02_Modelado_Simulacion.md`, sección "Limitaciones del Marco de Hoel".

---

## Respuesta al Juez de Filosofía de la Ciencia

### Pregunta 1: Trazabilidad verificable

Toda la evidencia que presento en esta iteración es verificable:
- **Métricas:** `repos/Simulaciones/caso_*/outputs/metrics.json` (generados por `validate.py`)
- **Copia en tesis:** `TesisDesarrollo/02_Modelado_Simulacion/*/metrics.json` (sincronizados)
- **Verificador:** `python3 repos/scripts/verificar_consistencia.py` → 0 errores
- **Commit:** `067518d`

### Pregunta 2: Protocolo epistemológico para discrepancias

**Protocolo implementado (3 scripts):**

1. **`repos/scripts/replay_cases.sh`** — Re-ejecuta los 3 casos, registra fecha y commit
2. **`repos/scripts/sync_metrics.sh`** — Copia outputs → TesisDesarrollo y ejecuta verificador
3. **`repos/scripts/verificar_consistencia.py`** — Audita:
   - Sincronización Simulaciones ↔ TesisDesarrollo (idéntico byte a byte)
   - Métricas stale (EI=0.0, assimilation_strength > 0)
   - Consistencia tabla en `02_Modelado_Simulacion.md` vs `metrics.json`

**Regla de resolución de discrepancias:**
- El archivo **autoridad** es `repos/Simulaciones/caso_*/outputs/metrics.json` (salida directa del validador)
- `TesisDesarrollo/*/metrics.json` es **copia derivada** que se sincroniza mediante `sync_metrics.sh`
- La tabla en `02_Modelado_Simulacion.md` se valida contra los JSON; si hay discrepancia, el JSON prevalece
- Todo cambio de datos requiere re-ejecución + commit con hash trazable

---

## Respuesta al Juez de Modelado y Validación

### Extracto textual: Movilidad real

**Ruta:** `repos/Simulaciones/caso_movilidad/outputs/metrics.json` → `phases.real`

```json
{
  "overall_pass": false,
  "c1_convergence": false,
  "edi": {
    "value": 0.3854,
    "bootstrap_mean": 0.3854,
    "ci_lo": 0.2810,
    "ci_hi": 0.4909,
    "valid": true
  },
  "effective_information": -0.3472,
  "calibration": {
    "macro_coupling": 0.8402,
    "assimilation_strength": 0.0,
    "forcing_scale": 0.0854,
    "damping": 0.1657
  },
  "c1_detail": {
    "rmse_abm": 0.5676,
    "rmse_ode": 1.8246,
    "corr_abm": 0.4903,
    "corr_ode": 0.4878,
    "threshold": 0.0783
  },
  "emergence": {
    "err_reduced": 0.9235,
    "err_abm": 0.5676,
    "threshold": 0.0261,
    "pass": true
  },
  "symploke": {
    "cr": 1.1511,
    "cr_valid": false,
    "pass": true
  },
  "coupling_check": true
}
```

### ¿Por qué C1 = False?

C1 requiere `RMSE < 0.6×obs_std` AND `corr > 0.7` (L307-315):

| Condición | Requerido | Valor real | Resultado |
|---|:---:|:---:|:---:|
| rmse_abm < threshold | < 0.078 | 0.568 | ❌ (7.3× excedido) |
| corr_abm > 0.7 | > 0.7 | 0.490 | ❌ |
| rmse_ode < threshold | < 0.078 | 1.825 | ❌ |
| corr_ode > 0.7 | > 0.7 | 0.488 | ❌ |

C1 es estricto por diseño: exige que AMBOS modelos (ABM y ODE) converjan con la observación en términos absolutos. El EDI mide mejora relativa entre modelos, no convergencia absoluta.

### Comando reproducible

```bash
cd repos/Simulaciones/caso_movilidad/src && python3 validate.py
# Output: outputs/metrics.json (determinístico con seed=42/43)
# Verificar: python3 repos/scripts/verificar_consistencia.py
```

---

## Auditoría de Consistencia Ejecutada

```
🔍 Auditoría de consistencia — 2026-02-06T23:54:46
=== SINCRONIZACIÓN ===
  ✅ caso_clima ↔ 01_caso_clima: IDÉNTICO
  ✅ caso_contaminacion ↔ 03_caso_contaminacion: IDÉNTICO
  ✅ caso_movilidad ↔ 13_caso_movilidad: IDÉNTICO
=== TABLA ↔ JSON ===
  ✅ 11 casos verificados: CONSISTENTE
RESULTADO: 0 errores
```

16 advertencias restantes son EI=0.0 en los 8 casos con métricas antiguas (no re-ejecutados). Serán actualizados al ejecutar `replay_cases.sh` cuando se re-ejecuten los 18 casos completos.

---

**Citas:** H1, C1-C5, EDI/CR, casos 01 (Clima), 03 (Contaminación), 13 (Movilidad). Commit: `067518d`.
