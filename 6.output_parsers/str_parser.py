from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
# this model does not give structured output
llm = HuggingFaceEndpoint(
    repo_id = 'google/gemma-2-2b-it',
    task = 'text-generation',
    max_new_tokens= 512,

)

# Load environment variables from .env file
load_dotenv()

# model  = ChatOpenAI(
#     model=os.getenv("CHAT_GPT_MODEL")
# )
model = ChatHuggingFace(
    llm=llm
)
template1 = PromptTemplate(
    template="""
    Write a 100 words report on {topic}""",
    input_variables=["topic"],
)

template2 = PromptTemplate(
    template="""
    Write a five line summary on {text} and give them in points""",
    input_variables=["text"],
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'blackhole'})

print(result)