from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
import os
load_dotenv()

prompt_one =  PromptTemplate(
    template="""
    You are an expert in this {topic}. Generate a detailed report on this {topic}.
    """,
    input_variables=["topic"],

)

prompt_two =  PromptTemplate(
    template="""
    Generate a five pointer summary from the following {text}.
    """,
    input_variables=["text"],

)

model = ChatOpenAI(
    model=os.getenv('CHAT_GPT_MODEL')
)

parser = StrOutputParser()

chain = prompt_one | model | parser | prompt_two | model | parser

print(chain.invoke({'topic':'unemployment in India'}))

chain.get_graph().print_ascii()