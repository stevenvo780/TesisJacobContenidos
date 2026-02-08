import random


def simulate_ode(params, steps, seed):
    random.seed(seed)
    alpha = params.get("ode_alpha", params.get("alpha", 0.1))
    beta = params.get("ode_beta", params.get("beta", 0.03))
    noise = params.get("ode_noise", params.get("noise", 0.01))
    x = params.get("p0", params.get("t0", 0.0))

    forcing = params["forcing_series"]
    assimilation_series = params.get("assimilation_series")
    assimilation_strength = params.get("assimilation_strength", 0.0)

    series = []
    for t in range(steps):
        f = forcing[t]
        dx = alpha * (f - beta * x)
        x = x + dx + random.uniform(-noise, noise)

        if assimilation_series is not None and t < len(assimilation_series):
            target = assimilation_series[t]
            if target is not None:
                x = x + assimilation_strength * (target - x)

        series.append(x)

    return {
        "v": series,
        "forcing": forcing,
    }
