import streamlit as st

import langchain
import openai

openai_api_key = '조교에게 문의하세요'
openai.api_key = openai_api_key
os.environ['OPENAI_API_KEY'] = openai_api_key

from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage, AIMessage

chat = ChatOpenAI(temperature=0.3, openai_api_key=openai_api_key)

chat(
    [
        SystemMessage(content="You are a nice AI bot that helps a user figure out various questions"),
        HumanMessage(content="I like the beaches where should I go?"),
        AIMessage(content="You should go to Nice, France"),
        HumanMessage(content="What else should I do when I'm there?")
    ]
)
