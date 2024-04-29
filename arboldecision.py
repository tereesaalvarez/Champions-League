import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Carga y preparación de datos
def load_and_prepare_data(filepath):
    data = pd.read_csv(filepath)
    # Supongamos que todas las columnas, excepto 'Porcentaje Victoria', son características
    X = data.drop('Porcentaje Victoria', axis=1)
    y = data['Porcentaje Victoria']
    return X, y

# Entrenamiento del modelo de árboles de decisión
def train_decision_tree(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    return model, X_test, y_test

# Evaluación del modelo
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    return accuracy, predictions

# Display the standings based on the model's predictions
def display_final_standings(predictions):
    # Asignación de posiciones basada en predicciones
    # Esto es solo un ejemplo simplificado, necesitarás ajustar esto basado en tus necesidades específicas
    standings = ["Bayern München", "Real Madrid", "Paris Saint-Germain", "Borussia Dortmund"]
    standings_sorted = sorted(zip(standings, predictions), key=lambda x: x[1], reverse=True)
    for position, (team, score) in enumerate(standings_sorted, 1):
        print(f"{position}st Place: {team} - Score: {score}")

if __name__ == "__main__":
    filepath = 'datos_semis/combined_data.csv'
    X, y = load_and_prepare_data(filepath)
    model, X_test, y_test = train_decision_tree(X, y)
    accuracy, predictions = evaluate_model(model, X_test, y_test)
    
    print(f"Model Accuracy: {accuracy}")
    display_final_standings(predictions)
