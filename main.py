
import sys
from chatbot.chatbot import *
from chatbot.lanzador import *
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
        import chatbot
        chatbot.test_chatbot()
    elif choice == '2':
        import lanzador
        print("Lanzador del Chatbot no es ejecutable directamente desde aquí. Por favor, ejecute el archivo lanzador.py manualmente.")
    elif choice == '3':
        import arboldecision
        arboldecision.main()
    elif choice == '4':
        import redneuronal2
        redneuronal2.main()
    elif choice == '5':
        import regresión
        regresión.main()
    else:
        print("Opción no válida. Por favor, seleccione una opción válida del 1 al 5.")

if __name__ == "__main__":
    main()
