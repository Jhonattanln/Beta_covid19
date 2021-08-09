import pandas as pd
import numpy as np
from statsmodels import regression
import statsmodels.api as smf
from statsmodels.tools.tools import add_constant
import matplotlib.pyplot as plt

df = pd.read_csv('HIST_PAINEL_COVIDBR_2020_Parte1_08ago2021.csv', sep=';', index_col='data', parse_dates=True)
df_20 = pd.read_csv('HIST_PAINEL_COVIDBR_2020_Parte2_08ago2021.csv', sep=';', index_col='data', parse_dates=True)
df_21 = pd.read_csv('HIST_PAINEL_COVIDBR_2021_Parte1_08ago2021.csv', sep=';', index_col='data', parse_dates=True)
df_211 = pd.read_csv('HIST_PAINEL_COVIDBR_2021_Parte2_08ago2021.csv', sep=';', index_col='data', parse_dates=True)



covid = pd.concat([df, df_20, df_21, df_211])



covid.sort_index(inplace=True)
covid_br = covid[df['estado'].isna()]
covid['obitosAcumulado'].plot()
plt.show()