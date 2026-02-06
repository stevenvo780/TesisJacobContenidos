# 00_01 Presupuestos y Axiomas: El Setup del Sistema

Para un programador, los axiomas no son verdades espirituales, son las **precondiciones** y el **setup** de nuestro entorno de ejecución. Si estos fallan, el programa (la tesis) lanza una excepción y se detiene.

## 1. Presupuestos Ontológicos (El Modelo de Datos)

### PO1: Realismo Inferencial (Inferencia de Tipos)
*   **Lógica:** Si un objeto se comporta como un pato y grazna como un pato, lo tratamos como un objeto de tipo `Pato`. 
*   **En la Tesis:** Si el clima se comporta como una entidad real y podemos predecirlo, lo tratamos como una entidad real, aunque no podamos "tocarlo" físicamente.

### PO3: Emergencia Fuerte (Propiedades Privadas vs Públicas)
*   **Lógica:** Un objeto de la clase `Clima` tiene propiedades que sus componentes (`Átomo`, `GotaDeAgua`) no tienen. No puedes calcular la `temperatura_global` mirando solo una instancia de `GotaDeAgua`.
*   **Prueba:** Si borras la lógica de la clase padre (Macro), los objetos hijos (Micro) no pueden explicar el comportamiento del sistema completo.

## 2. Axiomas Operativos (Las Reglas del Código)

Aquí definimos los `asserts` que deben cumplirse para validar la tesis:

| Axioma | Tradución para Programadores | Assert de Validación |
| :--- | :--- | :--- |
| **A1: Composición** | El objeto es un `Composite` de partes heterogéneas. | `assert len(objeto.components) > 1` |
| **A2: Estructura** | La arquitectura importa más que los datos crudos. | `assert sistema.run() != lista_partes.run()` |
| **A4: Persistencia** | El estado del sistema sobrevive a reinicios de sus partes. | `assert sistema.state == stable` después de `component.reset()` |

## 3. Criterios de Fallo (Excepciones)

Nuestro sistema lanza un `ValidationException` si:
1.  **Reduccionismo:** Un modelo simple (sólo micro) explica lo mismo que nuestro modelo complejo. (Principio DRY: No repitas lógica si no añade valor).
2.  **Incoherencia:** Los datos de la simulación divergen de los datos reales de entrada. (Error de Integración).
3.  **Caja Negra:** Si el modelo acierta pero no podemos explicar *por qué* (falta de trazabilidad).
