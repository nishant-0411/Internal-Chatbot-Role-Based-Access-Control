# 🏢 Internal RBAC Chatbot (Offline RAG System)

A fully offline **Role-Based Access Control (RBAC) AI Assistant** built using:

- 🔐 FastAPI (JWT Authentication)
- 🗂 BM25 / TF-IDF Lexical PageIndex (Custom Inverted Index)
- 🧠 Vectorless Keyword Search (High Precision, Zero Dep)
- 🤖 Ollama + Phi3 (Local LLM)
- 📊 Department-Based Access Control
- 🏗 Clean Modular Backend Architecture

This project simulates a real **enterprise internal knowledge assistant** that restricts document access based on user roles.

---

## 🚀 Features

- ✅ JWT-based authentication
- ✅ Role-Based Access Control (RBAC)
- ✅ Department-level document filtering
- ✅ Sub-second lexical similarity search using inverted indexes
- ✅ Fully offline LLM (no API key required)
- ✅ Context-aware RAG pipeline
- ✅ Clean service-based architecture
- ✅ Config-driven environment setup

---

## 🏗 Architecture Overview

User  
↓  
FastAPI (JWT Auth)  
↓  
Role Validation  
↓  
Lexical PageIndex (Inverted Index Search + Metadata Filter)  
↓  
Ollama (Local LLM - Phi3)  
↓  
Context-Aware Answer  

---

## 📂 Project Structure

```
Internal-Chatbot-RBAC/
│
├── app/
│   ├── api/
│   │   ├── auth.py
│   │   ├── chat.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── security.py
│   │
│   ├── services/
│   │   ├── index_builder.py
│   │   ├── rag_orchestrator.py
│   │   ├── retrieval.py
│   │   ├── streaming.py
│
├── data/                # Department documents
├── page_index/          # Offline lexical inverted index storage
├── main.py
├── requirements.txt
└── README.md
```

---

## 🔐 Roles & Access

| Role        | Access Scope |
|------------|-------------|
| HR         | HR documents |
| Finance    | Finance documents |
| Marketing  | Marketing documents |
| Engineering| Engineering documents |
| Employee   | General documents |
| C-Level    | All departments |

---

## 🧠 RAG Workflow

1. User logs in → receives JWT token  
2. User sends query to `/chat`  
3. Role extracted from JWT  
4. TF-IDF retrieval targets optimal content section filtered by department  
5. Retrieved context passed to local LLM  
6. LLM generates answer using ONLY internal context  

---

# ⚙️ Installation Guide (Step-by-Step)

This guide is for anyone cloning the repository.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/Internal-Chatbot-RBAC.git
cd Internal-Chatbot-RBAC
```

---

## 2️⃣ Create Virtual Environment

Mac/Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🗄 4️⃣ Seed the User Database (VERY IMPORTANT)

Before running the server, you must create initial users.

Run:

```bash
python app/seed.py
```

This will:

- Create SQLite database (`users_database.db`)
- Insert sample users with roles
- Prepare login credentials

---

## 🔐 Sample Seeded Users

| Username | Password | Role |
|----------|----------|------|
| hr_user | 1234 | hr |
| finance_user | 1234 | finance |
| marketing_user | 1234 | marketing |
| engineering_user | 1234 | engineering |
| nishant | 1234 | c-level |

---

# 🤖 5️⃣ Install Ollama (Required for LLM)

### Mac:

```bash
brew install ollama
```

### Pull Model:

```bash
ollama pull phi3
```

---

# ▶ 6️⃣ Start Ollama Server

```bash
ollama serve
```

Leave this running in background.

---

# 📚 7️⃣ Build Document PageIndex

Run:

```bash
python app/services/index_builder.py
```

This will:

- Read department folders inside `/data`
- Split documents into chunks
- Extract section tokens
- Generate inverted and IDF indices inside `page_index/`

---

# 🚀 8️⃣ Run FastAPI Server

```bash
uvicorn main:app --reload
```

Server runs at:

```
http://127.0.0.1:8000
```

---

# 🌐 9️⃣ Open API Docs

Open in browser:

```
http://127.0.0.1:8000/docs
```

---

# 🔑 🔟 Usage Flow

1. Call `/login`
2. Enter seeded credentials
3. Copy access token
4. Click **Authorize**
5. Paste token
6. Call `/chat`
7. Ask questions based on your role

---

# 🧪 Example Test Queries

### HR User:
```
What is the leave policy?
```

### Finance User:
```
Summarize financial performance over the past three years.
```

### C-Level User:
```
Provide an executive summary of company performance across all departments.
```

---

# 🛠 Configuration

All runtime configs are managed via:

```
app/core/config.py
```

Includes:
- Token expiry
- Ollama URL
- Model name
- Collection name

---

# 🧩 Tech Stack

| Component | Technology |
|------------|------------|
| Backend | FastAPI |
| Auth | JWT |
| Search Engine | Custom TF-IDF PageIndex |
| Extraction | Regex / NLTK Tokenization |
| LLM | Ollama (Phi3) |
| Chunking | Markdown Section Splitting |

---

# 🏆 Future Improvements

- Add document citations
- Add chat history memory
- Add streaming response
- Add audit logging
- Add Docker deployment
- Add frontend UI

---

# 👨‍💻 Author

Nishant  
B.Tech CSE | Backend & AI Systems Enthusiast  

---
