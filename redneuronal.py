import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# Carga y preparación de datos
def load_and_prepare_data(filepath):
    data = pd.read_csv(filepath)
    data = pd.get_dummies(data)
    X = data.drop('Porcentaje Victoria', axis=1)  # Asegúrate de que 'Porcentaje Victoria' es tu variable objetivo
    y = data['Porcentaje Victoria']
    scaler = StandardScaler()
    X = scaler.fit_transform(X)  # Estandarización de características
    return X, y

# Construcción del modelo de red neuronal
def build_neural_network(input_dim):
    model = Sequential([
        Dense(128, activation='relu', input_dim=input_dim),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)  # Capa de salida para regresión sin función de activación
    ])
    model.compile(optimizer=Adam(), loss='mean_squared_error', metrics=['mae'])
    return model

# Entrenamiento del modelo
def train_model(model, X_train, y_train, epochs=50, batch_size=10):
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, verbose=1)
    return model

# Evaluación del modelo
def evaluate_model(model, X_test, y_test):
    loss, mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss}, Test MAE: {mae}")

if __name__ == "__main__":
    filepath = 'datos_semis/combined_data.csv'
    X, y = load_and_prepare_data(filepath)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = build_neural_network(X_train.shape[1])
    model = train_model(model, X_train, y_train, epochs=100, batch_size=32)
    evaluate_model(model, X_test, y_test)
