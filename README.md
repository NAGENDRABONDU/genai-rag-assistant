# GenAI Assistant with RAG

## Overview

This project is a production-style GenAI Chat Assistant built using:

- FastAPI
- Gemini API
- Sentence Transformers
- FAISS Vector Store
- HTML/CSS/JavaScript Frontend

The assistant uses Retrieval-Augmented Generation (RAG) to answer user questions using information stored in a document knowledge base.

---

# Features

- Document ingestion from JSON
- Text chunking
- Embedding generation
- Vector similarity search using FAISS
- Context-aware responses using Gemini
- Conversation memory
- Session management
- FastAPI REST API
- Web Chat Interface

---

# Architecture

```text
User
 │
 ▼
Frontend (HTML/CSS/JS)
 │
 ▼
FastAPI Backend
 │
 ▼
Question Embedding
 │
 ▼
FAISS Similarity Search
 │
 ▼
Top-K Relevant Chunks
 │
 ▼
Prompt Builder
 │
 ▼
Gemini LLM
 │
 ▼
Response
```

---

# RAG Workflow

## Indexing Phase

1. Load documents from docs.json
2. Split documents into chunks
3. Generate embeddings for each chunk
4. Store vectors in FAISS
5. Store metadata for retrieval

## Query Phase

1. User sends question
2. Generate embedding for question
3. Search FAISS using cosine similarity
4. Retrieve top matching chunks
5. Apply similarity threshold
6. Build prompt using:
   - Retrieved context
   - Conversation history
   - User question
7. Send prompt to Gemini
8. Return generated response

---

# Embedding Strategy

The application uses:

SentenceTransformer:

all-MiniLM-L6-v2

Each document chunk is converted into a vector embedding.

Embeddings allow semantic search instead of keyword matching.

---

# Similarity Search

The system uses:

FAISS IndexFlatIP

with normalized vectors.

This performs cosine similarity search between:

- User query embedding
- Stored document embeddings

Top 3 most relevant chunks are retrieved.

---

# Prompt Design

Prompt structure:

```text
You are a helpful assistant.

Use ONLY the provided context.

Context:
{retrieved_context}

Conversation History:
{history}

Question:
{question}
```

The retrieved context acts as the primary source of truth.

---

# API Endpoints

## Health Check

GET

```text
/health
```

Response:

```json
{
  "status": "healthy"
}
```

---

## Chat Endpoint

POST

```text
/api/chat
```

Request:

```json
{
  "sessionId":"abc123",
  "message":"How do I reset my password?"
}
```

Response:

```json
{
  "reply":"Users can reset their password from Settings > Security.",
  "tokensUsed":21,
  "retrievedChunks":3
}
```

---

# Setup Instructions

## Clone Repository

```bash
git clone <repository-url>
cd project
```

## Create Virtual Environment

```bash
python -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Configure Environment

Create:

```text
.env
```

Add:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

## Run Application

```bash
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

---

# Project Structure

```text
project/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── vectorstore/
│   ├── prompts/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
│
├── data/
│   └── docs.json
│
├── requirements.txt
├── .env.example
└── README.md
```

---

# Screenshots

Add:

1. Chat Interface
2. Swagger Documentation
3. Successful API Response
4. Retrieval Logs

---

# Author

Bondu Nagendra