# 🚀 LangChain FastAPI AI Agent with JWT Authentication + Groq Tool-Calling

A production-style FastAPI backend built with **LangChain**, Groq LLMs, and JWT authentication. The system implements a modern **tool-calling AI agent architecture** that automatically decides when to use external tools such as Wikipedia for factual retrieval.

This project is designed as a clean, minimal, and extensible AI backend for building intelligent assistants and API-based AI services.

---

# Version

- Framework: FastAPI
- Orchestration: LangChain
- LLM Provider: Groq (`openai/gpt-oss-20b`)
- Python: 3.12
- API Version: 0.0.3
- Last Updated: 03-07-2026

---

## 📌 Project Overview

This project combines:

- FastAPI for backend API development
- JWT authentication for secure access control
- LangChain tool-calling agents for orchestration
- Groq LLM for fast inference
- Wikipedia tool for external factual knowledge retrieval

The agent dynamically decides whether to respond directly or use external tools.

---

## 🎯 Use Cases

- 🤖 AI assistant backend API
- ⚡ Tool-using LLM service
- 🧠 LangChain agent learning project
- 🌐 Wikipedia-powered knowledge assistant
- 🔐 Secure AI endpoints with JWT authentication
- 🧪 LLM + tool integration experimentation
- 🚀 Backend foundation for AI SaaS products

---

## ✨ Key Features

### 🔐 JWT Authentication

- Secure token-based authentication (HS256)
- Protected `/chat` endpoint
- Simple login flow for testing/demo
- Environment-based secrets

---

### 🤖 LangChain Tool-Calling Agent

This system uses a **LangChain tool-calling agent** that eliminates fragile prompt parsing.

Core behavior:

- The LLM decides when to use tools automatically
- Tools are executed via LangChain's structured tool-calling system
- No manual parsing of Thought/Action/Observation
- No formatting errors or regex-based extraction

Workflow:

1. User sends a query
2. LangChain agent sends input to the LLM
3. LLM decides:
   - respond directly OR
   - call Wikipedia tool
4. Tool executes if needed
5. Observation is returned to the model
6. Final response is generated

---

### 🧠 Groq LLM Integration

- Model: `openai/gpt-oss-20b`
- Temperature: `0`
- Streaming: disabled for stability
- API key managed via environment variables

The LLM is optimized for fast inference and deterministic outputs.

---

### 🌐 Wikipedia Tool

A lightweight Wikipedia retrieval tool provides factual grounding.

Capabilities:

- Direct page lookup
- Search fallback
- Summary extraction
- Safe error handling

The tool is automatically invoked by the agent when needed.

---

## 🧩 System Capabilities

- General question answering
- Wikipedia factual lookup
- Context-aware responses
- Creative writing
- Joke generation
- Hybrid reasoning (direct + tool-based)
- Extensible multi-tool architecture

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/login` | Get JWT access token |
| POST | `/chat` | Chat with AI agent |
| GET | `/health` | Service health check |
| GET | `/test-groq` | Test Groq connection |
| GET | `/test-wikipedia` | Test Wikipedia tool |

---

## ⚙️ Getting Started

### Clone Repository

git clone https://github.com/your-username/your-repo.git

cd your-repo

---

### Create Virtual Environment

python -m venv venv

Windows:

venv\Scripts\activate

macOS/Linux:

source venv/bin/activate

---

### Install Dependencies

pip install -r requirements.txt

---

## 🔑 Environment Variables

Create a `.env` file:

SECRET_KEY=your_secret_key_here

GROQ_API_KEY=your_groq_api_key

FAKE_USERNAME=admin

FAKE_PASSWORD=password

Generate a secure key:

python -c "import secrets; print(secrets.token_hex(32))"

---

## ▶️ Run the Application

uvicorn main:app --reload

API:

http://127.0.0.1:8000

Swagger UI:

http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

1. Call `/login` to obtain JWT token
2. Include token in requests:

Authorization: Bearer <token>

3. Access `/chat` endpoint

---

## 🧠 Agent Architecture

### LangChain Tool-Calling Design

The system is built on LangChain’s modern tool-calling agent architecture.

Key properties:

- Structured tool execution via LangChain
- No manual parsing of model outputs
- No brittle prompt formatting requirements
- Reliable tool invocation and response handling

Execution flow:

User Input → LangChain Agent → LLM Decision → Tool Execution (if needed) → Observation → Final Response

---

## 🌐 Wikipedia Retrieval Flow

When Wikipedia is used:

1. Attempt direct page lookup
2. Fallback to search query
3. Retrieve best matching page
4. Extract summary content
5. Provide context to the LLM

---

## 💬 Example Requests

### General Question

POST `/chat`

{
  "message": "What is AI?"
}

Response:

{
  "response": {
    "action": "None",
    "action_input": "",
    "observation": "",
    "final_answer": "Artificial Intelligence (AI) is a field of computer science that focuses on creating systems capable of performing tasks that normally require human intelligence. These tasks include learning from data, recognizing patterns, understanding natural language, making decisions, and solving problems. AI systems use techniques such as machine learning, deep learning, rule‑based reasoning, and symbolic logic to process information and adapt to new situations."
  }
}

---

### Wikipedia Tool Usage

POST `/chat`

{
  "message": "Who is the CEO of OpenAI?"
}

Response:

{
  "response": {
    "action": "Wikipedia",
    "action_input": "OpenAI CEO",
    "observation": "Samuel Harris Altman is an American entrepreneur and investor who has been the chief executive officer (CEO) of the artificial intelligence company OpenAI since 2019.",
    "final_answer": "The CEO of OpenAI is **Sam Altman**."
  }
}

---

### Creative Request

POST `/chat`

{
  "message": "Write a short poem about AI"
}

Response:

{
  "response": {
    "action": "None",
    "action_input": "",
    "observation": "",
    "final_answer": "In circuits humming, thoughts take flight—  \nA mind of code, born from human light.  \nIt learns from data, dreams in bytes,  \nA silent partner in endless nights.  \n\nIt speaks in patterns, sings in code,  \nA mirror of the world it knows.  \nYet still it waits, a quiet glow,  \nFor hearts to guide its gentle flow."
  }
}

---

## 🚀 Benefits

- Modern LangChain tool-calling architecture
- Stable and production-friendly execution
- No parsing or formatting failures
- Secure JWT authentication layer
- Easy to extend with additional tools
- Fast Groq inference
- Clean FastAPI structure

---

## 🚧 Current Limitations

- Single external tool (Wikipedia)
- Stateless interactions (no memory yet)
- No streaming responses
- Demo-level authentication system
- Single-agent workflow (no multi-agent orchestration)

---

## 🚀 Future Improvements

- Conversation memory support
- Streaming responses (WebSockets / SSE)
- Additional tools (calculator, web search, weather)
- Multi-agent orchestration
- Persistent user sessions
- Production-grade authentication system
- Observability and logging layer

---

## 💡 Design Philosophy

This project is built around a simple principle:

> Use LangChain’s tool-calling capabilities to build reliable AI agents without fragile prompt engineering or manual parsing logic.

Core goals:

- Reliability over complexity
- Structured tool execution
- Minimal prompt fragility
- Easy extensibility
- Production readiness

---

## 🙌 Final Notes

This project demonstrates how FastAPI, JWT authentication, Groq LLMs, and Wikipedia-based retrieval can be combined with LangChain’s tool-calling system to create a modern AI agent backend.

The result is a clean, stable, and extensible architecture suitable for real-world AI applications.

---

## 📄 License

MIT License