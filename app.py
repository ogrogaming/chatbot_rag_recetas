import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

@st.cache_resource
def cargar_modelos():
    model_emb = SentenceTransformer("all-MiniLM-L6-v2")
    qa_pipeline = pipeline("text-generation", model="tiiuae/falcon-rw-1b", max_new_tokens=100)
    return model_emb, qa_pipeline

@st.cache_data
def cargar_textos(path):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    textos = content.strip().split("\n\n")
    return textos

def crear_indice(textos, model_emb):
    embeddings = model_emb.encode(textos, convert_to_numpy=True)
    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(embeddings)
    return embeddings, index

def recuperar_contexto(pregunta, model_emb, textos, index):
    pregunta_embedding = model_emb.encode([pregunta])
    _, indices = index.search(np.array(pregunta_embedding), 1)
    return textos[indices[0][0]]

# Interfaz Streamlit
st.title("🍽️ Chatbot de Recetas Básicas")

pregunta = st.text_input("Escribí tu pregunta sobre una receta...")

if pregunta:
    with st.spinner("Pensando..."):
        model_emb, qa_pipeline = cargar_modelos()
        textos = cargar_textos("recetas.txt")
        _, index = crear_indice(textos, model_emb)
        contexto = recuperar_contexto(pregunta, model_emb, textos, index)
        prompt = f"Contexto: {contexto}\nPregunta: {pregunta}\nRespuesta:"
        respuesta = qa_pipeline(prompt)[0]["generated_text"].split("Respuesta:")[-1].strip()
        st.success(respuesta)
