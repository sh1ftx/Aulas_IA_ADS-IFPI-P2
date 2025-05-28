import pandas as pd
import matplotlib.pyplot as plt

# Verificando a versão do pandas
print("Testando a versão do pandas")
print(pd.__version__)

# Lendo o arquivo CSV
print("Exibindo um arquivo .CSV")
df = pd.read_csv('database/iris.csv')
df.columns = ['sepal_lenght', 'sepal_width','petal_lenght',  'petal_width', 'class']

# Mostrando formato dos dados
print("Exibindo o formato de dado:")
print('Mostrando o shape: ')
print(df.shape)
print('------------------------------------------------------------')

print(df.columns)
df['class'] = df['class'].astype('category')
df['class1'] = df['class'].cat.codes
print(df.info())
X = df.loc[: , 'sepal_lenght': 'petal_width']
y = df['class1']
