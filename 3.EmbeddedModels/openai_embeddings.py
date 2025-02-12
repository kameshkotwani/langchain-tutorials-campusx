from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(
    model='text-embedding-3-small',
    dimensions=64
)

result = embedding.embed_query("Delhi is the Capital of India.")




print(str(result))