# Caso 26: Erosión Dialéctica del Discurso

## Descripción
Validación del hiperobjeto 'Erosión Dialéctica' como degradación sistémica del discurso racional. Indicador proxy: tasa de alfabetización adulta (World Bank SE.ADT.LITR.ZS).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `SE.ADT.LITR.ZS` (tasa de alfabetización adulta)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/17_caso_erosion_dialectica/src/validate.py`

## Estado
⚠️ **Parcial** — EDI válido y alta correlación, pero convergencia C1 falla.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.715 | **0.739** |
| **IC 95%** | [0.651, 0.779] | [0.705, 0.776] |
| **Correlación ABM** | 0.674 | 0.992 |
| **Correlación ODE** | 0.611 | 0.991 |
| **CR (Symploké)** | 1.000 | 1.000 |
| **overall_pass** | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=✅ C5=✅

**Diagnóstico:** Caso paradójico. Las correlaciones en fase real son excepcionalmente altas (>0.99), y el EDI (0.74) confirma estructura macro. Sin embargo, C1 falla en la fase sintética (corr ~0.67), lo que arrastra el veredicto global. La tasa de alfabetización presenta una tendencia monotónica creciente que el modelo replica con facilidad, pero la prueba de convergencia sintética exige un umbral más estricto. El hiperobjeto «Erosión Dialéctica» muestra señales de emergencia parcial; un proxy más volátil podría mejorar la discriminación.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
