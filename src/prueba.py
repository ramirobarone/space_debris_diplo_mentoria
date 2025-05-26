# %% 
import pandas as pd
import numpy as np

# %%
df = pd.read_json("../data/raw/satellites.json")

# %%
df.info()