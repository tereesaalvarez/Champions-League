import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.optimizers import Adam


# Este es el correcto


# Carga y preparación de datos
def load_and_prepare_data(filepath):
    data = pd.read_csv(filepath)
    data = pd.get_dummies(data)
    X = data.drop('Porcentaje Victoria', axis=1)
    y = data['Porcentaje Victoria'].values.reshape(-1, 1)  # Reshape para scaler
    X_scaler = StandardScaler()
    y_scaler = StandardScaler()
    X_scaled = X_scaler.fit_transform(X)
    y_scaled = y_scaler.fit_transform(y)
    return X_scaled, y_scaled, X_scaler, y_scaler, data.columns.drop('Porcentaje Victoria')

# Construcción del modelo de red neuronal
def build_neural_network(input_dim):
    model = Sequential([
        Dense(128, activation='relu', input_dim=input_dim),
        Dense(64, activation='relu'),
        Dense(32, activation='relu'),
        Dense(1)  # Capa de salida para regresión
    ])
    model.compile(optimizer=Adam(), loss='mean_squared_error', metrics=['mae'])
    return model

# Entrenamiento del modelo con visualización y callbacks
def train_model(model, X_train, y_train, epochs=100, batch_size=32):
    early_stopping = EarlyStopping(monitor='val_loss', patience=10)
    checkpoint = ModelCheckpoint('best_model.keras', save_best_only=True, monitor='val_loss', mode='min')
    history = model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size,
                        validation_split=0.2, verbose=1, callbacks=[early_stopping, checkpoint])
    return model, history

# Evaluación del modelo
def evaluate_model(model, X_test, y_test):
    #model.load_weights('best_model.keras')
    loss, mae = model.evaluate(X_test, y_test, verbose=0)
    print(f"Test Loss: {loss}, Test MAE: {mae}")

# Visualización del entrenamiento
def plot_training_history(history):
    plt.plot(history.history['loss'], label='Train Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.title('Model Loss Progression')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend()
    plt.show()

# Predicción de los porcentajes de victoria y determinación del ganador
def predict_and_display_results(model, X, team_names, y_scaler):
    predictions = model.predict(X)
    rescaled_predictions = y_scaler.inverse_transform(predictions)  # Correctly rescaled
    for team, prediction in zip(team_names, rescaled_predictions):
        print(f"{team}: Predicted Victory Percentage: {prediction[0]:.2f}%")
    winner_index = np.argmax(rescaled_predictions)
    print(f"The predicted winner is: {team_names[winner_index]} with a predicted victory percentage of {rescaled_predictions[winner_index][0]:.2f}%")

if __name__ == "__main__":
    filepath = 'datos_semis/combined_data.csv'
    team_names = ['Bayern München', 'Real Madrid', 'Paris Saint-Germain', 'Borussia Dortmund']
    X, y, X_scaler, y_scaler, feature_names = load_and_prepare_data(filepath)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = build_neural_network(X_train.shape[1])
    model, history = train_model(model, X_train, y_train)
    evaluate_model(model, X_test, y_test)
    plot_training_history(history)
    predict_and_display_results(model, X, team_names, y_scaler)
