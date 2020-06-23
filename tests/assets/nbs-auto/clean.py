import pandas as pd

# + tags=["parameters"]
upstream = {'load.py': None}
product = {'nb': 'output/clean.ipynb', 'data': 'output/clean.csv'}

# +
df = pd.read_csv(str(upstream['load.py']['data']))
df = df + 1
df.to_csv(str(product['data']), index=False)
