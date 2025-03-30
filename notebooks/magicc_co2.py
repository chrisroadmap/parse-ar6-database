# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.7
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

# %%
# will it collapse if I give it a 3GB file?
df = pd.read_csv('../data/input/AR6_Scenarios_Database_World_ALL_CLIMATE_v1.1.csv')

# %%
df.Variable.unique()

# %%
df.loc[df.Variable == 'AR6 climate diagnostics|Atmospheric Concentrations|CO2|FaIRv1.6.2|50.0th Percentile']

# %%
df.loc[df.Variable == 'AR6 climate diagnostics|Atmospheric Concentrations|CO2|MAGICCv7.5.3|50.0th Percentile', '2024'].median()

# %%
df.loc[df.Variable == 'AR6 climate diagnostics|Atmospheric Concentrations|CO2|FaIRv1.6.2|50.0th Percentile', '2024'].median()

# %%
pl.hist(df.loc[df.Variable == 'AR6 climate diagnostics|Atmospheric Concentrations|CO2|FaIRv1.6.2|50.0th Percentile', '2024'], alpha=0.3, label='FAIR', bins=np.arange(414, 430.01, 0.5))
pl.hist(df.loc[df.Variable == 'AR6 climate diagnostics|Atmospheric Concentrations|CO2|MAGICCv7.5.3|50.0th Percentile', '2024'], alpha=0.3, label='MAGICC', bins=np.arange(414, 430.01, 0.5))
pl.axvline(422.77, color='k', label='NOAA GML')
pl.legend()
pl.title('CO2 concentrations 2024')

# %%
