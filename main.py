import os
from datetime import datetime, timedelta
import secrets
from typing import Optional

from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from dotenv import load_dotenv
import jwt

from langchain_groq import ChatGroq
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

# -----------------------------
# ENV
# -----------------------------
load_dotenv()

# Hardcoded user (for simplicity)
# SECRET_KEY = "supersecretkey"  # ⚠️ change in production

# 02-04-2026: Updated to use environment variable for secret key
SECRET_KEY=os.getenv("SECRET_KEY")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# Hardcoded user (for simplicity)
#FAKE_USERNAME = "admin"
#FAKE_PASSWORD = "password123"

# 02-04-2026: Updated to use environment variables for credentials
FAKE_USERNAME=os.getenv("FAKE_USERNAME")
FAKE_PASSWORD = os.getenv("FAKE_PASSWORD")

# 03-04-2026 - Due to an Error related to the secret key length when running the app, 
# I generated a new 32-byte key using Python's secrets module and set it as 
# the SECRET_KEY environment variable. 
# This should resolve the issue and allow the JWT authentication to work properly.
# new_key = secrets.token_bytes(32)
# print(new_key)

# -----------------------------
# FastAPI App
# -----------------------------
# app = FastAPI(title="AI Agent API with JWT Auth")

# Initialize the FastAPI app
app = FastAPI(

    title="Python + FastApi + JWT Auth + AI Agent + LLP + Groq + Langchain",
    description="03-04-2026 - FastAPI with JWT Auth serving an AI agent powered by one of Groq's LLaMA models, using Langchain for agent orchestration and Wikipedia tool integration",
    version="0.0.1",

    contact={
        "name": "Per Olsen",
        "url": "https://persteenolsen.netlify.app",
         },
)

security = HTTPBearer()

# -----------------------------
# Models
# -----------------------------
class LoginRequest(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    access_token: str

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# -----------------------------
# JWT Helpers
# -----------------------------
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username != FAKE_USERNAME:
            raise HTTPException(status_code=401, detail="Invalid user")
        return username
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

# -----------------------------
# Login Endpoint
# -----------------------------
@app.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    if request.username != FAKE_USERNAME or request.password != FAKE_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": request.username},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return TokenResponse(access_token=access_token)

# -----------------------------
# LLM Setup
# -----------------------------
llm = ChatGroq(

    # 02-04-2026: Updated to use the LLaMA 3.3 70B Versatile model
    model="llama-3.3-70b-versatile",
    temperature=0,

    # 02-04-2026: Updated to use the new GROQ API key environment variable
    api_key=os.getenv("GROQ_API_KEY")
)

wiki_tool = WikipediaQueryRun(
    api_wrapper=WikipediaAPIWrapper(top_k_results=2)
)

tools = [wiki_tool]

template = """Answer the following questions as best you can.

You have access to the following tools:

{tools}

Use the following format strictly:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat up to 5 times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

prompt = PromptTemplate.from_template(template)

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5,
    handle_parsing_errors=True
)

# -----------------------------
# Protected Chat Endpoint
# -----------------------------
@app.post("/chat", response_model=ChatResponse)
def chat(
    request: ChatRequest,
    user: str = Depends(verify_token)  # 🔐 Protected route
):
    try:
        result = agent_executor.invoke({
            "input": request.message
        })

        return ChatResponse(response=result["output"])

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))