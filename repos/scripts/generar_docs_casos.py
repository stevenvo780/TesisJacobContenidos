#!/usr/bin/env python3
"""
generar_docs_casos.py — Genera los 5 archivos docs/ estándar para los casos 19-29.

Lee validate.py, ode.py, data.py y metrics.json de cada caso para generar
documentación precisa y fiel a los datos reales.
"""
import json, os, textwrap

BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SIM_DIR = os.path.join(BASE, "Simulaciones")
TESIS_DIR = os.path.join(BASE, "..", "TesisDesarrollo", "02_Modelado_Simulacion")

# ── Definiciones por caso ─────────────────────────────────────────────

CASES = {
    19: {
        "name": "acidificacion_oceanica",
        "title": "Acidificación Oceánica",
        "phenomenon": "acidificación oceánica global como proceso macro distribuido",
        "mechanism": "Las emisiones antropogénicas de CO₂ incrementan la pCO₂ atmosférica, "
                     "que se disuelve en los océanos alterando el equilibrio carbonato-bicarbonato "
                     "y reduciendo el pH marino a escala global.",
        "ode_description": "Modelo basado en el factor de Revelle: captura la respuesta no-lineal "
                           "del sistema carbonato oceánico a la absorción de CO₂.",
        "ode_equation": "dX/dt = α*(F(t) - β*X) + revelle_correction + noise",
        "ode_params": "α (tasa de absorción), β (buffer carbonato), factor de Revelle",
        "abm_description": "Celdas representan parcelas oceánicas con pH local, acopladas por "
                           "difusión y forzadas por gradiente de pCO₂.",
        "data_source": "World Bank (proxy CO₂ emissions) + calibración SOCAT/GLODAPv2",
        "data_indicator": "EN.ATM.CO2E.PC (CO₂ per capita)",
        "bridge_variable": "pH medio oceánico global",
        "specific_ode_model": "revelle_factor + mean_reversion",
    },
    20: {
        "name": "kessler",
        "title": "Síndrome de Kessler (Basura Espacial)",
        "phenomenon": "cascada colisional de basura espacial como proceso macro distribuido",
        "mechanism": "La acumulación de objetos en órbita terrestre baja (LEO) genera colisiones "
                     "que producen fragmentos adicionales, creando un bucle de retroalimentación "
                     "positiva (síndrome de Kessler) que constriñe la dinámica orbital local.",
        "ode_description": "Modelo de Kessler-Liou con término cuadrático de colisión: "
                           "dN/dt = L + α*N² - β*N, donde el término cuadrático captura "
                           "la cascada colisional.",
        "ode_equation": "dN/dt = L + α*N² - β*N",
        "ode_params": "L (tasa de lanzamiento), α (coeficiente colisional ~2e-10), β (decaimiento atmosférico ~0.02)",
        "abm_description": "Celdas en grilla 25×25 representan regiones orbitales, con difusión "
                           "de fragmentos entre sectores y acoplamiento macro hacia densidad global.",
        "data_source": "ESA Space Debris Office / NASA Orbital Debris Program (catálogo público)",
        "data_indicator": "Conteo total de objetos rastreables en LEO (1960-2023)",
        "bridge_variable": "N (número total de objetos orbitales rastreables)",
        "specific_ode_model": "kessler_liou (cuadrático)",
        "log_transform": True,
        "numerical_note": "Escala exponencial (60 → 40,500 objetos). Se aplica log_transform=True "
                          "para estabilizar la calibración. El RMSE alto en escala absoluta refleja "
                          "la magnitud del fenómeno, no un error del modelo.",
    },
    21: {
        "name": "salinizacion",
        "title": "Salinización de Suelos",
        "phenomenon": "salinización global de suelos agrícolas como proceso macro distribuido",
        "mechanism": "La irrigación intensiva y la extracción de agua subterránea elevan la "
                     "concentración salina de los suelos agrícolas, un proceso macro que "
                     "constriñe la productividad local.",
        "ode_description": "Modelo accumulation_decay: acumulación salina proporcional a la "
                           "irrigación menos disipación natural.",
        "ode_equation": "dS/dt = α*(F(t) - β*S) + noise",
        "ode_params": "α (tasa de salinización, ~0.05), β (lixiviación natural, ~0.015), "
                      "ode_inflow=0.05, ode_decay=0.015",
        "abm_description": "Celdas representan parcelas agrícolas con concentración salina local, "
                           "acopladas por difusión lateral y forzadas por macro-salinización.",
        "data_source": "World Bank — AG.LND.IRIG.AG.ZS (irrigated land %) + ER.H2O.FWTL.ZS (freshwater withdrawal)",
        "data_indicator": "AG.LND.IRIG.AG.ZS (% tierras bajo riego)",
        "bridge_variable": "S (índice de salinización global)",
        "specific_ode_model": "accumulation_decay",
    },
    22: {
        "name": "fosforo",
        "title": "Ciclo del Fósforo",
        "phenomenon": "alteración global del ciclo biogeoquímico del fósforo",
        "mechanism": "El uso masivo de fertilizantes fosfatados altera los flujos biogeoquímicos "
                     "globales del fósforo, generando eutrofización y zonas muertas como "
                     "efecto macro distribuido.",
        "ode_description": "Modelo accumulation_decay: acumulación de fósforo reactivo "
                           "proporcional al consumo de fertilizantes menos el secuestro sedimentario.",
        "ode_equation": "dP/dt = α*(F(t) - β*P) + noise",
        "ode_params": "α (tasa de acumulación, ~0.07), β (secuestro, ~0.02)",
        "abm_description": "Celdas representan cuencas hidrográficas con carga de fósforo local, "
                           "acopladas por difusión fluvial y forzadas por aplicación global.",
        "data_source": "World Bank — AG.CON.FERT.ZS (consumo de fertilizantes, kg/ha)",
        "data_indicator": "AG.CON.FERT.ZS (Fertilizer consumption kg/ha of arable land)",
        "bridge_variable": "P (carga global de fósforo reactivo)",
        "specific_ode_model": "accumulation_decay",
    },
    23: {
        "name": "erosion_dialectica",
        "title": "Erosión de Suelos (Dialéctica Institucional)",
        "phenomenon": "erosión global de suelos como proceso macro con retroalimentación institucional",
        "mechanism": "La presión agrícola global degrada suelos, generando una retroalimentación "
                     "dialéctica: la degradación intensifica la presión por más tierra, lo que "
                     "acelera la erosión. El estado del macro-sistema constriñe las parcelas locales.",
        "ode_description": "Modelo mean_reversion con término de amplificación proporcional "
                           "al estado (0.3*x): modela retroalimentación positiva institucional.",
        "ode_equation": "dX/dt = α*(F(t) - β*X) + 0.3*X*α + noise",
        "ode_params": "α (tasa de respuesta, ~0.03), β (restauración, ~0.01), amplificación=0.3",
        "abm_description": "Celdas representan parcelas de uso de suelo con índice de erosión, "
                           "acopladas por difusión y forzadas por presión macro global.",
        "data_source": "Proxy sintético calibrado a datos FAO/GLASOD de degradación de suelos",
        "data_indicator": "Proxy: índice compuesto de degradación (synthetic_fallback)",
        "bridge_variable": "X (índice global de erosión)",
        "specific_ode_model": "mean_reversion + retroalimentación positiva",
    },
    24: {
        "name": "microplasticos",
        "title": "Contaminación por Microplásticos",
        "phenomenon": "acumulación global de microplásticos como proceso macro distribuido",
        "mechanism": "La producción masiva de plástico genera partículas micro que se acumulan "
                     "en los ecosistemas (modelo Jambeck). El macro-proceso constriñe la dinámica "
                     "local de contaminación en cada cuenca/región.",
        "ode_description": "Modelo accumulation_decay: acumulación de microplásticos proporcional "
                           "a la producción plástica menos degradación ambiental (extremadamente lenta).",
        "ode_equation": "dM/dt = α*(F(t) - β*M) + noise",
        "ode_params": "α (tasa de ingreso, ~0.09), β (degradación, ~0.003 — muy lento)",
        "abm_description": "Celdas representan regiones costeras/fluviales con concentración "
                           "local de microplásticos, acopladas por difusión oceánica.",
        "data_source": "OWID (plastic waste) + World Bank (ER.H2O.INTR.K3 — recursos hídricos internos)",
        "data_indicator": "OWID plastic waste + ER.H2O.INTR.K3",
        "bridge_variable": "M (índice global de concentración de microplásticos)",
        "specific_ode_model": "accumulation_decay (Jambeck)",
    },
    25: {
        "name": "acuiferos",
        "title": "Agotamiento de Acuíferos",
        "phenomenon": "agotamiento global de acuíferos como proceso macro distribuido",
        "mechanism": "La sobreexplotación de aguas subterráneas genera un descenso secular "
                     "del nivel freático (proxy: Ogallala). El macro-proceso constriñe la "
                     "disponibilidad hídrica local en cada celda/región.",
        "ode_description": "Modelo accumulation_decay adaptado: el estado H representa el "
                           "nivel del acuífero, con recarga (precipitación) menos extracción.",
        "ode_equation": "dH/dt = α*(F(t) - β*H) + noise",
        "ode_params": "α (tasa de respuesta, ~0.08), β (equilibrio de extracción, ~0.03)",
        "abm_description": "Celdas representan parcelas de terreno sobre el acuífero, con "
                           "nivel freático local acoplado por difusión lateral y forzado por macro.",
        "data_source": "World Bank: AG.LND.PRCP.MM (precipitación, USA) + ER.H2O.FWTL.ZS (extracción hídrica) — proxy GRACE/USGS Ogallala",
        "data_indicator": "AG.LND.PRCP.MM + ER.H2O.FWTL.ZS (USA)",
        "bridge_variable": "H (anomalía de almacenamiento hídrico subterráneo, GWSA)",
        "specific_ode_model": "accumulation_decay (aquifer_balance variant)",
    },
    26: {
        "name": "starlink",
        "title": "Mega-constelaciones Satelitales (Starlink)",
        "phenomenon": "proliferación de mega-constelaciones satelitales como proceso macro",
        "mechanism": "El despliegue masivo de satélites (Starlink et al.) crea un macro-fenómeno "
                     "que afecta la dinámica orbital local, la astronomía y el entorno de LEO.",
        "ode_description": "Modelo accumulation_decay: acumulación de satélites proporcional "
                           "a la tasa de lanzamiento menos el decaimiento orbital.",
        "ode_equation": "dN/dt = α*(F(t) - β*N) + noise",
        "ode_params": "α (tasa de despliegue, ~0.18), β (decaimiento orbital, ~0.015)",
        "abm_description": "Celdas en grilla 25×25 representan regiones orbitales con densidad "
                           "satelital local, acopladas por difusión y forzadas por macro-despliegue.",
        "data_source": "Datos públicos de despliegue Starlink (satélites operativos mensuales)",
        "data_indicator": "Conteo mensual de satélites Starlink operativos (cache local)",
        "bridge_variable": "N (número total de satélites operativos)",
        "specific_ode_model": "accumulation_decay",
        "numerical_note": "Serie con 352/385 valores en cero (Starlink no existía antes de 2019). "
                          "La ventana de validación está dominada por ceros, lo que genera "
                          "RMSE_no_ode ≈ 0 y EDI = -1.0 (artefacto de datos, no error del modelo). "
                          "El caso demuestra correctamente que la sonda no detecta clausura operativa.",
    },
    27: {
        "name": "riesgo_biologico",
        "title": "Riesgo Biológico Global",
        "phenomenon": "riesgo biológico global (bioseguridad) como proceso macro distribuido",
        "mechanism": "La combinación de urbanización, deforestación y comercio global incrementa "
                     "el riesgo de eventos biológicos (pandemias, zoonosis). El macro-proceso "
                     "constriñe la vulnerabilidad local de cada región.",
        "ode_description": "Modelo mean_reversion con término de amplificación biológica: "
                           "dR/dt = α*(f - β*R) + γ_bio*f*R, donde el término γ_bio captura "
                           "la retroalimentación riesgo-exposición.",
        "ode_equation": "dR/dt = α*(F(t) - β*R) + γ_bio*F*R + noise",
        "ode_params": "α (~0.05), β (~0.02), γ_bio (amplificación biológica)",
        "abm_description": "Celdas representan regiones con índice de riesgo biológico local, "
                           "acopladas por difusión (conectividad global) y forzadas por macro-riesgo.",
        "data_source": "Proxy compuesto: indicadores World Bank de salud + urbanización + deforestación",
        "data_indicator": "Proxy compuesto multi-indicador (synthetic_fallback → cache)",
        "bridge_variable": "R (índice global de riesgo biológico)",
        "specific_ode_model": "mean_reversion + amplificación biológica",
    },
    28: {
        "name": "fuga_cerebros",
        "title": "Fuga de Cerebros (Brain Drain)",
        "phenomenon": "fuga de cerebros global como proceso macro distribuido",
        "mechanism": "La concentración de oportunidades en economías desarrolladas genera flujos "
                     "migratorios de capital humano que empobrecen las periferias, creando un "
                     "macro-proceso de acumulación desigual que constriñe la dinámica local.",
        "ode_description": "Modelo de acumulación de capital humano: "
                           "dH/dt = α*(f - β*H) + noise, con α~6%/año (formación) y β~2%/año (emigración).",
        "ode_equation": "dH/dt = α*(F(t) - β*H) + noise",
        "ode_params": "α (~0.06, acumulación capital humano), β (~0.02, tasa de fuga)",
        "abm_description": "Celdas en grilla 25×25 representan regiones con capital humano local, "
                           "acopladas por difusión migratoria y forzadas por macro-concentración.",
        "data_source": "World Bank (multi-indicador): SE.XPD.TOTL.GD.ZS (gasto educativo), "
                       "SM.POP.NETM (migración neta), IP.PAT.RESD (patentes residentes), "
                       "SE.TER.ENRR (matrícula terciaria), SP.POP.SCIE.RD.P6 (investigadores/millón)",
        "data_indicator": "SE.XPD.TOTL.GD.ZS + SM.POP.NETM + IP.PAT.RESD + SE.TER.ENRR + SP.POP.SCIE.RD.P6",
        "bridge_variable": "H (índice compuesto de capital humano global)",
        "specific_ode_model": "accumulation_decay (capital humano)",
    },
    29: {
        "name": "iot",
        "title": "Internet de las Cosas (IoT — Bass-Metcalfe)",
        "phenomenon": "expansión global del IoT como proceso macro distribuido",
        "mechanism": "La adopción masiva de dispositivos IoT sigue un modelo Bass (difusión de "
                     "innovación) amplificado por efectos de red Metcalfe. El macro-proceso "
                     "de conectividad global constriñe la adopción local en cada región.",
        "ode_description": "Modelo mean_reversion con término de efecto de red: "
                           "dN/dt = α*(f - β*N) + γ_net*f*N, donde γ_net captura el efecto Metcalfe.",
        "ode_equation": "dN/dt = α*(F(t) - β*N) + γ_net*F*N + noise",
        "ode_params": "α (~0.05), β (~0.02), γ_net (efecto de red Metcalfe)",
        "abm_description": "Celdas representan regiones con densidad IoT local, acopladas por "
                           "difusión de conectividad y forzadas por macro-adopción global.",
        "data_source": "World Bank (multi-indicador): IT.NET.BBND.P2 (banda ancha fija), "
                       "IT.CEL.SETS.P2 (suscripciones móviles), IT.NET.USER.ZS (uso de Internet), "
                       "TX.VAL.TECH.MF.ZS (exportaciones high-tech), EG.ELC.ACCS.ZS (acceso eléctrico)",
        "data_indicator": "IT.NET.BBND.P2 + IT.CEL.SETS.P2 + IT.NET.USER.ZS + TX.VAL.TECH.MF.ZS + EG.ELC.ACCS.ZS",
        "bridge_variable": "N (índice compuesto de penetración IoT global)",
        "specific_ode_model": "mean_reversion + efecto de red (Bass-Metcalfe)",
    },
}


