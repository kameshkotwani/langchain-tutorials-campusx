from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from typing import List
import os

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from config import DATA_DIR
loader = PyPDFLoader(DATA_DIR / "KameshKotwani_CV.pdf")

load_dotenv()
documents: List[Document] = loader.load()

prompt = PromptTemplate(
    template="""Write 10 reasons why this {resume} should be rejected also tell how to improve upon it to get job interviews. suggest changes in resume.""",
    input_variables=["resume"]
)

model = ChatOpenAI(
    model = os.getenv('CHAT_GPT_MODEL')
)

parser  = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'resume':documents[0].page_content})

print(result)

