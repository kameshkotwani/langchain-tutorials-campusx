from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(
    model='gpt-4o',
    temperature= 1.5,
)

result = chat.invoke("write a five line poem on cricket")

print(result.content)
