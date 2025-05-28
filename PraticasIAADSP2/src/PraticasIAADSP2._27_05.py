import pandas as pd
import matplotlib.pyplot as plt

# Verificando a versão do pandas
print("Testando a versão do pandas")
print(pd.__version__)

# Lendo o arquivo CSV
print("Exibindo um arquivo .CSV")
df = pd.read_csv('database/mundo_feliz.csv')

# Mostrando formato dos dados
print("Exibindo o formato de dado:")
print('Mostrando o shape: ')
print(df.shape)
print('------------------------------------------------------------')

# Renomeando as colunas
df.columns = ['Country', 'Region', 'rank_felicidade', 'score_felicidade',
              'stand_error', 'PIB', 'Family', 'expect_vida', 'Freedom',
              'currupcao', 'Generosity', 'Dystopia Residual']


df['Country'] = df['Country'].astype('category')
df['classes1'] = df['Country'].cat.codes
# print(df.info())
# print(df.head())

# print(df['Region'].head(15))

df['Region'] = df['Region'].astype('category')
df['classes2'] = df['Region'].cat.codes
print(df.info())
print(df.head(15))
