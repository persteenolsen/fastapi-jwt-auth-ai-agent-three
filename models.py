from typing import Optional
from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str


class ChatRequest(BaseModel):
    message: str


class AgentResponse(BaseModel):
   
    action: str
    action_input: Optional[str] = None
    observation: str
    final_answer: str


class ChatResponse(BaseModel):
    response: AgentResponse