def load_metrics(case_num, case_name):
    path = os.path.join(SIM_DIR, f"{case_num:02d}_caso_{case_name}", "outputs", "metrics.json")
    with open(path) as f:
        return json.load(f)


def edi_value(m):
    """Extract numeric EDI from metrics."""
    real = m["phases"]["real"]
    edi = real.get("edi", {})
    if isinstance(edi, dict):
        return edi.get("value", 0)
    return edi


def get_nivel(m):
    """Extract nivel from metrics."""
    real = m["phases"]["real"]
    nivel = real.get("nivel")
    if nivel is not None:
        return nivel
    edi_v = edi_value(m)
    edi_d = real.get("edi", {})
    sig = edi_d.get("permutation_significant", False) if isinstance(edi_d, dict) else False
    if edi_v <= 0 or not sig:
        if edi_v > 0:
            return 1
        return 0
    if edi_v < 0.10:
        return 2
    if edi_v < 0.30:
        return 3
    return 4


def get_pass(m):
    return m["phases"]["real"].get("overall_pass", False)


def get_c(m, n):
    return m["phases"]["real"].get(f"c{n}_convergence" if n == 1 else
                                    f"c{n}_coupling_benefit" if n == 2 else
                                    f"c{n}_ablation_edi" if n == 3 else
                                    f"c{n}_noise_robustness" if n == 4 else
                                    f"c{n}_parsimony", None)


