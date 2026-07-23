# 🚀 FastAPI JWT LangChain AI Agent API

A production-style full-stack AI application built with **FastAPI**, **Vue 3**, **Pinia**, **LangChain**, **Groq LLMs**, and **JWT authentication**.

The backend uses LangChain's native tool-calling architecture, allowing the LLM to decide when external tools should be used for factual retrieval. The frontend provides a transparent chat interface where users can see both the AI's final response and the agent workflow behind it.

A companion Vue 3 Single Page Application is available for authenticated chat interactions.

**Vue Frontend**

https://github.com/persteenolsen/vue-fastapi-jwt-auth-ai-agent-three

---

# 📌 Project Information

- Version: 0.0.3
- Last Updated: 23-07-2026
- Python: 3.12
- Framework: FastAPI
- Authentication: JWT (HS256)
- Architecture: LangChain Tool Calling

---

# 🎯 Use Cases

This project can serve as the foundation for:

- AI assistants
- Full-stack AI applications
- Tool-augmented LLM systems
- Enterprise AI services
- Knowledge assistants
- Research assistants
- Information retrieval systems
- Customer support assistants
- Developer assistants
- Educational projects

---

# ✨ Features

## 🔐 Authentication

- JWT authentication
- OAuth2 compatible token endpoint
- SPA login endpoint
- Protected API endpoints
- Bearer token authorization
- Environment-based secrets

Authentication endpoints

- `POST /login-spa` (Vue frontend)
- `POST /token` (Swagger / OAuth2)

---

## 🤖 LangChain Tool-Calling Agent

The backend uses LangChain's structured tool-calling architecture.

Workflow

1. User sends a question
2. Vue sends the request to FastAPI
3. LangChain agent processes the request
4. The LLM decides whether a tool is needed
5. The selected tool executes
6. The observation is returned
7. The final answer is generated

Advantages

- Native LangChain tool calling
- No manual parsing of model output
- Automatic tool selection
- Easy to extend with additional tools

---

## 🧠 LLM Integration

Powered by Groq.

Current model

- openai/gpt-oss-20b

Used for

- Tool selection
- Response generation

Configuration

- Temperature: 0
- Streaming: Disabled
- API key stored in environment variables

Benefits

- Fast responses
- Stable output
- Simple API integration

---

## 🌐 Wikipedia Tool

The AI agent includes a Wikipedia retrieval tool.

Capabilities

- Direct page lookup
- Search fallback
- Summary extraction
- Error handling

The agent automatically decides when Wikipedia should be used.

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/login-spa` | Login for Vue SPA |
| POST | `/token` | OAuth2 login for Swagger |
| POST | `/chat` | Chat with the AI agent |
| GET | `/health` | Service health |
| GET | `/test-groq` | Test Groq connection |
| GET | `/test-wikipedia` | Test Wikipedia tool |

---

# 📦 Response Model

The chat endpoint returns a structured response.

Example

    {
      "response": {
        "action": "Wikipedia",
        "action_input": "Apple CEO",
        "observation": "Timothy Donald Cook is an American business executive...",
        "final_answer": "The CEO of Apple is Tim Cook."
      }
    }

---

# ⚙️ Getting Started

Clone

    git clone https://github.com/your-username/your-repository.git

Enter the backend project

    cd backend

Create virtual environment

Windows

    python -m venv venv
    venv\Scripts\activate

Linux/macOS

    python -m venv venv
    source venv/bin/activate

Install dependencies

    pip install -r requirements.txt

---

# 🔑 Environment Variables

Create a `.env` file

    SECRET_KEY=your_secret_key_here
    GROQ_API_KEY=your_groq_api_key
    FAKE_USERNAME=admin
    FAKE_PASSWORD=password

Generate a secret key

    python -c "import secrets; print(secrets.token_hex(32))"

---

# ▶️ Run

Start the FastAPI backend

    uvicorn main:app --reload

API

    http://127.0.0.1:8000

Swagger

    http://127.0.0.1:8000/docs

---

# 🔐 Authentication Flow

## Vue SPA

1. Login using `/login-spa`
2. Receive JWT
3. Store token
4. Include

       Authorization: Bearer <token>

5. Access `/chat`

---

## Swagger

1. Authenticate through `/token`
2. Swagger stores the JWT
3. Test protected endpoints

---

# 🧠 Agent Workflow

    User Question
          |
          v
    Vue 3 Frontend
          |
          v
   FastAPI Backend
          |
          v
 LangChain AI Agent
          |
      +---+---+
      |       |
   Groq LLM
 Wikipedia Tool
      |
      v
  Observation
      |
      v
  Final Answer

---

# 🏗️ Architecture

The application combines a FastAPI backend with a Vue 3 frontend.

The backend is responsible for

- Authentication
- API endpoints
- LangChain orchestration
- Tool execution
- LLM integration

The frontend is responsible for

- JWT authentication
- Chat interface
- State management
- Displaying agent actions
- Displaying tool observations

The AI agent is responsible for

- Deciding when tools are needed
- Calling external tools
- Producing the final answer

---

# 💬 Example Requests

## General Question

**Request**

    {
      "message": "Tell me a joke"
    }

**Response**

    {
      "response": {
        "action": null,
        "action_input": null,
        "observation": null,
        "final_answer": "Why don’t scientists trust atoms? Because they make up everything!"
      }
    }

---

## Wikipedia

**Request**

    {
      "message": "Who is the CEO of Apple?"
    }

**Response**

    {
      "response": {
        "action": "Wikipedia",
        "action_input": "Apple CEO",
        "observation": "Timothy Donald Cook is an American business executive...",
        "final_answer": "The CEO of Apple is Tim Cook."
      }
    }

---

# 🖥️ Vue Frontend

A companion Vue 3 application is available.

Features

- JWT authentication
- Pinia state management
- AI chat interface
- API integration
- Displays final answers
- Displays selected agent action
- Displays tool input
- Displays tool observations
- Transparent agent workflow

---

# 🚀 Benefits

- Full-stack AI agent architecture
- FastAPI backend
- Vue 3 frontend
- JWT security layer
- LangChain structured tool calling
- Groq fast inference
- Transparent agent workflow
- Easy tool extension

---

# 🚧 Current Limitations

- Single external tool (Wikipedia)
- No conversation memory
- No streaming responses
- Demo authentication system
- Single-agent workflow

---

# 🚀 Future Improvements

- Conversation memory
- Streaming responses
- Additional tools
- Multi-agent workflows
- Persistent user sessions
- Production authentication
- Monitoring and observability

---

# 💡 Design Philosophy

> Use structured AI agent workflows instead of fragile prompt parsing.

Goals

- Reliability
- Transparency
- Simple architecture
- Easy extension
- Clear separation between frontend and backend

---

# 🙌 Final Notes

This project demonstrates how FastAPI, Vue 3, JWT authentication, LangChain, and Groq LLMs can be combined to create a modern AI agent application.

The backend exposes a clean REST API while the companion Vue 3 SPA provides an authenticated user interface that visualizes the complete agent workflow, including selected actions and tool observations.

---

# 📄 License

MIT License
