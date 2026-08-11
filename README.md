# ⚖️ PakLex AI — Pakistan Penal Code RAG System

A production-quality **RAG (Retrieval-Augmented Generation)** system for the Pakistan Penal Code 1860.
Built with **LangChain + Groq API + ChromaDB**.

---

## 🗂️ Project Structure

```
paklex-ai/
│
├── notebooks/
│   ├── 01_ingest.ipynb       ← Load PDF → chunk → embed → ChromaDB
│   ├── 02_rag_engine.ipynb   ← LangChain RAG chain + Groq API
│   └── 03_app.ipynb          ← Flask API server
│
├── templates/
│   └── index.html            ← Dark Judicial web frontend
│
├── data/
│   └── ppc.pdf               ← ⬅ PUT YOUR PDF HERE
│
├── vector_store/             ← Auto-created by 01_ingest.ipynb
│
├── .env                      ← Your Groq API key (NOT on GitHub)
├── .env.example              ← Safe template (on GitHub)
├── .gitignore                ← Ignores .env + vector_store/
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

| Component | Choice | Reason |
|-----------|--------|--------|
| **Framework** | LangChain | LCEL chain, retrievers, prompt templates |
| **LLM** | Groq — mixtral-8x7b-32768 | Sub-second responses, free tier, 32K context |
| **Embeddings** | all-MiniLM-L6-v2 | Fast, 384-dim, great semantic similarity |
| **Vector DB** | ChromaDB | Zero-config, persistent, LangChain-native |
| **PDF Loader** | LangChain PyPDFLoader | Handles multi-page PDFs with metadata |
| **Backend** | Flask | Lightweight REST API |
| **Chunk Size** | 1000 chars / 200 overlap | Preserves complete legal clauses |

---

## 🚀 Setup

### 1. Get Free Groq API Key
```
https://console.groq.com → Sign up → API Keys → Create
```

### 2. Create .env file
```bash
# In project root (same folder as README.md)
echo "GROQ_API_KEY=gsk_your_key_here" > .env
```

### 3. Add your PDF
```
Copy your PPC PDF into the data/ folder.
Any filename works — the notebook auto-detects it.
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run notebooks in order
```bash
jupyter notebook
```

| Notebook | Task | Time |
|----------|------|------|
| `01_ingest.ipynb` | PDF → ChromaDB | ~2 min |
| `02_rag_engine.ipynb` | Test RAG chain | Interactive |
| `03_app.ipynb` | Start Flask server | Runs until stopped |

### 6. Open the app
```
http://localhost:5000
```

---

## 🔒 API Key Security

Your Groq API key is stored in `.env` — it is:
- ✅ Never hardcoded in any notebook or Python file
- ✅ Loaded via `python-dotenv` at runtime
- ✅ Listed in `.gitignore` — never pushed to GitHub
- ✅ `.env.example` provided as a safe template for collaborators

---

## 📡 API Endpoints

| Endpoint | Method | Body / Response |
|----------|--------|-----------------|
| `/` | GET | Serves `index.html` |
| `/api/query` | POST | `{"query":"..."}` → `{answer, sources, response_time}` |
| `/api/health` | GET | `{groq, chromadb, model, chunks}` |
| `/api/stats` | GET | `{total_documents, llm_model, chunk_size, ...}` |

---

*Pakistan Penal Code 1860 · pakistancode.gov.pk · LangChain + Groq + ChromaDB*
