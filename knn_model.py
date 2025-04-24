from sklearn.datasets import load_wine
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# veri setini yüklüyoruz
data = load_wine()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = pd.DataFrame(data.target, columns=['target'])

print("Özellikler:\n", X.head())
print("\nHedef Sınıflar:\n", y.value_counts())

# sınıf isimleri
print("\nSınıf İsimleri:", data.target_names)

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3, random_state=42)
print("Eğitim boyutu:",X_train.shape)
print("Test seti boyutu:",X_test.shape)

knn= KNeighborsClassifier(n_neighbors=5) # k=5 seçildi
knn.fit(X_train, y_train.values.ravel())

y_pred = knn.predict(X_test)
# accuracy
print("Model doğruluğu:", accuracy_score(y_test,y_pred))
print("\nSınıflandırma raporu:\n", classification_report(y_test,y_pred))




