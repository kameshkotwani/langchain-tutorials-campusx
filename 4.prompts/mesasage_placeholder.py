from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from pathlib import Path

# this is a tmplate for a chat model with message history
chat_template = ChatPromptTemplate([
    ('system',"you are a support assistant"),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_history_path = Path(__file__).parent / "chat_history.txt"
chat_history = []
# loading chat history
with open(chat_history_path, "r") as f:
    chat_history.extend(f.readlines())

prompt = chat_template.invoke(
    input={
        "query":"What is the staus of my refund?",
        "chat_history": chat_history
    }
)

print(prompt)
# # this is a chat model
# model = ChatOpenAI(model="gpt-3.5-turbo")
# response = model.invoke(prompt)

# print(response.content)
