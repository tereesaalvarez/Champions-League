import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Carga y preparación de datos
def load_and_prepare_data(filepath):
    data = pd.read_csv(filepath)
    # Convertir las variables categóricas a numéricas usando One-Hot Encoding
    data = pd.get_dummies(data)
    X = data.drop('Porcentaje Victoria', axis=1)  # Asegúrate de que 'Porcentaje Victoria' es el nombre correcto
    y = data['Porcentaje Victoria']
    return X, y

# Entrenamiento del modelo de regresión de árboles de decisión
def train_decision_tree(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    model = DecisionTreeRegressor(random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Evaluación del modelo
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    mse = mean_squared_error(y_test, predictions)
    return mse, predictions

# Display the standings based on the model's predictions
def display_final_standings(predictions):
    # Esta función deberá ajustarse si la salida es continua o de otro tipo no directamente ordinal
    standings = ["Bayern München", "Real Madrid", "Paris Saint-Germain", "Borussia Dortmund"]
    standings_sorted = sorted(zip(standings, predictions), key=lambda x: x[1], reverse=True)
    for position, (team, score) in enumerate(standings_sorted, 1):
        print(f"{position}st Place: {team} - Score: {score:.2f}")

if __name__ == "__main__":
    filepath = 'datos_semis/combined_data.csv'
    X, y = load_and_prepare_data(filepath)
    model, X_test, y_test = train_decision_tree(X, y)
    mse, predictions = evaluate_model(model, X_test, y_test)
    
    print(f"Model Mean Squared Error: {mse}")
    display_final_standings(predictions)
