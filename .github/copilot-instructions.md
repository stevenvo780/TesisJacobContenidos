# Copilot Instructions

## Project Overview

This repository validates the ontological reality of **Hyperobjects** (Climate, Economy, Pandemics) through hybrid computational models. The central hypothesis (H1): a hyperobject is real if its macroscopic model (ODE) reduces the entropy of its microscopic components (ABM) by more than 30%, measured via the **Effective Dependence Index (EDI > 0.30)**.

## Architecture

The project follows a **HybridModel** pattern combining two simulation layers:

- **ABM (Agent-Based Model)** — `abm.py`: Spatial n×n grid simulation with local diffusion, macro coupling, forcing, damping, and data assimilation (nudging). Represents microscopic dynamics.
- **ODE (Ordinary Differential Equation)** — `ode.py`: Energy balance model (`dT/dt = α(F - βT) + noise`). Represents macroscopic dynamics.
- **Metrics** — `metrics.py`: Computes EDI, Cohesion Ratio (CR), Effective Information (EI/Hoel), RMSE, correlation, and non-locality dominance.
- **Data** — `data.py`: Fetches real-world data (Meteostat for climate, yfinance for finance).
- **Validate** — `validate.py`: Orchestrator that calibrates parameters, runs both models, and evaluates the **C1–C5 protocol**.

Each case study (`caso_clima/`, `caso_finanzas/`) replicates this 5-file structure under `repos/SimulacionClimatica/02_Modelado_Simulacion/`.

### C1–C5 Validation Protocol

| Criterion | What it tests |
|-----------|--------------|
| C1 | Convergence: RMSE < threshold, correlation > 0.7 |
| C2 | Robustness: stability under parameter perturbation |
| C3 | Replication: window variance consistency |
| C4 | Validity: domain-law coherence (e.g., more forcing → higher temperature) |
| C5 | Uncertainty: sensitivity bounds < 1.0 |

### Key Metrics

- **EDI** = `(rmse_reduced - rmse_abm) / rmse_reduced` — emergence gain from hybrid model. **EDI > 0.30** confirms hyperobject; **EDI < 0.30** rejects it.
- **CR (Cohesion Ratio)** = `internal_correlation / external_correlation` — Symploké indicator.
- **EI (Effective Information)** — Causal emergence per Hoel's framework.

### Known Case Results

- **Climate**: Validated (EDI ≈ 0.45, Strong Emergence).
- **Finance**: Rejected (EDI ≈ 0.05, Temporal Aliasing/Reflexivity).

## Repository Layout

- **`TesisDesarrollo/`** — Thesis narrative: conceptual framework (`00_`), methodology (`01_`), modeling docs (`02_`), validation (`03_`), case studies (`04_`). Each section has a `*_SINTESIS.md` summary document.
- **`repos/SimulacionClimatica/`** — Python simulation engine (the runnable code).
- **`TesisFinal/`** — Consolidated thesis document (`Tesis.md`).
- **`Artifacts/`** — Debate history and audit records from validation cycles.
- **`scripts/`** — Utility scripts for table generation, simulation evaluation, and auditing.

## Build & Run

**Python 3.10+** required.

```bash
# Install dependencies
pip install -r repos/SimulacionClimatica/requirements.txt

# Run climate validation
python3 repos/SimulacionClimatica/02_Modelado_Simulacion/caso_clima/src/validate.py

# Run finance validation
python3 repos/SimulacionClimatica/02_Modelado_Simulacion/caso_finanzas/src/validate.py

# Audit all simulations (checks file presence, metric sanity, range validation)
python3 scripts/auditar_simulaciones.py

# Evaluate simulations and optionally write results
python3 scripts/evaluar_simulaciones.py --write
```

Each `validate.py` produces a `metrics.json` and `report.md` in its case directory.

## Conventions

- **Occam's Razor rule**: Never postulate a macro layer (Hyperobject) if micro-level interactions (ABM alone) or noise explain the data. All emergence claims must be backed by EDI calculations.
- **Bilingual style**: Code identifiers and structure are in English; comments and documentation are predominantly in Spanish.
- **Pure NumPy/Pandas**: No ML frameworks. Simulations use explicit parameter dictionaries, seed-based reproducibility, and train/validation splits on a `split_date`.
- **Lagged assimilation**: Data assimilation uses `[None] + obs[:-1]` to avoid look-ahead bias.
- **Terminology**: Consult `TesisDesarrollo/00_Marco_Conceptual/00_02_Glosario_Maestro.md` for domain-specific terms (Symploké, Causal Descendence, Nudging, etc.).
- **Academic citations**: Reference Haken (Synergetics) for self-organization metrics and Shannon (Entropy) for information-theoretic measures.
