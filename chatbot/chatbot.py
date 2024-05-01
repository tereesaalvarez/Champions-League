# chatbot.py
from transformers import RagTokenizer, RagTokenForGeneration, RagRetriever

def setup_rag_model():
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
    retriever = RagRetriever.from_pretrained("facebook/rag-token-nq", index_name="exact", use_dummy_dataset=True)
    model = RagTokenForGeneration.from_pretrained("facebook/rag-token-nq", retriever=retriever)
    return tokenizer, model

def get_response(question, tokenizer, model):
    input_ids = tokenizer(question, return_tensors="pt").input_ids
    response_ids = model.generate(input_ids)
    response = tokenizer.decode(response_ids[0], skip_special_tokens=True)
    return response

def test_chatbot():
    tokenizer, model = setup_rag_model()
    question = "¿Quién ganó la Copa del Mundo 2018?"
    response = get_response(question, tokenizer, model)
    print("Pregunta:", question)
    print("Respuesta del chatbot:", response)

# Llamada a la función de prueba
if __name__ == "__main__":
    test_chatbot()


