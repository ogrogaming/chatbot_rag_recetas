# Chatbot RAG de Recetas Básicas

Este proyecto implementa un chatbot simple de cocina que responde preguntas sobre recetas usando una arquitectura RAG (Retrieval-Augmented Generation), completamente funcional en Streamlit Cloud y también dockerizable para correr localmente.

---

## 🌐 Demo Online

Podés probar el chatbot online en Streamlit Cloud (enlace a tu app):

```
https://chatbot-recetas.streamlit.app/
```

---

## 📄 Tema elegido

**Recetas de cocina básicas**

### Justificación:

* Tema simple y comprensible por cualquier persona.
* Permite simular RAG con textos cortos.
* No requiere datasets pesados.

---

## 🪧 Tecnologías utilizadas

* **Streamlit** (frontend y ejecución del modelo)
* **SentenceTransformers** para embeddings (modelo: `all-MiniLM-L6-v2`)
* **FAISS** como motor vectorial
* **Transformers** (modelo QA: `mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es`)
* **Docker** para empaquetado

---

## 📂 Estructura del proyecto

```
chatbot_rag_recetas/
├── app.py              # App principal en Streamlit
├── recetas.txt         # Base de conocimiento
├── requirements.txt    # Dependencias
├── Dockerfile          # Para ejecutar localmente en contenedor
```

---

## 🔄 Cómo ejecutar en local (con Docker)

1. Instalá Docker: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)
2. Abrí una terminal y posicionate en la carpeta del proyecto

### 3. Construí la imagen Docker:

```bash
docker build -t chatbot-recetas .
```

### 4. Ejecutá la app:

```bash
docker run -p 8501:8501 chatbot-recetas
```

### 5. Abrí en el navegador:

```
http://localhost:8501
```

---

## 📁 Cómo ejecutar en Streamlit Cloud

1. Subí el repositorio a GitHub
2. Ingresá a [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Seleccioná tu repo y archivo `app.py`
4. Deploy

---

## 📚 Base de conocimiento

El archivo `recetas.txt` contiene 20 recetas básicas separadas por doble salto de línea. Se cargan, se vectorizan con SentenceTransformer y se indexan con FAISS para recuperación por similitud semántica.

---

## 📋 Prompt usado

```
Pregunta: ¿Cómo preparo tortilla de papas?
Contexto: Tortilla de papas: Ingredientes: papas, huevos, cebolla, sal. Preparación: Pelar y cortar las papas. Freírlas. Batir los huevos con sal, agregar las papas y cebolla picada. Cocinar en sartén por ambos lados.
Respuesta: [...generado por el modelo...]
```

---

## 📄 Informe PDF + Video

* El informe está en `informe_final.pdf` en este mismo repo.
* El video está disponible en Drive: \[link a video] (a completar por el grupo)

---

## 📚 Créditos y referencias

* [https://huggingface.co/mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es](https://huggingface.co/mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es)
* [https://www.sbert.net/](https://www.sbert.net/)
* [https://www.streamlit.io/](https://www.streamlit.io/)

---

## 🔐 Requisitos (requirements.txt)

```
streamlit
transformers
sentence-transformers
faiss-cpu
torch
```

---

## 🚀 Próximos pasos

* Agregar más recetas y categorías
* Incorporar botones con ejemplos sugeridos
* Optimizar recuperación con más embeddings o chunks más pequeños
