from sklearn.datasets import make_classification
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE

# Generate imbalanced data
X, y = make_classification(n_samples=1000, n_features=2, n_classes=2,
                           n_informative=2, n_redundant=0, n_repeated=0,
                           weights=[0.9, 0.1], random_state=42)
data = pd.DataFrame(X, columns=["Feature1", "Feature2"])
data["Target"] = y

# Visualize the imbalanced data
print("Class distribution (imbalanced):")
print(data["Target"].value_counts())
plt.scatter(data["Feature1"], data["Feature2"], c=data["Target"], cmap="coolwarm", alpha=0.6)
plt.title("Original Imbalanced Data")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()

# Split data
X_train, X_test, y_train, y_test = train_test_split(data[["Feature1", "Feature2"]],
                                                    data["Target"], test_size=0.3, random_state=42)

# Train model on imbalanced data
model = LogisticRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Classification Report (Imbalanced Model):")
print(classification_report(y_test, y_pred))

# Apply SMOTE to balance the data
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# Visualize balanced data
plt.scatter(X_resampled.iloc[:, 0], X_resampled.iloc[:, 1], c=y_resampled, cmap="coolwarm", alpha=0.6)
plt.title("SMOTE-Balanced Data")
plt.xlabel("Feature1")
plt.ylabel("Feature2")
plt.show()

# Train model on balanced data
model.fit(X_resampled, y_resampled)
y_pred_resampled = model.predict(X_test)
print("Classification Report (Balanced Model):")
print(classification_report(y_test, y_pred_resampled))

