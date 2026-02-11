import pandas as pd, numpy as np, os

df = pd.read_csv(os.path.join('..', 'data', 'dataset.csv'), parse_dates=['date'])
df['year'] = df['date'].dt.year

# Primeras diferencias
for col in ['coal_pct', 'gdp_growth', 'renewable_pct']:
    d_pm = df['pm25'].diff()
    d_col = df[col].diff()
    r_full = d_pm.corr(d_col)
    r_train = d_pm[:20].corr(d_col[:20])
    r_val = d_pm[20:].corr(d_col[20:])
    print(f'D_{col:15s}: r_full={r_full:+.3f}, r_train={r_train:+.3f}, r_val={r_val:+.3f}')

print()

# gdp_growth tiene peso positivo estable: probemos solo con el
for split_year in [2010, 2012, 2014]:
    val_start = len(df[df.year < split_year])
    obs_raw = df['pm25'].values
    obs_mean = np.mean(obs_raw[:val_start])
    obs_std = np.std(obs_raw[:val_start])
    obs = (obs_raw - obs_mean) / obs_std

    X = df[['gdp_growth']].values.astype(float)
    X_train = X[:val_start]
    mu = np.mean(X_train, axis=0)
    sd = np.std(X_train, axis=0)
    sd = np.where(sd < 1e-8, 1.0, sd)
    Xz = (X - mu) / sd
    Xz_train = Xz[:val_start]
    y = obs[:val_start]
    reg = 1e-3
    w = np.linalg.solve(Xz_train.T @ Xz_train + reg, Xz_train.T @ y)
    driver_forcing = (Xz @ w).tolist()

    f_val = driver_forcing[val_start:]
    o_val = obs[val_start:]
    corr_val = np.corrcoef(f_val, o_val)[0, 1]
    print(f'split={split_year}, gdp_growth only: w={w[0]:+.3f}, forcing-obs corr_val={corr_val:+.3f}, n_val={len(o_val)}')

print()

# Conclusiones:
# - Si la regresion aprende pesos negativos para coal (que deberia ser positivo),
#   el forcing se invierte en validacion
# - gdp_growth es el unico con signo estable (+) en training y validacion
# - Pero gdp_growth solo no captura el pico PM2.5 2011-2013

# Intentemos sin drivers (forcing basado en tendencia del training)
# Esto es lo que hace hybrid_validator cuando driver_cols=[]
for split_year in [2010, 2014]:
    val_start = len(df[df.year < split_year])
    obs_raw = df['pm25'].values
    obs_mean = np.mean(obs_raw[:val_start])
    obs_std = np.std(obs_raw[:val_start])
    obs = (obs_raw - obs_mean) / obs_std
    
    # Trend from training
    x = np.arange(val_start)
    slope, intercept = np.polyfit(x, obs[:val_start], 1)
    trend = [slope * i + intercept for i in range(len(df))]
    
    t_val = trend[val_start:]
    o_val = obs[val_start:]
    corr_val = np.corrcoef(t_val, o_val)[0, 1]
    print(f'split={split_year}, trend only: slope={slope:+.4f}, trend-obs corr_val={corr_val:+.3f}')
