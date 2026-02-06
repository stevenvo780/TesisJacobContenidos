# Guía Simplificada de Reproducción (Auditoría Externa)

Este documento permite replicar el entorno de simulación para validar el **Caso Clima (EDI 0.45)**.

## 1. Requisitos Previos
*   Python 3.10+
*   pip
*   git

## 2. Instalación Rápida
```bash
# Clonar repositorio (si tiene acceso)
git clone <repo_url>
cd SimulacionClimatica

# Crear entorno virtual (Recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependencias exactas
pip install -r repos/SimulacionClimatica/requirements.txt
```

## 3. Ejecución del Caso Clima (Prueba de Humo)
Para verificar que el EDI > 0.30 se sostiene:

```bash
python3 repos/SimulacionClimatica/02_Modelado_Simulacion/01_caso_clima/src/validate.py --mode=audit
```

*Salida esperada:*
> `[PASS] EDI: 0.458 | CR: 1.05`

## 4. Notas de Reproducibilidad
*   **Semillas:** El sistema usa `random.seed(42)` por defecto.
*   **Datos:** Los datos de Meteostat están cacheados en `data/raw`. Si desea descargar datos frescos, use `--force-download`.