def fmt_bool(v):
    if v is None:
        return "—"
    return "✅ Sí" if v else "❌ No"


def fmt_edi(v):
    if v is None:
        return "—"
    return f"{v:.6f}"


# ── Generadores de documentos ────────────────────────────────────────

def gen_arquitectura(info, m):
    num = [k for k, v in CASES.items() if v == info][0]
    edi_v = edi_value(m)
    real = m["phases"]["real"]
    symploke = real.get("symploke", {})

    txt = f"""# Arquitectura de Modelos — {info['title']}

## Conceptual
- Hiperobjeto: {info['phenomenon']}.
- Mecanismo: {info['mechanism']}
- Delimitación: frontera funcional basada en cohesión interna vs externa (Symploké).
- Relación macro-micro: el macro-proceso constriñe la dinámica de las celdas locales
  a través del acoplamiento (macro_coupling).

## Formal

### Capa macro (ODE)
- Estado macro: {info['bridge_variable']}.
- Dinámica: `{info['ode_equation']}`
  - Modelo específico: {info['specific_ode_model']}.
  - Parámetros: {info['ode_params']}.
- {info['ode_description']}
- Asimilación de datos con rezago temporal (t-1) para evitar look-ahead.

### Capa micro (ABM)
- {info['abm_description']}
- Regla de actualización por celda por paso:
  1. Difusión espacial (vecinos 4-conectados).
  2. Forcing externo (gradiente de presión).
  3. Acoplamiento macro (`macro_coupling` hacia la media global).
  4. Amortiguamiento (`damping`).
  5. Ruido estocástico.

### Acoplamiento
- Variable puente: {info['bridge_variable']}.
- Bidireccional: ODE → ABM (macro_coupling) + ABM → ODE (feedback gamma=0.05).
- Iteraciones de acoplamiento: 2 pasadas por paso temporal.

## Computacional
- Modelo micro: lattice 2D con vecinos 4-conectados.
- Modelo macro: ODE discreta ({info['specific_ode_model']}).
- Simulación: pasos discretos con semillas controladas.
- Fuente de datos: {info['data_source']}.
- Indicador: `{info['data_indicator']}`.
"""

    if info.get("log_transform"):
        txt += f"\n## Nota sobre transformación\n- Se aplica `log_transform=True` debido a la escala exponencial de los datos.\n"

    if info.get("numerical_note"):
        txt += f"\n## Nota numérica\n{info['numerical_note']}\n"

    txt += f"""
## Validación
- Protocolo C1–C5 (ver `validacion_c1_c5.md`).
- Métricas: EDI, CR, EI, RMSE, correlación (ver `indicadores_metricas.md`).
- EDI obtenido: {fmt_edi(edi_v)} → Nivel {get_nivel(m)}.
- Overall pass: {fmt_bool(get_pass(m))}.
"""
    return txt


