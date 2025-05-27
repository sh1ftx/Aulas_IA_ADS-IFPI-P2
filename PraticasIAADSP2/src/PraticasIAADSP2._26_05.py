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

# print(df.columns)
# print('------------------------------------------------------------')
# print()
# print(df.info())
# print('------------------------------------------------------------')
# print()

# # Estatísticas descritivas de uma coluna
# hp = df['rank_felicidade']
# print(hp.describe)
# print('------------------------------------------------------------')

# print()
# print(df['rank_felicidade'].describe())
# print('------------------------------------------------------------')
# print()
# print(df.isnull().sum())
# print('------------------------------------------------------------')
# print()
# print("Média da expectativa de vida:", df['expect_vida'].mean())
# print('------------------------------------------------------------')
# print()
# print("Mediana da expectativa de vida:", df['expect_vida'].median())
# print('------------------------------------------------------------')
# print()
# print("PIB máximo:", df['PIB'].max())

# # Gráfico 1 - Distribuição da Felicidade
# plt.figure(figsize=(10, 6))
# plt.hist(df['score_felicidade'], bins=20, color='skyblue', edgecolor='black')
# plt.title("Distribuição da Felicidade")
# plt.xlabel("Score de Felicidade")
# plt.ylabel("Frequência")
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.savefig("grafico_felicidade.png")  # Salva o gráfico como imagem
# plt.show()

# # Gráfico 2 - Expectativa de vida por região (Boxplot)
# plt.figure(figsize=(12, 6))
# df.boxplot(column='expect_vida', by='Region', rot=90)
# plt.title("Expectativa de Vida por Região")
# plt.suptitle("")  # Remove o título automático do pandas
# plt.xlabel("Região")
# plt.ylabel("Expectativa de Vida")
# plt.tight_layout()
# plt.show()

# # Gráfico 3 - Correlação entre PIB e Expectativa de Vida (Scatter plot)
# plt.figure(figsize=(10, 6))
# plt.scatter(df['PIB'], df['expect_vida'], alpha=0.7, color='seagreen')
# plt.title("Correlação entre PIB e Expectativa de Vida")
# plt.xlabel("PIB")
# plt.ylabel("Expectativa de Vida")
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()

# paises = df['Country']
# print(paises.head())

# *** Converter tipo da coluna para category 

df['Country'] = df['Country'].astype('category')

# *** Cria nov
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
df['classes'] = df['Country'].cat.codes
print(df.info())
print(df.head())


# print(df.columns)
# print('------------------------------------------------------------')
# print()
# print(df.info())
# print('------------------------------------------------------------')
# print()

# # Estatísticas descritivas de uma coluna
# hp = df['rank_felicidade']
# print(hp.describe)
# print('------------------------------------------------------------')

# print()
# print(df['rank_felicidade'].describe())
# print('------------------------------------------------------------')
# print()
# print(df.isnull().sum())
# print('------------------------------------------------------------')
# print()
# print("Média da expectativa de vida:", df['expect_vida'].mean())
# print('------------------------------------------------------------')
# print()
# print("Mediana da expectativa de vida:", df['expect_vida'].median())
# print('------------------------------------------------------------')
# print()
# print("PIB máximo:", df['PIB'].max())

# # Gráfico 1 - Distribuição da Felicidade
# plt.figure(figsize=(10, 6))
# plt.hist(df['score_felicidade'], bins=20, color='skyblue', edgecolor='black')
# plt.title("Distribuição da Felicidade")
# plt.xlabel("Score de Felicidade")
# plt.ylabel("Frequência")
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.savefig("grafico_felicidade.png")  # Salva o gráfico como imagem
# plt.show()

# # Gráfico 2 - Expectativa de vida por região (Boxplot)
# plt.figure(figsize=(12, 6))
# df.boxplot(column='expect_vida', by='Region', rot=90)
# plt.title("Expectativa de Vida por Região")
# plt.suptitle("")  # Remove o título automático do pandas
# plt.xlabel("Região")
# plt.ylabel("Expectativa de Vida")
# plt.tight_layout()
# plt.show()

# # Gráfico 3 - Correlação entre PIB e Expectativa de Vida (Scatter plot)
# plt.figure(figsize=(10, 6))
# plt.scatter(df['PIB'], df['expect_vida'], alpha=0.7, color='seagreen')
# plt.title("Correlação entre PIB e Expectativa de Vida")
# plt.xlabel("PIB")
# plt.ylabel("Expectativa de Vida")
# plt.grid(True, linestyle='--', alpha=0.5)
# plt.tight_layout()
# plt.show()

# paises = df['Country']
# print(paises.head())

# *** Converter tipo da coluna para category 

# df['Country'] = df['Country'].astype('category')

# *** Cria nova coluna

# df['class'] = df['Country'].cat.codes
# print(df['class'].head())
