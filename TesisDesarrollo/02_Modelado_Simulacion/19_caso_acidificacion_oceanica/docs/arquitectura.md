# Arquitectura de Simulación: Acidificación Oceánica (Caso 19)

## 1. Definición del Hiperobjeto
La Acidificación Oceánica es una entidad masivamente distribuida en el espacio (70% de la superficie) y el tiempo (siglos). Su realidad ontológica se manifiesta como una restricción química macro sobre la vida micro (plancton y corales).

## 2. Variables Nucleares (Blindadas)
- **Variable Macro (X):** Promedio global de $pCO_2$ oceánico superficial. (Dato NOAA).
- **Variable Micro (x_i):** pH local y saturación de aragonito por celda. (Dato Argo Floats).
- **Parámetro de Orden:** La capacidad de amortiguación (Buffering) global que impide la disolución inmediata del micro.

## 3. Escudo de Rigor (C1-C5 + Titanio)
Para evitar las críticas de la Iteración 2, este caso implementa:
1.  **Test de Surrogados (Anti-Inercia):** El EDI se compara contra 1,000 series de pH barajadas. Si p > 0.01, se rechaza el caso.
2.  **Invarianza de Escala (Anti-ToyModel):** Se ejecutan grillas de 20x20, 40x40 y 80x80. El hiperobjeto solo es válido si el EDI es estable ante el aumento de resolución.
3.  **Ablación Causal (Anti-Ventriloquismo):** Se apaga la interacción de la Ley de Henry (macro) para medir cuánto se desvía el pH local del equilibrio real.

## 4. Fuentes de Datos (LoE 5)
- **Macro:** Mauna Loa CO2 Record / NOAA Global Monitoring.
- **Micro:** World Ocean Database (WOD) de la NOAA / Red de boyas Argo.
