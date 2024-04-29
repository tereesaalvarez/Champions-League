from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.schema import ChainingConfiguration

# Inicializa el modelo de lenguaje con la configuración adecuada
def setup_chatbot(api_key):
    config = ChainingConfiguration(
        name="football-qna",
        description="Use GPT-3.5 Turbo to answer questions about football."
    )
    llm = OpenAI(api_key=api_key, model="gpt-3.5-turbo")
    return LLMChain(llm=llm, config=config)

# Función para hacer preguntas al chatbot
def ask_question(chatbot, question):
    return chatbot.run(question)

def main():
    # Asumiendo que has obtenido una clave API válida de OpenAI
    API_KEY = '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'
    
    # Configurar el chatbot
    football_chatbot = setup_chatbot(API_KEY)
    
    # Bucle para permitir al usuario hacer preguntas
    print("Bienvenido al chatbot de fútbol! Puedes hacerme preguntas sobre fútbol.")
    try:
        while True:
            question = input("¿Cuál es tu pregunta? (escribe 'exit' para quitar) ")
            if question.lower() == 'exit':
                break
            response = ask_question(football_chatbot, question)
            print("Respuesta:", response)
    except KeyboardInterrupt:
        print("\nHasta la proxima!")

if __name__ == "__main__":
    main()
