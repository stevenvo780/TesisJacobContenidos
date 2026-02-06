# Problemas Pendientes para la Defensa (Sintetizado)

Este archivo contiene los riesgos críticos y fallos metodológicos identificados en las auditorías "Brutal" y "Termonuclear" que aún no han sido resueltos.

## 1. El "Número Mágico" (EDI > 0.30)
- **Problema:** No existe una justificación teórica sólida para el umbral del 30%. Parece un ajuste ad-hoc para validar el Caso Clima.
- **Riesgo:** Acusación de "Pseudo-Ciencia de Datos" por parte del jurado.
- **Acción necesaria:** Derivar el umbral desde la Sinergética de Haken o la Redundancia de Shannon.

## 2. Inconsistencia Narrativa vs. Técnica
- **Problema:** El motor de simulación arroja `overall_pass: True` para casos que la tesis clasifica como "Rechazados" (Finanzas) o "Dudosos" (Justicia). 
- **Riesgo:** Falta de integridad. El linter de validación no está siendo lo suficientemente estricto o los parámetros se están forzando.
- **Acción necesaria:** Endurecer los criterios de los archivos `.py` de validación o alinear la narrativa con los datos crudos.

## 3. Paradoja de la Inercia Social
- **Problema:** El modelo otorga más "realidad" al Arte (Estética) que al Estado de Derecho (Justicia).
- **Riesgo:** El jurado señalará que el modelo mide "suavidad de la serie temporal" (inercia de datos) y no "eficacia causal" real.
- **Acción necesaria:** Diferenciar técnicamente entre inercia informacional y estructura ontológica.

## 4. Calidad de Datos y Reproducibilidad
- **Problema:** El Caso Clima es robusto (30 años de datos), pero los casos sociales son "esqueletos" de datos. Falta un entorno de ejecución claro para auditores externos.
- **Riesgo:** Que los casos sociales sean vistos como decorativos o retóricos.
- **Acción necesaria:** Crear un `INSTALL.md` y etiquetar claramente el LoE (Level of Evidence) de cada caso.

## 5. El Tono "Modo Dios"
- **Problema:** La redacción es excesivamente segura y no admite las limitaciones del motor ODE para sistemas de alta frecuencia.
- **Riesgo:** El jurado castigará la falta de humildad científica.
- **Acción necesaria:** Refactorizar capítulos 02 y 03 con lenguaje de incertidumbre y límites epistémicos.
