from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-small',
    dimensions=64
)

documents = [
    "My name is Kamesh",
    "I am from India",
    "I am a Data Scientist",
]

result = embedding.embed_documents(documents)

print(str(result))