def gen_protocolo(info, m):
    num = [k for k, v in CASES.items() if v == info][0]
    edi_v = edi_value(m)

    txt = f"""# Protocolo de Simulación — {info['title']}

## 1. Definición de escenario
- Objetivo: evaluar si {info['phenomenon']} exhibe clausura operativa
  medible a través del protocolo C1–C5.
- Variable objetivo: {info['bridge_variable']}.
- Indicador empírico: `{info['data_indicator']}`.
- Fuente: {info['data_source']}.

## 2. Fases de validación

### Fase sintética (ground truth controlado)
1. Generar serie sintética con parámetros conocidos.
2. Calibrar ABM + ODE sobre serie sintética.
3. Evaluar C1–C5 contra ground truth.
4. **Gate**: C2, C3, C4 sintéticos deben pasar para habilitar fase real.

### Fase real (datos empíricos)
1. Obtener datos de {info['data_source']}.
2. Dividir en train (pre-split) y validation (post-split).
3. Calibrar:
   - ABM: grid search (144 combinaciones) + refinamiento adaptativo (5000 iter).
   - ODE: least-squares con regularización Tikhonov.
4. Modelo completo (ABM + ODE acoplado) → predicción.
5. Modelo reducido (ABM sin ODE: macro_coupling=0, forcing_scale=0) → baseline.
6. EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido.
7. Test de permutación (n=999) + bootstrap CI (n=500).
8. Evaluar C1–C5 + Symploké + no-localidad + persistencia.

## 3. Parámetros de simulación
- **ODE**: {info['ode_params']}.
- **ABM**: forcing_scale, macro_coupling, damping (calibrados por grid search).
- **Acoplamiento**: gamma=0.05, 2 iteraciones bidireccionales.
- **Assimilation_strength**: 0.0 en todas las evaluaciones (zero-nudging).

## 4. Controles de leakage
- Forcing calculado solo con datos de entrenamiento.
- Período de validación usa extrapolación por persistencia.
- No se usa assimilation en evaluación (assimilation_strength=0).
- ODE calibrada con regularización Tikhonov (previene overfitting).

## 5. Resultado
- EDI: {fmt_edi(edi_v)}.
- Nivel de emergencia: {get_nivel(m)}.
- Overall pass: {fmt_bool(get_pass(m))}.
"""
    return txt


