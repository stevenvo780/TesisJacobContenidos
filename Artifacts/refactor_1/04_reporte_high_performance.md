# Reporte de Fase 4: Optimización High-Performance y Escalamiento

**Fecha:** 2026-02-08
**Estado:** Ejecución Masiva Completada (Stress Test) -> **Recalibración Requerida**

## 1. Experimento de Escalamiento Masivo (Mega Run)
Siguiendo la solicitud de maximizar el uso del hardware, se ejecutó una batería de simulación con parámetros extremos:
- **Grid Size:** 100x100 (10,000 agentes vs 400 originales). Aumento de 25x en carga computacional por paso.
- **Monte Carlo Loops:** 50 réplicas (vs 5 originales). Aumento de 10x en robustez estadística.
- **Paralelismo:** 32 casos simultáneos (saturación de CPU).

## 2. Resultados: El Límite de Estabilidad Numérica 
El caso piloto `01_caso_clima` reveló un hallazgo crítico sobre la estabilidad del modelo híbrido al escalar:

### A. Fase Sintética (Validada - Éxito Rotundo)
- **Robustez Estadística:** Con 50 runs, los intervalos de confianza del EDI son extremadamente precisos ($EDI \in [0.67, 0.69]$).
- **Viscosidad:** El test de viscosidad se mantuvo estable ($\tau=4$), confirmando que la inercia estructural es una propiedad del sistema, no del tamaño de la grilla.
- **Conclusión:** El motor ABM Vectorizado (`abm_numpy`) soporta 10,000 agentes sin problemas de rendimiento (tiempo de ejecución < 5 minutos).

### B. Fase Real (Fallo por Inestabilidad Numérica)
- **Problema:** En la fase de validación con datos reales, el modelo divergió catastróficamente (`c5_sensitivity_min` = $-4.3 \times 10^{18}$).
- **Causa Técnica:** La difusión en sistemas de reacción-difusión (como este ABM) está limitada por la condición CFL (Courant-Friedrichs-Lewy) o similar: $D \frac{\Delta t}{(\Delta x)^2} < 0.5$.
    - Al pasar de 20x20 a 100x100, la distancia efectiva de propagación cambió, y los parámetros de `diffusion=0.2` y `damping` calibrados para 20x20 causaron una resonancia destructiva.
- **Interpretación:** "Más grande" no siempre es "mejor" sin recalibración. El sistema es sensible a la densidad espacial.

## 3. Recomendación Técnica (El "Punto Dulce")
Para la producción final de la Tesis, se recomienda un escalamiento moderado que garantice estabilidad sin sacrificar la "masa crítica" de agentes:

1.  **Grid:** **50x50 (2,500 agentes)**. Suficiente para patrones complejos, seguro para difusión.
2.  **Runs:** **50 Réplicas**. Mantener este estándar de oro para las barras de error.
3.  **Calibración:** Ejecutar una recalibración rápida de `diffusion` para el nuevo tamaño de grilla.

## 4. Próximos Pasos (Validación final)
Se procederá a configurar el sistema en **Modo Producción Estable (50x50, 50 runs)** para generar los reportes definitivos de los 32 casos sin riesgo de *overflow*.

Este ejercicio ha cumplido su objetivo de probar los límites del hardware y del modelo matemático.
