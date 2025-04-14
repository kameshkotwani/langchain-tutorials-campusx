from langchain_community.retrievers import WikipediaRetriever
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEmbeddings
load_dotenv
# Initialize the retriever (optional: set language and top_k)
retriever = WikipediaRetriever(top_k_results=2, lang="en")

# Define your query
query = "the geopolitical history of india and pakistan from the perspective of a chinese"

# Get relevant Wikipedia documents
docs = retriever.invoke(query)

# Initialize Ollama embeddings
ollama_embeddings = OllamaEmbeddings(model="llama2")

# Generate embeddings for the retrieved documents
for doc in docs:
    doc_embedding = ollama_embeddings.embed_query(doc.page_content)
    print(f"Document: {doc.page_content}\nEmbedding: {doc_embedding}\n")

from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document
from langchain_community.embeddings import OllamaEmbeddings

# Step 1: Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]



model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
hf = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)
# Step 3: Create Chroma vector store in memory
vectorstore = Chroma.from_documents(
    documents=documents,
    embedding=hf,
    collection_name="my_collection"
)