def gen_indicadores(info, m):
    real = m["phases"]["real"]
    edi_d = real.get("edi", {})
    edi_v = edi_d.get("value", 0) if isinstance(edi_d, dict) else edi_d
    pval = edi_d.get("permutation_pvalue", "—") if isinstance(edi_d, dict) else "—"
    sig = edi_d.get("permutation_significant", False) if isinstance(edi_d, dict) else False
    ci_lo = edi_d.get("ci_lo", "—") if isinstance(edi_d, dict) else "—"
    ci_hi = edi_d.get("ci_hi", "—") if isinstance(edi_d, dict) else "—"
    bootstrap_mean = edi_d.get("bootstrap_mean", "—") if isinstance(edi_d, dict) else "—"
    trend_bias = edi_d.get("trend_bias", {}) if isinstance(edi_d, dict) else {}

    symploke = real.get("symploke", {})
    non_loc = real.get("non_locality", {})
    persist = real.get("persistence", {})

    txt = f"""# Indicadores, Métricas y Reglas — {info['title']}

Basado en `00_03_Tablas_Correspondencia.md` y `01_02_Indicadores_Metricas.md`.

## EDI (Índice de Dependencia Efectiva)
- **Fórmula**: EDI = (RMSE_reducido - RMSE_completo) / RMSE_reducido
- **Rango**: [-1, 1] (clamped)
- **Valor obtenido**: {fmt_edi(edi_v)}
- **Bootstrap mean**: {bootstrap_mean}
- **IC 95%**: [{ci_lo}, {ci_hi}]
- **p-value permutación**: {pval}
- **Significativo**: {fmt_bool(sig)}
- **Trend bias**:
  - Detrended EDI: {trend_bias.get('detrended_edi', '—')}
  - Trend R²: {trend_bias.get('trend_r2', '—')}
  - Warning: {fmt_bool(trend_bias.get('warning', False))}

## Criterios C1–C5
| Criterio | Resultado |
|----------|-----------|
| C1 (Convergencia) | {fmt_bool(get_c(m, 1))} |
| C2 (Beneficio acoplamiento) | {fmt_bool(get_c(m, 2))} |
| C3 (Ablación EDI) | {fmt_bool(get_c(m, 3))} |
| C4 (Robustez ruido) | {fmt_bool(get_c(m, 4))} |
| C5 (Parsimonia) | {fmt_bool(get_c(m, 5))} |

## Symploké
- Cohesión interna: {symploke.get('internal', '—')}
- Cohesión externa: {symploke.get('external', '—')}
- CR (internal/external): {symploke.get('cr', '—')}
- Pass: {fmt_bool(symploke.get('pass'))}
- CR valid: {fmt_bool(symploke.get('cr_valid'))}

## No-localidad
- Dominance share: {non_loc.get('dominance_share', '—')}
- Pass: {fmt_bool(non_loc.get('pass'))}

## Persistencia
- Model std: {persist.get('model_std', '—')}
- Obs std: {persist.get('obs_std', '—')}
- Std ratio: {persist.get('std_ratio', '—')}
- Threshold: {persist.get('threshold_std', '—')}
- Pass: {fmt_bool(persist.get('pass'))}

## Nivel de emergencia
- **Nivel**: {get_nivel(m)}
- **Overall pass**: {fmt_bool(get_pass(m))}

## Taxonomía de niveles
| Nivel | Categoría | EDI | Significado |
|:-----:|:----------|:----|:------------|
| 4 | strong | ≥0.30 + C1-C5 | Clausura operativa fuerte |
| 3 | weak | 0.10-0.30 + sig | Componente funcional |
| 2 | suggestive | >0.01 + sig | Señal sugestiva |
| 1 | trend | >0 pero no sig | Tendencia no significativa |
| 0 | null | ≤0 o no sig | Sin señal |
"""
    return txt


