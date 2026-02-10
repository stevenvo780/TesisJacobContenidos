# Copilot Instructions

Responder siempre en español.

## Project Overview

Doctoral thesis ("Irrealismo Operativo de Hiperobjetos") classifying the degree of **operational closure** of massively distributed phenomena (Climate, Deforestation, Pandemics) through hybrid ABM+ODE models. Central hypothesis (H1): a phenomenon exhibits operational closure of degree G when removing its macro construct degrades micro prediction by EDI ≥ G/100, verifiable via C1-C5 protocol with zero-nudging. No metaphysical existence is affirmed or denied.

## Build & Run

Python 3.10+ required. No test suite or linter exists.

```bash
# Install dependencies
pip install -r repos/Simulaciones/requirements.txt

# Run a single case validation (deforestation — strongest case)
cd repos/Simulaciones/16_caso_deforestacion/src && python3 validate.py

# Run climate validation
cd repos/Simulaciones/01_caso_clima/src && python3 validate.py

# Audit all 29 simulation cases
python3 repos/scripts/auditar_simulaciones.py
python3 repos/scripts/_audit_fresh.py

# Evaluate and write summary tables
python3 repos/scripts/evaluar_simulaciones.py --write

# Update tables in 02_Modelado_Simulacion.md
python3 repos/scripts/actualizar_tablas_002.py

# Build final thesis
python3 repos/scripts/tesis.py build
```

Each `validate.py` outputs `metrics.json` and `report.md` to its case's `outputs/` directory. It runs two phases: synthetic (controlled ground truth) then real data—if synthetic fails, real is gated to fail.

## Architecture

### HybridModel Pattern (5-file convention per case)

Every case in `repos/Simulaciones/{NN}_caso_*/src/` follows the same structure:

| File | Role |
|------|------|
| `validate.py` | Orchestrator: calibrate → simulate → evaluate C1–C5 → write outputs |
| `abm.py` | Micro layer: n×n grid with diffusion, macro coupling, forcing, damping, nudging |
| `ode.py` | Macro layer: `dX/dt = α(F - βX) + noise` with optional data assimilation |
| `metrics.py` | EDI, CR, EI (Hoel), RMSE, correlation, dominance, window variance |
| `data.py` | Data fetching (Meteostat for climate, yfinance for finance, World Bank for most) |

The ABM update rule combines five terms per cell per step: spatial diffusion, external forcing, macro coupling (toward global mean), damping, and noise. Imports between files use bare module names (`from abm import simulate_abm`), so scripts must run from within the `src/` directory.

### Simulation Pipeline

1. **Calibration** on training window: grid-search ABM params (forcing_scale, macro_coupling, damping) + least-squares fit ODE (alpha, beta)
2. **Full model** run (ABM + ODE) with `assimilation_strength=0.0` to avoid leakage
3. **Reduced model** run: same ABM with `macro_coupling=0.0, forcing_scale=0.0` (ablation baseline)
4. **EDI** = `(rmse_reduced - rmse_abm) / rmse_reduced` computed on validation window only
5. **C1–C5 protocol** evaluation + Symploké, non-locality, persistence checks

### Emergence Level Taxonomy

| Level | Category | EDI | Meaning |
|:-----:|:---------|:----|:--------|
| 4 | strong | ≥0.30 + C1-C5 | Strong operational closure |
| 3 | weak | 0.10-0.30 + sig | Functional component |
| 2 | suggestive | >0.01 + sig | Suggestive signal |
| 1 | trend | >0 but not sig | Non-significant trend |
| 0 | null | ≤0 or not sig | No signal |
| — | falsification | — | Correct negative control |

### Known Case Results (current data)

- **Deforestation** (16): EDI=0.633, Level 4, overall_pass=True. Von Thünen model + BC full.
- **Microplastics** (24): EDI=0.427, Level 4, overall_pass=True. Jambeck model. No BC.
- **Climate** (01): EDI=0.010, Level 1. Probe insufficient, not refutation of phenomenon.
- **Finance** (09): EDI=0.040, Level 2. Reflexivity/temporal aliasing.
- **Overall**: 2/29 pass, 6/29 significant, Levels: {0:13, 1:7, 2:3, 3:1, 4:2}

### Two Repository Locations for Cases

- `repos/Simulaciones/{NN}_caso_*/` — Runnable Python code (all 29 cases have the 5-file `src/` structure)
- `TesisDesarrollo/02_Modelado_Simulacion/{NN}_caso_*/` — Thesis narrative per case with `metrics.json`, `report.md`, and `docs/` (audit scripts read from here)

## Conventions

- **Occam's Razor**: Never claim operational closure unless EDI backs it. If ABM-alone or noise explains the data, classify as Level 0.
- **Operative irrealism**: Never affirm "X *is* a hyperobject"; affirm "X exhibits operational closure of degree G per this instrument".
- **Bilingual**: Code identifiers in English; comments and documentation in Spanish. Respond to the user in Spanish.
- **Pure NumPy/Pandas**: No ML frameworks. Parameters passed as plain dicts, reproducibility via explicit seeds.
- **Train/validation split**: All metrics evaluated on `val_df = df[df["date"] >= split_date]` only.
- **No look-ahead**: Data assimilation uses lagged observations `[None] + obs[:-1]`. Evaluation runs use `assimilation_strength=0.0`.
- **Zero-nudging**: All evaluation runs with assimilation_strength=0 (enforced in 9 code points in hybrid_validator.py).
- **Terminology**: See `TesisDesarrollo/00_Marco_Conceptual/00_02_Glosario_Maestro.md` for domain terms (Symploké, Operational Closure, Nudging, etc.).
