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
# This is the chat model.
# It does NOT know about our Python functions yet.
# Tool descriptions are added to the agent prompt later
# by create_tool_calling_agent()
llm = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0,
    api_key=GROQ_API_KEY,
)

# -------------------------------------------------
# TOOL WRAPPER
# -------------------------------------------------
# The LLM does not execute Python code directly.
# If the LLM chooses the Wikipedia tool, LangChain
# calls this function, handles the Python execution,
# and sends the returned result back to the LLM
def wikipedia_search(query: str) -> str:
    try:
        result = wikipedia_tool(query)
        return result.get("content", "No result found.")
    except Exception as e:
        logger.exception("Wikipedia tool error")
        return f"Tool error: {str(e)}"

# -------------------------------------------------
# AVAILABLE TOOLS
# -------------------------------------------------
# These are the tools the LLM is allowed to use.
# The descriptions are sent to the model, which
# decides if and when a tool should be called
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
# The prompt defines the assistant's behavior.
# The {agent_scratchpad} placeholder is where
# LangChain stores previous tool calls and results
# during the agent loop
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a helpful AI assistant. "
     "Use tools when needed. Otherwise answer directly. "
     "Be concise and accurate."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

# -------------------------------------------------
# AGENT
# -------------------------------------------------
# Connect the LLM, prompt and available tools.
# The tool names and descriptions are sent to the
# LLM so it knows which tools it may use
agent = create_tool_calling_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

# -------------------------------------------------
# AGENT EXECUTOR
# -------------------------------------------------
# The LLM decides whether to answer directly or
# request one or more tool calls. LangChain simply
# executes the requested tools and sends the results
# back to the LLM until a final answer is produced.
#
# max_iterations prevents endless tool loops
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=False,
    return_intermediate_steps=True,
    max_iterations=3,
    max_execution_time=15,
)

# -------------------------------------------------
# RUN AGENT
# -------------------------------------------------
def run_agent(query: str):
    try:
        
        # Start the agent.
        # AgentExecutor handles the complete LLM/tool loop.
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