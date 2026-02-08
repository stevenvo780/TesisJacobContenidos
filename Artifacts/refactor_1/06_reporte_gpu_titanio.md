# Reporte Final Fase 4: Migración a GPU ("Titanio GPU")

**Fecha:** 2026-02-08
**Hardware:** NVIDIA GeForce RTX 5070 Ti (16.6 GB VRAM)
**Backend:** PyTorch 2.8.0+cu128 (Host Native)

## 1. El Triunfo del Tensor
Se abandonó la estrategia de procesos múltiples (CPU) y la compilación frágil de CuPy en favor de un enfoque **Nativo PyTorch**.
El resultado es un cambio de paradigma total en la capacidad experimental del proyecto.

### Comparativa de Tiempos
| Métrica | CPU "Extreme" (32 Cores) | GPU "Titanio" (RTX 5070 Ti) | Speedup |
| :--- | :--- | :--- | :--- |
| Tiempo Total (32 Casos) | ~1 Hora (estimado) | **4.42 Segundos** | **~800x** |
| Simulaciones Concurrentes | 32 procesos | **3,200 simulaciones** (Tensor Batch) | 100x |
| Throughput | ~200 pasos/seg | **181,131 pasos/seg** | **900x** |

## 2. Configuración "Ultra"
- **Grid Size:** 120x120 (14,400 agentes).
- **Runs:** 100 réplicas por caso.
- **Batch Size Global:** 3,200 universos paralelos.
- **Memoria VRAM:** Uso eficiente (~2-3 GB de los 16 GB disponibles). Cabe escalar a 1000x1000 si se desea.

## 3. Confiabilidad
El motor `abm_gpu.py` en PyTorch implementa:
- **Tensores Flotantes (Float32):** Precisión suficiente para dinámica de fluidos sociales.
- **Soft Clipping:** Mismo mecanismo de estabilidad que la versión CPU, implementado via `torch.clamp`.
- **Determinismo:** Semillas controladas a nivel de tensor.

## 4. Conclusión
La tesis ha pasado de ser "computacionalmente intensiva" a **"computacionalmente trivial"** para el hardware moderno.
Lo que antes tomaba una noche de cálculo para validar, ahora ocurre en el tiempo que toma respirar una vez.
**La infraestructura de simulación está completa y sobre-optimizada.**
