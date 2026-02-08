
import os
import sys
import glob
import subprocess
import time
from joblib import Parallel, delayed

# Configuración Maestra
GRID_SIZE = 120  # ~14,400 agentes (Factor 36x sobre el original)
N_RUNS = 100      # Intervalos de confianza < 0.5%
MAX_WORKERS = -1 # Usar TODOS los cores disponibles (32)

def run_case_validation(validate_path):
    """
    Ejecuta un script validate.py inyectándole la configuración de alto rendimiento
    a través de variables de entorno (HYPER_GRID_SIZE, HYPER_N_RUNS).
    """
    case_dir = os.path.dirname(os.path.dirname(validate_path))
    case_name = os.path.basename(case_dir)
    print(f"🚀 Iniciando {case_name} (Grid={GRID_SIZE}, Runs={N_RUNS})...")
    
    # Preparar entorno
    env = os.environ.copy()
    env["HYPER_GRID_SIZE"] = str(GRID_SIZE)
    env["HYPER_N_RUNS"] = str(N_RUNS)
    # Force numpy to use 1 thread per process to avoid oversubscription
    env["OMP_NUM_THREADS"] = "1"
    env["MKL_NUM_THREADS"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    
    # 2. Ejecutar
    start_time = time.time()
    try:
        # Usamos python3 explícito del entorno actual
        cmd = [sys.executable, validate_path]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True, env=env)
        duration = time.time() - start_time
        print(f"✅ {case_name} completado en {duration:.2f}s")
        return {"case": case_name, "status": "success", "duration": duration, "output": result.stdout}
    except subprocess.CalledProcessError as e:
        print(f"❌ {case_name} falló: {e.stderr[:500]}") # Mostrar más error
        return {"case": case_name, "status": "error", "error": e.stderr}

def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    sim_dir = os.path.join(root_dir, "repos", "Simulaciones")
    
    # Buscar todos los validate.py
    validate_scripts = glob.glob(os.path.join(sim_dir, "*_caso_*", "src", "validate.py"))
    
    # Ordernar para consistencia
    validate_scripts.sort()
    
    print(f"🔥 MEGA RUN: Ejecutando {len(validate_scripts)} casos en PARALELO (Workers={MAX_WORKERS}) 🔥")
    print(f"Configuración: Grid Size={GRID_SIZE}x{GRID_SIZE}, Monte Carlo Loops={N_RUNS}")
    print(f"Hardware: Usando {MAX_WORKERS} cores lógicos. NumPy threads limitados a 1 por proceso.")
    
    # Ejecución Paralela
    # backend="loky" es default y robusto
    results = Parallel(n_jobs=MAX_WORKERS, backend="loky")(delayed(run_case_validation)(script) for script in validate_scripts)
    
    # Resumen
    success = [r for r in results if r["status"] == "success"]
    failed = [r for r in results if r["status"] == "error"]
    
    print(f"\n📊 RESUMEN FINAL:")
    print(f"Total: {len(results)}")
    print(f"Éxitos: {len(success)}")
    print(f"Fallos: {len(failed)}")
    
    if failed:
        print("\nLista de Fallos:")
        for f in failed:
             print(f"- {f['case']}: {f.get('error', 'Unknown error')[:200]}...")

if __name__ == "__main__":
    main()
