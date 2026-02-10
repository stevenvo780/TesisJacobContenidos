#!/usr/bin/env python3
import re
from pathlib import Path

def generate_anchor(text):
    # Genera un anchor de GitHub para los links internos
    anchor = text.lower()
    anchor = re.sub(r'[^\w\s-]', '', anchor).strip().replace(' ', '-')
    anchor = re.sub(r'-+', '-', anchor)
    return anchor

def update_toc(file_path):
    path = Path(file_path)
    if not path.exists():
        print(f"Error: {file_path} no existe")
        return

    lines = path.read_text(encoding="utf-8").splitlines()
    
    headers = []
    toc_start = -1
    toc_end = -1
    
    # Encontrar el inicio y fin de la TOC actual para reemplazarla
    for i, line in enumerate(lines):
        if line.strip() == "## Tabla de Contenidos":
            toc_start = i
        elif toc_start != -1 and toc_end == -1 and line.startswith("---"):
            toc_end = i
        
        # Recolectar headers excluyendo el título principal (# al inicio) y la propia TOC
        if line.startswith("#") and not line.strip().startswith("## Tabla de Contenidos"):
            # El título de la tesis es el primer #. Lo ignoramos si está en las primeras líneas.
            if line.startswith("# ") and i < 5:
                continue
            headers.append(line)

    if toc_start == -1 or toc_end == -1:
        print("No se encontró la sección de Tabla de Contenidos con delimitador '---'")
        # Si no se encuentra el fin pero sí el inicio, intentamos buscar el separador
        return

    # Generar nueva TOC
    toc_lines = ["## Tabla de Contenidos\n"]
    for header in headers:
        level = 0
        while level < len(header) and header[level] == '#':
            level += 1
        
        if level > 4: continue # Limitar profundidad
        
        title = header.replace('#', '').strip()
        anchor = generate_anchor(title)
        
        # Ajustar indentación: # -> nivel 1 (0 espacios), ## -> nivel 2 (2 espacios), etc.
        indent = "  " * (level - 1)
        toc_lines.append(f"{indent}- [{title}](#{anchor})")
    
    toc_lines.append("")
    
    # Reconstruir el archivo
    new_content = lines[:toc_start] + toc_lines + lines[toc_end:]
    path.write_text("\n".join(new_content), encoding="utf-8")
    print(f"✅ Índice detallado actualizado en {file_path}")

if __name__ == "__main__":
    update_toc("TesisFinal/Tesis.md")