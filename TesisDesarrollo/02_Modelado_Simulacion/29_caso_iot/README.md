# Caso 32: Emergencia IoT

## Descripción
Validación del hiperobjeto 'Internet de las Cosas' como sistema emergente de conectividad global. Indicador: suscripciones móviles por 100 personas (World Bank IT.CEL.SETS.P2).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `IT.CEL.SETS.P2` (suscripciones móviles por 100 personas)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/17_caso_iot/src/validate.py`

## Estado
⚠️ **Parcial** — EDI válido pero convergencia C1 insuficiente.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.833 | **0.477** |
| **IC 95%** | [0.784, 0.871] | [0.459, 0.488] |
| **Correlación ABM** | 0.810 | 0.995 |
| **Correlación ODE** | 0.707 | 0.980 |
| **CR (Symploké)** | 1.000 | 1.000 |
| **overall_pass** | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=✅ C5=✅

**Diagnóstico:** El EDI real (0.48) confirma estructura macro operativa, y las correlaciones son excelentes (>0.98). Sin embargo, C1 falla, impidiendo la validación completa. La caída de EDI entre fase sintética (0.83) y real (0.48) indica que el modelo híbrido pierde poder explicativo al enfrentar datos reales con mayor complejidad estructural. Las suscripciones móviles presentan una curva de saturación tipo sigmoide que el ABM captura bien por sí solo, reduciendo la ganancia marginal del acoplamiento ODE. El hiperobjeto «IoT» muestra señales de emergencia pero requiere un proxy con mayor variabilidad para discriminar la contribución macro.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
