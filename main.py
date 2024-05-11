import sys
from chatbot.chatbot import *
from modelos.arboldecision import *
from modelos.redneuronal2 import *
from modelos.regresión import *

def main():
    print("Seleccione el programa a ejecutar:")
    print("1: Chatbot")
    print("2: Lanzador del Chatbot")
    print("3: Modelo de Árbol de Decisión")
    print("4: Red Neuronal")
    print("5: Regresión")

    choice = input("Introduzca el número del programa: ")

    if choice == '1':
        test_chatbot()
    elif choice == '2':
        print("Lanzador del Chatbot no es ejecutable directamente desde aquí. Por favor, ejecute el archivo lanzador.py manualmente.")
    elif choice == '3':
        filepath = 'datos_semis/combined_data.csv'
        X, y = load_and_prepare_data(filepath)
        model, X_test, y_test = train_decision_tree(X, y)
        mse, predictions = evaluate_model(model, X_test, y_test)
        
        print(f"Model Mean Squared Error: {mse}")
        display_final_standings(predictions)

    elif choice == '4':
        filepath = 'datos_semis/combined_data.csv'
        team_names = ['Bayern München', 'Real Madrid', 'Paris Saint-Germain', 'Borussia Dortmund']
        X, y, X_scaler, y_scaler, feature_names = load_and_prepare_data(filepath)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = build_neural_network(X_train.shape[1])
        model, history = train_model(model, X_train, y_train)
        evaluate_model(model, X_test, y_test)
        plot_training_history(history)
        predict_and_display_results(model, X, team_names, y_scaler)
    elif choice == '5':
        filepath = 'datos_semis/combined_data.csv'
        data = load_and_prepare_data(filepath)
        results, final_teams = simulate_results(data)
        accuracy, conf_matrices = train_and_evaluate(data, results)
        
        print("Accuracy of models:", accuracy)
        print("Confusion matrices of models:", conf_matrices)
        display_final_standings(results, final_teams)

    else:
        print("Opción no válida. Por favor, seleccione una opción válida del 1 al 5.")

if __name__ == "__main__":
    main()

