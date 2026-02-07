# Caso 25: Ciclo del Fósforo

## Descripción
Validación del hiperobjeto 'Disrupción del Ciclo del Fósforo'. Indicador: consumo de fertilizantes por hectárea (World Bank AG.CON.FERT.ZS).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `AG.CON.FERT.ZS` (consumo de fertilizantes por hectárea)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/25_caso_fosforo/src/validate.py`

## Estado
✅ **Validado** — Emergencia macro confirmada con protocolo C1-C5 completo.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.833 | **0.901** |
| **IC 95%** | [0.784, 0.871] | [0.862, 0.942] |
| **Correlación ABM** | 0.810 | 0.881 |
| **Correlación ODE** | 0.707 | 0.883 |
| **CR (Symploké)** | 1.000 | 1.000 |
| **overall_pass** | ✅ | ✅ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Diagnóstico:** Validación exitosa. El EDI real (0.90) se sitúa en el límite superior del rango aceptable, indicando fuerte dependencia macro. Ambas correlaciones superan 0.88, confirmando convergencia robusta ABM-ODE sobre datos reales. El consumo de fertilizantes como proxy del ciclo del fósforo captura adecuadamente la dinámica de acumulación global: el hiperobjeto «Disrupción del Ciclo del Fósforo» exhibe causalidad descendente medible y emergencia metaestable.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
