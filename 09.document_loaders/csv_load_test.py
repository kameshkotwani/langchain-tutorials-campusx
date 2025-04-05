from dotenv import load_dotenv
from langchain_community.document_loaders import CSVLoader
from langchain_core.documents import Document
from typing import List
import os
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from config import DATA_DIR
loader =CSVLoader(DATA_DIR / "synthetic_online_retail_data.csv")

load_dotenv()

model = ChatOpenAI(
    model = os.getenv('CHAT_GPT_MODEL')
)
documents: List[Document] = loader.load()

# print(documents[0])
# print(len(documents))
#
prompt = PromptTemplate(
    template = """
    Answer the {question} based on the following context: {context}""",
    input_variables=["question","context"]
)

parser = StrOutputParser()

chain = prompt | model | parser

# result = chain.invoke({'context':documents,"question":"what is the number of missing values column wise?"})

# print(result)