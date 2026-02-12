# Tesis: Irrealismo Operativo de Hiperobjetos

## Objetivo
Medir el **cierre operativo** de fenómenos de gran escala (hiperobjetos) mediante un motor de simulación híbrido (ODE+ABM) y un protocolo de validación C1-C5 con zero-nudging.

## Instalación
```bash
pip install -r repos/Simulaciones/requirements.txt
```

## Resultados Principales

### Paisaje de Emergencia Operativa (29 Casos)

| Nivel | Categoría | Conteo | Porcentaje |
|:-----:|:----------|:------:|:----------:|
| 4 | Cierre Operativo Fuerte (strong) | 11 | 37.9% |
| 2 | Señal Sugestiva (suggestive) | 2 | 6.9% |
| 1 | Tendencia (trend) | 6 | 20.7% |
| 0 | Sin Señal (null) | 7 | 24.1% |
| — | Falsificación (controles) | 3 | 10.3% |

- **overall_pass=True:** 9/29 (Epidemiología, Movilidad, Políticas, Postverdad, Wikipedia, Urbanización, Kessler, Fósforo, Riesgo Biológico)
- **Significancia** (p<0.05 + EDI>0.01): 11/29
- **Falsaciones:** 3/3 correctamente rechazadas
- **Reproducibilidad:** seed=42, 999 permutaciones

### Casos con Mayor EDI
| Caso | EDI | overall_pass | Nota |
|:-----|----:|:---:|:---|
| Microplásticos | 0.656 | No | Falla C2 |
| Deforestación | 0.589 | No | Falla C2 |
| Kessler | 0.381 | Sí | |
| Fósforo | 0.376 | Sí | |
| Postverdad | 0.325 | Sí | |
| Políticas | 0.288 | Sí | |
| Riesgo Bio. | 0.266 | Sí | |

## Estructura de la Tesis (Lectura recomendada)

1. `TesisDesarrollo/00_Marco_Conceptual/` — Fundamentación filosófica (Irrealismo Operativo)
2. `TesisDesarrollo/01_Metodologia_Medicion/` — Protocolo C1-C5, métricas (EDI, LoE)
3. `TesisDesarrollo/02_Modelado_Simulacion/` — Motor híbrido (ABM+ODE) y 29 casos
4. `TesisDesarrollo/03_Validacion_Praxis/` — Resultados consolidados y paisaje de emergencia
5. `TesisDesarrollo/04_Casos_De_Estudio/` — Síntesis cualitativa de cada caso
6. `TesisDesarrollo/05_Bibliografia/` — Referencias nucleares
7. `TesisFinal/Tesis.md` — Documento compilado

Ejercicios Críticos:
- `TesisDesarrollo/EjerciciosCriticos/Ejercicio_Critico_Gladiadores_Partida1.md`
- `TesisDesarrollo/EjerciciosCriticos/Trazas_Mejoras_Possibles_Dudas.md`
- `TesisFinal/documentacion_procedimental.md`

## Mapa de Código
- `repos/Simulaciones/common/` — Motor híbrido y validador
- `repos/Simulaciones/01_caso_clima/` … `29_caso_iot/` — 29 simulaciones
- `repos/scripts/tesis.py` — Compilador de tesis
- `repos/scripts/actualizar_tablas_002.py` — Generador de tablas
