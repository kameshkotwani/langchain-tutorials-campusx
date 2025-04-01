from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

template = PromptTemplate(
    template="""
    You are an expert in this {topic}. Generate five rare facts about this {topic} that are not commonly known.
    """,
    input_variables=["topic"],

)

model = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

parser = StrOutputParser()

chain = template | model | parser

# print(chain.invoke({'topic':'North Korea'}))

chain.get_graph().print_ascii()