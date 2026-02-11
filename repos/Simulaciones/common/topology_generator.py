"""
topology_generator.py — Generadores de topologías para ABM.

Retorna matrices de adyacencia dispersas (row-normalized) para ser usadas
en abm_core/_neighbor_mean_topology.
"""

from __future__ import annotations

import numpy as np
import networkx as nx
from scipy import sparse


def _row_normalize(adj: sparse.spmatrix) -> sparse.csr_matrix:
    """Normaliza filas a suma 1 (evita división por cero)."""
    adj = adj.tocsr().astype(np.float64)
    row_sums = np.asarray(adj.sum(axis=1)).ravel()
    row_sums[row_sums == 0.0] = 1.0
    inv = 1.0 / row_sums
    d_inv = sparse.diags(inv)
    return d_inv @ adj


def _to_sparse_adj(G: nx.Graph) -> sparse.csr_matrix:
    """Convierte grafo a CSR (compatibilidad networkx)."""
    to_sparse = getattr(nx, "to_scipy_sparse_array", None)
    if to_sparse is not None:
        adj = to_sparse(G, format="csr", dtype=np.float64)
    else:
        adj = nx.to_scipy_sparse_matrix(G, format="csr", dtype=np.float64)
    return adj


def generate_small_world(n_agents: int, k: int = 4, p: float = 0.1, seed: int = 42) -> sparse.csr_matrix:
    """Watts-Strogatz small-world, row-normalized."""
    n_agents = max(2, int(n_agents))
    k = int(k)
    if k < 2:
        k = 2
    if k >= n_agents:
        k = n_agents - 1
    if k % 2 == 1:
        k += 1
        if k >= n_agents:
            k = n_agents - 1 if (n_agents - 1) % 2 == 0 else n_agents - 2
    p = float(p)
    if p < 0.0:
        p = 0.0
    if p > 1.0:
        p = 1.0
    G = nx.watts_strogatz_graph(n_agents, k, p, seed=seed)
    return _row_normalize(_to_sparse_adj(G))


def generate_scale_free(n_agents: int, m: int = 3, seed: int = 42) -> sparse.csr_matrix:
    """Barabasi-Albert scale-free, row-normalized."""
    n_agents = max(2, int(n_agents))
    m = int(m)
    if m < 1:
        m = 1
    if m >= n_agents:
        m = n_agents - 1
    G = nx.barabasi_albert_graph(n_agents, m, seed=seed)
    return _row_normalize(_to_sparse_adj(G))
