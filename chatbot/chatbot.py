import os
import pandas as pd
from transformers import RagTokenizer, RagTokenForGeneration

# Resolver conflicto de la biblioteca transformers con OpenMP
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

# Cargar los datos del CSV
def load_data(csv_path):
    return pd.read_csv(csv_path)

# Normalizar texto para la búsqueda
def normalize_text(text):
    return text.replace(" ", "").lower()

# Buscar en los datos
def search_data(data, query):
    query = normalize_text(query)
    results = []
    for _, row in data.iterrows():
        # Normalizar los nombres de los equipos antes de la comparación
        home_team = normalize_text(row['HomeTeam'])
        away_team = normalize_text(row['AwayTeam'])
        match_query = f"{home_team} {away_team} {row['Result']}"
        if query in match_query:
            results.append(match_query)
    return " ".join(results)

# Inicialización del modelo de RAG
def setup_rag_model():
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq")
    return tokenizer, model

# Obtener respuesta del modelo
def get_response(question, data, tokenizer, model):
    search_results = search_data(data, question)
    if not search_results:
        print("No se encontraron datos para la pregunta:", question)
        return "No se encontró información relevante."
    
    inputs = tokenizer(search_results, return_tensors="pt", truncation=True)
    input_ids = inputs.input_ids

    if input_ids.nelement() == 0:
        print("Error: input_ids está vacío.")
        return "Lo siento, no puedo generar una respuesta basada en la entrada proporcionada."

    try:
        response_ids = model.generate(input_ids)
        response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
        return response
    except Exception as e:
        print("Error al generar la respuesta:", str(e))
        return "Error al procesar la respuesta."

def test_chatbot():
    data = load_data('chatbot/spain.csv')  # Asegúrate de que la ruta al archivo es correcta
    tokenizer, model = setup_rag_model()
    question = normalize_text("¿Cuál fue el resultado de AthleticClub contra Barcelona?")
    response = get_response(question, data, tokenizer, model)
    print("Pregunta:", question)
    print("Respuesta del chatbot:", response)

if __name__ == "__main__":
    test_chatbot()