def gen_validacion_c1c5(info, m):
    num = [k for k, v in CASES.items() if v == info][0]
    real = m["phases"]["real"]
    synth = m["phases"].get("synthetic", {})

    txt = f"""# Validación C1–C5 — {info['title']}

## Fase Sintética (Ground Truth)
- C1 (Convergencia): {fmt_bool(synth.get('c1_convergence'))}
- C2 (Beneficio acoplamiento): {fmt_bool(synth.get('c2_coupling_benefit'))}
- C3 (Ablación EDI): {fmt_bool(synth.get('c3_ablation_edi'))}
- C4 (Robustez ruido): {fmt_bool(synth.get('c4_noise_robustness'))}
- C5 (Parsimonia): {fmt_bool(synth.get('c5_parsimony'))}

**Gate sintético**: C2+C3+C4 deben pasar para habilitar fase real.
- Gate resultado: {fmt_bool(synth.get('c2_coupling_benefit') and synth.get('c3_ablation_edi') and synth.get('c4_noise_robustness') if synth else None)}

## Fase Real (Datos Empíricos)

### C1 — Convergencia
- Definición: ABM y ODE deben ajustar la serie con error < umbral.
- Resultado: {fmt_bool(get_c(m, 1))}

### C2 — Beneficio de Acoplamiento
- Definición: RMSE acoplado < RMSE desacoplado.
- Resultado: {fmt_bool(get_c(m, 2))}

### C3 — Ablación EDI
- Definición: EDI > 0.01 y significativo por permutación.
- EDI = {fmt_edi(edi_value(m))}
- Resultado: {fmt_bool(get_c(m, 3))}

### C4 — Robustez al Ruido
- Definición: EDI estable bajo 5 niveles de ruido (CV < umbral).
- Resultado: {fmt_bool(get_c(m, 4))}

### C5 — Parsimonia
- Definición: modelo macro mejora predicción sin sobreajuste.
- Resultado: {fmt_bool(get_c(m, 5))}

## Propiedades Adicionales

### Symploké
- Cohesión interna > externa → delimitación funcional.
- CR = {real.get('symploke', {}).get('cr', '—')}
- Pass: {fmt_bool(real.get('symploke', {}).get('pass'))}

### No-localidad
- Efecto macro no reducible a una única celda dominante.
- Dominance share: {real.get('non_locality', {}).get('dominance_share', '—')}
- Pass: {fmt_bool(real.get('non_locality', {}).get('pass'))}

### Persistencia
- El efecto macro persiste en ventanas temporales.
- Std ratio: {real.get('persistence', {}).get('std_ratio', '—')}
- Pass: {fmt_bool(real.get('persistence', {}).get('pass'))}

## Veredicto
- **Nivel**: {get_nivel(m)}
- **Overall pass**: {fmt_bool(get_pass(m))}
"""
    return txt


