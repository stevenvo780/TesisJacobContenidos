#!/usr/bin/env python3
"""
renumber_cases.py — Renumerar todos los casos para eliminar gaps (06, 12, 17)

Mapa de renumeración:
OLD → NEW
01 → 01 (clima)
02 → 02 (conciencia)
03 → 03 (contaminacion)
04 → 04 (energia)
05 → 05 (epidemiologia)
06 → REMOVED
07 → 06 (falsacion_exogeneidad)
08 → 07 (falsacion_no_estacionariedad)
09 → 08 (falsacion_observabilidad)
10 → 09 (finanzas)
11 → 10 (justicia)
12 → REMOVED
13 → 11 (movilidad)
14 → 12 (paradigmas)
15 → 13 (politicas_estrategicas)
16 → 14 (postverdad)
17 → REMOVED
18 → 15 (wikipedia)
19 → 16 (deforestacion)
20 → 17 (oceanos)
21 → 18 (urbanizacion)
22 → 19 (acidificacion_oceanica)
23 → 20 (kessler)
24 → 21 (salinizacion)
25 → 22 (fosforo)
26 → 23 (erosion_dialectica)
27 → 24 (microplasticos)
28 → 25 (acuiferos)
29 → 26 (starlink)
30 → 27 (riesgo_biologico)
31 → 28 (fuga_cerebros)
32 → 29 (iot)
"""

import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
SIMULACIONES_DIR = ROOT / "repos" / "Simulaciones"
TESIS_DEV_DIR = ROOT / "TesisDesarrollo" / "02_Modelado_Simulacion"

# Casos removidos (no existen en Simulaciones)
REMOVED = {6, 12, 17}

# Construir mapa de renumeración
def build_renumber_map():
    """Construye mapa OLD_NUM → NEW_NUM"""
    renumber_map = {}
    new_num = 1
    for old_num in range(1, 33):
        if old_num in REMOVED:
            continue
        renumber_map[old_num] = new_num
        new_num += 1
    return renumber_map

def get_case_folders(directory):
    """Obtiene lista de carpetas de casos ordenadas"""
    if not directory.exists():
        return []
    pattern = re.compile(r'^(\d{2})_caso_(.+)$')
    folders = []
    for d in sorted(directory.iterdir()):
        if d.is_dir():
            m = pattern.match(d.name)
            if m:
                folders.append((int(m.group(1)), m.group(2), d))
    return folders

def rename_folders(directory, renumber_map, dry_run=True):
    """Renombra carpetas según el mapa"""
    folders = get_case_folders(directory)
    renames = []
    
    for old_num, case_name, folder_path in folders:
        if old_num not in renumber_map:
            print(f"⚠️ Caso {old_num} no en mapa (probablemente removido)")
            continue
        
        new_num = renumber_map[old_num]
        old_name = folder_path.name
        new_name = f"{new_num:02d}_caso_{case_name}"
        
        if old_name == new_name:
            continue
        
        new_path = folder_path.parent / new_name
        renames.append((folder_path, new_path, old_name, new_name))
    
    # Ordenar de mayor a menor para evitar colisiones
    renames.sort(key=lambda x: x[2], reverse=True)
    
    for old_path, new_path, old_name, new_name in renames:
        if dry_run:
            print(f"  📁 {old_name} → {new_name}")
        else:
            # Usar rename temporal para evitar colisiones
            temp_path = old_path.parent / f"_temp_{new_name}"
            shutil.move(str(old_path), str(temp_path))
            shutil.move(str(temp_path), str(new_path))
            print(f"  ✅ {old_name} → {new_name}")
    
    return renames

def update_file_references(file_path, renumber_map):
    """Actualiza referencias numéricas en un archivo"""
    if not file_path.exists():
        return False
    
    content = file_path.read_text(encoding='utf-8')
    original = content
    
    # Patrones a reemplazar
    for old_num, new_num in sorted(renumber_map.items(), reverse=True):
        if old_num == new_num:
            continue
        
        # Formato XX_caso_  
        old_pattern = f"{old_num:02d}_caso_"
        new_pattern = f"{new_num:02d}_caso_"
        content = content.replace(old_pattern, new_pattern)
        
        # Formato (XX) en listas
        old_pattern = f"({old_num:02d})"
        new_pattern = f"({new_num:02d})"
        content = content.replace(old_pattern, new_pattern)
        
        # Formato | XX | en tablas
        old_pattern = f"| {old_num:02d} |"
        new_pattern = f"| {new_num:02d} |"
        content = content.replace(old_pattern, new_pattern)
    
    if content != original:
        file_path.write_text(content, encoding='utf-8')
        return True
    return False

def main():
    print("🔢 RENUMERACIÓN DE CASOS (32 → 29)")
    print("=" * 60)
    
    renumber_map = build_renumber_map()
    
    print("\n📋 MAPA DE RENUMERACIÓN:")
    for old_num, new_num in sorted(renumber_map.items()):
        if old_num != new_num:
            print(f"   {old_num:02d} → {new_num:02d}")
    
    print(f"\n📁 CARPETAS A RENOMBRAR en repos/Simulaciones:")
    sim_renames = rename_folders(SIMULACIONES_DIR, renumber_map, dry_run=True)
    
    print(f"\n📁 CARPETAS A RENOMBRAR en TesisDesarrollo/02_Modelado_Simulacion:")
    dev_renames = rename_folders(TESIS_DEV_DIR, renumber_map, dry_run=True)
    
    # Confirmar
    print(f"\n⚠️ CAMBIOS PENDIENTES:")
    print(f"   - {len(sim_renames)} carpetas en Simulaciones")
    print(f"   - {len(dev_renames)} carpetas en TesisDesarrollo")
    
    print("\n" + "=" * 60)
    print("Para ejecutar los cambios, ejecuta:")
    print("  python3 repos/scripts/renumber_cases.py --execute")
    
    import sys
    if "--execute" in sys.argv:
        print("\n🚀 EJECUTANDO RENUMERACIÓN...")
        
        print("\n📁 Renombrando en repos/Simulaciones:")
        rename_folders(SIMULACIONES_DIR, renumber_map, dry_run=False)
        
        print("\n📁 Renombrando en TesisDesarrollo:")
        rename_folders(TESIS_DEV_DIR, renumber_map, dry_run=False)
        
        print("\n📝 Actualizando referencias en archivos...")
        files_updated = 0
        
        # Actualizar archivos clave
        key_files = [
            ROOT / "TesisFinal" / "Tesis.md",
            ROOT / "TesisDesarrollo" / "04_Casos_De_Estudio" / "04_Casos_De_Estudio.md",
            ROOT / "repos" / "scripts" / "tesis.py",
            ROOT / "repos" / "Simulaciones" / "upgrade_all_data_sources.py",
            ROOT / "repos" / "Simulaciones" / "worldbank_universal_fetcher.py",
        ]
        
        for f in key_files:
            if update_file_references(f, renumber_map):
                print(f"  ✅ {f.name}")
                files_updated += 1
        
        # Actualizar todos los .md en TesisDesarrollo
        for md_file in (ROOT / "TesisDesarrollo").rglob("*.md"):
            if update_file_references(md_file, renumber_map):
                print(f"  ✅ {md_file.relative_to(ROOT)}")
                files_updated += 1
        
        print(f"\n✅ RENUMERACIÓN COMPLETA:")
        print(f"   - {len(sim_renames)} carpetas renombradas en Simulaciones")
        print(f"   - {len(dev_renames)} carpetas renombradas en TesisDesarrollo")
        print(f"   - {files_updated} archivos actualizados")

if __name__ == "__main__":
    main()
