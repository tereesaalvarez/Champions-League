import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

# Carga y preparación de datos
def load_and_prepare_data(filepath):
    combined_data = pd.read_csv(filepath)
    combined_data_dummies = pd.get_dummies(combined_data, columns=['Equipos'])
    scaler = StandardScaler()
    numeric_columns = combined_data_dummies.select_dtypes(include=['float64', 'int64']).columns
    combined_data_dummies[numeric_columns] = scaler.fit_transform(combined_data_dummies[numeric_columns])
    return combined_data_dummies

# Simulación de resultados basados en el promedio de rating
def simulate_results(data):
    results = {}
    # Madrid vs Bayern
    madrid_rating = data.loc[data['Equipos_Real Madrid'] == 1, 'Promedio_Rating'].values[0]
    bayern_rating = data.loc[data['Equipos_Bayern München'] == 1, 'Promedio_Rating'].values[0]
    results['madrid_vs_bayern'] = 1 if madrid_rating > bayern_rating else 0

    # PSG vs Dortmund
    psg_rating = data.loc[data['Equipos_Paris Saint-Germain'] == 1, 'Promedio_Rating'].values[0]
    dortmund_rating = data.loc[data['Equipos_Borussia Dortmund'] == 1, 'Promedio_Rating'].values[0]
    results['psg_vs_dortmund'] = 1 if psg_rating > dortmund_rating else 0

    # Determinar los equipos en la final y simular el resultado
    final_teams = {
        'final_team_1': 'Real Madrid' if results['madrid_vs_bayern'] == 1 else 'Bayern München',
        'final_team_2': 'Paris Saint-Germain' if results['psg_vs_dortmund'] == 1 else 'Borussia Dortmund'
    }
    final_team_1_rating = data.loc[data[f'Equipos_{final_teams["final_team_1"]}'] == 1, 'Promedio_Rating'].values[0]
    final_team_2_rating = data.loc[data[f'Equipos_{final_teams["final_team_2"]}'] == 1, 'Promedio_Rating'].values[0]
    results['final'] = 1 if final_team_1_rating > final_team_2_rating else 0
    
    return results, final_teams

# Entrenamiento y evaluación del modelo
def train_and_evaluate(data, results):
    X = data.drop(columns=[col for col in data.columns if 'Equipos_' in col])
    model_accuracy = {}
    conf_matrices = {}

    for match, result in results.items():
        y = [result, result, 1-result, 1-result]  # Duplicamos entradas para ajustar
        model = LogisticRegression()
        model.fit(X, y)
        predictions = model.predict(X)
        model_accuracy[match] = accuracy_score(y, predictions)
        conf_matrices[match] = confusion_matrix(y, predictions)

    return model_accuracy, conf_matrices

def display_final_standings(results, final_teams):
    first = final_teams['final_team_1'] if results['final'] == 1 else final_teams['final_team_2']
    second = final_teams['final_team_2'] if results['final'] == 1 else final_teams['final_team_1']
    third = 'Real Madrid' if results['madrid_vs_bayern'] == 0 else 'Bayern München'
    fourth = 'Paris Saint-Germain' if results['psg_vs_dortmund'] == 0 else 'Borussia Dortmund'
    print(f"1st Place: {first}")
    print(f"2nd Place: {second}")
    print(f"3rd Place: {third}")
    print(f"4th Place: {fourth}")

if __name__ == "__main__":
    filepath = 'datos_semis/combined_data.csv'
    data = load_and_prepare_data(filepath)
    results, final_teams = simulate_results(data)
    accuracy, conf_matrices = train_and_evaluate(data, results)
    
    print("Accuracy of models:", accuracy)
    print("Confusion matrices of models:", conf_matrices)
    display_final_standings(results, final_teams)
