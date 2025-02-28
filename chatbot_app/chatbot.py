from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage ,AIMessage


load_dotenv()

# create a model to chat with
model = ChatOpenAI()

chat_history = [
    SystemMessage(content='You are a helpful Python Assistant'),
]
while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(user_input))

    if user_input == "exit":
        break
    response = model.invoke(chat_history)
    print(response.content)
    chat_history.append(AIMessage(response.content))

print(chat_history)

