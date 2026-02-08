# Caso 27: Contaminación por Microplásticos

## Descripción
Validación del hiperobjeto 'Microplásticos' como contaminante distribuido. Indicador proxy: consumo de energía fósil como % total (World Bank EG.USE.COMM.FO.ZS).

## Datos
- **Fuente:** World Bank Open Data
- **Indicador:** `EG.USE.COMM.FO.ZS` (consumo de energía fósil % del total)
- **Resolución:** Anual
- **Pipeline:** `repos/Simulaciones/06_caso_microplasticos/src/validate.py`

## Estado
⚠️ **Parcial** — EDI válido pero desacoplamiento ODE y C5 falla.

## Resultados
| Métrica | Fase Sintética | Fase Real |
|---------|---------------|-----------|
| **EDI** | 0.833 | **0.432** |
| **IC 95%** | [0.784, 0.871] | [0.243, 0.581] |
| **Correlación ABM** | 0.810 | 0.917 |
| **Correlación ODE** | 0.707 | 0.018 |
| **CR (Symploké)** | 1.000 | 4.359 |
| **overall_pass** | ✅ | ❌ |

**Protocolo C1-C5 (fase real):** C1=✅ C2=✅ C3=✅ C4=✅ C5=❌

**Diagnóstico:** El EDI real (0.43) supera el umbral mínimo, pero C5 (incertidumbre) falla, indicando alta sensibilidad paramétrica. El hallazgo más relevante es el desacoplamiento macro: la correlación ODE-observación es prácticamente nula (0.02), mientras que el ABM por sí solo alcanza 0.92. Esto sugiere que la capa micro captura la dinámica sin necesidad de la ecuación macro, señalando posible epifenomenalismo parcial. El proxy de energía fósil tiene relación indirecta con la producción de plásticos pero no captura la dinámica de dispersión de micropartículas.

## Modelo Híbrido
- **ABM:** Grid 20×20 agentes con difusión espacial + acoplamiento macro
- **ODE:** `dX/dt = α(F - βX) + noise` con asimilación de datos
- **Protocolo:** C1-C5, Symploké, No-localidad, Persistencia, Emergencia
