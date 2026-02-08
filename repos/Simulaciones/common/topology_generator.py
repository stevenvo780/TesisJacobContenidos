"""
topology_generator.py — Generador de Topologías Scale-Free y Small-World para GPU.
Crea matrices de adyacencia dispersas compatibles con torch.sparse.

Uso:
    from topology_generator import generate_scale_free, generate_small_world
    adj = generate_scale_free(n_agents=400, m=3)  # Barabási-Albert
    adj = generate_small_world(n_agents=400, k=4, p=0.1)  # Watts-Strogatz
"""

import torch
import numpy as np
try:
    import networkx as nx
    HAS_NETWORKX = True
except ImportError:
    HAS_NETWORKX = False
    print("⚠️ networkx no instalado. Topologías complejas deshabilitadas.")

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def _networkx_to_sparse_torch(G, row_normalize=True):
    """
    Convierte un grafo NetworkX a tensor disperso PyTorch.
    
    Args:
        G: NetworkX Graph
        row_normalize: Si True, normaliza por grado (suma de fila = 1)
    
    Returns:
        torch.sparse_coo_tensor (N, N) en DEVICE
    """
    n = G.number_of_nodes()
    edges = list(G.edges())
    
    # Bidireccional
    row = []
    col = []
    for u, v in edges:
        row.append(u)
        col.append(v)
        if not G.is_directed():
            row.append(v)
            col.append(u)
    
    indices = torch.tensor([row, col], dtype=torch.long)
    values = torch.ones(len(row), dtype=torch.float32)
    
    adj = torch.sparse_coo_tensor(indices, values, (n, n))
    
    if row_normalize:
        # Normalizar por grado (Row-sum = 1)
        dense = adj.to_dense()
        row_sum = dense.sum(dim=1, keepdim=True).clamp(min=1.0)
        dense = dense / row_sum
        # Reconvertir a sparse
        adj = dense.to_sparse_coo()
    
    return adj.to(DEVICE)


def generate_scale_free(n_agents, m=3, seed=None):
    """
    Genera topología Scale-Free (Barabási-Albert).
    
    Args:
        n_agents: Número de agentes (nodos)
        m: Número de aristas a añadir por nodo nuevo
        seed: Semilla para reproducibilidad
    
    Returns:
        torch.sparse_coo_tensor (n_agents, n_agents)
    """
    if not HAS_NETWORKX:
        raise ImportError("networkx requerido para topologías complejas")
    
    G = nx.barabasi_albert_graph(n_agents, m, seed=seed)
    return _networkx_to_sparse_torch(G)


def generate_small_world(n_agents, k=4, p=0.1, seed=None):
    """
    Genera topología Small-World (Watts-Strogatz).
    
    Args:
        n_agents: Número de agentes (nodos)
        k: Cada nodo conectado a k vecinos cercanos
        p: Probabilidad de reconexión aleatoria
        seed: Semilla para reproducibilidad
    
    Returns:
        torch.sparse_coo_tensor (n_agents, n_agents)
    """
    if not HAS_NETWORKX:
        raise ImportError("networkx requerido para topologías complejas")
    
    G = nx.watts_strogatz_graph(n_agents, k, p, seed=seed)
    return _networkx_to_sparse_torch(G)


def generate_regular_grid(grid_size):
    """
    Genera topología de grilla regular (4-conectada).
    Equivalente a la difusión por defecto, pero como matriz.
    
    Returns:
        torch.sparse_coo_tensor (grid_size*grid_size, grid_size*grid_size)
    """
    n = grid_size * grid_size
    row = []
    col = []
    
    for i in range(grid_size):
        for j in range(grid_size):
            idx = i * grid_size + j
            # Vecinos 4-conectados
            neighbors = []
            if i > 0:
                neighbors.append((i-1) * grid_size + j)
            if i < grid_size - 1:
                neighbors.append((i+1) * grid_size + j)
            if j > 0:
                neighbors.append(i * grid_size + (j-1))
            if j < grid_size - 1:
                neighbors.append(i * grid_size + (j+1))
            
            for nb in neighbors:
                row.append(idx)
                col.append(nb)
    
    indices = torch.tensor([row, col], dtype=torch.long)
    values = torch.ones(len(row), dtype=torch.float32)
    
    adj = torch.sparse_coo_tensor(indices, values, (n, n))
    
    # Row normalize
    dense = adj.to_dense()
    row_sum = dense.sum(dim=1, keepdim=True).clamp(min=1.0)
    dense = dense / row_sum
    
    return dense.to_sparse_coo().to(DEVICE)


def compute_topology_metrics(adj_tensor):
    """
    Calcula métricas de la topología para verificar heterogeneidad.
    
    Returns:
        dict con: mean_degree, std_degree, max_degree, min_degree, sparsity
    """
    dense = adj_tensor.to_dense().cpu().numpy()
    degrees = (dense > 0).sum(axis=1)
    
    n = len(degrees)
    n_edges = (dense > 0).sum()
    
    return {
        "n_nodes": n,
        "mean_degree": float(degrees.mean()),
        "std_degree": float(degrees.std()),
        "max_degree": int(degrees.max()),
        "min_degree": int(degrees.min()),
        "sparsity": 1.0 - (n_edges / (n * n)),
        "heterogeneity": float(degrees.std() / (degrees.mean() + 1e-8))
    }


if __name__ == "__main__":
    print("🔬 Testing Topology Generator...")
    
    # Test Scale-Free
    sf = generate_scale_free(400, m=3, seed=42)
    metrics_sf = compute_topology_metrics(sf)
    print(f"Scale-Free (400 nodes, m=3): {metrics_sf}")
    
    # Test Small-World
    sw = generate_small_world(400, k=4, p=0.1, seed=42)
    metrics_sw = compute_topology_metrics(sw)
    print(f"Small-World (400 nodes, k=4, p=0.1): {metrics_sw}")
    
    # Test Regular Grid
    rg = generate_regular_grid(20)  # 400 nodes
    metrics_rg = compute_topology_metrics(rg)
    print(f"Regular Grid (20x20): {metrics_rg}")
    
    print("✅ Topology Generator OK")
