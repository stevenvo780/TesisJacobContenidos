# Caso 24: Salinización de Suelos

## Descripción
Validación del hiperobjeto 'Salinización' como degradación sistémica del suelo. Indicador: tierra cultivable como % del territorio (World Bank AG.LND.ARBL.ZS).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `AG.LND.ARBL.ZS` (tierra cultivable % del territorio)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/24_caso_salinizacion/src/validate.py`

## Estado
❌ **Rechazado** — EDI < 0.30, sin estructura macro detectable.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.824 | **0.164** |
| **IC 95%** | [0.771, 0.872] | [0.089, 0.247] |
| **Correlación ABM** | 0.790 | −0.275 |
| **Correlación ODE** | 0.698 | 0.802 |
| **CR (Symploké)** | 1.000 | 26.899 |
| **overall_pass** | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=❌ C3=✅ C4=✅ C5=✅

**Diagnóstico:** Caso de falsación clara. El EDI real (0.16) cae por debajo del umbral de 0.30 y su intervalo de confianza no lo incluye, lo que indica ausencia de estructura macro operativa. La correlación ABM-observación es negativa (−0.28), señalando que el modelo micro diverge de los datos reales. El proxy de tierra cultivable no captura adecuadamente la dinámica de salinización, que opera a escalas espaciales más finas que las disponibles en datos agregados del Banco Mundial. La fase sintética validó (EDI=0.82), confirmando que el motor es correcto pero el proxy es inadecuado.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