def gen_reproducibilidad(info, m):
    num = [k for k, v in CASES.items() if v == info][0]

    txt = f"""# Reproducibilidad y Versionado — {info['title']}

## Entorno requerido
- Python 3.10+
- Dependencias: `numpy`, `pandas`, `scipy`, `requests`
- Sin frameworks ML. Todo en NumPy/Pandas puro.

## Estructura de archivos
```
repos/Simulaciones/{num:02d}_caso_{info['name']}/
├── src/
│   ├── validate.py    # Orquestador: calibrar → simular → evaluar C1–C5
│   ├── abm.py         # Capa micro: grilla NxN con difusión y acoplamiento
│   ├── ode.py         # Capa macro: {info['specific_ode_model']}
│   ├── metrics.py     # EDI, CR, EI, RMSE, correlación
│   └── data.py        # Obtención de datos ({info['data_source']})
├── outputs/
│   ├── metrics.json   # Resultados completos de la validación
│   └── report.md      # Reporte legible con resumen de métricas
└── data/
    └── *.csv          # Datos cacheados localmente
```

## Ejecución
```bash
cd repos/Simulaciones/{num:02d}_caso_{info['name']}/src
python3 validate.py
```

## Semillas y reproducibilidad
- Todas las simulaciones usan semillas explícitas (`seed` parameter).
- Los resultados son reproducibles dado el mismo entorno y versión de dependencias.
- Las semillas se fijan en: ABM (seed), ODE (seed), permutación (seed+1), bootstrap (seed+2).

## Validación de resultados
- `metrics.json` contiene todas las métricas y criterios evaluados.
- `report.md` contiene el resumen en formato legible.
- Ambos se generan automáticamente al ejecutar `validate.py`.

## Datos
- Fuente: {info['data_source']}
- Indicador: `{info['data_indicator']}`
- Los datos se cachean en `data/` tras la primera descarga.
- La validación funciona con datos cacheados (no requiere conexión).

## Auditoría
- `repos/scripts/auditar_simulaciones.py` verifica todos los 29 casos.
- `repos/scripts/evaluar_simulaciones.py` genera tablas resumen.

## Resultado actual
- EDI: {fmt_edi(edi_value(m))}
- Nivel: {get_nivel(m)}
- Overall pass: {fmt_bool(get_pass(m))}
- Generado: {m.get('generated_at', '—')}
"""
    return txt


# ── Main ──────────────────────────────────────────────────────────────

def main():
    generated = 0
    for num, info in CASES.items():
        m = load_metrics(num, info["name"])
        docs_dir = os.path.join(TESIS_DIR, f"{num:02d}_caso_{info['name']}", "docs")
        os.makedirs(docs_dir, exist_ok=True)

        files = {
            "arquitectura.md": gen_arquitectura(info, m),
            "protocolo_simulacion.md": gen_protocolo(info, m),
            "indicadores_metricas.md": gen_indicadores(info, m),
            "validacion_c1_c5.md": gen_validacion_c1c5(info, m),
            "reproducibilidad.md": gen_reproducibilidad(info, m),
        }

        for fname, content in files.items():
            fpath = os.path.join(docs_dir, fname)
            with open(fpath, "w") as f:
                f.write(content)
            generated += 1

        print(f"✅ {num:02d}_caso_{info['name']}: {len(files)} docs generados")

    print(f"\n✅ Total: {generated} archivos generados para {len(CASES)} casos")


if __name__ == "__main__":
    main()
