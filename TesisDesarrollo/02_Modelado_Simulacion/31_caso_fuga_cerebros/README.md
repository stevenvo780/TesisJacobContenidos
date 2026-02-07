# Caso 31: Fuga de Cerebros Global

## Descripción
Validación del hiperobjeto 'Fuga de Cerebros' como flujo migratorio sistémico. Indicador: migración neta (World Bank SM.POP.NETM).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `GB.XPD.RSDV.GD.ZS` (gasto en I+D % del PIB)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/31_caso_fuga_cerebros/src/validate.py`

## Estado
✅ **Validado** — Emergencia macro confirmada con protocolo C1-C5 completo.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.450 | **0.433** |
| **IC 95%** | [0.368, 0.563] | [0.339, 0.480] |
| **Correlación ABM** | 0.291 | 0.970 |
| **Correlación ODE** | 0.372 | 0.978 |
| **CR (Symploké)** | 4.945 | 0.999 |
| **overall_pass** | ❌ | ✅ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Diagnóstico:** Validación exitosa con EDI moderado (0.43), bien dentro del rango [0.30, 0.90]. Las correlaciones reales son altas (>0.97), confirmando convergencia robusta del modelo híbrido sobre datos de gasto en I+D. El EDI moderado —lejos del límite de tautología— es epistemológicamente favorable: indica que la capa macro aporta información genuina sin dominar trivialmente al sistema micro. El hiperobjeto «Fuga de Cerebros» exhibe emergencia metaestable moderada, coherente con la naturaleza distribuida y multifactorial de los flujos de capital humano.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
