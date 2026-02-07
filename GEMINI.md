# GEMINI.md - Contexto Maestro: Proyecto SimulacionClimatica (Titanio)

Este archivo proporciona el contexto necesario para operar en el repositorio de la tesis "Validación de Hiperobjetos mediante Eficacia Causal".

## 1. Visión General del Proyecto
El proyecto busca validar la realidad ontológica de los **Hiperobjetos** (ej. Clima, Economía, Pandemias) utilizando modelos computacionales híbridos. 

*   **Hipótesis Central (H1):** Un hiperobjeto es real si su modelo macroscópico (ODE) reduce la entropía de sus componentes microscópicos (ABM) en más del 30% (Índice de Dependencia Efectiva, EDI > 0.30).
*   **Marco Filosófico:** Realismo Especulativo (Morton), Sinergética (Haken), y Teoría de la Información (Shannon).

## 2. Estructura del Workspace
El repositorio se divide en cuatro áreas críticas:

*   **/TesisDesarrollo/**: Contiene la fundamentación teórica, metodología y narrativa consolidada de la tesis.
    *   `00_Marco_Conceptual/`: Ontología y Axiomas.
    *   `01_Metodologia_Medicion/`: Protocolo C1-C5 y métricas (EDI, CR).
    *   `02_Modelado_Simulacion/`: Documentación del motor `HybridModel`.
*   **/repos/Simulaciones/**: Motor de simulación en Python — 32 casos con pipeline completo.
    *   `01_caso_clima/`: Validado (EDI 0.434).
    *   `10_caso_finanzas/`: Validado (EDI 0.882).
    *   24 casos validados en total, 3 controles de falsación, 5 rechazados genuinos.
*   **/Artifacts/**: Historial de debates, auditorías y ciclos de validación (C1-C5).
*   **/TesisFinal/**: El documento de tesis consolidado (`Tesis.md`).

## 3. Guía de Ejecución (Building & Running)
El motor de simulación requiere Python 3.10+ y las dependencias listadas en `repos/Simulaciones/requirements.txt`.

### Comandos Clave:
*   **Instalar Dependencias:**
    ```bash
    pip install -r repos/Simulaciones/requirements.txt
    ```
*   **Validar Caso Clima:**
    ```bash
    python3 repos/Simulaciones/01_caso_clima/src/validate.py
    ```
*   **Validar Caso Finanzas:**
    ```bash
    python3 repos/Simulaciones/10_caso_finanzas/src/validate.py
    ```

## 4. Convenciones y Rigor
Al interactuar con este proyecto, se deben seguir estas reglas:

1.  **Navaja de Ockham:** No postular una capa macro (Hiperobjeto) si los datos se explican mediante interacciones micro (ABM) o ruido.
2.  **Rigor Académico:** Las afirmaciones sobre emergencia deben estar respaldadas por el cálculo de EDI. Citar a Haken (Sinergética) o Shannon (Entropía) cuando se hable de métricas de información.
3.  **Estado de los Casos:**
    *   `Clima`: Validado (EDI=0.434, Emergencia Fuerte).
    *   `Finanzas`: Validado (EDI=0.882, Emergencia Muy Fuerte).
    *   24/29 genuinos validados (83%), 3 controles falsación correctos.
4.  **Terminología:** Consultar `TesisDesarrollo/00_Marco_Conceptual/00_00_Marco_Conceptual.md` para términos como "Symploké", "Causalidad Descendente" o "Nudging".

## 5. Documentos de Referencia Rápida
*   **Indice Maestro:** `TesisDesarrollo/Indice_Maestro.md`
*   **Resumen Ultra:** `TesisDesarrollo/README.md`
*   **Métricas Específicas:** `TesisDesarrollo/01_Metodologia_Medicion/01_00_Metodologia_Medicion.md`
