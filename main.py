from fastapi import FastAPI
from routes import router
from config import logger

app = FastAPI(
    title="FastAPI with JWT Auth serving a Tool-Calling AI Agent using LangChain",
    description="19-07-2026 - FastAPI backend with JWT authentication serving a LangChain tool-calling AI agent powered by Groq, with optional Wikipedia-based factual retrieval for enhanced responses",
    version="0.0.3", 
    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
    },
)

# Include API routes
app.include_router(router)