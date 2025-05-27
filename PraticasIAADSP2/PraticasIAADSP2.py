# from google.colab import drive #importa o drive do colab
# import pandas as pd #importa a biblioteca com o as pd
# #print("Testando a versão do pandas")
# #print(pd.__version__) #verifica a versão do pandas

# drive.mount("/content/drive")

# #print("Exibindo um arquivo .csv")

# df = pd.read_csv("/content/drive/MyDrive/world_happiness_report_2015.csv")

# #print("Exibindo o formato dos dados")

# #print(df.describe)

# #print(df.describe())

# #print(df.shape)

# #print(df.tail())

# #print(df.columns)

# df.columns = ['Country', 'Region', 'rank_felicidade', 'score_felicidade',
#               'stand_error', 'PIB',
#               'Family',
#               'expect_vida', 'Freedom',
#               'corrupcao',
#               'Generosity', 'Dystopia Residual']


# print(df.head())

# print(df.tail())

# print(df.columns)

# print(df.info())

# print()

# print("Nenhum dado nulo")

# print()

# print("Media ",df['expect_vida'].mean())

# print()

# print("Mediana ",df['PIB'].median())

# print()

# print("Valor maximo ",df['PIB'].max())

# #print(df.hist())

# #hp = df.HapRank

# #print(hp.describe())

# #print(df['HapRank'].describe())
# print(df.info())
# # X = df.loc[['Country', 'Region', 'rank_felicidade', 'score_felicidade',
# #               'stand_error', 'PIB',
# #               'Family',
# #               'expect_vida', 'Freedom',
# #               'corrupcao',
# #               'Generosity']]

# X = df.loc[: , 'Country':'Generosity']
# print(X.describe())
# print(X.shape)
# y = df['Dystopia Residencial']
# print(y.shape)

from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
# define o dataset fictício com dados X e sua respectiva saída y para cada linha
X , y = make_classification(n_samples=5000,n_features=8, n_informative=5,
n_redundant=2, n_classes=2)
# 80-20
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
r = Ridge(alpha=1.0)
r.fit(X_train, y_train)
score = r.score(X_test, y_test) #Em vez de usar um .predict(X_test, y_test) para depois calcular a métrica,
# empregou-se diretamente o método .score( ) que devolve de forma fixa a acurácia;
print(score)