from langchain_core.messages import SystemMessage, HumanMessage ,AIMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

# create a model to chat with
model = ChatOpenAI()

messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain'),
]

response = model.invoke(messages)
# Expected Output:

messages.append(AIMessage(content=response.content))

print(messages)