from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt
# Generar datos desbalanceados
# The sum of n_informative + n_redundant + n_repeated should be less than or equal to
X, y = make_classification(n_samples=1000, n_features=2, n_classes=2,
n_informative=2, n_redundant=0, n_repeated=0, # Adjusted parameters
weights=[0.9, 0.1], random_state=42)
data = pd.DataFrame(X, columns=["Feature1", "Feature2"])
data["Target"] = y
# Visualización inicial
print("Distribución de las clases:")
print(data["Target"].value_counts())
# Graficar la distribución de datos
plt.scatter(data["Feature1"], data["Feature2"], c=data["Target"], cmap="coolwarm",
alpha=0.6)
plt.title("Distribución del conjunto de datos")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()
