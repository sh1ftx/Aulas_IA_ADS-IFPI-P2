import sklearn
import pandas as pd

from sklearn.preprocessing import LabelEncoder, OrdinalEncoder
enc = LabelEncoder() #Instanciamos o encoder na variável enc, poderia ser OrdinalEncoder
cidades = ["paris", "paris", "tokyo", "amsterdam"] #Imagine isto como uma coluna contendo vários itens, inclusive repetidos
enc.fit(cidades) #Aqui ele esta se ajustando aos valores
print(enc.classes_) #O objeto cria um atributo .classes_ que cotém as novas classes que serão aplicadas aos dados
com .transorm( )
nova_coluna = enc.transform(cidades) #Note que aplicamos o transform( ) nos mesmos dados, poderiamos fazer em um passo
com .fit_transform( )
print(nova_coluna) #mostramos o conteúdo modificado
print(enc.inverse_transform([2, 1])) #Temos ainda uma função que mostra o label orginal passando o numérico

# Criando o Dataframe
tipos = ['Arco', 'Canhão', 'Torre', 'Elevada', 'Arco amarrado', 'Suspensa' , 'Cordas']
df = pd.DataFrame(tipos, columns=['tipos_de_pontes']) #Cria um dataframe com uma coluna chamada tipos_de_pontes
print(df)
enc = LabelEncoder() # Instancia um LabelEncoder que irá centralizar as transformações
df['tipos_de_pontes'] = enc.fit_transform(df['tipos_de_pontes']) #transforma diretamente a coluna
print(df)
