# Caso 30: Riesgo Biológico Global

## Descripción
Validación del hiperobjeto 'Riesgo Biológico' como amenaza sistémica. Indicador: tasa de mortalidad infantil bajo 5 años (World Bank SH.DYN.MORT).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `SH.DYN.MORT` (mortalidad infantil menores de 5 años)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/06_caso_riesgo_biologico/src/validate.py`

## Estado
❌ **Rechazado** — EDI > 0.90, sospecha de tautología.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.833 | **0.917** |
| **IC 95%** | [0.784, 0.871] | [0.896, 0.944] |
| **Correlación ABM** | 0.810 | 0.988 |
| **Correlación ODE** | 0.707 | 0.986 |
| **CR (Symploké)** | 1.000 | 0.989 |
| **overall_pass** | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=✅

**Diagnóstico:** Todos los criterios C1-C5 pasan individualmente, pero el EDI real (0.92) excede el umbral de tautología (0.90), activando la regla de rechazo por sobredeterminación. Esto significa que la capa macro explica casi toda la varianza micro, indicando posible circularidad en el acoplamiento. La mortalidad infantil sigue una tendencia decreciente global altamente predecible que el modelo ODE captura trivialmente. El hiperobjeto «Riesgo Biológico» no se invalida conceptualmente, pero el proxy elegido es demasiado regular para discriminar emergencia genuina de mero ajuste de tendencia.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
