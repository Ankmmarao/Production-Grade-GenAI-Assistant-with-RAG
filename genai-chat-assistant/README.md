<img width="960" height="540" alt="2026-03-08" src="https://github.com/user-attachments/assets/695cd03a-0ab8-4a5f-b4d5-527550430a3f" />
# Production-Grade GenAI Assistant with RAG

## Overview

This project implements a **Production-Grade Generative AI Chat Assistant** using the **Retrieval-Augmented Generation (RAG)** architecture. The assistant answers user queries by retrieving relevant information from a document knowledge base and using a **Large Language Model (Gemini API)** to generate accurate responses.

The system ensures responses are **context-aware and grounded in provided documents** rather than relying solely on the model’s internal knowledge.

---

## Features

* AI-powered chat assistant
* Retrieval-Augmented Generation (RAG) pipeline
* Document-based question answering
* Context-aware responses
* Simple and interactive web chat interface
* Gemini API integration
* Lightweight vector similarity retrieval

---

## Technologies Used

**Backend**

* Python
* Flask

**Frontend**

* HTML
* CSS
* JavaScript

**AI & ML**

* Gemini API
* Embeddings
* Cosine Similarity

**Libraries**

* Flask
* NumPy
* Scikit-learn
* Google Generative AI SDK

---

## Project Structure

```
genai-chat-assistant
│
├── app.py
├── docs.json
├── requirements.txt
│
├── templates
│   └── index.html
│
└── static
    ├── script.js
    └── styles.css
```

---

## How It Works

1. Documents are stored in **docs.json** as the knowledge base.
2. Each document is converted into **vector embeddings**.
3. When a user asks a question:

   * The query is converted into an embedding.
   * The system retrieves the **most similar document chunks**.
4. Retrieved context is sent to the **Gemini Large Language Model**.
5. The model generates a **final contextual answer**.

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/Ankmmarao/Production-Grade-GenAI-Assistant-with-RAG.git
cd Production-Grade-GenAI-Assistant-with-RAG
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Add Gemini API Key

Open **app.py** and add your API key:

```
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

You can obtain a Gemini API key from:

https://aistudio.google.com/app/apikey

---

## Run the Application

```
python app.py
```

Open your browser and go to:

```
http://localhost:5000
```

---

## Example Queries

* How can I reset my password?
* How do I create an account?
* How can I delete my account?

---

## Future Improvements

* PDF document upload support
* Vector database integration (FAISS / Pinecone)
* Conversation memory
* ChatGPT-style UI
* Deployment on cloud platforms (Render / Railway)

---

## Author

**Ankmmarao**

---

## License

This project is created for educational and demonstration purposes.
