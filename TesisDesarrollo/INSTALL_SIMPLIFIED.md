# Guía Simplificada de Reproducción (Auditoría Externa)

Este documento permite replicar el entorno de simulación para validar el **Caso Clima (EDI 0.103, CR 2.355 en modo zero-nudging)**.

## 1. Requisitos Previos
*   Python 3.10+
*   pip
*   git

## 2. Instalación Rápida
```bash
# Usar el repositorio local de simulaciones
cd /workspace

# Crear entorno virtual (Recomendado)
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Instalar dependencias exactas
pip install -r repos/Simulaciones/requirements.txt
```

## 3. Ejecución del Caso Clima (Prueba de Humo)
Para ejecutar la validación:

```bash
python3 repos/Simulaciones/caso_clima/src/validate.py
```

*Salida esperada:*
> `EDI: 0.103 | CR: 2.355 | overall_pass: False`

## 4. Notas de Reproducibilidad
*   **Semillas:** El sistema usa `random.seed(42)` por defecto.
*   **Datos:** Los datos de Meteostat están cacheados en `data/raw`. Si desea descargar datos frescos, use `--force-download`.
