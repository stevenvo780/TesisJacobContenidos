# Caso 22: Acidificación Oceánica

## Descripción
Validación del hiperobjeto 'Acidificación Oceánica' como sistema distribuido con eficacia causal medible. Indicador proxy: emisiones de CO2 per cápita (World Bank EN.ATM.CO2E.PC).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `EG.USE.PCAP.KG.OE` (consumo energético per cápita)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/12_caso_acidificacion_oceanica/src/validate.py`

## Estado
⚠️ **Parcial** — EDI en rango válido pero convergencia insuficiente.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.386 | **0.737** |
| **IC 95%** | [0.319, 0.468] | [0.609, 0.849] |
| **Correlación ABM** | 0.274 | 0.361 |
| **Correlación ODE** | 0.225 | 0.374 |
| **CR (Symploké)** | 14.74 | 1.005 |
| **overall_pass** | ❌ | ❌ |

**Protocolo C1-C5 (fase real):** C1=❌ C2=✅ C3=✅ C4=✅ C5=✅

**Diagnóstico:** El EDI real (0.74) supera ampliamente el umbral de 0.30, indicando estructura macro detectable. Sin embargo, C1 (convergencia) falla: las correlaciones ABM-observación y ODE-observación son moderadas (~0.36), lo que impide validar la convergencia completa del modelo híbrido. El indicador proxy (consumo energético) captura la tendencia global pero no la dinámica fina de acidificación oceánica.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
