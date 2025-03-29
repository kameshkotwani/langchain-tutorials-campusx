from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


chat_template = ChatPromptTemplate(
    messages=[
        ('system',"You are a helpful {domain} expert."),
        ('human',"Explain in simple terms, what is {user_input}"),
    ]
)

# this is a tmplate for a chat model
prompt = chat_template.invoke(
    input={
        "domain": "cricket",
        "user_input": "googly",
    }
)

# this is a chat model
chat = ChatOpenAI(model="gpt-3.5-turbo")
response = chat.invoke(prompt)

print(response.content)