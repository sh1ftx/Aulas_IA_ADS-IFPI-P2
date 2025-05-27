from sklearn.datasets import make_classification

X,y = make_classification(n_samples=5000,n_features=8, n_informative=5, n_redundant=2, n_classes=2)

print(X.shape, y.shape)