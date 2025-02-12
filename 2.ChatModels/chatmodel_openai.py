from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(
    model='gpt-4o',
    temperature= 1.2,
    max_completion_tokens=10
)

result = chat.invoke("write a five line poem on cricket")

print(result.content)
