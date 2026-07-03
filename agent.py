import logging

from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import Tool
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from config import GROQ_API_KEY
from tools.wikipedia import wikipedia_tool

logger = logging.getLogger(__name__)

# -------------------------------------------------
# LLM (tool-calling safe mode)
# -------------------------------------------------

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY,
)

# -------------------------------------------------
# TOOL WRAPPER
# -------------------------------------------------

def wikipedia_search(query: str) -> str:
    try:
        result = wikipedia_tool(query)
        return result.get("content", "No result found.")
    except Exception as e:
        logger.exception("Wikipedia tool error")
        return f"Tool error: {str(e)}"


tools = [
    Tool(
        name="Wikipedia",
        func=wikipedia_search,
        description=(
            "Search Wikipedia for factual information about people, "
            "places, history, science, technology, companies, and general knowledge."
        ),
    )
]

# -------------------------------------------------
# MODERN TOOL-CALLING PROMPT
# -------------------------------------------------

prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful AI assistant. "
     "Use tools when needed. Otherwise answer directly. "
     "Be concise and accurate."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# -------------------------------------------------
# AGENT (NO REACT)
# -------------------------------------------------

agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    return_intermediate_steps=True,
    max_iterations=3,
    max_execution_time=15,
)

# -------------------------------------------------
# PUBLIC API (same response format as before)
# -------------------------------------------------

def run_agent(query: str):
    try:
        result = agent_executor.invoke({"input": query.strip()})

        steps = result.get("intermediate_steps", [])

        tool = "None"
        tool_input = ""
        observation = ""

        if steps:
            action, obs = steps[-1]

            tool = getattr(action, "tool", "None")
            tool_input = getattr(action, "tool_input", "")
            observation = obs

        return {
            "response": {

                "action": tool,
                "action_input": tool_input,
                "observation": observation,
                "final_answer": result.get("output", ""),
            }
        }

    except Exception as e:
        logger.exception("Agent error")

        return {
            "response": {
                
                "action": "None",
                "action_input": "",
                "observation": str(e),
                "final_answer": str(e),
            }
        }