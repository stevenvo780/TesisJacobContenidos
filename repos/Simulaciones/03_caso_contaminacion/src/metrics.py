import math


def mean(xs):
    return sum(xs) / len(xs) if xs else 0.0


def variance(xs):
    if not xs:
        return 0.0
    m = mean(xs)
    return sum((x - m) ** 2 for x in xs) / len(xs)


def rmse(a, b):
    if len(a) != len(b) or not a:
        return 0.0
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)) / len(a))


def correlation(a, b):
    if len(a) != len(b) or len(a) < 2:
        return 0.0
    ma = mean(a)
    mb = mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den_a = math.sqrt(sum((x - ma) ** 2 for x in a))
    den_b = math.sqrt(sum((y - mb) ** 2 for y in b))
    if den_a == 0.0 or den_b == 0.0:
        return 0.0
    return num / (den_a * den_b)


def window_variance(xs, window):
    if len(xs) < window:
        return variance(xs)
    tail = xs[-window:]
    return variance(tail)


def internal_vs_external_cohesion(grid_series, forcing_series):
    steps = len(grid_series)
    if steps == 0:
        return 0.0, 0.0
    n = len(grid_series[0])

    internal_corrs = []
    external_corrs = []
    for i in range(n):
        for j in range(n):
            cell_series = [grid_series[t][i][j] for t in range(steps)]
            neighbor_series = []
            for t in range(steps):
                neighbors = []
                if i > 0:
                    neighbors.append(grid_series[t][i - 1][j])
                if i < n - 1:
                    neighbors.append(grid_series[t][i + 1][j])
                if j > 0:
                    neighbors.append(grid_series[t][i][j - 1])
                if j < n - 1:
                    neighbors.append(grid_series[t][i][j + 1])
                neighbor_series.append(sum(neighbors) / len(neighbors))

            internal_corrs.append(correlation(cell_series, neighbor_series))
            external_corrs.append(correlation(cell_series, forcing_series))

    internal = mean(internal_corrs)
    external = mean(external_corrs)
    return internal, external


def dominance_share(grid_series):
    steps = len(grid_series)
    if steps == 0:
        return 1.0
    n = len(grid_series[0])
    regional = []
    for t in range(steps):
        total = 0.0
        for i in range(n):
            total += sum(grid_series[t][i])
        regional.append(total / (n * n))

    scores = []
    for i in range(n):
        for j in range(n):
            cell_series = [grid_series[t][i][j] for t in range(steps)]
            scores.append(abs(correlation(cell_series, regional)))

    total = sum(scores) if scores else 1.0
    max_share = max(scores) / total if scores else 1.0
    return max_share


# --- Spatial Metrics (Inequality & Clustering) ---

def gini_coefficient(grid):
    """
    Calculates Gini Coefficient of pollution distribution.
    0 = Perfect Equality (Uniform pollution)
    1 = Perfect Inequality (All pollution in one cell)
    """
    values = [c for row in grid for c in row if c >= 0]
    if not values: return 0.0
    
    sorted_v = sorted(values)
    n = len(values)
    cum_v = [0]
    for v in sorted_v: cum_v.append(cum_v[-1] + v)
    
    numerator = sum((i + 1) * v for i, v in enumerate(sorted_v))
    denominator = n * sum(sorted_v)
    
    if denominator == 0: return 0.0
    
    # Gini formula: (2 * sum(i*xi)) / (n * sum(xi)) - (n + 1) / n
    # Adjusted for 0-indexed i: 
    # G = (2 * sum((i+1)*xi)) / (n * sum(xi)) - (n+1)/n
    return (2 * numerator) / denominator - (n + 1) / n


def morans_i(grid):
    """
    Calculates Moran's I for spatial autocorrelation.
    +1 = Clustered (Pollution clouds)
    0 = Random
    -1 = Dispersed (Checkerboard)
    """
    rows = len(grid)
    cols = len(grid[0])
    N = rows * cols
    
    values = [c for row in grid for c in row]
    mean_v = sum(values) / N
    
    # Denominator: sum((xi - mean)^2)
    denom = sum((x - mean_v)**2 for x in values)
    if denom == 0: return 0.0
    
    # Numerator: N * sum(wij * (xi - mean) * (xj - mean))
    # Weights wij = 1 if neighbors (Queen), 0 otherwise
    num = 0.0
    w_sum = 0.0
    
    for i in range(rows):
        for j in range(cols):
            idx_i = i * cols + j
            val_i = values[idx_i]
            
            # Neighbors
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0: continue
                    ni, nj = i + di, j + dj
                    if 0 <= ni < rows and 0 <= nj < cols:
                        idx_j = ni * cols + nj
                        val_j = values[idx_j]
                        num += (val_i - mean_v) * (val_j - mean_v)
                        w_sum += 1.0
                        
    return (N / w_sum) * (num / denom)
