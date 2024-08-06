import joblib
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def load_data():
    data_path = os.path.join(os.path.dirname(__file__), '..', '..', 'data', 'processed', 'prepared_data.csv')
    return pd.read_csv(data_path)

def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    return model

def save_model(model):
    model_path = os.path.join(os.path.dirname(__file__), '..', '..', 'models', 'model.pkl')
    joblib.dump(model, model_path)

if __name__ == '__main__':
    data = load_data()
    X = data.drop('target', axis=1)
    y = data['target']
    model = train_model(X, y)
    save_model(model)
    print("Model trained and saved successfully.")