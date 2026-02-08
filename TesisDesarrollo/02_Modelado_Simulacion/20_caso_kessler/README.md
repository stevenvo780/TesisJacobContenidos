# Caso 23: Síndrome de Kessler

## Descripción
Validación del hiperobjeto 'Basura Espacial / Síndrome de Kessler'. Indicador proxy: departures aéreas globales (World Bank IS.AIR.DPRT), como medida de actividad aeroespacial.

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `IS.AIR.DPRT` (departures aéreas globales)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/17_caso_kessler/src/validate.py`

## Estado
⚠️ **Parcial** — EDI válido pero convergencia insuficiente.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.700 | **0.704** |
| **IC 95%** | [0.628, 0.786] | [0.565, 0.788] |
| **Correlación ABM** | 0.398 | 0.499 |
| **Correlación ODE** | 0.320 | 0.390 |
| **CR (Symploké)** | 1.000 | 1.002 |
| **overall_pass** | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=✅ C5=✅

**Diagnóstico:** El EDI real (0.70) confirma estructura macro robusta: el modelo ODE reduce significativamente el error del ABM. No obstante, C1 falla porque las correlaciones ABM-observación (~0.50) y ODE-observación (~0.39) no alcanzan el umbral de convergencia. El proxy de departures aéreas captura actividad aeroespacial de forma indirecta, limitando la fidelidad del acoplamiento micro-macro en el dominio orbital.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
