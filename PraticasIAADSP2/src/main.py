import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminho do CSV
file_path = './database/mundo_feliz.csv'

# Verifica se o arquivo existe
if not os.path.exists(file_path):
    print(f"Arquivo não encontrado: {file_path}")
    exit()

# Lê o CSV
df = pd.read_csv(file_path)

# Renomeia colunas
df.columns = ['Country', 'Region', 'rank_felicidade', 'score_felicidade',
              'stand_error', 'PIB', 'Family', 'expect_vida', 'Freedom',
              'currupcao', 'Generosity', 'Dystopia Residual']

# Estilo dos gráficos
sns.set(style="darkgrid")
plt.rcParams['figure.figsize'] = (10, 6)

# Gráfico 1 - Shape do DataFrame (tamanho de linhas e colunas)
plt.figure()
plt.bar(['Linhas', 'Colunas'], df.shape, color='slateblue')
plt.title("Shape do DataFrame (linhas e colunas)")
plt.ylabel("Quantidade")
plt.tight_layout()
plt.show()

# Gráfico 2 - Valores nulos por coluna
plt.figure()
df.isnull().sum().plot(kind='bar', color='darkred')
plt.title("Valores Nulos por Coluna")
plt.ylabel("Quantidade de Nulos")
plt.xlabel("Colunas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico 3 - Histograma do Rank de F elicidade
plt.figure()
plt.hist(df['rank_felicidade'], bins=20, color='orange', edgecolor='black')
plt.title("Distribuição do Rank de Felicidade")
plt.xlabel("Rank")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()

# Gráfico 4 - Estatísticas Descritivas (exemplo: expectativa de vida)
expect = df['expect_vida'].describe()
plt.figure()
plt.bar(expect.index, expect.values, color='green')
plt.title("Estatísticas da Expectativa de Vida")
plt.ylabel("Valor")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("Testando a versão do pandas")

plt.tight_layout()
plt.show()

# Gráfico 6 - Score de Felicidade (Histograma)
plt.figure()
plt.hist(df['score_felicidade'], bins=15, color='deepskyblue', edgecolor='black')
plt.title("Distribuição do Score de Felicidade")
plt.xlabel("Score")
plt.ylabel("Frequência")
plt.tight_layout()
plt.show()

# Gráfico 7 - Correlação entre PIB e Expectativa de Vida (Scatter)
plt.figure()
plt.scatter(df['PIB'], df['expect_vida'], alpha=0.7, color='teal')
plt.title("PIB vs Expectativa de Vida")
plt.xlabel("PIB")
plt.ylabel("Expectativa de Vida")
plt.grid(True)
plt.tight_layout()
plt.show()

# Gráfico 8 - Média, Mediana e Máximo da Expectativa de Vida
valores = {
    'Média': df['expect_vida'].mean(),
    'Mediana': df['expect_vida'].median(),
    'Máximo': df['expect_vida'].max()
}

plt.figure()
plt.bar(valores.keys(), valores.values(), color=['cyan', 'magenta', 'yellow'])
plt.title("Expectativa de Vida - Média, Mediana e Máximo")
plt.ylabel("Expectativa de Vida")
plt.tight_layout()
plt.show()
