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
print(X.info())
print(X.head())

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
# define o dataset fictício com dados X e sua respectiva saída y para cada linha
# X , y = make_classification(n_samples=5000,n_features=8, n_informative=5,
# n_redundant=2, n_classes=2)
# 80-20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
r = Ridge(alpha=1.0)
r.fit(X_train, y_train)
score = r.score(X_test, y_test) #Em vez de usar um .predict(X_test, y_test) para depois calcular a métrica,
# empregou-se diretamente o método .score( ) que devolve de forma fixa a acurácia;
print(score)
