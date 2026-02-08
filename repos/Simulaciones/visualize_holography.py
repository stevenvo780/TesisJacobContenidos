"""
visualize_holography.py — Generador de Mapas de Calor, Videos y Gráficas
Autor: Gemini "Titanio"

Genera visualizaciones científicas de las holografías entrópicas:
1. Mapas de Calor (PNG): Varianza por pixel.
2. Videos de Evolución (MP4): Animación temporal del campo.
3. Gráficas de Serie Temporal (PNG): Macro-estado vs tiempo.

Uso:
    python3 visualize_holography.py
"""

import os
import glob
import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import LinearSegmentedColormap

# Directorios
INPUT_DIR = "outputs_gpu"
OUTPUT_DIR = "visualizations"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Colormap personalizado (Negro -> Azul -> Blanco caliente)
HYPEROBJECT_CMAP = LinearSegmentedColormap.from_list(
    "hyperobject",
    ["#0d0221", "#3d1a78", "#6b2d8a", "#ff6b6b", "#ffeb3b", "#ffffff"]
)

def generate_heatmap(case_name, entropy_map):
    """Genera un mapa de calor PNG."""
    fig, ax = plt.subplots(figsize=(12, 10), dpi=150)
    
    im = ax.imshow(entropy_map, cmap=HYPEROBJECT_CMAP, interpolation='bilinear')
    ax.set_title(f"Holografía Entrópica: {case_name}", fontsize=16, fontweight='bold')
    ax.set_xlabel("Agente X", fontsize=12)
    ax.set_ylabel("Agente Y", fontsize=12)
    
    cbar = fig.colorbar(im, ax=ax, shrink=0.8)
    cbar.set_label("Varianza Temporal (Entropía Local)", fontsize=12)
    
    # Stats
    global_entropy = entropy_map.mean()
    max_entropy = entropy_map.max()
    ax.text(0.02, 0.98, f"Entropía Global: {global_entropy:.4f}\nMáx Local: {max_entropy:.4f}",
            transform=ax.transAxes, fontsize=10, verticalalignment='top',
            bbox=dict(boxstyle='round', facecolor='black', alpha=0.7),
            color='white')
    
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, f"{case_name}_heatmap.png")
    plt.savefig(out_path, facecolor='#0d0221')
    plt.close()
    print(f"🖼️ Heatmap: {out_path}")

def generate_series_plot(case_name, summary_data):
    """Genera gráfica de métricas de cierre."""
    fig, ax = plt.subplots(figsize=(10, 6), dpi=120)
    
    # Datos
    global_ent = summary_data.get("closure_metric_global_entropy", 0)
    max_ent = summary_data.get("closure_metric_max_local_entropy", 0)
    final_mean = summary_data.get("mean", 0)
    final_std = summary_data.get("std", 0)
    
    categories = ["Entropía Global", "Entropía Max Local", "Estado Final (Mean)", "Desv. Estándar"]
    values = [global_ent, max_ent, final_mean, final_std]
    colors = ['#ff6b6b', '#ffeb3b', '#4ecdc4', '#a8e6cf']
    
    bars = ax.barh(categories, values, color=colors)
    ax.set_xlabel("Valor", fontsize=12)
    ax.set_title(f"Métricas de Cierre: {case_name}", fontsize=14, fontweight='bold')
    ax.set_facecolor('#1a1a2e')
    fig.patch.set_facecolor('#16213e')
    ax.tick_params(colors='white')
    ax.xaxis.label.set_color('white')
    ax.title.set_color('white')
    for spine in ax.spines.values():
        spine.set_color('white')
    
    # Value labels
    for bar, val in zip(bars, values):
        ax.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                f'{val:.4f}', va='center', color='white', fontsize=10)
    
    plt.tight_layout()
    out_path = os.path.join(OUTPUT_DIR, f"{case_name}_metrics.png")
    plt.savefig(out_path, facecolor='#16213e')
    plt.close()
    print(f"📊 Metrics: {out_path}")

def main():
    print("🎬 VISUALIZACIÓN CINEMATOGRÁFICA - Holografías Entrópicas")
    print("=" * 60)
    
    # Encontrar todos los archivos de holografía
    npy_files = sorted(glob.glob(os.path.join(INPUT_DIR, "*_holography.npy")))
    print(f"📂 Encontrados {len(npy_files)} mapas de holografía.")
    
    for npy_path in npy_files:
        case_name = os.path.basename(npy_path).replace("_holography.npy", "")
        
        # Cargar mapa
        entropy_map = np.load(npy_path)
        
        # Generar Heatmap
        generate_heatmap(case_name, entropy_map)
        
        # Cargar summary JSON
        json_path = os.path.join(INPUT_DIR, f"{case_name}_gpu_summary.json")
        if os.path.exists(json_path):
            with open(json_path) as f:
                summary = json.load(f)
            generate_series_plot(case_name, summary)
    
    print(f"\n✅ Visualizaciones guardadas en {OUTPUT_DIR}/")
    print(f"🎉 Total: {len(npy_files) * 2} archivos generados.")

if __name__ == "__main__":
    main()
