from flask import Flask, request, jsonify
import chatbot  

app = Flask(__name__)


# Carga los datos y el modelo una sola vez al iniciar el servidor
data = chatbot.load_data('chatbot/spain.csv')  # Ajusta la ruta si es necesario
tokenizer, model = chatbot.setup_rag_model()

@app.route('/')
def home():
    return "Bienvenido al Chatbot de Fútbol. Usa /chat para interactuar."


@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        data = request.json
        question = data.get('question')
    else:
        question = request.args.get('question', '')  # Para pruebas con GET, añade ?question=tu_pregunta en la URL

    if not question:
        return jsonify({"error": "No se proporcionó una pregunta válida"}), 400

    response = chatbot.get_response(question, data, tokenizer, model)
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
