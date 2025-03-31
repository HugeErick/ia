from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import classification_report, confusion_matrix
import pandas as pd
import numpy as np

# Step 1: Generate synthetic transaction data
def generate_synthetic_data(num_samples=1000):
    # Define possible values for categorical features
    locations = ['USA', 'Canada', 'UK', 'Australia', 'Germany']
    user_device_types = ['Mobile', 'Desktop', 'Tablet']
    
    # Generate random data
    np.random.seed(42)  # For reproducibility
    transaction_amount = np.random.uniform(10, 5000, num_samples)  # Random transaction amounts
    transaction_frequency = np.random.randint(1, 30, num_samples)  # Random transaction frequency
    location = np.random.choice(locations, num_samples)           # Random locations
    user_device_type = np.random.choice(user_device_types, num_samples)  # Random device types
    
    # Simulate fraudulent transactions (10% fraud rate)
    is_fraud = np.random.choice([0, 1], num_samples, p=[0.9, 0.1])  # 10% fraud
    
    # Create a DataFrame
    data_frame = pd.DataFrame({
        'transactionAmount': transaction_amount,
        'transactionFrequency': transaction_frequency,
        'location': location,
        'userDeviceType': user_device_type,
        'isFraud': is_fraud
    })
    
    return data_frame

# Step 2: Preprocess the dataset
def preprocess_data(data_frame):
    # Encode categorical variables
    data_frame = pd.get_dummies(data_frame, columns=['location', 'userDeviceType'], drop_first=True)
    
    # Normalize numerical features
    numerical_features = ['transactionAmount', 'transactionFrequency']
    for feature in numerical_features:
        data_frame[feature] = (data_frame[feature] - data_frame[feature].mean()) / data_frame[feature].std()
    
    return data_frame

# Step 3: Split the data into training and testing sets
def split_data(data_frame):
    X = data_frame.drop('isFraud', axis=1)  # Features
    y = data_frame['isFraud']              # Target variable
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

# Step 4: Train the Decision Tree model
def train_decision_tree(X_train, y_train):
    decision_tree_model = DecisionTreeClassifier(max_depth=5, random_state=42)
    decision_tree_model.fit(X_train, y_train)
    return decision_tree_model

# Step 5: Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    
    # Print classification report
    print("Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Print confusion matrix
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))

# Main function
if __name__ == "__main__":
    # Generate synthetic data
    synthetic_data = generate_synthetic_data(num_samples=1000)
    
    # Preprocess the data
    preprocessed_data = preprocess_data(synthetic_data)
    
    # Split the data
    X_train, X_test, y_train, y_test = split_data(preprocessed_data)
    
    # Train the model
    decision_tree_model = train_decision_tree(X_train, y_train)
    
    # Evaluate the model
    evaluate_model(decision_tree_model, X_test, y_test)
