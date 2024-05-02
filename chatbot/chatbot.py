import os
import json
from transformers import RagTokenizer, RagTokenForGeneration

# Resolver conflicto de la biblioteca transformers con OpenMP
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Cargar los datos del JSON
def load_data(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# Buscar en los datos
def search_data(data, query):
    results = []
    for team, games in data['team_games'].items():
        for game in games:
            if query.lower() in " ".join(game).lower():
                results.append(f"{game[0]} {game[1]} {game[2]}")
    return " ".join(results)

# Inicialización del modelo de RAG
def setup_rag_model():
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")
    return tokenizer, model

def get_response(question, data, tokenizer, model):
    # Buscar coincidencias en los datos
    search_results = search_data(data, question)
    if not search_results:
        search_results = "No se encontró información relevante."
    # Preparar la entrada para el modelo usando tokenizer
    input_ids = tokenizer(search_results, return_tensors="pt").input_ids
    response_ids = model.generate(input_ids)
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response


def test_chatbot():
    data = load_data('chatbot/spain.json')
    tokenizer, model = setup_rag_model()
    question = "¿Cuál fue el resultado de Athletic Club contra Barcelona?"
    response = get_response(question, data, tokenizer, model)
    print("Pregunta:", question)
    print("Respuesta del chatbot:", response)

if __name__ == "__main__":
    test_chatbot()
