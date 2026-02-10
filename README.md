# Proyecto Hiperobjetos (Titanio)

## 🌌 Visión General
Este repositorio alberga la investigación y el motor de simulación de la tesis **"Irrealismo Operativo de Hiperobjetos"**. El objetivo es clasificar el grado de cierre operativo de fenómenos masivamente distribuidos (Hiperobjetos) como el Clima, la Deforestación o las Pandemias, utilizando modelos computacionales híbridos que integran Modelado Basado en Agentes (ABM) y Ecuaciones Diferenciales Ordinarias (ODE). No se afirma ni se niega existencia metafísica; se mide suficiencia operativa.

### 🔬 Hipótesis Central (H1)
Un fenómeno exhibe cierre operativo de grado G cuando la eliminación de su constructo macro degrada la predicción micro en una proporción **EDI ≥ G/100**, verificable mediante el protocolo C1-C5 con zero-nudging. Nivel 4 (cierre fuerte) requiere EDI ≥ 0.30 + 11 condiciones simultáneas.

---

## 🏗️ Estructura del Proyecto

*   **`/TesisDesarrollo/`**: Marco teórico (irrealismo operativo), metodología C1-C5 y documentación técnica de los 29 casos.
*   **`/repos/Simulaciones/`**: Motor de simulación en Python con el pipeline completo de validación.
*   **`/Artifacts/`**: Registro de auditorías, debates dialécticos (Gladiadores) y ciclos de validación.
*   **`/TesisFinal/`**: Documento consolidado de la tesis (`Tesis.md`).

---

## 📊 Resultados de Validación
Se han evaluado **29 casos** (tras la remoción de 3 casos por falta de datos reales). El resultado principal es un **paisaje de emergencia operativa** de 6 niveles:

| Nivel | Interpretación | Casos | Ejemplos |
|:-----:|:---|:---:|:---|
| 4 | Cierre operativo fuerte | 2 | Deforestación (EDI=0.633), Microplásticos (EDI=0.427) |
| 3 | Componente funcional | 1 | Fuga de Cerebros (EDI=0.183) |
| 2 | Señal sugestiva | 3 | Finanzas, Océanos, IoT |
| 1 | Tendencia | 7 | Clima, Movilidad, Políticas, Postverdad, Urbanización, Salinización, Riesgo Biológico |
| 0 | Sin señal | 13 | Sin constricción macro detectable |
| — | Falsificación correcta | 3 | Controles negativos rechazados correctamente |

| Métrica | Valor |
|---------|-------|
| overall_pass (11 condiciones) | 2/29 |
| Significancia estadística (p<0.05) | 6/29 |
| Estabilidad numérica | 25/29 |
| Persistencia temporal | 27/29 |
| Controles de falsación | 3/3 correctos |

> **Nota:** Los casos de Estética, Moderación Adversarial y RTB Publicidad fueron archivados en `/Artifacts/casos_removidos/` por carecer de fuentes de datos reales verificables.


### Casos Destacados:
*   **Deforestación:** Nivel 4 (EDI=0.633). Máximo cierre operativo. Modelo von Thünen + Bias Correction full.
*   **Microplásticos:** Nivel 4 (EDI=0.427). Modelo Jambeck. Sin Bias Correction necesario.
*   **Clima:** Nivel 1 (EDI=0.010). Modelo Budyko-Sellers con datos regionales — sonda insuficiente, no refutación del fenómeno.

---

## 🚀 Guía de Inicio Rápido

### Requisitos
*   Python 3.10+
*   Instalación de dependencias:
    ```bash
    pip install -r repos/Simulaciones/requirements.txt
    ```

### Ejecución de Simulaciones
Para validar un caso específico (ej. Clima):
```bash
cd repos/Simulaciones/01_caso_clima/src && python3 validate.py
```

### Ejecución de Scripts de Auditoría
```bash
python3 repos/scripts/actualizar_tablas_002.py
python3 repos/scripts/evaluar_simulaciones.py --write
python3 repos/scripts/auditar_simulaciones.py
python3 repos/scripts/_audit_fresh.py
python3 repos/scripts/tesis.py build
```

---

## 📜 Convenciones de Investigación
1.  **Navaja de Ockham:** No se postula cierre operativo si los datos se explican satisfactoriamente mediante interacciones micro o ruido.
2.  **Irrealismo operativo:** Nunca afirmamos "X *es* un hiperobjeto"; afirmamos "X exhibe cierre operativo de grado G según este instrumento".
3.  **Zero-nudging:** Toda evaluación con assimilation_strength=0 para evitar leakage.

---

## 🗺️ Mapa de Documentación
*   **Índice Maestro:** `TesisDesarrollo/Indice_Maestro.md`
*   **Metodología Completa:** `TesisDesarrollo/01_Metodologia_Medicion/01_00_Metodologia_Medicion.md`
*   **Protocolo de Validación:** `repos/Simulaciones/PROTOCOLO_VALIDACION.md`

---
*Investigación doctoral sobre irrealismo operativo, emergentismo gradual y fenómenos de gran escala.*
