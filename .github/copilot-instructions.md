# Copilot Instructions

Responder siempre en español.

## Project Overview

Doctoral thesis ("Ontología Operativa de Hiperobjetos") validating the computational reality of **Hyperobjects** (Climate, Economy, Pandemics) through hybrid ABM+ODE models. Central hypothesis (H1): a hyperobject is real if its macroscopic model (ODE) reduces the entropy of its microscopic components (ABM) by >30%, measured via the **Effective Dependence Index (EDI > 0.30)**.

## Build & Run

Python 3.10+ required. No test suite or linter exists.

```bash
# Install dependencies
pip install -r repos/Simulaciones/requirements.txt

# Run a single case validation (climate example)
cd repos/Simulaciones/caso_clima/src && python3 validate.py

# Run finance validation
cd repos/Simulaciones/caso_finanzas/src && python3 validate.py

# Audit all 18 simulation cases (reads TesisDesarrollo/02_Modelado_Simulacion/*/metrics.json)
python3 repos/scripts/auditar_simulaciones.py

# Evaluate and write summary tables
python3 repos/scripts/evaluar_simulaciones.py --write

# Update tables in 02_Modelado_Simulacion.md
python3 repos/scripts/actualizar_tablas_002.py
```

Each `validate.py` outputs `metrics.json` and `report.md` to its case's `outputs/` directory. It runs two phases: synthetic (controlled ground truth) then real data—if synthetic fails, real is gated to fail.

## Architecture

### HybridModel Pattern (5-file convention per case)

Every case in `repos/Simulaciones/caso_*/src/` follows the same structure:

| File | Role |
|------|------|
| `validate.py` | Orchestrator: calibrate → simulate → evaluate C1–C5 → write outputs |
| `abm.py` | Micro layer: n×n grid with diffusion, macro coupling, forcing, damping, nudging |
| `ode.py` | Macro layer: `dX/dt = α(F - βX) + noise` with optional data assimilation |
| `metrics.py` | EDI, CR, EI (Hoel), RMSE, correlation, dominance, window variance |
| `data.py` | Data fetching (Meteostat for climate, yfinance for finance, synthetic for others) |

The ABM update rule combines five terms per cell per step: spatial diffusion, external forcing, macro coupling (toward global mean), damping, and noise. Imports between files use bare module names (`from abm import simulate_abm`), so scripts must run from within the `src/` directory.

### Simulation Pipeline

1. **Calibration** on training window: grid-search ABM params (forcing_scale, macro_coupling, damping) + least-squares fit ODE (alpha, beta)
2. **Full model** run (ABM + ODE) with `assimilation_strength=0.0` to avoid leakage
3. **Reduced model** run: same ABM with `macro_coupling=0.0, forcing_scale=0.0` (ablation baseline)
4. **EDI** = `(rmse_reduced - rmse_abm) / rmse_reduced` computed on validation window only
5. **C1–C5 protocol** evaluation + Symploké, non-locality, persistence checks

### Validation Rejection Thresholds

| Metric | Threshold | Meaning |
|--------|-----------|---------|
| EDI < 0.30 | REJECT | No macro structure detected |
| EDI > 0.90 | REJECT | Tautology / calibration error |
| Coupling < 0.10 | REJECT | Epiphenomenalism |
| RMSE < 1e-10 | REJECT | Overfitting fraud |
| CR > 2.0 | PASS | Internal cohesion exceeds external |

### Known Case Results

- **Climate** (`caso_clima`): Validated — EDI ≈ 0.45, Strong Emergence
- **Finance** (`caso_finanzas`): Rejected — EDI ≈ 0.05, Temporal Aliasing/Reflexivity

### Two Repository Locations for Cases

- `repos/Simulaciones/caso_*/` — Runnable Python code (all 20 cases have the 5-file `src/` structure)
- `TesisDesarrollo/02_Modelado_Simulacion/*_caso_*/` — Thesis narrative per case with `metrics.json`, `report.md`, and `docs/` (audit scripts read from here)

## Conventions

- **Occam's Razor**: Never claim emergence unless EDI backs it. If ABM-alone or noise explains the data, reject the hyperobject.
- **Bilingual**: Code identifiers in English; comments and documentation in Spanish. Respond to the user in Spanish.
- **Pure NumPy/Pandas**: No ML frameworks. Parameters passed as plain dicts, reproducibility via explicit seeds.
- **Train/validation split**: All metrics evaluated on `val_df = df[df["date"] >= split_date]` only.
- **No look-ahead**: Data assimilation uses lagged observations `[None] + obs[:-1]`. Evaluation runs use `assimilation_strength=0.0`.
- **Metastable emergence**: Hyperobjects are metastable attractors, not strong autonomous attractors. Nudging is theoretically justified as hyperobject-matter coupling, not a computational artifact.
- **Terminology**: See `TesisDesarrollo/00_Marco_Conceptual/00_02_Glosario_Maestro.md` for domain terms (Symploké, Causal Descendence, Nudging, etc.).
