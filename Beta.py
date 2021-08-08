import pandas as pd
import numpy as np
from statsmodels import regression
import statsmodels.api as smf
from statsmodels.tools.tools import add_constant

cov_1 = pd.read_csv('HIST_PAINEL_COVIDBR_2020_Parte1_14jun2021.csv', delimiter=';')
print(cov_1.head())
