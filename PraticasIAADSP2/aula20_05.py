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
