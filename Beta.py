import pandas as pd
import numpy as np
from statsmodels import regression
import statsmodels.api as smf
from statsmodels.tools.tools import add_constant
import matplotlib.pyplot as plt

#### Importando dados covid19 Brasil
df = pd.read_csv('HIST_PAINEL_COVIDBR_2020_Parte1_08ago2021.csv', sep=';', index_col='data', parse_dates=True)
df_20 = pd.read_csv('HIST_PAINEL_COVIDBR_2020_Parte2_08ago2021.csv', sep=';', index_col='data', parse_dates=True)
df_21 = pd.read_csv('HIST_PAINEL_COVIDBR_2021_Parte1_08ago2021.csv', sep=';', index_col='data', parse_dates=True)
df_211 = pd.read_csv('HIST_PAINEL_COVIDBR_2021_Parte2_08ago2021.csv', sep=';', index_col='data', parse_dates=True)

#### Tratando a base de dados
covid = pd.concat([df, df_20, df_21, df_211])

covid.sort_index(inplace=True)
covid = covid[covid['estado'].isna()]
covid_br = covid['obitosNovos']
covid_br = pd.DataFrame(covid_br)


#### Importando dados ibov
stocks = pd.read_excel('economatica.xlsx', parse_dates=True, index_col=0)

#### Tratando dados 
stocks.replace('-', np.nan, inplace=True) #removendo finais de semana e feriados

def columns(df): #renomeando colunas com as ações
    df.columns = df.columns.str[39:]
columns(stocks)


ibov_cov = pd.concat([stocks, covid_br], axis=1) #concatenando as bases
ibov_cov.dropna(inplace=True)
ibov_pct = ibov_cov.pct_change().dropna() #tratando os dados para a regressão
ibov_pct = ibov_pct.iloc[5:]


def reg(x, y): #função da regressão linear
    X = add_constant(x)
    fit = regression.linear_model.OLS(y, X).fit()
    beta = fit.params[1]
    return beta

dict = {}

for i in stocks.columns:
    x = reg(ibov_pct[i], ibov_pct['obitosNovos'])
    dict[i] = x

plt.scatter(ibov_pct['VALE3'], ibov_pct['obitosNovos'])
plt.show()


