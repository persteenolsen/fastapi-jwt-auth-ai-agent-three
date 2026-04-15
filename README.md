# Python + FastAPI + JWT Auth + AI Agent + Groq + LLM + Langchain 
 
A production-style **AI Agent API** built with **FastAPI**, featuring **JWT authentication**, **Groq-powered LLMs**, and **LangChain agent orchestration**.

This project demonstrates how to build a **tool-using AI agent** that can reason, take actions, and fetch real-time information (via Wikipedia) before generating responses.

---

## 📌 Project Info

- **Version:** 0.0.1  
- **Python:** 3.12  
- **Last Updated:** 15-04-2026  

---

## ✨ Features

### 🔐 Authentication
- JWT-based authentication (HS256)  
- Secure protected endpoints  
- Token expiration handling  
- Environment-based credentials  

---

### 🤖 AI Agent (LangChain)
- Built using LangChain's **ReAct agent pattern**  
- Multi-step reasoning (Thought → Action → Observation)  
- Tool usage with iterative decision-making  
- Max iteration control for safety  

---

### 🧠 LLM Integration (Groq)
- Model: `llama-3.3-70b-versatile`  
- Zero-temperature for deterministic outputs  
- Fast inference via Groq API  

---

### 🌐 Tool Integration (Wikipedia)
- Uses LangChain `WikipediaQueryRun`  
- Fetches real-time factual data  
- Top-K results for better context  

---

### 🧩 Agent Capabilities
- Answers general knowledge questions  
- Searches Wikipedia when needed  
- Combines reasoning + external data  
- Produces structured final answers  

---

## 📡 API Endpoints

| Method | Endpoint   | Description                     |
|--------|-----------|---------------------------------|
| POST   | `/login`  | Get JWT access token            |
| POST   | `/chat`   | Chat with AI agent 🔐           |

🔐 = Requires authentication

---

## ⚙️ Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key_here
GROQ_API_KEY=your_groq_api_key

FAKE_USERNAME=admin
FAKE_PASSWORD=password
```

> 💡 Tip: Generate a secure key using Python:
```python
import secrets
print(secrets.token_hex(32))
```

---

## ▶️ Run the Application

```bash
uvicorn main:app --reload
```

Available at:

- 🌐 API: http://127.0.0.1:8000

- 📄 Swagger UI: http://127.0.0.1:8000/docs  

---

## 🔐 Authentication Flow

1. Call `/login` with credentials  
2. Receive JWT access token  
3. Use in headers:

```http
Authorization: Bearer <your_token>
```

---

## 🧠 How the AI Agent Works

```text
User Question
   ↓
LangChain Agent (ReAct)
   ↓
Thought → Decide Action
   ↓
Wikipedia Tool (if needed)
   ↓
Observation
   ↓
Repeat (max 5 iterations)
   ↓
Final Answer (LLM - Groq)
```

---

## 🧩 Agent Architecture

### 🔹 LLM
- Groq `llama-3.3-70b-versatile`  
- Handles reasoning + final response generation  

---

### 🔹 Agent Type
- ReAct (Reasoning + Acting)  
- Structured prompt with tool usage rules  

---

### 🔹 Tools
- Wikipedia API (via LangChain)  
- Limited to top 2 results per query  

---

### 🔹 Execution Control
- Max iterations: 5  
- Parsing error handling enabled  
- Verbose logging for debugging  

---

## 💬 Example Request

### `/chat`

```json
{
  "message": "Who is the president of France?"
}
```

---

## 📌 Use Cases

- 🤖 AI assistants  
- 🌐 Knowledge-based chat systems  
- 🧠 Agent-based reasoning demos  
- 🔎 Tool-augmented LLM applications  

---

## 🚧 Limitations

- Single tool (Wikipedia)  
- No conversation memory (stateless)  
- Hardcoded user authentication (demo setup)  

---

## 📌 Future Improvements

- 🧠 Add memory (conversation history)  
- 🧩 Add more tools (search, APIs, databases)  
- 🔄 Refresh tokens  
- 📊 Logging & monitoring  
- 🔐 OAuth / multi-user support
- Splitting up the main.py into seperate files and folders for improved structure  

---

## 📄 License

MIT License  

---

## 🙌 Final Notes

This project demonstrates how to combine:

- FastAPI (backend)  
- JWT (security)  
- Groq (fast LLM inference)  
- LangChain (agent orchestration)  

to build a **tool-using AI agent API** ready for real-world extensions.