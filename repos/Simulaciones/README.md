# Simulaciones

29 casos de simulación híbrida ABM+ODE para la tesis "Irrealismo Operativo de Hiperobjetos".

## Estructura por caso

Cada `XX_caso_NAME/src/` contiene 4 archivos canónicos:

| Archivo | Rol |
|---------|-----|
| `validate.py` | Orquestador: calibrar → simular → evaluar C1–C5 → escribir outputs |
| `abm.py` | Capa micro: grid n×n con difusión, acoplamiento macro, forcing, damping |
| `ode.py` | Capa macro: `dX/dt = α(F - βX) + noise` |
| `data.py` | Obtención de datos (APIs reales + fallback sintético) |

## Ejecución

```bash
# Un caso individual
cd XX_caso_NAME/src && python3 validate.py

# Todos en paralelo
python3 run_all_validations_parallel.py
```

## Los 29 casos

| # | Caso | Dominio |
|---|------|---------|
| 01 | clima | Ambiental |
| 02 | conciencia | Cognitivo-social |
| 03 | contaminacion | Ambiental |
| 04 | energia | Infraestructura |
| 05 | epidemiologia | Salud pública |
| 06 | falsacion_exogeneidad | Control negativo |
| 07 | falsacion_no_estacionariedad | Control negativo |
| 08 | falsacion_observabilidad | Control negativo |
| 09 | finanzas | Económico |
| 10 | justicia | Social |
| 11 | movilidad | Urbano |
| 12 | paradigmas | Ciencia |
| 13 | politicas_estrategicas | Geopolítico |
| 14 | postverdad | Informacional |
| 15 | wikipedia | Conocimiento |
| 16 | deforestacion | Ambiental |
| 17 | oceanos | Ambiental |
| 18 | urbanizacion | Urbano |
| 19 | acidificacion_oceanica | Ambiental |
| 20 | kessler | Espacial |
| 21 | salinizacion | Ambiental |
| 22 | fosforo | Ambiental |
| 23 | erosion_dialectica | Social |
| 24 | microplasticos | Ambiental |
| 25 | acuiferos | Ambiental |
| 26 | starlink | Espacial |
| 27 | riesgo_biologico | Salud pública |
| 28 | fuga_cerebros | Social |
| 29 | iot | Tecnológico |

## Bibliotecas compartidas

- `common/` — Módulos reutilizados: `hybrid_validator`, `abm_core`, `abm_numpy`, `ode_models`, `data_universal`
- `enhanced_data_fetchers.py` — APIs de datos (CelesTrak, WMO, OWID, etc.)
- `worldbank_universal_fetcher.py` — Indicadores World Bank
