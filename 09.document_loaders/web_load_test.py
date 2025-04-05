from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_core.documents import Document
from typing import List
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from config import DATA_DIR
loader = WebBaseLoader("https://ai.meta.com/blog/llama-4-multimodal-intelligence/?_fb_noscript=1")

load_dotenv()
model = ChatOpenAI(
    model = os.getenv('CHAT_GPT_MODEL')
)
documents: List[Document] = loader.load()

prompt = PromptTemplate(
    template = """
    Answer the {question} based on the following context: {context}""",
    input_variables=["question","context"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'context':documents[0].page_content,"question":"How to use it for free?"})

print(result)