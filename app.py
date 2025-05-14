import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from transformers import pipeline

@st.cache_resource
def cargar_modelos():
    model_emb = SentenceTransformer("all-MiniLM-L6-v2")
    qa_pipeline = pipeline("question-answering", model="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es")
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

def recuperar_contextos(pregunta, model_emb, textos, index, k=3):
    pregunta_embedding = model_emb.encode([pregunta])
    _, indices = index.search(np.array(pregunta_embedding), k)
    return [textos[i] for i in indices[0]]

# Interfaz
st.title("🍳 Chatbot de Recetas en Español")

pregunta = st.text_input("Escribí tu pregunta sobre una receta:")
if pregunta:
    with st.spinner("Buscando respuesta..."):
        model_emb, qa_pipeline = cargar_modelos()
        textos = cargar_textos("recetas.txt")
        _, index = crear_indice(textos, model_emb)
        contextos = recuperar_contextos(pregunta, model_emb, textos, index, k=3)
        contexto_completo = "\n".join(contextos)
        respuesta = qa_pipeline(question=pregunta, context=contexto_completo)["answer"]
        st.success(respuesta)


