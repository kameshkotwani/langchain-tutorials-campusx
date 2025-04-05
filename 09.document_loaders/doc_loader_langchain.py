from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document
from typing import List
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config import DATA_DIR
import os

load_dotenv()
model = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)
loader = TextLoader(DATA_DIR /  "sample.txt",autodetect_encoding=True,encoding="utf-8")

# all the loaders return a List[Document]
docs:List[Document] = loader.load()

prompt = PromptTemplate(
    template="""Write a summary in 50 words about {topic}""",
    input_variables=["topic"]
)

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic':docs[0].page_content})

print(result)


