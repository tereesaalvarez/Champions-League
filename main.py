import sys
from chatbot.chatbot import test_chatbot
from modelos.arboldecision import load_and_prepare_data as load_ad, train_decision_tree, evaluate_model as eval_ad, display_final_standings as display_ad
from modelos.redneuronal2 import load_and_prepare_data as load_rn, build_neural_network, train_model, evaluate_model as eval_rn, plot_training_history, predict_and_display_results, train_test_split
from modelos.regresión import load_and_prepare_data as load_rg, simulate_results, train_and_evaluate, display_final_standings as display_rg

def main():
    print("Seleccione el programa a ejecutar:")
    print("1: Chatbot")
    print("2: Lanzador del Chatbot")
    print("3: Modelo de Árbol de Decisión")
    print("4: Red Neuronal")
    print("5: Regresión")

    choice = input("Introduzca el número del programa: ")

    filepath = 'datos_semis/combined_data.csv'  # Asumiendo que todos usan el mismo archivo

    if choice == '1':
        test_chatbot()
    elif choice == '2':
        print("Lanzador del Chatbot no es ejecutable directamente desde aquí. Ejecute el archivo lanzador.py manualmente.")
    elif choice == '3':
        X, y = load_ad(filepath)
        model, X_test, y_test = train_decision_tree(X, y)
        mse, predictions = eval_ad(model, X_test, y_test)
        print(f"Model Mean Squared Error: {mse}")
        display_ad(predictions)
    elif choice == '4':
        team_names = ['Bayern München', 'Real Madrid', 'Paris Saint-Germain', 'Borussia Dortmund']
        X, y, X_scaler, y_scaler, feature_names = load_rn(filepath)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = build_neural_network(X_train.shape[1])
        model, history = train_model(model, X_train, y_train)
        eval_rn(model, X_test, y_test)
        plot_training_history(history)
        predict_and_display_results(model, X, team_names, y_scaler)
    elif choice == '5':
        data = load_rg(filepath)
        results, final_teams = simulate_results(data)
        accuracy, conf_matrices = train_and_evaluate(data, results)
        
        print("Accuracy of models:", accuracy)
        print("Confusion matrices of models:", conf_matrices)
        display_rg(results, final_teams)
    else:
        print("Opción no válida. Por favor, seleccione una opción válida del 1 al 5.")

if __name__ == "__main__":
    main()
