import pandas as pd
import matplotlib.pyplot as plt

# Verificando a versão do pandas
print("Testando a versão do pandas")
print(pd.__version__)

# Lendo o arquivo CSV
print("Exibindo um arquivo .CSV")
df = pd.read_csv('database/iris.csv')

# Mostrando formato dos dados
print("Exibindo o formato de dado:")
print('Mostrando o shape: ')
print(df.shape)
print('------------------------------------------------------------')

