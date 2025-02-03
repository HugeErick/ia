import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline

def plot_data(X, y, title):
    plt.figure(figsize=(8, 6))
    plt.scatter(X["rank"], X["points"], c=y, cmap="coolwarm", alpha=0.6, edgecolor="k")
    plt.title(title)
    plt.xlabel("Rank")
    plt.ylabel("Points")
    plt.show()

def print_class_distribution(y, label):
    print(f"Class distribution ({label}):")
    print(y.value_counts())
    print(f"Total samples: {len(y)}")
    print()

def train_and_evaluate_model(X_train, y_train, X_test, y_test, label):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"Classification Report ({label}):")
    print(classification_report(y_test, y_pred, zero_division=1))
    print()

def linearRegresion():
    # Load and preprocess data
    file_path = "dataBalance/imbalanceFifaR.csv"
    df = pd.read_csv(file_path)
    df["association"] = df["association"].str.strip().str.lower()
    filtered_data = df[df["association"].isin(["uefa", "conmebol"])].copy()

    # Debug info
    if filtered_data.empty:
        print("No data found for 'uefa' and 'conmebol'. Check the input CSV.")
        exit()

    filtered_data["Target"] = filtered_data["association"].map({"uefa": 1, "conmebol": 0})
    X = filtered_data[["rank", "points"]]
    y = filtered_data["Target"]

    # Original imbalanced data
    print_class_distribution(y, "imbalanced")
    plot_data(X, y, "Original Imbalanced Data")

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # Train and evaluate on imbalanced data
    train_and_evaluate_model(X_train, y_train, X_test, y_test, "Imbalanced Model")

    # Oversampling with SMOTE
    smote = SMOTE(random_state=42)
    X_resampled_over, y_resampled_over = smote.fit_resample(X_train, y_train)
    print_class_distribution(y_resampled_over, "after SMOTE oversampling")
    plot_data(pd.DataFrame(X_resampled_over, columns=["rank", "points"]), y_resampled_over, "SMOTE-Oversampled Data")
    train_and_evaluate_model(X_resampled_over, y_resampled_over, X_test, y_test, "SMOTE-Oversampled Model")

    # Undersampling with RandomUnderSampler
    rus = RandomUnderSampler(random_state=42)
    X_resampled_under, y_resampled_under = rus.fit_resample(X_train, y_train)
    print_class_distribution(y_resampled_under, "after Random Undersampling")
    plot_data(pd.DataFrame(X_resampled_under, columns=["rank", "points"]), y_resampled_under, "Undersampled Data")
    train_and_evaluate_model(X_resampled_under, y_resampled_under, X_test, y_test, "Undersampled Model")

    # Combination of SMOTE and Undersampling
    over_under_pipeline = Pipeline([
        ('smote', SMOTE(random_state=42)),
        ('undersampler', RandomUnderSampler(random_state=42))
    ])
    X_resampled_combined, y_resampled_combined = over_under_pipeline.fit_resample(X_train, y_train)
    print_class_distribution(y_resampled_combined, "after SMOTE + Undersampling")
    plot_data(pd.DataFrame(X_resampled_combined, columns=["rank", "points"]), y_resampled_combined, "SMOTE + Undersampled Data")
    train_and_evaluate_model(X_resampled_combined, y_resampled_combined, X_test, y_test, "SMOTE + Undersampled Model")

    print("How did the model's performance change after balancing the data?")
    print("Ans: The model did in fact improve the hability to not make mistakes, if not obvious these greatly increases the chance of a correct prediction for the clasification prediction and like said before the presition")
    print("Which technique (oversampling or undersampling) was more effective, and why?")
    print("Ans: Oversampling conquers over undersampling due to the data balance tha oversampling normally achieves, this aint always like this but in a normal scenario we would want to balance the data as balanced as posible")
    print("Which metrics are most useful for evaluating models in problems withimbalanced classes?")
    print("Ans: In my humble opinion I would say precision, recall, and accuracy al of them calculated a strict precision based on what data can be wrong or truhty")

# if u're pasting and running this single file directly just uncomment the line below
#linearRegresion
