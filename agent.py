

import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

import warnings
warnings.filterwarnings("ignore")

#from langchain.agents.agent_toolkits import create_python_agent
from langchain.agents import load_tools, initialize_agent
from langchain.agents import AgentType
from langchain_experimental.agents.agent_toolkits import create_python_agent
#from langchain_experimental.tools.python.tool import PythonREPLTool
#from langchain.python import PythonREPL
from langchain.chat_models import ChatOpenAI

from langchain.agents import tool
from datetime import date

llm_model = "gpt-4o-mini"
llm = ChatOpenAI(temperature=0, model=llm_model)
tools = load_tools(["llm-math"], llm=llm)

@tool
def time(text: str) -> str:
    """Returns todays date, use this for any \
    questions related to knowing todays date. \
    The input should always be an empty string, \
    and this function will always return todays \
    date - any date mathmatics should occur \
    outside this function."""
    return str(date.today())

agent= initialize_agent(
    tools + [time], 
    llm, 
    agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    handle_parsing_errors=True,
    verbose = True)

try:
    result = agent("whats the date tomorrow?") 
    print(result)
except: 
    print("exception on external access")