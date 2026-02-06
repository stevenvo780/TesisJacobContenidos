# 03_8 Matriz de Validación: Casos Base y Falsación

Estado consolidado de resultados en casos base y falsación.

## Casos base
| Caso de Estudio | EDI (Emergencia) | CR (Cohesión) | Estado de Validación | Veredicto |
| :--- | :--- | :--- | :--- | :--- |
| **Clima** | 0.45 | 2.5 | PASS (C1-C5) | **VALIDADO** |
| **Contaminación** | 0.52 | 2.8 | PASS (C1-C5) | **VALIDADO** |
| **Energía** | 0.38 | 2.4 | PASS (C1-C5) | **VALIDADO** |
| **Epidemiología** | 0.55 | 3.2 | PASS (C1-C5) | **VALIDADO** |
| **Wikipedia** | 0.41 | 2.6 | PASS (C1-C5) | **VALIDADO** |
| **Paradigmas** | 0.44 | 2.28 | PASS (C1-C5) | **VALIDADO** |
| **Estética** | 0.36 | 2.2 | PASS (C1-C5) | **VALIDADO** |
| **Justicia** | 0.34 | 2.15 | PASS (C1-C5) | **VALIDADO** |
| **Conciencia** | 0.33 | 2.05 | PASS (C1-C5) | **VALIDADO** |
| **Postverdad** | 0.31 | 2.02 | PASS (C1-C5) | **VALIDADO** |
| **Movilidad** | 0.32 | 2.1 | WEAK PASS | **PROTOTIPO** |
| **Finanzas (SPY)** | 0.05 | 1.1 | FAIL (C4) | **RECHAZADO** |

## Casos de falsación
| Caso de Falsación | Resultado | Fallo principal |
| :--- | :--- | :--- |
| **Exogeneidad y shock** | FAIL | C1 (convergencia) |
| **Observabilidad insuficiente** | FAIL | C1 y C5 (cobertura) |
| **No‑estacionariedad extrema** | FAIL | C1 y C4 (validez) |

## Nota de Integridad
Los casos de falsación están diseñados para fallar; su ejecución refuerza la falsabilidad del marco.
