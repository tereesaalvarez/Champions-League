import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Carga y preparación de datos
def load_and_prepare_data(filepath):
    data = pd.read_csv(filepath)
    data = pd.get_dummies(data)
    X = data.drop('Porcentaje Victoria', axis=1)
    y = data['Porcentaje Victoria']
    return X, y

# Normalización de los datos
def normalize_data(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

# Construcción del modelo de red neuronal
def build_model(input_shape):
    model = Sequential([
        Dense(128, activation='relu', input_shape=(input_shape,)),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)  # Sin función de activación para regresión
    ])
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_squared_error'])
    return model

# Entrenamiento del modelo
def train_model(model, X_train, y_train):
    model.fit(X_train, y_train, epochs=100, batch_size=10, verbose=1)
    return model

# Evaluación del modelo
def evaluate_model(model, X_test, y_test):
    mse = model.evaluate(X_test, y_test, verbose=0)
    return mse

if __name__ == "__main__":
    filepath = 'datos_semis/combined_data.csv'
    X, y = load_and_prepare_data(filepath)
    X_scaled = normalize_data(X)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.25, random_state=42)

    model = build_model(X_train.shape[1])
    model = train_model(model, X_train, y_train)
    mse = evaluate_model(model, X_test, y_test)

    print(f"Model Mean Squared Error: {mse[0]}")  # mse es una lista donde el primer elemento es el MSE
